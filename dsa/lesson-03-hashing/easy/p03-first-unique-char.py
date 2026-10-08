"""
LESSON 03 — Hashing (Dict & Set Patterns)
EASY P03 — First Unique Character
============================================

CONCEPT:
  Two passes with a frequency table. Pass 1: count every character.
  Pass 2: scan the string again and return the index of the first
  character whose count is 1. The second pass preserves order — the
  set/dict alone can't tell you who came FIRST.

PROBLEM:
  Write a function `first_unique_char(s: str) -> int` that returns
  the index of the first character that appears exactly once, or -1
  if there is none.

TRY THIS INPUT:
  ```python
  print(first_unique_char("leetcode"))
  print(first_unique_char("loveleetcode"))
  print(first_unique_char("aabb"))
  ```

EXPECTED OUTPUT:
  ```
  0
  2
  -1
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
