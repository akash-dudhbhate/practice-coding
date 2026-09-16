"""
LEVEL 00B — Weights & Training
EASY P03 (Chapter 3) — The Loss Table
======================================

CONCEPT:
  Before fixing weights, MEASURE how wrong they are. StatQuest's
  method: for each example, residual = prediction − truth.
  Square each residual, add them all → that's the loss.
  loss = 0 means perfect. Squaring punishes big mistakes extra.

PROBLEM:
  Write loss(data, w, b) where data = [(x, truth), ...]:
    for each (x, truth): pred = w*x + b; res = pred − truth
    return the SUM of res² over all rows.

TRY THIS INPUT:
  ```python
  data = [(1000, 200), (2000, 400)]
  print(loss(data, 0.3, 0))   # wrong weight — big loss
  print(loss(data, 0.2, 0))   # right weight — zero loss
  ```

EXPECTED OUTPUT:
  ```
  50000.0
  0.0
  ```
  (0.3: residuals +100,+200 → 100² + 200² = 50000)

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement loss(data, w, b)


def loss(data, w, b):
    """Sum of squared residuals — the number training tries to shrink."""
    pass


# === TEST ===
# data = [(1000, 200), (2000, 400)]
# print(loss(data, 0.3, 0))
# print(loss(data, 0.2, 0))
