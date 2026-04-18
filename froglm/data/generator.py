"""Dataset generation — produces train/eval JSONL files from topic generators.

Each generator in topics.ALL_TOPICS produces a {input, output, category} sample.
We call them equally often so the model sees balanced topic coverage.
"""

import json
import os
import random
from collections import Counter

from .topics import ALL_TOPICS

# Fixed seed so data generation is reproducible across runs
random.seed(42)


def format_sample(sample):
    """Format a sample using the ChatML template for training.

    The <|im_start|> and <|im_end|> tokens teach the model where user turns
    end and assistant turns begin. This is what enables structured chat behavior.
    """
    return f"<|im_start|>user\n{sample['input']}<|im_end|>\n<|im_start|>assistant\n{sample['output']}<|im_end|>"


def generate_dataset(total_samples=60000, eval_ratio=0.05):
    """Generate training and evaluation datasets.

    Distributes samples equally across all topics so no personality trait
    dominates the training data.
    """
    # Split total evenly across topics; give any remainder to the first N topics
    samples_per_topic = total_samples // len(ALL_TOPICS)
    remainder = total_samples - samples_per_topic * len(ALL_TOPICS)

    samples = []
    for i, topic_generator in enumerate(ALL_TOPICS):
        count = samples_per_topic + (1 if i < remainder else 0)
        for _ in range(count):
            samples.append(topic_generator())

    # Shuffle so batches mix topics (important for stable training)
    random.shuffle(samples)

    num_eval = int(len(samples) * eval_ratio)
    eval_samples = samples[:num_eval]
    train_samples = samples[num_eval:]

    # Write as JSONL — one JSON object per line, easy to stream
    os.makedirs("data", exist_ok=True)
    for filepath, data in [("data/train.jsonl", train_samples), ("data/eval.jsonl", eval_samples)]:
        with open(filepath, "w") as f:
            for sample in data:
                f.write(json.dumps({"text": format_sample(sample), "category": sample["category"]}) + "\n")

    # Print summary stats
    category_counts = Counter(s["category"] for s in samples)
    unique_outputs = len(set(s["output"] for s in samples))
    uniqueness_pct = unique_outputs / len(samples) * 100
    print(f"Generated {len(samples)} samples ({unique_outputs} unique outputs, {uniqueness_pct:.1f}% unique):")
    print(f"  Train: {len(train_samples)}, Eval: {num_eval}")
    print(f"  Topics: {len(ALL_TOPICS)}")
    print("\nBy category:")
    for category, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        print(f"  {category}: {count}")
