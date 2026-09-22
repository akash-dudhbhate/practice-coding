"""
LESSON 02 — Strings & String Methods
EASY P02 — Reverse a String
============================================

CONCEPT:
  Strings are immutable — you can't change one in place, so you build a
  new string instead. Prepending each character (char + result) or walking
  the string backwards both produce a reversed copy.

PROBLEM:
  Write a function `reverse_string(s: str) -> str` that returns the
  reversed version of `s` WITHOUT using slicing (no [::-1]).

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

CHECK: python3 check.py easy/p02
"""
def reverse_string(s:str)->str:
   return s[::-1]
print(reverse_string("hello"))
print(reverse_string("abc"))
print(reverse_string(""))