"""Device detection — pick the best available accelerator.

Order of preference: CUDA (NVIDIA GPU) → MPS (Apple Silicon) → CPU.
"""

import torch


def get_device(preference: str = "auto") -> torch.device:
    """Return a torch.device based on preference.

    Args:
        preference: "auto" picks the best available. Otherwise uses the
                    specified device name directly ("cuda", "mps", "cpu").
    """
    if preference != "auto":
        return torch.device(preference)
    if torch.cuda.is_available():
        return torch.device("cuda")
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")
