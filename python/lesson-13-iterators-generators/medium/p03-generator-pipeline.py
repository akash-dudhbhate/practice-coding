"""
LESSON 13 — Iterators & Generators
MEDIUM P03 — Generator Pipeline
============================================

CONCEPT:
  Generators chain beautifully: each stage consumes the previous one
  lazily, so the whole pipeline processes items one at a time — no
  intermediate lists, minimal memory.

PROBLEM:
  Build a pipeline of 4 generator functions:
    - `generate_nums(n)` — yields 1..n
    - `filter_multiples_of_3(gen)` — yields only x where x % 3 == 0
    - `square_them(gen)` — yields x * x
    - `take_first(gen, n)` — yields at most the first n items
  Chain them: numbers 1-100 → multiples of 3 → squared → first 5.

TRY THIS INPUT:
  ```python
  pipeline = take_first(square_them(filter_multiples_of_3(generate_nums(100))), 5)
  print(list(pipeline))
  ```

EXPECTED OUTPUT:
  ```
  [9, 36, 81, 144, 225]
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
