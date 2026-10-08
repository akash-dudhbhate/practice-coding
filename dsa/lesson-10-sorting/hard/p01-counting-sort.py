"""
LESSON 10 — Sorting
HARD P01 — Counting Sort (with Negative Numbers)
============================================

CONCEPT:
  Not all sorting needs comparisons. When keys are integers in a
  small range, count how many times each value appears, then emit
  each value that many times — O(n + k) where k is the value
  range. The catch: values are indices, so NEGATIVES need an
  offset — index = value - min_value.

PROBLEM:
  Write `counting_sort(arr: list) -> list` returning a NEW sorted
  list. Must handle negative numbers, duplicates, and an empty
  input. Do NOT use sorted() or comparison-based sorts — count
  occurrences into a counts array indexed by (value - offset).

TRY THIS INPUT:
  ```python
  print(counting_sort([4, 2, 2, 8, 3, 3, 1]))
  print(counting_sort([-3, 1, -1, 2]))
  print(counting_sort([]))
  ```

EXPECTED OUTPUT:
  ```
  [1, 2, 2, 3, 3, 4, 8]
  [-3, -1, 1, 2]
  []
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
