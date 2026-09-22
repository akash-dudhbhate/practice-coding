"""
LEVEL 17 — Fine-Tuning / LoRA
MEDIUM P02 — Build a LoRA Linear Layer
========================================

CONCEPT:
  LoRA (Low-Rank Adaptation): instead of retraining a weight
  matrix W (out × in), freeze it and learn a LOW-RANK correction:
      W_eff = W + B @ A
      A: (rank × in)   B: (out × rank)   rank << min(in, out)
  Forward pass:  y = W x + B(A x) = base(x) + (x @ A.T) @ B.T
  Trainable params drop from in*out to rank*(in + out).
  Initialize B = 0 so the layer starts as an exact copy of the base.

PROBLEM:
  Write `lora_linear(in_f, out_f, rank)` that returns an nn.Module
  (e.g. a LoRALinear class instance) where:
    - it wraps a normal nn.Linear(in_f, out_f) whose weight AND bias
      are frozen (requires_grad=False)
    - it has trainable params A (rank × in_f) and B (out_f × rank),
      A ~ small random (e.g. randn * 0.01), B = zeros
    - forward(x) = base(x) + (x @ A.T) @ B.T

  Signature:
      def lora_linear(in_f, out_f, rank):
          # returns: nn.Module — LoRA-wrapped linear layer

TRY THIS INPUT:
  ```python
  import torch
  layer = lora_linear(8, 32, 4)
  x = torch.randn(5, 8)
  print(layer(x).shape)
  trainable = sum(p.numel() for p in layer.parameters() if p.requires_grad)
  total = sum(p.numel() for p in layer.parameters())
  print(trainable, total)
  ```

EXPECTED OUTPUT:
  ```
  torch.Size([5, 32])
  160 448       # 4*8 + 32*4 = 160 trainable, base (256+32) frozen
  ```

HINT:
  class LoRALinear(nn.Module):
      def __init__(self, in_f, out_f, rank): ...
      def forward(self, x): return self.base(x) + (x @ self.A.T) @ self.B.T

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import torch
# layer = lora_linear(8, 32, 4)
# print(layer(torch.randn(5, 8)).shape)
# print(sum(p.numel() for p in layer.parameters() if p.requires_grad))
