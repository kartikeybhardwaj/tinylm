"""Generic LM inference — loads a trained checkpoint and generates chat responses."""

import json
import os

import torch
from tokenizers import Tokenizer

from .config import ModelConfig
from .model import TinyLM
from .device import get_device


class LMInference:
    """Wraps a trained model + tokenizer with a simple chat API."""

    def __init__(self, checkpoint_path, tokenizer_path, device="auto"):
        self.device = get_device(device)
        self.tokenizer = Tokenizer.from_file(tokenizer_path)

        checkpoint = torch.load(checkpoint_path, map_location=self.device, weights_only=False)

        if isinstance(checkpoint, dict) and "model_state_dict" in checkpoint:
            model_weights = checkpoint["model_state_dict"]
        else:
            model_weights = checkpoint

        self.config = self._load_config(checkpoint, checkpoint_path)

        self.model = TinyLM(self.config).to(self.device)
        filtered_weights = {k: v for k, v in model_weights.items() if k in self.model.state_dict()}
        self.model.load_state_dict(filtered_weights)
        self.model.eval()
        print(f"Model loaded: {self.model.param_count() / 1e6:.1f}M params")

    def _load_config(self, checkpoint, checkpoint_path):
        """Try loading config from (1) sibling config.json, (2) checkpoint dict, (3) defaults."""
        config_path = os.path.join(os.path.dirname(os.path.abspath(checkpoint_path)), "config.json")
        valid_fields = ModelConfig.__dataclass_fields__

        if os.path.exists(config_path):
            with open(config_path) as f:
                raw_config = json.load(f)
            model_fields = raw_config.get("model", raw_config)
            return ModelConfig(**{k: v for k, v in model_fields.items() if k in valid_fields})

        if isinstance(checkpoint, dict) and "config" in checkpoint:
            return ModelConfig(**{k: v for k, v in checkpoint["config"].items() if k in valid_fields})

        return ModelConfig()

    def chat(self, messages, temperature=0.7, max_tokens=64, top_k=50):
        """Generate a response to a list of chat messages."""
        prompt = self._format_chat_prompt(messages)
        prompt_token_ids = self.tokenizer.encode(prompt).ids
        prompt_length = len(prompt_token_ids)

        input_tensor = torch.tensor([prompt_token_ids], dtype=torch.long, device=self.device)
        output_tensor = self.model.generate(input_tensor, max_tokens, temperature, top_k)

        generated_ids = output_tensor[0].tolist()[prompt_length:]
        generated_text = self.tokenizer.decode(generated_ids)

        if "<|im_end|>" in generated_text:
            generated_text = generated_text.split("<|im_end|>")[0]
        if "<|im_start|>" in generated_text:
            generated_text = generated_text.split("<|im_start|>")[0]

        return generated_text.strip()

    def _format_chat_prompt(self, messages):
        """Format messages using the ChatML template."""
        parts = []
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            parts.append(f"<|im_start|>{role}\n{content}<|im_end|>")
        parts.append("<|im_start|>assistant\n")
        return "\n".join(parts)
