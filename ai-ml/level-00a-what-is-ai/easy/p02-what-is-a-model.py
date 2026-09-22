"""
LEVEL 00A — What is AI?
EASY P02 — What is a Model?
==========================

CONCEPT:
  A "model" is just a function. `y = m*x + b` IS a model —
  the simplest possible one. When people say "our model predicts
  house prices" they mean "we have a function that takes size
  and outputs a price."

PROBLEM:
  Write `predict(size_sqft)` that returns `0.2 * size_sqft` —
  a model that says "$200 per square foot" (learned from data).

TRY THIS INPUT:
  ```python
  print(predict(1000))   # 1000 sqft
  print(predict(2000))   # 2000 sqft
  ```

EXPECTED OUTPUT:
  ```
  200.0
  400.0
  ```

WHY THIS MATTERS:
  GPT-4 is the SAME thing — just a function with billions of
  weights instead of one. The concept doesn't change.

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement predict(size_sqft)


def predict(size_sqft):
    """Predict house price: $200 per square foot."""
    pass


# === TEST ===
# print(predict(1000))
# print(predict(2000))
