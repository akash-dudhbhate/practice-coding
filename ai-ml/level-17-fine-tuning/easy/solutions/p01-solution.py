"""Level 17 — Fine-Tuning / LoRA — Easy P01 Solution"""

import torch
import torch.nn as nn


def freeze_backbone(model):
    """Freeze all parameters except the last layer's; return trainable count."""
    layers = list(model.children())
    for layer in layers[:-1]:
        for p in layer.parameters():
            p.requires_grad_(False)
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


if __name__ == "__main__":
    torch.manual_seed(42)
    model = nn.Sequential(nn.Linear(8, 32), nn.ReLU(), nn.Linear(32, 3))
    n = freeze_backbone(model)
    print(f"Trainable params: {n}")
    print(f"Backbone frozen: {not model[0].weight.requires_grad}")
    print(f"Head trainable: {model[2].weight.requires_grad}")
