"""TinyLM — a vanilla decoder-only transformer.

The model predicts the next token given all previous tokens. Same core
architecture as GPT, just much smaller (8.7M params vs billions).
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

from ..config import ModelConfig
from .block import Block


class TinyLM(nn.Module):
    def __init__(self, config: ModelConfig):
        super().__init__()
        self.config = config

        # `tok_emb` converts token IDs (integers) into d_model-dim vectors.
        self.tok_emb = nn.Embedding(config.vocab_size, config.d_model)

        # `pos_emb` tells the model WHERE each token is in the sequence.
        # Without this, attention would treat sequences as unordered bags of tokens.
        self.pos_emb = nn.Embedding(config.max_seq_len, config.d_model)

        self.drop = nn.Dropout(config.dropout)
        self.blocks = nn.ModuleList([Block(config) for _ in range(config.n_layers)])
        self.norm = nn.LayerNorm(config.d_model)

        # `lm_head` projects back to vocabulary size to predict next token probabilities.
        # Weight tying: reuse tok_emb's weights (saves ~1.5M params for our model).
        self.lm_head = nn.Linear(config.d_model, config.vocab_size, bias=False)
        self.lm_head.weight = self.tok_emb.weight

        # Precompute causal mask (lower-triangular matrix) as a buffer so it moves
        # with the model to GPU/MPS automatically. Shape: (1, 1, max_seq_len, max_seq_len).
        # Position (i, j) = 1 if j <= i (allowed), 0 if j > i (masked, future token).
        causal_mask = torch.tril(torch.ones(config.max_seq_len, config.max_seq_len))
        self.register_buffer("causal_mask", causal_mask.unsqueeze(0).unsqueeze(0))

        self.apply(self._init_weights)

    def _init_weights(self, module):
        """Initialize weights with small random values.

        Using std=0.02 (GPT-2 convention) keeps initial activations in a
        sensible range so training starts stable.
        """
        if isinstance(module, nn.Linear):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def forward(self, idx, targets=None):
        """Forward pass. Returns (logits, optional_loss).

        Args:
            idx: (batch, seq_len) integer token IDs
            targets: (batch, seq_len) target token IDs for loss computation (training only)
        """
        batch_size, seq_len = idx.shape

        # Embed tokens and add positional information
        positions = torch.arange(seq_len, device=idx.device)
        x = self.drop(self.tok_emb(idx) + self.pos_emb(positions))

        # Slice the precomputed causal mask to match current sequence length
        mask = self.causal_mask[:, :, :seq_len, :seq_len]

        # Run through all transformer layers
        for block in self.blocks:
            x = block(x, mask)

        # Final norm + projection to vocabulary logits
        logits = self.lm_head(self.norm(x))

        # Compute cross-entropy loss if targets provided.
        # ignore_index=0 means padding tokens don't contribute to the loss.
        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.view(-1, self.config.vocab_size), targets.view(-1), ignore_index=0)
        return logits, loss

    @torch.no_grad()
    def generate(self, idx, max_new_tokens=64, temperature=0.7, top_k=50):
        """Autoregressive generation: produce tokens one at a time.

        Args:
            idx: (1, prompt_len) starting tokens (the prompt)
            max_new_tokens: how many tokens to generate before stopping
            temperature: controls randomness. Lower=deterministic, higher=creative
            top_k: only sample from the top K most likely tokens (filters out noise)
        """
        self.eval()
        for _ in range(max_new_tokens):
            # If we're past max_seq_len, crop to fit (model can't handle longer sequences)
            context = idx[:, -self.config.max_seq_len :]

            # Get logits for the LAST position only — that's our next-token prediction
            logits, _ = self(context)
            next_token_logits = logits[:, -1, :] / temperature

            # Top-k filtering: keep only the K highest-scoring tokens, mask out the rest.
            # Prevents the model from occasionally picking a wildly unlikely token.
            if top_k > 0:
                top_values, _ = torch.topk(next_token_logits, min(top_k, next_token_logits.size(-1)))
                # Set logits below the Kth value to -inf so softmax assigns them 0 probability
                next_token_logits[next_token_logits < top_values[:, [-1]]] = float("-inf")

            # Convert to probabilities and sample one token
            probs = F.softmax(next_token_logits, dim=-1)
            next_id = torch.multinomial(probs, num_samples=1)

            # Append the new token and check for end-of-sequence
            idx = torch.cat([idx, next_id], dim=1)
            if next_id.item() == self.config.eos_id:
                break

        return idx

    def param_count(self):
        return sum(p.numel() for p in self.parameters())

    def param_summary(self):
        total = self.param_count()
        return f"TinyLM: {total:,} params ({total / 1e6:.1f}M)"
