"""
LEVEL 00B — Weights & Training
EASY P01 (Chapter 1) — One Weight
===================================

CONCEPT:
  A model is a function. The simplest: prediction = weight × input.
  The weight is a number the model stores — a volume knob on the
  input. Change it, the answer changes. Training = finding the
  right knob position.

PROBLEM:
  Write predict(size, weight) → returns weight * size.
  Our data says 1000 sqft → $200k, so the right weight is 0.2.
  See what wrong weights do.

TRY THIS INPUT:
  ```python
  print(predict(1000, 0.2))   # right weight
  print(predict(1000, 0.5))   # too big
  print(predict(1000, 0.0))   # input gets no vote at all
  ```

EXPECTED OUTPUT:
  ```
  200.0
  500.0
  0.0
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement predict(size, weight)


def predict(size, weight):
    """prediction = weight × size — that's the whole model."""
    pass


# === TEST ===
# print(predict(1000, 0.2))
# print(predict(1000, 0.5))
# print(predict(1000, 0.0))
