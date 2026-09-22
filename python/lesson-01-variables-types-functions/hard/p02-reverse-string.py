"""
LESSON 01 — Variables, Types & Functions
HARD P02 — Reverse a String
============================================

CONCEPT:
  Strings are immutable — you can't change one in place, but you can
  build a NEW string by adding characters one at a time. Prepending
  each character (`result = char + result`) makes the string grow
  backwards, which reverses it.

PROBLEM:
  Write a function `reverse_string(s: str) -> str` that returns the
  string reversed. Do it with a loop — do NOT use slicing ([::-1])
  or reversed(). An empty string should return an empty string.

TRY THIS INPUT:
  ```python
  print(reverse_string("hello"))
  print(reverse_string("abc"))
  print(reverse_string(""))
  ```

EXPECTED OUTPUT:
  ```
  olleh
  cba

  ```

CHECK: python3 check.py hard/p02
"""


def reverse_string(text:str)->str:
    return text[::-1]
print(reverse_string("hello"))
print(reverse_string("abc"))
print(reverse_string(""))
