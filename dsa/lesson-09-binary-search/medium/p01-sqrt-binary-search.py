"""
LESSON 09 — Binary Search
MEDIUM P01 — Integer Square Root via Binary Search
============================================

CONCEPT:
  The answer lives in a RANGE, not an array: sqrt(x) is somewhere
  in [0, x]. "Is mid*mid <= x?" is a monotone predicate — true for
  all small mid, false for all big mid. Binary search for the last
  mid where it's still true.

PROBLEM:
  Write a function `my_sqrt(x: int) -> int` that returns
  floor(sqrt(x)) WITHOUT using math.sqrt or ** 0.5.
  floor means round down: sqrt(8) = 2.82... → return 2.

TRY THIS INPUT:
  ```python
  print(my_sqrt(4))
  print(my_sqrt(8))
  print(my_sqrt(0))
  print(my_sqrt(15))
  ```

EXPECTED OUTPUT:
  ```
  2
  2
  0
  3
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
