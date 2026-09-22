"""Level 17 — Fine-Tuning / LoRA — Easy P02 Solution"""

import torch
import torch.nn as nn


def count_trainable(model):
    """Return (total_params, trainable_params)."""
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return total, trainable


if __name__ == "__main__":
    torch.manual_seed(42)
    model = nn.Sequential(nn.Linear(8, 32), nn.ReLU(), nn.Linear(32, 3))
    print(count_trainable(model))
    for p in model[0].parameters():
        p.requires_grad_(False)
    print(count_trainable(model))
