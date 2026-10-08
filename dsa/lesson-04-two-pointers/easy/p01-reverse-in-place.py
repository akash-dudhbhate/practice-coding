"""
LESSON 04 — Two Pointers
EASY P01 — Reverse a List In Place
============================================

CONCEPT:
  Opposite-end pointers: put L at index 0 and R at the last index,
  swap arr[L] and arr[R], then move both inward (L += 1, R -= 1).
  Stop when L >= R. O(n) time, O(1) extra space — no copy.

PROBLEM:
  Write a function `reverse_in_place(arr: list) -> list` that reverses
  `arr` IN PLACE (mutates the given list, no new list, no slicing)
  and returns it.

TRY THIS INPUT:
  ```python
  a = [1, 2, 3, 4]
  print(reverse_in_place(a))   # same object, mutated
  print(a)
  print(reverse_in_place([]))
  ```

EXPECTED OUTPUT:
  ```
  [4, 3, 2, 1]
  [4, 3, 2, 1]
  []
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
