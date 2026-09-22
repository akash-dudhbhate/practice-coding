"""
LESSON 07 — File I/O & Error Handling
HARD P02 — Process File
============================================

CONCEPT:
  Real files are messy: blank lines, bad rows, missing files. Robust
  code skips bad data, warns about it, and re-raises errors the
  caller must know about.

PROBLEM:
  Write a function `process_file(path)` that reads a file with one
  number per line and returns the sum.
    - Skip blank lines.
    - Skip non-numeric lines, printing a warning for each.
    - If the file doesn't exist, raise FileNotFoundError with a
      clear message.

TRY THIS INPUT:
  ```python
  # file contains: 10, 20, (blank), abc, 30
  print(process_file("nums.txt"))
  ```

EXPECTED OUTPUT:
  ```
  Warning: skipping non-numeric line: abc
  60
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
