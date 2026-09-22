"""
LEVEL 00A — What is AI?
EASY P03 — What are Weights?
============================

CONCEPT:
  Weights are the knobs a model turns. Change a weight → the
  answer changes. "Training" = finding the right weight values.

PROBLEM:
  `predict_with_weight(size, weight)` returns `weight * size`.
  The "right" weight for our data is 0.2 (price = $200/sqft).
  See what happens when the weight is wrong.

TRY THIS INPUT:
  ```python
  print(predict_with_weight(1000, 0.2))   # correct weight
  print(predict_with_weight(1000, 0.5))   # too big
  print(predict_with_weight(1000, 0.1))   # too small
  ```

EXPECTED OUTPUT:
  ```
  200.0
  500.0
  100.0
  ```

WHY THIS MATTERS:
  Same input, different weight → different answer. Training is
  the process of finding weight=0.2 instead of 0.5 or 0.1.
  That's all "learning" means: adjusting weights.

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement predict_with_weight(size, weight)


def predict_with_weight(size, weight):
    """Predict price with a given weight."""
    pass


# === TEST ===
# print(predict_with_weight(1000, 0.2))
# print(predict_with_weight(1000, 0.5))
# print(predict_with_weight(1000, 0.1))
