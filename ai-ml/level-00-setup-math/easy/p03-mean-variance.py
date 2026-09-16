"""
LEVEL 00 — Setup & Math
EASY P03 — Mean, Variance, Standard Deviation
========================================

CONCEPT:
  mean     = sum / count              (center of the data)
  variance = mean of (x - mean)²      (spread²)
  std      = sqrt(variance)           (spread, same units as data)

  Example: [2, 4, 6]
    mean = 4, variance = ((-2)² + 0² + 2²)/3 = 8/3 ≈ 2.67
    std ≈ 1.63

PROBLEM:
  Write `stats(data)` that returns (mean, variance, std)
  for a list of numbers. No numpy — pure Python.

TRY THIS INPUT:
  ```python
  m, v, s = stats([2, 4, 6])
  print(f"{m:.2f} {v:.2f} {s:.2f}")
  ```

EXPECTED OUTPUT:
  ```
  4.00 2.67 1.63
  ```

HINT:
  variance uses (x - mean)**2 summed, divided by len(data).

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# m, v, s = stats([2, 4, 6])
# print(m, v, s)
