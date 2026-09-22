"""
LEVEL 01 — ML Foundations
HARD P03 — Bias-Variance Tradeoff
====================================

CONCEPT:
  Bias     = error from oversimplified assumptions.
             High bias → underfitting (fails on both train and test)

  Variance = error from sensitivity to training data.
             High variance → overfitting (memorizes training, fails on new)

  Tradeoff = you can't have both low bias AND low variance.
             More complex → lower bias but higher variance.
             Simpler → higher bias but lower variance.

PROBLEM:
  Write a function `explain()` that returns a dictionary answering:

  Questions:
    1. bias: what is bias in one sentence?
    2. variance: what is variance in one sentence?
    3. high_bias: high bias + low variance = ? (underfitting/overfitting)
    4. high_variance: low bias + high variance = ? (underfitting/overfitting)
    5. tree_100_65: 100% train, 65% test — high bias or high variance?
    6. linear_70_70: 70% train, 70% test — high bias or high variance?
    7. tradeoff: why can't we have both low bias AND low variance?

TRY THIS INPUT:
  ```python
  result = explain()
  print(result["high_bias"])      # "underfitting"
  print(result["high_variance"])  # "overfitting"
  print(result["tree_100_65"])    # "high variance"
  ```

EXPECTED OUTPUT:
  ```
  {
    "bias": "Error from oversimplified assumptions — model is too simple",
    "variance": "Error from sensitivity to training data — model memorizes noise",
    "high_bias": "underfitting",
    "high_variance": "overfitting",
    "tree_100_65": "high variance (overfitting) — fix: prune the tree, limit depth",
    "linear_70_70": "high bias (underfitting) — fix: use a more complex model",
    "tradeoff": "Reducing bias increases variance and vice versa — it's a balance"
  }
  ```

Write your function below.
CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# Uncomment to test your solution:
# result = explain()
# for key, value in result.items():
#     print(f"{key}: {value}")
