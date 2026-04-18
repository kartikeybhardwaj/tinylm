"""Entry point for: python -m froglm"""

import os
import sys


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
        from .data.tokenizer import prepare

        prepare()
    elif cmd == "train":
        from .train import train

        train()
    elif cmd == "chat":
        if not os.path.exists("checkpoints/best_model.pt"):
            print("Model not found. Train first:\n")
            print("  python -m froglm prepare")
            print("  python -m froglm train")
            return
        from .inference import main as inference_main

        inference_main()
    elif cmd == "eval":
        if not os.path.exists("checkpoints/best_model.pt"):
            print("Model not found. Train first.")
            return
        from .eval import run_eval
        from .inference import FrogInference

        engine = FrogInference("checkpoints/best_model.pt", "data/tokenizer.json")
        run_eval(engine)
    else:
        print(f"Unknown command: {cmd}")
        print("Run 'python -m froglm' for usage.")


if __name__ == "__main__":
    main()
