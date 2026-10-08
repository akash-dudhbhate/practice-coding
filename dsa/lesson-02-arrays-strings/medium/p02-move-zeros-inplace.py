"""
LESSON 02 — Arrays & Strings
MEDIUM P02 — Move Zeros In-Place
============================================

CONCEPT:
  In-place array edits use a WRITE POINTER: scan with a read pointer,
  write kept elements at position w, then fill the tail. O(n) time,
  O(1) extra space — and the caller's list is actually mutated.

PROBLEM:
  Write a function `move_zeros(nums: list) -> None` that moves all
  zeros to the end IN PLACE while keeping the order of non-zero
  elements. Do NOT return a new list — mutate `nums` itself.

TRY THIS INPUT:
  ```python
  a = [0, 1, 0, 3, 12]
  move_zeros(a)
  print(a)
  b = [0, 0, 1]
  move_zeros(b)
  print(b)
  ```

EXPECTED OUTPUT:
  ```
  [1, 3, 12, 0, 0]
  [1, 0, 0]
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
