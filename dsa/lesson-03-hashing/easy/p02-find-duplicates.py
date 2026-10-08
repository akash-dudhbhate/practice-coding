"""
LESSON 03 — Hashing (Dict & Set Patterns)
EASY P02 — Find Duplicates
============================================

CONCEPT:
  A `seen` set answers "have I seen this value before?" in O(1).
  Collect the repeats in a second set (a value might repeat several
  times but should be reported once), then return it sorted.

PROBLEM:
  Write a function `find_duplicates(nums: list) -> list` that returns
  a sorted list of the values that appear more than once in `nums`.
  Each duplicated value appears exactly once in the result.

TRY THIS INPUT:
  ```python
  print(find_duplicates([4, 3, 2, 4, 3, 5]))
  print(find_duplicates([1, 2, 3]))
  print(find_duplicates([5, 5, 5, 5]))
  ```

EXPECTED OUTPUT:
  ```
  [3, 4]
  []
  [5]
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
