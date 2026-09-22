"""
LESSON 07 — File I/O & Error Handling
MEDIUM P01 — Count Lines
============================================

CONCEPT:
  `f.readlines()` gives a list of lines, so `len()` counts them.
  A missing file raises FileNotFoundError — catch it for a fallback.

PROBLEM:
  Write a function `count_lines(path)` that returns the number of
  lines in the file. Return 0 if the file does not exist.

TRY THIS INPUT:
  ```python
  # file contains: line1 \\n line2 \\n line3
  print(count_lines("three_line_file.txt"))
  print(count_lines("/nonexistent"))
  ```

EXPECTED OUTPUT:
  ```
  3
  0
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
