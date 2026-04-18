"""Tokenizer training and the `prepare` pipeline.

BPE (Byte Pair Encoding) learns common subword patterns. Instead of having a
fixed dictionary of words, it builds up tokens by repeatedly merging the most
frequent pair of adjacent tokens. ByteLevel means we operate on raw UTF-8 bytes,
so the tokenizer can handle ANY text (even characters it's never seen).
"""

import json
import os

DATA_DIR = "data"
VOCAB_SIZE = 4096

# Order matters — this defines token IDs 0, 1, 2.
# These IDs are referenced in FrogConfig (pad_id, bos_id, eos_id).
SPECIAL_TOKENS = [
    "",  # 0 — padding (ignored in loss)
    "<|im_start|>",  # 1 — marks start of a message turn
    "<|im_end|>",  # 2 — marks end of a message turn
]


def train_tokenizer(training_texts, save_path, vocab_size=VOCAB_SIZE):
    """Train a ByteLevel BPE tokenizer from a corpus of texts.

    Why ByteLevel BPE?
    - Handles any text (including unicode/emoji) since it operates on bytes
    - No <unk> tokens needed (rare chars just decompose into single bytes)
    - Same approach as GPT-2, RoBERTa, and Llama

    Why min_frequency=2?
    - A merge must appear in at least 2 texts to be included.
    - Prevents overfitting to rare one-off patterns in the training data.
    """
    from tokenizers import Tokenizer, decoders, models, pre_tokenizers, processors, trainers

    tokenizer = Tokenizer(models.BPE())

    # Pre-tokenizer: split text into bytes before BPE. add_prefix_space=False
    # means we don't prepend a space to the input (cleaner for our chat format).
    tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)

    # Decoder converts token IDs back to text (reverses the byte-level encoding).
    tokenizer.decoder = decoders.ByteLevel()

    trainer = trainers.BpeTrainer(
        vocab_size=vocab_size, special_tokens=SPECIAL_TOKENS, show_progress=True, min_frequency=2
    )
    print(f"Training BPE tokenizer (vocab_size={vocab_size}) on {len(training_texts)} texts...")
    tokenizer.train_from_iterator(training_texts, trainer)

    # Post-processor handles offset adjustments when tokens are rendered back to text.
    tokenizer.post_processor = processors.ByteLevel(trim_offsets=False)

    os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)
    tokenizer.save(save_path)
    print(f"Tokenizer saved to {save_path} ({tokenizer.get_vocab_size()} tokens)")
    return tokenizer


def prepare(data_dir=DATA_DIR, n_samples=60000, eval_ratio=0.05):
    """Full data preparation pipeline: generate conversations, train tokenizer, verify.

    Running this produces:
      data/train.jsonl    — training conversations
      data/eval.jsonl     — held-out eval conversations
      data/tokenizer.json — trained BPE tokenizer
    """
    os.makedirs(data_dir, exist_ok=True)

    # Step 1: generate synthetic conversations
    print(f"Generating {n_samples} samples...")
    from .generator import generate_dataset

    generate_dataset(n_samples, eval_ratio)

    # Step 2: collect all formatted texts to train the tokenizer on
    all_texts = []
    for jsonl_path in [f"{data_dir}/train.jsonl", f"{data_dir}/eval.jsonl"]:
        if os.path.exists(jsonl_path):
            with open(jsonl_path) as f:
                for line in f:
                    all_texts.append(json.loads(line)["text"])

    # Step 3: train the tokenizer on the corpus
    tokenizer_path = os.path.join(data_dir, "tokenizer.json")
    tokenizer = train_tokenizer(all_texts, tokenizer_path)

    # Step 4: sanity check — encode/decode a sample to verify it works
    test_text = "<|im_start|>user\nhi frog<|im_end|>"
    token_ids = tokenizer.encode(test_text).ids
    decoded_text = tokenizer.decode(token_ids)
    print("\nTokenizer test:")
    print(f"  Input:   {test_text}")
    print(f"  Tokens:  {len(token_ids)} ids")
    print(f"  Decoded: {decoded_text}")
