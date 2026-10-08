"""
LESSON 18 — Advanced Mix
MEDIUM P03 — Next Greater Element (Circular)
============================================

CONCEPT:
  Monotonic stack of INDICES holding unresolved elements (values
  decreasing top→bottom). A new value pops every index it dominates and
  becomes their answer. Circular twist: loop i over range(2*n), read
  nums[i % n] — the second lap resolves leftovers via wraparound — but
  PUSH only when i < n, or indices get stacked twice.

PROBLEM:
  Write a function `next_greater_elements(nums: list[int]) -> list[int]`.
  For each index, return the next element strictly greater, searching
  circularly (the array wraps around); -1 if none exists. nums may
  contain duplicates; a single-element array answers [-1].

TRY THIS INPUT:
  ```python
  print(next_greater_elements([1,2,1]))
  print(next_greater_elements([1,2,3,4,3]))
  print(next_greater_elements([5,4,3,2,1]))
  print(next_greater_elements([1,2,3,2,1]))
  print(next_greater_elements([3]))
  ```

EXPECTED OUTPUT:
  ```
  [2, -1, 2]
  [2, 3, 4, -1, 4]
  [-1, 5, 5, 5, 5]
  [2, 3, -1, 3, 2]
  [-1]
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
