"""
LEVEL 17 — Fine-Tuning / LoRA
EASY P02 — Count Trainable Parameters
========================================

CONCEPT:
  Parameter-efficient fine-tuning is all about the ratio
      trainable_params / total_params
  Before you can shrink it, you have to measure it.
  `p.numel()` gives the number of elements in a parameter tensor.

PROBLEM:
  Write `count_trainable(model)` that returns a tuple:
      (total_params, trainable_params)
  where total = every parameter, trainable = params with
  requires_grad == True.

  Signature:
      def count_trainable(model):
          # returns: (int, int)

TRY THIS INPUT:
  ```python
  import torch, torch.nn as nn
  torch.manual_seed(42)
  model = nn.Sequential(nn.Linear(8,32), nn.ReLU(), nn.Linear(32,3))
  print(count_trainable(model))
  for p in model[0].parameters(): p.requires_grad_(False)
  print(count_trainable(model))
  ```

EXPECTED OUTPUT:
  ```
  (387, 387)   # 8*32+32 + 32*3+3 = 288 + 99
  (387, 99)    # only the head is trainable after freezing
  ```

HINT:
  Two generator expressions over `model.parameters()`,
  one filtered on `p.requires_grad`.

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import torch, torch.nn as nn
# torch.manual_seed(42)
# model = nn.Sequential(nn.Linear(8,32), nn.ReLU(), nn.Linear(32,3))
# print(count_trainable(model))
