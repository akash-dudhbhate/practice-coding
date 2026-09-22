"""
LESSON 05 — Control Flow & Loops
HARD P01 — Is Palindrome (Two Pointers)
============================================

CONCEPT:
  The two-pointer technique puts one index at each end and walks them
  toward the middle, comparing characters as it goes. It checks a
  palindrome without ever building a reversed copy.

PROBLEM:
  Write a function `is_palindrome(s: str) -> bool` that returns True if
  `s` reads the same forwards and backwards (case-insensitive), using
  a loop with two pointers — no slicing ([::-1]) allowed.

TRY THIS INPUT:
  ```python
  print(is_palindrome("racecar"))
  print(is_palindrome("hello"))
  print(is_palindrome(""))
  ```

EXPECTED OUTPUT:
  ```
  True
  False
  True
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
