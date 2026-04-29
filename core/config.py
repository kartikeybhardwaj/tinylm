"""Model and training hyperparameters."""

from dataclasses import dataclass


@dataclass
class ModelConfig:
    """Model architecture hyperparameters."""

    vocab_size: int = 4096  # Number of unique tokens the model can handle
    max_seq_len: int = 128  # Maximum context length in tokens
    d_model: int = 384  # Embedding dimension (size of hidden state)
    n_layers: int = 6  # Number of transformer blocks
    n_heads: int = 6  # Number of attention heads per layer
    ffn_hidden: int = 768  # Feed-forward network hidden dimension
    dropout: float = 0.1  # Dropout rate (applied after attention/FFN for regularization)

    # Special token IDs (must match tokenizer's special_tokens list order)
    pad_id: int = 0  # Padding token (ignored in loss computation)
    bos_id: int = 1  # <|im_start|> — marks start of a message
    eos_id: int = 2  # <|im_end|> — marks end of a message


@dataclass
class TrainConfig:
    """Training loop hyperparameters."""

    batch_size: int = 32
    learning_rate: float = 3e-4  # Peak LR after warmup
    min_lr: float = 3e-5  # Minimum LR at end of cosine decay
    weight_decay: float = 0.1  # L2 regularization strength
    warmup_steps: int = 200  # Steps to linearly ramp LR from 0 to peak
    max_steps: int = 10000  # Total training steps
    eval_interval: int = 200  # How often to run evaluation
    save_interval: int = 500  # How often to save a checkpoint snapshot
    grad_clip: float = 1.0  # Gradient norm clipping threshold (prevents explosion)
    device: str = "auto"  # "auto" | "cuda" | "mps" | "cpu"
    seed: int = 42
    data_dir: str = "data"
    output_dir: str = "checkpoints"
