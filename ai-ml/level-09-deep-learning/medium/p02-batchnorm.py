"""
LEVEL 09 — Deep Learning
MEDIUM P02 — Batch Normalization
========================================

CONCEPT:
  BatchNorm normalizes each layer's inputs to mean=0, std=1
  DURING training — stabilizes and speeds up learning.
  Without it, later layers chase a moving target.

  nn.BatchNorm1d(features) between Linear and ReLU.

PROBLEM:
  Write `compare_bn()` that trains two MLPs on the same data:
    Model A: Linear(10→64) → ReLU → Linear(64→2)
    Model B: Linear(10→64) → BatchNorm1d(64) → ReLU → Linear(64→2)
    Same data, same epochs, same lr. Returns (loss_A, loss_B)

TRY THIS INPUT:
  ```python
  a, b = compare_bn()
  print(f"No BN: {a:.4f}  With BN: {b:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  No BN: ~0.6x   With BN: ~0.6x
  (BN usually converges faster — lower loss in same epochs)
  ```

HINT:
  nn.Sequential(Linear(10,64), BatchNorm1d(64), ReLU(), Linear(64,2))

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# a, b = compare_bn()
# print(a, b)
