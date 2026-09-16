"""
LEVEL 17 — Fine-Tuning / LoRA
EASY P03 — Replace the Classification Head
========================================

CONCEPT:
  A pretrained model splits into BACKBONE (feature extractor) and
  HEAD (final classifier). New task with a different number of
  classes? Throw the head away and attach a fresh Linear layer.
  The backbone keeps everything it learned; the new head starts
  from random init and gets trained on the new task.

PROBLEM:
  Write `replace_head(model, n_classes)` that:
    1. Finds the LAST Linear layer of `model` (it's model[-1])
    2. Replaces it with a new nn.Linear(same_in_features, n_classes)
    3. Returns the modified model

  Signature:
      def replace_head(model, n_classes):
          # model: nn.Sequential(Linear(8,32), ReLU, Linear(32,3))
          # returns: nn.Sequential with a new final Linear

TRY THIS INPUT:
  ```python
  import torch, torch.nn as nn
  torch.manual_seed(42)
  model = nn.Sequential(nn.Linear(8,32), nn.ReLU(), nn.Linear(32,3))
  model = replace_head(model, 5)
  print(model[-1])
  out = model(torch.randn(4, 8))
  print(out.shape)   # batch of 4, 5 classes
  ```

EXPECTED OUTPUT:
  ```
  Linear(in_features=32, out_features=5, bias=True)
  torch.Size([4, 5])
  ```

HINT:
  `model[-1].in_features` tells you the input size to preserve.
  Assigning `model[-1] = nn.Linear(...)` mutates the Sequential.

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import torch, torch.nn as nn
# torch.manual_seed(42)
# model = nn.Sequential(nn.Linear(8,32), nn.ReLU(), nn.Linear(32,3))
# model = replace_head(model, 5)
# print(model(torch.randn(4,8)).shape)
