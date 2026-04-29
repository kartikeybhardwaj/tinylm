"""A single transformer block: attention + feed-forward with residual connections."""

import torch.nn as nn

from .attention import FFN, Attention


class Block(nn.Module):
    """One transformer layer.

    Uses pre-norm architecture: LayerNorm is applied BEFORE attention/FFN,
    not after. This is more stable for training deep networks than post-norm.

    Residual connections (x + ...) let gradients flow directly to earlier
    layers, which prevents vanishing gradients in deep models.
    """

    def __init__(self, config):
        super().__init__()
        # norm1 normalizes before attention, norm2 normalizes before FFN
        self.norm1 = nn.LayerNorm(config.d_model)
        self.attn = Attention(config)
        self.norm2 = nn.LayerNorm(config.d_model)
        self.ffn = FFN(config)

    def forward(self, x, mask=None):
        # Attention sub-layer with residual connection
        x = x + self.attn(self.norm1(x), mask)
        # Feed-forward sub-layer with residual connection
        x = x + self.ffn(self.norm2(x))
        return x
