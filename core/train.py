"""Training loop with cosine learning rate schedule, AMP, and checkpointing.

The model learns by predicting the next token and adjusting weights to reduce
cross-entropy loss. Every `eval_interval` steps, we test on held-out data
and save the best-performing checkpoint.
"""

import json
import math
import os
import time

import torch

from .config import ModelConfig, TrainConfig
from .data import get_dataloader
from .device import get_device
from .model import TinyLM


def compute_lr(step, config):
    """Cosine learning rate schedule with linear warmup.

    - Steps 0 to warmup_steps: linearly ramp up from 0 to peak learning rate
    - Steps warmup_steps to max_steps: cosine decay from peak down to min_lr

    Warmup prevents the optimizer from making wild jumps at the start when
    weights are still random. Cosine decay gives finer adjustments at the end.
    """
    if step < config.warmup_steps:
        return config.learning_rate * step / config.warmup_steps

    decay_progress = (step - config.warmup_steps) / max(1, config.max_steps - config.warmup_steps)
    cosine_factor = 0.5 * (1 + math.cos(math.pi * decay_progress))
    return config.min_lr + (config.learning_rate - config.min_lr) * cosine_factor


@torch.no_grad()
def evaluate_model(model, eval_loader, device, max_batches=50):
    """Compute average loss on held-out data without updating weights."""
    model.eval()
    total_loss, batch_count = 0, 0
    for inputs, targets in eval_loader:
        if batch_count >= max_batches:
            break
        inputs, targets = inputs.to(device), targets.to(device)
        _, loss = model(inputs, targets)
        total_loss += loss.item()
        batch_count += 1
    model.train()
    return total_loss / max(1, batch_count)


def train(train_config=None):
    model_config = ModelConfig()
    if train_config is None:
        train_config = TrainConfig()
    device = get_device(train_config.device)
    torch.manual_seed(train_config.seed)
    print(f"Device: {device}")

    # ── Setup model and data ──
    tokenizer_path = os.path.join(train_config.data_dir, "tokenizer.json")
    model = TinyLM(model_config).to(device)
    print(model.param_summary())

    train_loader = get_dataloader(
        os.path.join(train_config.data_dir, "train.jsonl"),
        tokenizer_path,
        model_config.max_seq_len,
        train_config.batch_size,
        shuffle=True,
    )
    eval_loader = get_dataloader(
        os.path.join(train_config.data_dir, "eval.jsonl"),
        tokenizer_path,
        model_config.max_seq_len,
        train_config.batch_size,
        shuffle=False,
    )
    print(f"Train: {len(train_loader.dataset):,}, Eval: {len(eval_loader.dataset):,}")

    # ── Optimizer ──
    # AdamW is Adam with decoupled weight decay — the standard for transformers.
    # betas=(0.9, 0.95) is GPT-style (default 0.999 is too aggressive for large LRs).
    optimizer = torch.optim.AdamW(
        model.parameters(), lr=train_config.learning_rate, weight_decay=train_config.weight_decay, betas=(0.9, 0.95)
    )

    # Automatic Mixed Precision speeds up CUDA training ~2x by using fp16 where safe.
    # Not supported on MPS, so we only enable it for CUDA.
    use_amp = device.type == "cuda"
    grad_scaler = torch.amp.GradScaler("cuda") if use_amp else None

    # ── Save config alongside checkpoints ──
    os.makedirs(train_config.output_dir, exist_ok=True)
    with open(os.path.join(train_config.output_dir, "config.json"), "w") as f:
        json.dump({"model": vars(model_config), "train": vars(train_config)}, f, indent=2)

    # ── Training loop ──
    model.train()
    step = 0
    best_eval_loss = float("inf")
    recent_losses = []
    start_time = time.time()

    print(f"\nTraining for {train_config.max_steps} steps...")
    print(f"{'Step':>6} | {'LR':>10} | {'Train':>10} | {'Eval':>10} | {'Time':>8}")
    print("-" * 56)

    while step < train_config.max_steps:
        for inputs, targets in train_loader:
            if step >= train_config.max_steps:
                break
            inputs, targets = inputs.to(device), targets.to(device)

            # Update learning rate according to schedule
            current_lr = compute_lr(step, train_config)
            for param_group in optimizer.param_groups:
                param_group["lr"] = current_lr

            # Forward + backward pass
            if use_amp:
                with torch.amp.autocast("cuda"):
                    _, loss = model(inputs, targets)
                # Scale loss up before backward, unscale before clipping, step, then update scaler
                grad_scaler.scale(loss).backward()
                grad_scaler.unscale_(optimizer)
                torch.nn.utils.clip_grad_norm_(model.parameters(), train_config.grad_clip)
                grad_scaler.step(optimizer)
                grad_scaler.update()
            else:
                _, loss = model(inputs, targets)
                loss.backward()
                # Clip gradients to prevent explosion (common in transformer training)
                torch.nn.utils.clip_grad_norm_(model.parameters(), train_config.grad_clip)
                optimizer.step()

            optimizer.zero_grad(set_to_none=True)
            recent_losses.append(loss.item())

            # ── Logging ──
            if step % 100 == 0:
                avg_loss = sum(recent_losses[-100:]) / len(recent_losses[-100:])
                elapsed = time.time() - start_time
                print(f"{step:6d} | {current_lr:10.6f} | {avg_loss:10.4f} | {'--':>10} | {elapsed:7.1f}s")

            # ── Eval + save best model ──
            if step > 0 and step % train_config.eval_interval == 0:
                eval_loss = evaluate_model(model, eval_loader, device)
                train_window = min(len(recent_losses), train_config.eval_interval)
                avg_train_loss = sum(recent_losses[-train_config.eval_interval :]) / train_window
                elapsed = time.time() - start_time
                print(f"{step:6d} | {current_lr:10.6f} | {avg_train_loss:10.4f} | {eval_loss:10.4f} | {elapsed:7.1f}s")

                if eval_loss < best_eval_loss:
                    best_eval_loss = eval_loss
                    torch.save(
                        {
                            "step": step,
                            "model_state_dict": model.state_dict(),
                            "config": vars(model_config),
                            "eval_loss": eval_loss,
                        },
                        os.path.join(train_config.output_dir, "best_model.pt"),
                    )
                    print(f"  -> Best model (eval={eval_loss:.4f})")

            # ── Periodic snapshot ──
            if step > 0 and step % train_config.save_interval == 0:
                torch.save(
                    {"step": step, "model_state_dict": model.state_dict(), "config": vars(model_config)},
                    os.path.join(train_config.output_dir, f"step_{step}.pt"),
                )

            step += 1

    # ── Final save ──
    torch.save(
        {
            "step": step,
            "model_state_dict": model.state_dict(),
            "config": vars(model_config),
            "train_losses": recent_losses,
        },
        os.path.join(train_config.output_dir, "final_model.pt"),
    )

    elapsed = time.time() - start_time
    print(f"\nDone! {elapsed:.0f}s, best eval: {best_eval_loss:.4f}")
