"""
LESSON 13 — Iterators & Generators
HARD P01 — read_lines File Generator
============================================

CONCEPT:
  Iterating a file object already yields lines lazily, so wrapping it in
  a generator lets you process huge files without loading them into
  memory. A generator can also `try/except` around setup work — like a
  missing file — and just stop early.

PROBLEM:
  Write a generator `read_lines(filename)` that opens the file and
  yields each line with the trailing newline stripped. If the file does
  not exist, print a warning and yield nothing (don't crash).

TRY THIS INPUT:
  ```python
  # file contains: line1\\nline2\\nline3
  print(list(read_lines("myfile.txt")))
  print(list(read_lines("/does/not/exist.txt")))
  ```

EXPECTED OUTPUT:
  ```
  ['line1', 'line2', 'line3']
  Warning: /does/not/exist.txt not found
  []
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
