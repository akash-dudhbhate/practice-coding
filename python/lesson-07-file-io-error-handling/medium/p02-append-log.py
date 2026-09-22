"""
LESSON 07 — File I/O & Error Handling
MEDIUM P02 — Append Log
============================================

CONCEPT:
  Mode "a" opens a file for appending — new text goes at the end and
  the file is created if it doesn't exist yet.

PROBLEM:
  Write a function `append_log(path, message)` that appends
  `message` plus a newline to the file at `path`, creating the file
  if missing.

TRY THIS INPUT:
  ```python
  append_log("/tmp/log.txt", "First")
  append_log("/tmp/log.txt", "Second")
  print(open("/tmp/log.txt").read())
  ```

EXPECTED OUTPUT:
  ```
  First
  Second
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
