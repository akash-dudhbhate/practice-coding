"""
LESSON 03 — Hashing (Dict & Set Patterns)
HARD P01 — Longest Consecutive Sequence (must be O(n))
============================================

CONCEPT:
  Put all numbers in a set for O(1) membership. Then only start
  counting a run from a number that is a RUN START — i.e. `x - 1` is
  NOT in the set. From each run start, walk x+1, x+2, ... while they
  exist. Each number is visited at most twice total -> O(n). Sorting
  would work but costs O(n log n).

PROBLEM:
  Write a function `longest_consecutive(nums: list) -> int` that
  returns the length of the longest run of consecutive integers
  (in any order, duplicates allowed in input). Must run in O(n).

TRY THIS INPUT:
  ```python
  print(longest_consecutive([100, 4, 200, 1, 3, 2]))
  print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
  print(longest_consecutive([]))
  ```

EXPECTED OUTPUT:
  ```
  4
  9
  0
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
