"""
LESSON 07 — Linked Lists
EASY P01 — Build a Linked List
============================================

CONCEPT:
  A linked list is nodes + pointers: each Node holds `val` and `next`.
  Building from a Python list uses a dummy head + tail pointer so the
  first attach looks like every other attach. You'll reuse the Node
  class you define here in every problem this lesson.

PROBLEM:
  Define `class Node` with `__init__(self, val=0, next=None)`, then
  write `build_list(values: list) -> Node` that returns the head of a
  chain containing the values IN ORDER: build_list([1,2,3]) must
  produce 1 -> 2 -> 3 -> None (NOT reversed). Return None for [].

TRY THIS INPUT:
  ```python
  # assuming a to_list() helper that walks .next and collects .val:
  print(to_list(build_list([1, 2, 3])))
  print(to_list(build_list([])))
  print(to_list(build_list([7])))
  ```

EXPECTED OUTPUT:
  ```
  [1, 2, 3]
  []
  [7]
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
