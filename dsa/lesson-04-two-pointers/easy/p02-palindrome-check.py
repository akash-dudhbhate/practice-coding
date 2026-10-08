"""
LESSON 04 — Two Pointers
EASY P02 — Palindrome Check (ignore non-alphanumeric)
============================================

CONCEPT:
  Opposite-end pointers walk inward comparing characters. Skip any
  character that isn't alphanumeric (advance the pointer past it),
  compare the rest case-insensitively. O(n) time, O(1) space — no
  cleaned-copy needed (though building one is acceptable).

PROBLEM:
  Write a function `is_palindrome(s: str) -> bool` that returns True
  if `s` reads the same forwards and backwards, considering ONLY
  letters and digits and ignoring case.

TRY THIS INPUT:
  ```python
  print(is_palindrome("A man, a plan, a canal: Panama"))
  print(is_palindrome("race a car"))
  print(is_palindrome(" "))
  ```

EXPECTED OUTPUT:
  ```
  True
  False
  True
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
