"""
LESSON 10 — Sorting
HARD P03 — Sort a Nearly-Sorted Array Efficiently
============================================

CONCEPT:
  If every element is at most k positions away from its final
  place, the correct element for output position i is always
  among the next k+1 inputs. Keep a min-heap of size k+1: push
  the first k+1 elements, then for each remaining element push it
  and pop the smallest into the output; drain the heap at the
  end. O(n log k) — beats O(n log n) when k << n.

PROBLEM:
  Write `sort_nearly_sorted(arr: list, k: int) -> list` returning
  a NEW sorted list. Guarantee: each element starts at most k
  indices away from its final sorted position. Use heapq — a full
  re-sort is correct but wastes the k-neighborhood structure.

TRY THIS INPUT:
  ```python
  print(sort_nearly_sorted([6, 5, 3, 2, 8, 10, 9], 3))
  print(sort_nearly_sorted([2, 1, 3], 1))
  print(sort_nearly_sorted([], 3))
  ```

EXPECTED OUTPUT:
  ```
  [2, 3, 5, 6, 8, 9, 10]
  [1, 2, 3]
  []
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
