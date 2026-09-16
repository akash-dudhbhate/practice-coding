"""Level 17 — Fine-Tuning / LoRA — Medium P02 Solution"""

import torch
import torch.nn as nn


class LoRALinear(nn.Module):
    """Linear + low-rank adapter: y = (W + B@A) x + b, only A and B train."""

    def __init__(self, in_f, out_f, rank):
        super().__init__()
        self.base = nn.Linear(in_f, out_f)
        for p in self.base.parameters():
            p.requires_grad_(False)
        self.A = nn.Parameter(torch.randn(rank, in_f) * 0.01)
        self.B = nn.Parameter(torch.zeros(out_f, rank))  # zero → identity at init

    def forward(self, x):
        return self.base(x) + (x @ self.A.T) @ self.B.T


def lora_linear(in_f, out_f, rank):
    """Return a LoRA-wrapped Linear layer."""
    return LoRALinear(in_f, out_f, rank)


if __name__ == "__main__":
    torch.manual_seed(42)
    layer = lora_linear(8, 32, 4)
    x = torch.randn(5, 8)
    print("Output shape:", layer(x).shape)
    trainable = sum(p.numel() for p in layer.parameters() if p.requires_grad)
    total = sum(p.numel() for p in layer.parameters())
    print(f"Trainable: {trainable} / {total}")
