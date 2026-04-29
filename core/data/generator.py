"""Dataset generation — produces train/eval JSONL files from topic generators.

This module is personality-agnostic. Each personality package passes its own
ALL_TOPICS list to generate_dataset().
"""

import json
import os
import random
from collections import Counter

# Fixed seed so data generation is reproducible across runs
random.seed(42)


def format_sample(sample):
    """Format a sample using the ChatML template for training."""
    return (
        f"<|im_start|>user\n{sample['input']}<|im_end|>\n"
        f"<|im_start|>assistant\n{sample['output']}<|im_end|>"
    )


def generate_dataset(all_topics, total_samples=60000, eval_ratio=0.05, data_dir="data"):
    """Generate training and evaluation datasets from a list of topic generators.

    Args:
        all_topics: list of callables, each returning {"input": ..., "output": ..., "category": ...}
        total_samples: total number of samples to generate
        eval_ratio: fraction held out for evaluation
        data_dir: directory to write JSONL files to
    """
    samples_per_topic = total_samples // len(all_topics)
    remainder = total_samples - samples_per_topic * len(all_topics)

    samples = []
    for i, topic_generator in enumerate(all_topics):
        count = samples_per_topic + (1 if i < remainder else 0)
        for _ in range(count):
            samples.append(topic_generator())

    random.shuffle(samples)

    num_eval = int(len(samples) * eval_ratio)
    eval_samples = samples[:num_eval]
    train_samples = samples[num_eval:]

    os.makedirs(data_dir, exist_ok=True)
    for filepath, data in [
        (os.path.join(data_dir, "train.jsonl"), train_samples),
        (os.path.join(data_dir, "eval.jsonl"), eval_samples),
    ]:
        with open(filepath, "w") as f:
            for sample in data:
                f.write(json.dumps({"text": format_sample(sample), "category": sample["category"]}) + "\n")

    category_counts = Counter(s["category"] for s in samples)
    unique_outputs = len(set(s["output"] for s in samples))
    uniqueness_pct = unique_outputs / len(samples) * 100
    print(f"Generated {len(samples)} samples ({unique_outputs} unique outputs, {uniqueness_pct:.1f}% unique):")
    print(f"  Train: {len(train_samples)}, Eval: {num_eval}")
    print(f"  Topics: {len(all_topics)}")
    print("\nBy category:")
    for category, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        print(f"  {category}: {count}")
