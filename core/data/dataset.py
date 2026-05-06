"""Dataset loading with dynamic padding.

Each sample is a tokenized conversation. For language modeling, we shift
the tokens by 1 to create (input, target) pairs — the model learns to
predict each target token from the input tokens that came before it.
"""

import json

import torch
from torch.utils.data import DataLoader, Dataset


class TinyLMDataset(Dataset):
    """Loads pre-tokenized conversations from a JSONL file."""

    def __init__(self, jsonl_path: str, tokenizer_path: str, max_len: int = 512):
        from tokenizers import Tokenizer

        self.tokenizer = Tokenizer.from_file(tokenizer_path)
        self.max_len = max_len
        self.token_sequences = []

        # Load and tokenize all samples upfront. Keeps training loop fast
        # since we don't re-tokenize on every epoch.
        with open(jsonl_path) as f:
            for line in f:
                data = json.loads(line)
                token_ids = self.tokenizer.encode(data["text"]).ids
                if len(token_ids) > max_len:
                    token_ids = token_ids[:max_len]
                # Need at least 2 tokens: one for input, one for target
                if len(token_ids) >= 2:
                    self.token_sequences.append(token_ids)

    def __len__(self):
        return len(self.token_sequences)

    def __getitem__(self, idx):
        token_ids = self.token_sequences[idx]

        # Next-token prediction: input is all tokens except last,
        # target is all tokens except first (shifted by 1).
        # Example: tokens [A, B, C, D] -> input [A, B, C], target [B, C, D]
        # The model learns: given A predict B, given A,B predict C, etc.
        input_ids = token_ids[:-1]
        target_ids = token_ids[1:]
        return torch.tensor(input_ids, dtype=torch.long), torch.tensor(target_ids, dtype=torch.long)


def pad_batch(batch, pad_token_id=0):
    """Pad variable-length sequences in a batch to the same length.

    Uses dynamic padding: each batch is only padded to its longest sequence,
    not to max_seq_len. Saves compute vs fixed-length padding.
    """
    inputs, targets = zip(*batch)
    batch_max_len = max(len(seq) for seq in inputs)

    padded_inputs = torch.full((len(inputs), batch_max_len), pad_token_id, dtype=torch.long)
    padded_targets = torch.full((len(targets), batch_max_len), pad_token_id, dtype=torch.long)

    for i, (input_seq, target_seq) in enumerate(zip(inputs, targets)):
        padded_inputs[i, : len(input_seq)] = input_seq
        padded_targets[i, : len(target_seq)] = target_seq

    return padded_inputs, padded_targets


def get_dataloader(jsonl_path, tokenizer_path, max_len=512, batch_size=32, shuffle=True):
    dataset = TinyLMDataset(jsonl_path, tokenizer_path, max_len)
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        collate_fn=pad_batch,
        num_workers=0,
        pin_memory=torch.cuda.is_available(),  # pin_memory only helps with CUDA
    )
