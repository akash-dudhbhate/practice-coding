"""
LESSON 02 — Strings & String Methods
MEDIUM P03 — Replace Spaces with Underscores
============================================

CONCEPT:
  String methods can be chained because each one returns a new string.
  .strip() trims whitespace at the ends, and .replace(" ", "_") swaps
  every remaining space for an underscore.

PROBLEM:
  Write a function `replace_spaces(text: str) -> str` that first strips
  leading/trailing whitespace, then replaces every internal space with
  an underscore. "  hello world  " -> "hello_world".

TRY THIS INPUT:
  ```python
  print(replace_spaces("  hello world  "))
  print(replace_spaces("no spaces"))
  print(replace_spaces("  single  "))
  ```

EXPECTED OUTPUT:
  ```
  hello_world
  no_spaces
  single
  ```

CHECK: python3 check.py medium/p03
"""
def replace_spaces(text: str) -> str:
    return text.strip().replace(" ", "_")
print(replace_spaces("  hello world  "))
print(replace_spaces("no spaces"))
print(replace_spaces("  single  "))