"""
LESSON 11 — Modules & Packages
MEDIUM P03 — Listing Files with os and pathlib
============================================

CONCEPT:
  `pathlib.Path` is the modern, object-oriented way to work with files
  and folders. `Path(dir).glob("*.py")` finds matching files and
  `path.stat().st_size` gives a file's size in bytes.

PROBLEM:
  Write a function `list_py_files(directory=".")` that returns a list
  of `(filename, size_in_bytes)` tuples for every `.py` file directly
  inside `directory`. Then print them in a `__main__` block.

TRY THIS INPUT:
  ```python
  # given a folder containing a.py (10 bytes) and b.py (20 bytes):
  for name, size in list_py_files("some_folder"):
      print(f"{name}: {size} bytes")
  ```

EXPECTED OUTPUT:
  ```
  some_folder/a.py: 10 bytes
  some_folder/b.py: 20 bytes
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
