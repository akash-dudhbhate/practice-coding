"""
LEVEL 02 — Python for ML
MEDIUM P02 — Detect and Cap Outliers (IQR)
========================================

CONCEPT:
  Outliers = values far from the rest. They skew models.

  IQR method:
    Q1 = 25th percentile, Q3 = 75th percentile
    IQR = Q3 - Q1
    Outlier if: value < Q1 - 1.5×IQR  OR  value > Q3 + 1.5×IQR

  "Capping" = replace outliers with the boundary value
  (np.clip does this).

PROBLEM:
  Write `detect_outliers(data)` that:
    1. Computes Q1, Q3, IQR, lower/upper bounds
    2. Finds outlier values
    3. Returns (cleaned_array, outlier_count)

TRY THIS INPUT:
  ```python
  data = np.array([1,2,3,4,5,6,7,8,9,100])
  cleaned, n = detect_outliers(data)
  print(f"Outliers found: {n}")
  print(f"Cleaned: {cleaned}")
  ```

EXPECTED OUTPUT:
  ```
  Outliers found: 1
  Cleaned: [ 1.   2.   3.   4.   5.   6.   7.   8.   9.  14.5]
  ```
  (The 100 gets capped to upper bound 14.5)

HINT:
  np.percentile(data, 25) and np.percentile(data, 75).
  np.clip(data, lower, upper) caps values.

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import numpy as np
# data = np.array([1,2,3,4,5,6,7,8,9,100])
# cleaned, n = detect_outliers(data)
# print(n, cleaned)
