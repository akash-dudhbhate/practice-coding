"""
LESSON 06 — Functions Deep Dive
MEDIUM P02 — Safe Append
============================================

CONCEPT:
  Never use a mutable default like `lst=[]` — Python creates it once
  and every call shares it. Use `lst=None` and build a new list inside.

PROBLEM:
  Write a function `safe_append(item, lst=None)` that appends `item`
  to `lst` and returns the list. When `lst` is None, create a fresh
  list so repeated calls don't accumulate old items.

TRY THIS INPUT:
  ```python
  print(safe_append(1))
  print(safe_append(2))
  print(safe_append(1, [0]))
  ```

EXPECTED OUTPUT:
  ```
  [1]
  [2]
  [0, 1]
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
