"""Inference — loads a trained checkpoint and generates chat responses."""

import json
import os

import torch
from tokenizers import Tokenizer

from .config import FrogConfig
from .device import get_device
from .model import FrogLM


class FrogInference:
    """Wraps a trained model + tokenizer with a simple chat API."""

    def __init__(self, checkpoint_path, tokenizer_path, device="auto"):
        self.device = get_device(device)
        self.tokenizer = Tokenizer.from_file(tokenizer_path)

        checkpoint = torch.load(checkpoint_path, map_location=self.device, weights_only=False)

        # Checkpoints may be wrapped in a dict (new format) or raw state_dict (old format)
        if isinstance(checkpoint, dict) and "model_state_dict" in checkpoint:
            model_weights = checkpoint["model_state_dict"]
        else:
            model_weights = checkpoint

        self.config = self._load_config(checkpoint, checkpoint_path)

        # Build model and load weights. strict=False allows missing/extra keys
        # (helpful when loading checkpoints across minor architecture changes).
        self.model = FrogLM(self.config).to(self.device)
        filtered_weights = {k: v for k, v in model_weights.items() if k in self.model.state_dict()}
        self.model.load_state_dict(filtered_weights)
        self.model.eval()
        print(f"FrogLM loaded: {self.model.param_count() / 1e6:.1f}M params")

    def _load_config(self, checkpoint, checkpoint_path):
        """Try loading config from (1) sibling config.json, (2) checkpoint dict, (3) defaults."""
        config_path = os.path.join(os.path.dirname(os.path.abspath(checkpoint_path)), "config.json")
        valid_fields = FrogConfig.__dataclass_fields__

        if os.path.exists(config_path):
            with open(config_path) as f:
                raw_config = json.load(f)
            # Config file may wrap model config under "model" key
            model_fields = raw_config.get("model", raw_config)
            return FrogConfig(**{k: v for k, v in model_fields.items() if k in valid_fields})

        if isinstance(checkpoint, dict) and "config" in checkpoint:
            return FrogConfig(**{k: v for k, v in checkpoint["config"].items() if k in valid_fields})

        return FrogConfig()

    def chat(self, messages, temperature=0.7, max_tokens=64, top_k=50):
        """Generate a response to a list of chat messages.

        Args:
            messages: list of {"role": "user"|"assistant", "content": str}
        """
        # Format messages using the chat template (matches training format)
        prompt = self._format_chat_prompt(messages)
        prompt_token_ids = self.tokenizer.encode(prompt).ids
        prompt_length = len(prompt_token_ids)

        # Run generation
        input_tensor = torch.tensor([prompt_token_ids], dtype=torch.long, device=self.device)
        output_tensor = self.model.generate(input_tensor, max_tokens, temperature, top_k)

        # Decode only the NEW tokens (skip the prompt we fed in)
        generated_ids = output_tensor[0].tolist()[prompt_length:]
        generated_text = self.tokenizer.decode(generated_ids)

        # Safety net: in case the model hallucinates a chat control token,
        # cut the response at that boundary so we don't leak into the next turn.
        if "<|im_end|>" in generated_text:
            generated_text = generated_text.split("<|im_end|>")[0]
        if "<|im_start|>" in generated_text:
            generated_text = generated_text.split("<|im_start|>")[0]

        return generated_text.strip()

    def _format_chat_prompt(self, messages):
        """Format messages using the ChatML template:

            <|im_start|>user
            hi frog<|im_end|>
            <|im_start|>assistant

        The trailing "assistant\\n" tells the model to start generating a response.
        """
        parts = []
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            parts.append(f"<|im_start|>{role}\n{content}<|im_end|>")
        parts.append("<|im_start|>assistant\n")
        return "\n".join(parts)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Chat with Frog")
    parser.add_argument("--checkpoint", default="checkpoints/best_model.pt")
    parser.add_argument("--tokenizer", default="data/tokenizer.json")
    parser.add_argument("--device", default="auto")
    parser.add_argument("--prompt", "-p", help="Single prompt mode (non-interactive)")
    args = parser.parse_args()

    engine = FrogInference(args.checkpoint, args.tokenizer, args.device)

    if args.prompt:
        print(f"Frog> {engine.chat([{'role': 'user', 'content': args.prompt}])}")
        return

    print("\nFrog Chat (type 'quit' to exit)\n")
    while True:
        try:
            user_input = input("You> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if user_input.lower() in ("quit", "exit", "q"):
            break
        if not user_input:
            continue
        response = engine.chat([{"role": "user", "content": user_input}])
        print(f"Frog> {response}\n")
