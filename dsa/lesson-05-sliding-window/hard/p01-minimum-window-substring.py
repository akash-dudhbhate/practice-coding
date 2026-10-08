"""
LESSON 05 — Sliding Window
HARD P01 — Minimum Window Substring
============================================

CONCEPT:
  Variable window + richer bookkeeping. You need every char of t inside
  the window. Track a `need` counter for t, a `window` counter for the
  current window, and `formed` = how many required chars are fully
  satisfied. Expand right until formed == len(need), then shrink left
  recording the smallest valid window.

PROBLEM:
  Write a function `min_window(s: str, t: str) -> str` that returns the
  smallest substring of s containing every character of t (with
  multiplicity). Return "" if no such window exists. Characters are
  case-sensitive; t may contain duplicates.

TRY THIS INPUT:
  ```python
  print(min_window("ADOBECODEBANC", "ABC"))
  print(min_window("a", "a"))
  print(min_window("a", "aa"))
  print(min_window("ab", "b"))
  ```

EXPECTED OUTPUT:
  ```
  BANC
  a

  b
  ```
  (The third line is an empty string — prints as a blank line.)

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
