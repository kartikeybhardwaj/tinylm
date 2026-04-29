"""Entry point for: python -m froglm"""

import os
import sys

NAME = "frog"
DATA_DIR = f"data/{NAME}"
CHECKPOINT_DIR = f"checkpoints/{NAME}"


def main():
    if len(sys.argv) < 2:
        print("FrogLM — A tiny frog brain")
        print()
        print("Usage:")
        print("  python -m froglm prepare   Generate data & train tokenizer")
        print("  python -m froglm train     Train the model")
        print("  python -m froglm chat      Chat with Frog")
        print("  python -m froglm eval      Run personality eval cases")
        return

    cmd = sys.argv[1]
    sys.argv = sys.argv[1:]

    if cmd == "prepare":
        from .data.topics import ALL_TOPICS
        from core.data.tokenizer import prepare

        prepare(ALL_TOPICS, data_dir=DATA_DIR)

    elif cmd == "train":
        from core.config import TrainConfig

        tc = TrainConfig(data_dir=DATA_DIR, output_dir=CHECKPOINT_DIR)
        from core.train import train

        train(tc)

    elif cmd == "chat":
        checkpoint_path = os.path.join(CHECKPOINT_DIR, "best_model.pt")
        tokenizer_path = os.path.join(DATA_DIR, "tokenizer.json")
        if not os.path.exists(checkpoint_path):
            print("Model not found. Train first:\n")
            print("  python -m froglm prepare")
            print("  python -m froglm train")
            return

        import argparse

        parser = argparse.ArgumentParser(description="Chat with Frog")
        parser.add_argument("--prompt", "-p", help="Single prompt mode")
        args = parser.parse_args()

        from core.inference import LMInference

        engine = LMInference(checkpoint_path, tokenizer_path)

        if args.prompt:
            print(f"Frog> {engine.chat([{'role': 'user', 'content': args.prompt}])}")
            return

        print("\nFrog Chat (type 'quit' to exit)\n")
        while True:
            try:
                user_input = input("You> ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if user_input.lower() in ("quit", "exit", "q"):
                break
            if not user_input:
                continue
            response = engine.chat([{"role": "user", "content": user_input}])
            print(f"Frog> {response}\n")

    elif cmd == "eval":
        checkpoint_path = os.path.join(CHECKPOINT_DIR, "best_model.pt")
        tokenizer_path = os.path.join(DATA_DIR, "tokenizer.json")
        if not os.path.exists(checkpoint_path):
            print("Model not found. Train first.")
            return
        from core.inference import LMInference
        from core.eval import run_eval
        from .data.eval_cases import EVAL_CASES

        engine = LMInference(checkpoint_path, tokenizer_path)
        run_eval(engine, EVAL_CASES)

    else:
        print(f"Unknown command: {cmd}")
        print("Run 'python -m froglm' for usage.")


if __name__ == "__main__":
    main()
