"""
LESSON 10 — Sorting
EASY P03 — Merge Two Sorted Arrays
============================================

CONCEPT:
  The merge subroutine — the heart of merge sort. Two sorted
  lists, two pointers: repeatedly take the smaller front element.
  O(len_a + len_b) time, one pass, no comparisons wasted. Master
  this and merge sort is just "split + merge + merge + ...".

PROBLEM:
  Write `merge_two_sorted(a: list, b: list) -> list` returning a
  NEW sorted list containing every element of sorted lists `a`
  and `b`. Do NOT concatenate-and-sort — walk both with pointers.

TRY THIS INPUT:
  ```python
  print(merge_two_sorted([1, 3, 5], [2, 4, 6]))
  print(merge_two_sorted([], [1]))
  print(merge_two_sorted([1, 4], [2, 3]))
  ```

EXPECTED OUTPUT:
  ```
  [1, 2, 3, 4, 5, 6]
  [1]
  [1, 2, 3, 4]
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
