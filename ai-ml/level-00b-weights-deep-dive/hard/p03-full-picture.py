"""
LEVEL 00B — Weights & Training
HARD P03 (Chapter 9) — The Full Picture
=========================================

CONCEPT:
  Everything together: train w₁·size + w₂·rooms + b on 4 real
  examples with gradient descent, then predict a NEW house.
  Rooms secretly don't matter in this data — watch the model
  zero out that vote by itself.

PROBLEM:
  Write fit_multi(data, step, rounds) → (weights_list, bias):
      data = [([size, rooms], truth), ...]
      start weights=[0.0, 0.0], b=0.0
      each round, over all rows:
          pred = w₁·x₁ + w₂·x₂ + b ;  res = pred − truth
          each wᵢ −= step × mean(res × xᵢ)
          b       −= step × mean(res)
      return ([w1, w2], b)

TRY THIS INPUT:
  ```python
  data = [
      ([1200, 2], 240), ([1500, 3], 300),
      ([2000, 4], 400), ([1000, 2], 200),
  ]
  w, b = fit_multi(data, step=0.0000002, rounds=3000)
  print([round(x, 4) for x in w], round(b, 4))
  ```

EXPECTED OUTPUT (approximately — within 0.01):
  ```
  [0.2, 0.0] 0.0
  ```
  The model found w₁≈0.2 and ZEROED w₂ — it learned rooms
  don't matter, all by itself. That's feature selection for free.

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement fit_multi(data, step, rounds)


def fit_multi(data, step, rounds):
    """Multi-feature gradient descent → ([w1, w2], b)."""
    pass


# === TEST ===
# data = [
#     ([1200, 2], 240), ([1500, 3], 300),
#     ([2000, 4], 400), ([1000, 2], 200),
# ]
# w, b = fit_multi(data, step=0.0000002, rounds=3000)
# print([round(x, 4) for x in w], round(b, 4))
