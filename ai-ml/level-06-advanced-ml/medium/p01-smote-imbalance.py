"""
LEVEL 06 — Advanced ML
MEDIUM P01 — Fix Imbalance by Resampling
========================================

CONCEPT:
  With 95% class-0 / 5% class-1, a model can get 95% accuracy by
  predicting 0 always — useless. Fix: OVERSAMPLE the minority class
  (duplicate random samples) until classes are balanced.

  Manual oversampling (no extra libraries needed):
    minority = X[y==1]; repeat/choice until counts match.

PROBLEM:
  Write `oversample(X, y)` that:
    1. Finds majority/minority class counts
    2. Randomly resamples the minority (with replacement) to match
    3. Returns (X_balanced, y_balanced) as numpy arrays
  np.random.seed(42) inside the function.

TRY THIS INPUT:
  ```python
  X = np.arange(100).reshape(-1, 1)   # 100 samples
  y = np.array([0]*95 + [1]*5)        # 95:5 imbalance
  Xb, yb = oversample(X, y)
  print(np.bincount(yb))   # [95 95]
  ```

EXPECTED OUTPUT:
  ```
  [95 95]
  ```

HINT:
  minority_idx = np.where(y == minority_label)[0]
  np.random.choice(minority_idx, size=needed, replace=True)

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import numpy as np
# Xb, yb = oversample(np.arange(100).reshape(-1,1), np.array([0]*95+[1]*5))
# print(np.bincount(yb))
