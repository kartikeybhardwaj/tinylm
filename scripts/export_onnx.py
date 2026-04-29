"""ONNX export + quantization for browser demo."""

import os
import shutil
import sys
import warnings
import logging

import torch

logging.getLogger("torch.onnx").setLevel(logging.ERROR)


def export(personality="frog"):
    """Export a trained model to ONNX and quantize for browser use.

    Args:
        personality: "frog" or "cat" — determines which checkpoint/data dirs to use
    """
    data_dir = f"data/{personality}"
    checkpoint_dir = f"checkpoints/{personality}"
    docs_dir = f"docs/{personality}"

    checkpoint_path = os.path.join(checkpoint_dir, "best_model.pt")
    tokenizer_path = os.path.join(data_dir, "tokenizer.json")

    if not os.path.exists(checkpoint_path):
        print(f"No checkpoint found at {checkpoint_path}. Train first.")
        return

    os.makedirs(docs_dir, exist_ok=True)

    from core.config import ModelConfig
    from core.model import TinyLM

    config = ModelConfig()
    model = TinyLM(config)
    ckpt = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    model.load_state_dict(ckpt["model_state_dict"], strict=False)
    model.eval()

    onnx_path = os.path.join(docs_dir, "model.onnx")
    quantized_path = os.path.join(docs_dir, "model_q.onnx")
    dummy = torch.randint(0, 100, (1, config.max_seq_len - 1))

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        torch.onnx.export(
            model, dummy, onnx_path,
            input_names=["input_ids"], output_names=["logits"],
            dynamic_axes={"input_ids": {1: "seq_len"}, "logits": {1: "seq_len"}},
            opset_version=18,
        )
    print(f"Exported to {onnx_path}")

    from onnxruntime.quantization import quantize_dynamic, QuantType
    quantize_dynamic(onnx_path, quantized_path, weight_type=QuantType.QUInt8)
    print(f"Quantized to {quantized_path}")

    shutil.copy(tokenizer_path, os.path.join(docs_dir, "tokenizer.json"))
    print(f"Copied tokenizer to {docs_dir}/tokenizer.json")


if __name__ == "__main__":
    personality = sys.argv[1] if len(sys.argv) > 1 else "frog"
    export(personality)
