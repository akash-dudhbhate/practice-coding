"""
LEVEL 00B — Weights & Training
HARD P01 (Chapter 7) — Gradient Descent
=========================================

CONCEPT:
  The real training loop — medium/p01 + medium/p03 repeated until
  the loss is tiny:
      repeat N rounds:
          for each (x,truth): res = w*x + b − truth
          w −= step × mean(res·x);  b −= step × mean(res)
  This is gradient descent — the algorithm inside PyTorch.

PROBLEM:
  Write fit(data, step, rounds) → (w, b):
      start w=0.0, b=0.0
      loop `rounds` times doing a batch update (your medium/p03 code)
      return final (w, b)

TRY THIS INPUT:
  ```python
  data = [(1000, 200), (2000, 400), (1500, 300)]
  w, b = fit(data, step=0.0000001, rounds=500)
  print(round(w, 4), round(b, 4))
  ```

EXPECTED OUTPUT:
  ```
  0.2 0.0
  ```
  The model DISCOVERED w=0.2 — nobody told it. That's learning.

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement fit(data, step, rounds)


def fit(data, step, rounds):
    """Gradient descent: loop batch updates, return (w, b)."""
    pass


# === TEST ===
# data = [(1000, 200), (2000, 400), (1500, 300)]
# w, b = fit(data, step=0.0000001, rounds=500)
# print(round(w, 4), round(b, 4))
