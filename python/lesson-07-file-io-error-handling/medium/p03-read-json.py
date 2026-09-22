"""
LESSON 07 — File I/O & Error Handling
MEDIUM P03 — Read JSON
============================================

CONCEPT:
  `json.load(f)` parses a file's JSON text into Python objects.
  Bad JSON raises json.JSONDecodeError; missing files raise
  FileNotFoundError — you can catch both in one except clause.

PROBLEM:
  Write a function `read_json(path)` that reads a JSON file and
  returns the parsed object. Return None if the file is missing or
  contains invalid JSON.

TRY THIS INPUT:
  ```python
  # file contains: {"key": "val"}
  print(read_json("good.json"))
  print(read_json("/nonexistent"))
  # file contains: not json
  print(read_json("bad.json"))
  ```

EXPECTED OUTPUT:
  ```
  {'key': 'val'}
  None
  None
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
