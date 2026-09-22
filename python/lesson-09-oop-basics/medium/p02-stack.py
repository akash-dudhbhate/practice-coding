"""
LESSON 09 — OOP Basics
MEDIUM P02 — Stack Class
============================================

CONCEPT:
  A class can wrap a list to present a restricted interface — only
  the operations a stack allows: push, pop, peek. `__len__` makes
  `len(obj)` work.

PROBLEM:
  Write a class `Stack` backed by a list with `push(item)`,
  `pop()` (raise IndexError if empty), `peek()` (raise IndexError
  if empty), `is_empty()`, and `__len__`.

TRY THIS INPUT:
  ```python
  s = Stack()
  s.push(1)
  s.push(2)
  print(len(s), s.pop(), s.peek())
  ```

EXPECTED OUTPUT:
  ```
  2 2 1
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
