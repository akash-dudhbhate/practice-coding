"""
LEVEL 00B — Weights & Training
MEDIUM P01 (Chapter 4) — One Training Step
============================================

CONCEPT:
  The residual's sign says which way to fix the weight:
    residual positive → prediction too high → decrease w
    residual negative → prediction too low  → increase w
  Update rule:  new_w = w − step × residual × input
  (the ×input scales the fix to how much this input caused;
   the minus walks DOWNHILL on the loss)

PROBLEM:
  Write train_step(x, truth, w, b, step) → returns (new_w, new_b):
      pred = w*x + b
      res  = pred − truth
      new_w = w − step*res*x
      new_b = b − step*res          # bias's "input" is always 1

TRY THIS INPUT:
  ```python
  print(train_step(1000, 200, w=0.3, b=0, step=0.0000001))
  ```

EXPECTED OUTPUT:
  ```
  (0.29, -1e-05)
  ```
  (residual +100 → w shrank 0.3→0.29, b dropped to −0.00001 —
   bias pushes the too-high prediction DOWN too)

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement train_step(x, truth, w, b, step)


def train_step(x, truth, w, b, step):
    """One gradient step on one example → (new_w, new_b)."""
    pass


# === TEST ===
# print(train_step(1000, 200, 0.3, 0, 0.0000001))
