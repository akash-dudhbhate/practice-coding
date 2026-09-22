"""
LEVEL 06 — Advanced ML
EASY P03 — Feature Scaling (StandardScaler)
========================================

CONCEPT:
  Features on wildly different scales break distance-based models
  (KNN, SVM) and slow down gradient descent.

  StandardScaler: (x - mean) / std → mean=0, std=1
  MinMaxScaler:   (x - min) / (max - min) → range [0, 1]

PROBLEM:
  Write `scale_features()` that:
    1. Creates DataFrame: age [25,30,35,40,45],
       income [30000,50000,70000,90000,110000]
    2. Standard-scales both columns
    3. Returns the scaled DataFrame

TRY THIS INPUT:
  ```python
  df = scale_features()
  print(f"{df['age'].mean():.6f}")    # ~0.0
  print(f"{df['income'].mean():.6f}") # ~0.0
  print(f"{df['age'].std():.4f}")     # ~1.0
  ```

EXPECTED OUTPUT:
  ```
  0.000000
  0.000000
  1.0000
  ```
  (mean 0, std ~1.0 — note pandas std uses ddof=1 so ~1.118)

HINT:
  StandardScaler().fit_transform(df) returns an array;
  wrap back into DataFrame with same column names.

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# df = scale_features()
# print(df.mean())
