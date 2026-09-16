"""
LEVEL 00B — Weights & Training
MEDIUM P03 (Chapter 6) — Many Examples
========================================

CONCEPT:
  One example can lie (noise, typos). Real training averages the
  correction over ALL data each round:
    w −= step × mean(residual_i × input_i)
    b −= step × mean(residual_i)

PROBLEM:
  Write batch_step(data, w, b, step) → (new_w, new_b):
    for each (x, truth): res = w*x + b − truth
    collect res values and res*x values, average each
    apply both updates, return new (w, b)

TRY THIS INPUT:
  ```python
  data = [(1000, 200), (2000, 400), (1500, 300)]
  print(batch_step(data, 0.1, 0.0, 0.0000001))
  ```

EXPECTED OUTPUT:
  ```
  (0.12416666666666668, 1.5000000000000002e-05)
  ```
  (all 3 predictions were too low → w and b both rose)

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement batch_step(data, w, b, step)


def batch_step(data, w, b, step):
    """One gradient step averaging over the whole dataset."""
    pass


# === TEST ===
# data = [(1000, 200), (2000, 400), (1500, 300)]
# print(batch_step(data, 0.1, 0.0, 0.0000001))
