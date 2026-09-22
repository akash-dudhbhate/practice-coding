"""
LEVEL 00 — Setup & Math
MEDIUM P02 — Min-Max Normalization
========================================

CONCEPT:
  Features on different scales confuse models (age 0-100 vs
  income 0-100000). Normalization squashes everything to [0, 1]:

    normalized = (x - min) / (max - min)

  Example: [10, 20, 30] → [0.0, 0.5, 1.0]

PROBLEM:
  Write `normalize(data)` that min-max normalizes a list to [0, 1].
  No sklearn — pure Python.

TRY THIS INPUT:
  ```python
  print(normalize([10, 20, 30]))        # [0.0, 0.5, 1.0]
  print(normalize([5, 5, 5]))           # edge case! what happens?
  ```

EXPECTED OUTPUT:
  ```
  [0.0, 0.5, 1.0]
  ```
  For the edge case: if max == min, return all zeros (avoid ÷0).

HINT:
  mn, mx = min(data), max(data)
  guard: if mx == mn return [0.0] * len(data)

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(normalize([10, 20, 30]))
