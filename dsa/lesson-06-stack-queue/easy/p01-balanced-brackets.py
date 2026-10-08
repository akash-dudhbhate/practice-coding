"""
LESSON 06 — Stacks & Queues
EASY P01 — Balanced Brackets
============================================

CONCEPT:
  THE canonical stack problem. Push every opener; on every closer, the
  top of the stack MUST be its matching opener — because the correct
  match is always the MOST RECENT unclosed opener (LIFO). After the
  scan, the stack must be empty.

PROBLEM:
  Write a function `is_balanced(s: str) -> bool` that returns True if
  every opening bracket (), [], {} has a matching closer in the right
  order. Ignore non-bracket characters. Empty string is balanced.

TRY THIS INPUT:
  ```python
  print(is_balanced("{[()]}"))
  print(is_balanced("([)]"))
  print(is_balanced("()[]{}"))
  print(is_balanced("((("))
  ```

EXPECTED OUTPUT:
  ```
  True
  False
  True
  False
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
