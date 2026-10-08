"""
LESSON 01 — Time/Space Complexity & Big-O
EASY P02 — Identify Big-O
============================================

CONCEPT:
  You can identify Big-O by watching how op counts change when n
  DOUBLES: constant stays flat, log adds ~1, linear doubles,
  quadratic quadruples, exponential squares.

PROBLEM:
  Write a function `classify_growth(ops_n, ops_2n, ops_4n)` that takes
  measured op counts at sizes n, 2n, and 4n, and returns one of:
  "O(1)", "O(log n)", "O(n)", "O(n^2)", "O(2^n)", or "unknown".

TRY THIS INPUT:
  ```python
  print(classify_growth(7, 7, 7))        # flat -> O(1)
  print(classify_growth(10, 11, 12))     # +1 per doubling -> O(log n)
  print(classify_growth(50, 100, 200))   # x2 per doubling -> O(n)
  print(classify_growth(25, 100, 400))   # x4 per doubling -> O(n^2)
  print(classify_growth(8, 64, 4096))    # squared per doubling -> O(2^n)
  ```

EXPECTED OUTPUT:
  ```
  O(1)
  O(log n)
  O(n)
  O(n^2)
  O(2^n)
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
