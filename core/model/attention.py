"""Multi-head self-attention and feed-forward network.

Attention is the core mechanism that lets each token "look at" other tokens
in the sequence to understand context. The FFN processes each token independently
after attention has gathered contextual information.
"""

import math

import torch.nn as nn
import torch.nn.functional as F


class Attention(nn.Module):
    """Multi-head self-attention.

    Each of the n_heads performs attention in a subspace of d_model/n_heads
    dimensions. Multiple heads let the model attend to different patterns
    (e.g., one head for syntax, another for semantics) in parallel.
    """

    def __init__(self, config):
        super().__init__()
        self.n_heads = config.n_heads
        self.head_dim = config.d_model // config.n_heads

        # `qkv` is a single projection that produces Q, K, V at once — more
        # efficient than 3 separate linears. `out` projects back after attention.
        self.qkv = nn.Linear(config.d_model, 3 * config.d_model)
        self.out = nn.Linear(config.d_model, config.d_model)
        self.dropout = nn.Dropout(config.dropout)

    def forward(self, x, mask=None):
        batch_size, seq_len, d_model = x.shape

        # Project input into Q, K, V for all heads simultaneously, then split:
        #   (batch, seq, 3*d_model) -> (batch, seq, 3, n_heads, head_dim)
        # Permute to get separate Q/K/V tensors shaped (batch, n_heads, seq, head_dim)
        qkv = self.qkv(x).reshape(batch_size, seq_len, 3, self.n_heads, self.head_dim)
        qkv = qkv.permute(2, 0, 3, 1, 4)
        queries, keys, values = qkv[0], qkv[1], qkv[2]

        # Attention scores: how much each query should attend to each key.
        # Scaled by sqrt(head_dim) for gradient stability (from "Attention Is All You Need").
        scores = (queries @ keys.transpose(-2, -1)) / math.sqrt(self.head_dim)

        # Causal mask: prevent each token from attending to future tokens.
        # Without this, the model would "cheat" by looking at the answer during training.
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float("-inf"))

        # Softmax converts scores to probabilities that sum to 1 across keys
        weights = self.dropout(F.softmax(scores, dim=-1))

        # Weighted sum of values, then reshape back:
        #   (batch, n_heads, seq, head_dim) -> (batch, seq, n_heads * head_dim) = (batch, seq, d_model)
        attended = (weights @ values).transpose(1, 2).contiguous().view(batch_size, seq_len, d_model)
        return self.out(attended)


class FFN(nn.Module):
    """Feed-forward network applied to each token independently.

    Expands to 2x d_model, applies ReLU nonlinearity, then projects back.
    This is where most of the model's "knowledge" is stored.
    """

    def __init__(self, config):
        super().__init__()
        # `up` expands from d_model to ffn_hidden (wider), `down` contracts back.
        self.up = nn.Linear(config.d_model, config.ffn_hidden)
        self.down = nn.Linear(config.ffn_hidden, config.d_model)
        self.dropout = nn.Dropout(config.dropout)

    def forward(self, x):
        return self.dropout(self.down(F.relu(self.up(x))))
