"""
LESSON 11 — Modules & Packages
HARD P02 — requirements.txt Generator
============================================

CONCEPT:
  `pip freeze > requirements.txt` records a project's dependencies so
  others can install them. You can also find dependencies by scanning
  source files for `import` / `from` statements and keeping only the
  modules that are NOT in the standard library.

PROBLEM:
  Write `extract_imports(filepath)` that reads a .py file, collects the
  top-level module name from every `import x` / `from x import y` line,
  filters OUT standard-library modules (keep a STDLIB set of names like
  os, sys, re, json, math, ...), and returns a sorted list of the
  remaining (third-party) module names.

TRY THIS INPUT:
  ```python
  # given a file containing:
  #   import os
  #   import requests
  #   from flask import Flask
  print(extract_imports("that_file.py"))
  ```

EXPECTED OUTPUT:
  ```
  ['flask', 'requests']
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
