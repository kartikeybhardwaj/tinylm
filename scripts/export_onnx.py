import logging
import os
import shutil
import warnings

import torch

from froglm.config import FrogConfig
from froglm.model import FrogLM

logging.getLogger("torch.onnx").setLevel(logging.ERROR)


def export():
    os.makedirs("docs", exist_ok=True)

    config = FrogConfig()
    model = FrogLM(config)
    ckpt = torch.load("checkpoints/best_model.pt", map_location="cpu", weights_only=False)
    model.load_state_dict(ckpt["model_state_dict"], strict=False)
    model.eval()

    dummy = torch.randint(0, 100, (1, config.max_seq_len - 1))

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        torch.onnx.export(
            model,
            dummy,
            "docs/model.onnx",
            input_names=["input_ids"],
            output_names=["logits"],
            dynamic_axes={"input_ids": {1: "seq_len"}, "logits": {1: "seq_len"}},
            opset_version=18,
        )
    print("Exported to docs/model.onnx")

    from onnxruntime.quantization import QuantType, quantize_dynamic

    quantize_dynamic("docs/model.onnx", "docs/model_q.onnx", weight_type=QuantType.QUInt8)
    print("Quantized to docs/model_q.onnx")

    shutil.copy("data/tokenizer.json", "docs/tokenizer.json")
    print("Copied tokenizer to docs/tokenizer.json")


if __name__ == "__main__":
    export()
