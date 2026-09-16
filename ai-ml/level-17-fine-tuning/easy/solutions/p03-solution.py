"""Level 17 — Fine-Tuning / LoRA — Easy P03 Solution"""

import torch
import torch.nn as nn


def replace_head(model, n_classes):
    """Swap the final Linear for a new one with n_classes outputs."""
    in_features = model[-1].in_features
    model[-1] = nn.Linear(in_features, n_classes)
    return model


if __name__ == "__main__":
    torch.manual_seed(42)
    model = nn.Sequential(nn.Linear(8, 32), nn.ReLU(), nn.Linear(32, 3))
    model = replace_head(model, 5)
    print(model[-1])
    print(model(torch.randn(4, 8)).shape)
