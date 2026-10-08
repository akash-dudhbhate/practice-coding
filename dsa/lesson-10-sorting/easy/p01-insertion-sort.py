"""
LESSON 10 — Sorting
EASY P01 — Implement Insertion Sort
============================================

CONCEPT:
  Grow a sorted prefix one element at a time: take arr[i], shift
  every bigger element in arr[0..i-1] one slot right, and drop the
  element into the gap. O(n^2) worst case but O(n) on nearly-sorted
  input — that's why real sorts use it for small slices.

PROBLEM:
  Write `insertion_sort(arr: list) -> list` that sorts `arr`
  ascending IN PLACE (mutates it) and returns it. Do NOT use
  sorted(), list.sort(), or any other built-in sort — implement
  the algorithm.

TRY THIS INPUT:
  ```python
  a = [5, 2, 4, 1, 3]
  print(insertion_sort(a))
  print(insertion_sort([]))
  print(insertion_sort([3, -1, 0]))
  ```

EXPECTED OUTPUT:
  ```
  [1, 2, 3, 4, 5]
  []
  [-1, 0, 3]
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
