"""
LESSON 06 — Stacks & Queues
EASY P02 — Reverse a String With a Stack
============================================

CONCEPT:
  A stack reverses order for free: push each character left-to-right,
  then pop them all — they come out right-to-left. This is why undo
  systems and the function call stack are built on LIFO.

PROBLEM:
  Write a function `reverse_with_stack(s: str) -> str` that returns the
  reversed string. You must actually use a stack (a list with
  append/pop) — no slicing tricks like s[::-1], no reversed().

TRY THIS INPUT:
  ```python
  print(reverse_with_stack("hello"))
  print(reverse_with_stack("abc"))
  print(reverse_with_stack(""))
  print(reverse_with_stack("racecar"))
  ```

EXPECTED OUTPUT:
  ```
  olleh
  cba

  racecar
  ```
  (The third line is an empty string — prints as a blank line.)

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
