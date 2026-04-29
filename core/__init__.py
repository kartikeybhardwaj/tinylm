"""TinyLM core — shared model, training, and inference engine."""

from .config import ModelConfig, TrainConfig
from .model import TinyLM
from .inference import LMInference

__all__ = ["ModelConfig", "TrainConfig", "TinyLM", "LMInference"]
