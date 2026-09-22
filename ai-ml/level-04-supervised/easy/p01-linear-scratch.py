"""
LEVEL 04 — Supervised Learning
EASY P01 — Linear Regression From Scratch
========================================

CONCEPT:
  Linear regression finds the best line y = mx + b.
  Closed-form formula:
    m = Σ((x - x̄)(y - ȳ)) / Σ((x - x̄)²)
    b = ȳ - m·x̄
  R² measures fit quality: 1 = perfect, 0 = no better than mean.

PROBLEM:
  Write `linreg(x, y)` that takes two lists and returns (m, b).

TRY THIS INPUT:
  ```python
  m, b = linreg([1,2,3,4,5], [2,4,5,4,5])
  print(f"{m:.4f} {b:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  0.6000 2.2000
  ```

HINT:
  x_mean = np.mean(x); numerator = np.sum((x - x_mean) * (y - y_mean))

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# m, b = linreg([1,2,3,4,5], [2,4,5,4,5])
# print(m, b)
