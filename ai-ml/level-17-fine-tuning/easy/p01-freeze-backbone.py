"""
LEVEL 17 — Fine-Tuning / LoRA
EASY P01 — Freeze the Backbone
========================================

CONCEPT:
  Fine-tuning a pretrained model usually means: keep most weights
  frozen, update only a few. In PyTorch you freeze a parameter with
      param.requires_grad_(False)
  A frozen param gets no gradient → the optimizer can't change it.

PROBLEM:
  Write `freeze_backbone(model)` that:
    1. Freezes EVERY parameter in the model EXCEPT the last layer's
       (for nn.Sequential(Linear, ReLU, Linear): freeze model[0],
       leave model[2] trainable — ReLU has no params anyway)
    2. Returns the number of trainable parameters remaining

  Signature:
      def freeze_backbone(model):
          # model: nn.Sequential(Linear(8,32), ReLU, Linear(32,3))
          # returns: int — count of params with requires_grad == True

TRY THIS INPUT:
  ```python
  import torch, torch.nn as nn
  torch.manual_seed(42)
  model = nn.Sequential(nn.Linear(8,32), nn.ReLU(), nn.Linear(32,3))
  n = freeze_backbone(model)
  print(n)                                 # trainable params left
  print(model[0].weight.requires_grad)     # should be False
  print(model[2].weight.requires_grad)     # should be True
  ```

EXPECTED OUTPUT:
  ```
  99            # 32*3 weights + 3 biases in the last Linear
  False
  True
  ```

HINT:
  Loop over `model.parameters()` — but skip the last layer.
  `list(model.children())` gives [Linear, ReLU, Linear].

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import torch, torch.nn as nn
# torch.manual_seed(42)
# model = nn.Sequential(nn.Linear(8,32), nn.ReLU(), nn.Linear(32,3))
# print(freeze_backbone(model))
