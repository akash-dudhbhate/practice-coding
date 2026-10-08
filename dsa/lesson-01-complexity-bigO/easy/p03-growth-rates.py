"""
LESSON 01 — Time/Space Complexity & Big-O
EASY P03 — Growth Rates
============================================

CONCEPT:
  Big-O classes grow at wildly different speeds. Seeing real numbers
  makes it concrete: at n=8, O(2^n) is already 256 while O(log n) is 3.

PROBLEM:
  Write a function `growth_values(n: int) -> dict` returning a dict
  with keys "O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)",
  "O(2^n)" mapping to their op counts at size n. Use math.log2 and
  int() for the log terms.

TRY THIS INPUT:
  ```python
  print(growth_values(8))
  ```

EXPECTED OUTPUT:
  ```
  {'O(1)': 1, 'O(log n)': 3, 'O(n)': 8, 'O(n log n)': 24, 'O(n^2)': 64, 'O(2^n)': 256}
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
