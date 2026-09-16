"""
LESSON 03 — Lists & Tuples
HARD P02 — Second Largest
============================================

CONCEPT:
  set(nums) collapses duplicates so "second largest" means second
  largest UNIQUE value. Sorting the unique values descending puts the
  answer at index 1 — but only if at least 2 unique values exist.

PROBLEM:
  Write a function `second_largest(nums: list)` that returns the
  second largest unique value in `nums`. Return None if there are
  fewer than 2 unique values.

TRY THIS INPUT:
  ```python
  print(second_largest([5, 1, 4, 4, 3]))
  print(second_largest([1, 1, 1]))
  print(second_largest([3, 1]))
  ```

EXPECTED OUTPUT:
  ```
  4
  None
  1
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
