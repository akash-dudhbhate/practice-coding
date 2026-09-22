"""
LESSON 05 — Control Flow & Loops
HARD P02 — Find Pair
============================================

CONCEPT:
  Nested loops let you try every combination: outer loop picks index i,
  inner loop picks j (starting at i+1 so you don't repeat pairs).
  Returning inside both loops exits as soon as the first match is found.

PROBLEM:
  Write a function `find_pair(nums: list, target: int) -> tuple` that
  returns the indices (i, j) of the first pair of numbers summing to
  `target`. Return None if no pair exists. Use nested loops.

TRY THIS INPUT:
  ```python
  print(find_pair([2, 7, 11, 15], 9))
  print(find_pair([1, 2, 3], 10))
  ```

EXPECTED OUTPUT:
  ```
  (0, 1)
  None
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
