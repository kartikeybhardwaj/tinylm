"""Tokenizer training and the prepare pipeline.

Personality-agnostic: each personality passes its own topic list.
"""

import json
import os

VOCAB_SIZE = 4096
SPECIAL_TOKENS = ["", "<|im_start|>", "<|im_end|>"]


def train_tokenizer(training_texts, save_path, vocab_size=VOCAB_SIZE):
    """Train a ByteLevel BPE tokenizer from a corpus of texts."""
    from tokenizers import Tokenizer, models, trainers, pre_tokenizers, decoders, processors

    tokenizer = Tokenizer(models.BPE())
    tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
    tokenizer.decoder = decoders.ByteLevel()
    trainer = trainers.BpeTrainer(
        vocab_size=vocab_size, special_tokens=SPECIAL_TOKENS, show_progress=True, min_frequency=2
    )
    print(f"Training BPE tokenizer (vocab_size={vocab_size}) on {len(training_texts)} texts...")
    tokenizer.train_from_iterator(training_texts, trainer)
    tokenizer.post_processor = processors.ByteLevel(trim_offsets=False)

    os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)
    tokenizer.save(save_path)
    print(f"Tokenizer saved to {save_path} ({tokenizer.get_vocab_size()} tokens)")
    return tokenizer


def prepare(all_topics, data_dir="data", n_samples=60000, eval_ratio=0.05):
    """Full data preparation: generate conversations from topics, train tokenizer."""
    os.makedirs(data_dir, exist_ok=True)

    print(f"Generating {n_samples} samples...")
    from .generator import generate_dataset

    generate_dataset(all_topics, n_samples, eval_ratio, data_dir)

    all_texts = []
    for jsonl_path in [os.path.join(data_dir, "train.jsonl"), os.path.join(data_dir, "eval.jsonl")]:
        if os.path.exists(jsonl_path):
            with open(jsonl_path) as f:
                for line in f:
                    all_texts.append(json.loads(line)["text"])

    tokenizer_path = os.path.join(data_dir, "tokenizer.json")
    tokenizer = train_tokenizer(all_texts, tokenizer_path)

    test_text = "<|im_start|>user\nhi<|im_end|>"
    token_ids = tokenizer.encode(test_text).ids
    decoded_text = tokenizer.decode(token_ids)
    print(f"\nTokenizer test:")
    print(f"  Input:   {test_text}")
    print(f"  Tokens:  {len(token_ids)} ids")
    print(f"  Decoded: {decoded_text}")
