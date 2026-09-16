"""Level 17 — Fine-Tuning / LoRA — Hard P02 Solution"""

import torch
import torch.nn as nn


def param_efficiency(model, lora_model):
    """Return {'full_trainable', 'lora_trainable', 'ratio'} counts."""
    full = sum(p.numel() for p in model.parameters() if p.requires_grad)
    lora = sum(p.numel() for p in lora_model.parameters() if p.requires_grad)
    return {
        'full_trainable': full,
        'lora_trainable': lora,
        'ratio': lora / full if full > 0 else 0.0,
    }


if __name__ == "__main__":
    torch.manual_seed(42)
    model = nn.Sequential(nn.Linear(8, 32), nn.ReLU(), nn.Linear(32, 3))
    lora_model = nn.Sequential(nn.Linear(8, 32), nn.ReLU(), nn.Linear(32, 3))
    for p in lora_model[0].parameters():
        p.requires_grad_(False)
    print(param_efficiency(model, lora_model))
