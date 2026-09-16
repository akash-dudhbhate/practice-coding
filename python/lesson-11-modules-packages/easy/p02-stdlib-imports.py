"""
LESSON 11 — Modules & Packages
EASY P02 — Importing from the Standard Library
============================================

CONCEPT:
  Python ships with a huge standard library — modules like `math` and
  `random` that you can use with a simple `import` statement, no
  installation needed. After `import math` you call its tools with the
  dotted form: `math.sqrt(16)`.

PROBLEM:
  Write a script that imports `math` and `random` from the standard
  library. Inside `if __name__ == "__main__":`, generate 3 random
  integers between 1 and 100 with `random.randint`, then print each
  number's square root using `math.sqrt` formatted to 2 decimals.

TRY THIS INPUT:
  ```python
  import math
  print(f"sqrt({16}) = {math.sqrt(16):.2f}")
  ```

EXPECTED OUTPUT:
  ```
  sqrt(16) = 4.00
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
