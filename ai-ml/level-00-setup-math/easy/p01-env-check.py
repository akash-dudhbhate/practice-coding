"""
LEVEL 00 — Setup & Math
EASY P01 — Environment Check
========================================

CONCEPT:
  Before any ML work, verify your tools import and run.
  This catches broken installs early.

PROBLEM:
  Write `check_env()` that:
    1. Imports numpy, pandas, sklearn
    2. Returns a dict with their version strings:
       {"numpy": "x.y.z", "pandas": "x.y.z", "sklearn": "x.y.z"}

TRY THIS INPUT:
  ```python
  env = check_env()
  print(env["numpy"])   # e.g. "2.2.6"
  ```

EXPECTED OUTPUT:
  ```
  {'numpy': '2.2.6', 'pandas': '2.x.x', 'sklearn': '1.x.x'}
  ```
  (exact versions depend on your install — just needs all 3 keys)

HINT:
  import numpy; numpy.__version__

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(check_env())
