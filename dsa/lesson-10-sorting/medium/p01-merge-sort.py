"""
LESSON 10 — Sorting
MEDIUM P01 — Implement Merge Sort
============================================

CONCEPT:
  Divide and conquer: split the array in half, recursively sort
  each half, then merge the two sorted halves (the pointer walk
  from easy/p03). O(n log n) GUARANTEED — every level does O(n)
  merge work and there are log n levels. Cost: O(n) extra space.

PROBLEM:
  Write `merge_sort(arr: list) -> list` returning a NEW sorted
  list. Do NOT use sorted() or list.sort() — implement split +
  recursion + merge yourself.

TRY THIS INPUT:
  ```python
  print(merge_sort([5, 2, 4, 1, 3]))
  print(merge_sort([]))
  print(merge_sort([3, -1, 0, -7]))
  ```

EXPECTED OUTPUT:
  ```
  [1, 2, 3, 4, 5]
  []
  [-7, -1, 0, 3]
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
