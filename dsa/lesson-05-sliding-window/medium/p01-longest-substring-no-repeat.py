"""
LESSON 05 — Sliding Window
MEDIUM P01 — Longest Substring Without Repeating Characters
============================================

CONCEPT:
  A VARIABLE-size window. Expand right; when a character you've already
  got in the window enters, the window is invalid — shrink left until
  the duplicate is gone. Track each character's last-seen index (or a
  count dict) so you know how far to shrink.

PROBLEM:
  Write a function `length_of_longest_substring(s: str) -> int` that
  returns the length of the longest substring of s with no repeated
  characters.

TRY THIS INPUT:
  ```python
  print(length_of_longest_substring("abcabcbb"))
  print(length_of_longest_substring("bbbbb"))
  print(length_of_longest_substring("pwwkew"))
  print(length_of_longest_substring(""))
  ```

EXPECTED OUTPUT:
  ```
  3
  1
  3
  0
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
