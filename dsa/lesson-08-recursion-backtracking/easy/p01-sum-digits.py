"""
LESSON 08 — Recursion & Backtracking
EASY P01 — Sum Digits Recursively
============================================

CONCEPT:
  The three questions: (1) returns an int — the digit sum; (2) base
  case n == 0 -> 0; (3) shrink via n // 10 which drops the last digit.
  One digit's contribution + the recursive promise = the whole answer.
  That's the leap of faith: trust sum_digits(n // 10) already works.

PROBLEM:
  Write `sum_digits(n: int) -> int` RECURSIVELY — no loops, no
  str()/list tricks — returning the sum of n's decimal digits.
  Assume n >= 0. sum_digits(1234) -> 1+2+3+4 = 10.

TRY THIS INPUT:
  ```python
  print(sum_digits(1234))
  print(sum_digits(0))
  print(sum_digits(999))
  ```

EXPECTED OUTPUT:
  ```
  10
  0
  27
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
