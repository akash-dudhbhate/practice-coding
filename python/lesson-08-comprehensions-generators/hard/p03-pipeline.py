"""
LESSON 08 — Comprehensions & Generators
HARD P03 — Generator Pipeline
============================================

CONCEPT:
  Generators chain naturally: each stage consumes the previous one
  lazily, so data flows through the pipeline one item at a time.

PROBLEM:
  Write three generator functions and one combiner:
    - `filter_positive(data)` — yields only items > 0
    - `double(data)` — yields each item * 2
    - `to_strings(data)` — yields each item as a string
    - `pipeline(data)` — chains all three and returns the final list.

TRY THIS INPUT:
  ```python
  print(pipeline([-1, 2, -3, 4]))
  print(pipeline([]))
  ```

EXPECTED OUTPUT:
  ```
  ['4', '8']
  []
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
