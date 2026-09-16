"""
LEVEL 08 — Neural Networks
MEDIUM P02 — PyTorch Linear Model
========================================

CONCEPT:
  torch.nn.Linear(in, out) = a layer: output = x·W + b
  Loss + optimizer + training loop:
    loss = criterion(pred, target)
    optimizer.zero_grad(); loss.backward(); optimizer.step()

  This is the standard PyTorch training pattern — memorize it.

PROBLEM:
  Write `train_linear()` that:
    1. X = torch.randn(100, 1); y = 3*X + 2 + noise
    2. model = nn.Linear(1, 1); optimizer = SGD(lr=0.01)
    3. criterion = MSELoss; train 100 epochs
    4. Returns (final_loss, learned_w, learned_b)

TRY THIS INPUT:
  ```python
  loss, w, b = train_linear()
  print(f"{loss:.4f} {w:.4f} {b:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  ~0.0x  ~3.0  ~2.0   (recovered the true line y = 3x + 2)
  ```

HINT:
  import torch.nn as nn; import torch.optim as optim
  model.weight.item(), model.bias.item()

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# loss, w, b = train_linear()
# print(loss, w, b)
