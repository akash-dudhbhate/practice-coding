"""
LESSON 07 — File I/O & Error Handling
EASY P02 — Write File
============================================

CONCEPT:
  Opening a file with mode "w" creates it (or truncates it) so you
  can write text. `with` makes sure it is flushed and closed.

PROBLEM:
  Write a function `write_file(path, text)` that writes `text` to
  `path` in overwrite mode using `with`. Return True on success,
  False if anything goes wrong.

TRY THIS INPUT:
  ```python
  print(write_file("/tmp/out.txt", "content"))
  print(open("/tmp/out.txt").read())
  ```

EXPECTED OUTPUT:
  ```
  True
  content
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
