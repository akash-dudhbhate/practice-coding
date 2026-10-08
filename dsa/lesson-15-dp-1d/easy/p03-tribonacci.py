"""
LESSON 15 — 1D Dynamic Programming
EASY P03 — Tribonacci
============================================

CONCEPT:
  Same skeleton, one term deeper: each state reads THREE cells back.
  T(n) = T(n-1) + T(n-2) + T(n-3). The exercise is noticing that the
  recipe doesn't change — only the recurrence's reach does.

PROBLEM:
  Write `tribonacci(n: int) -> int` with T(0) = 0, T(1) = 1,
  T(2) = 1, and T(n) = T(n-1) + T(n-2) + T(n-3) for n >= 3.
  Handle n < 3 without index errors.

TRY THIS INPUT:
  ```python
  print(tribonacci(4))
  print(tribonacci(25))
  print(tribonacci(37))
  ```

EXPECTED OUTPUT:
  ```
  4
  1389537
  2082876103
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
