"""
LESSON 07 — File I/O & Error Handling
EASY P01 — Read File
============================================

CONCEPT:
  `with open(path) as f:` opens a file and closes it automatically.
  `f.read()` returns the whole contents as a string.

PROBLEM:
  Write a function `read_file(path)` that returns the full contents
  of the file at `path` as a string. If the file does not exist,
  catch FileNotFoundError and return None.

TRY THIS INPUT:
  ```python
  print(read_file("some_existing_file.txt"))
  print(read_file("/nonexistent"))
  ```

EXPECTED OUTPUT:
  ```
  <file contents>
  None
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
