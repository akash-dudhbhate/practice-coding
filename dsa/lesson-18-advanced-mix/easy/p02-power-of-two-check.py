"""
LESSON 18 — Advanced Mix
EASY P02 — Power of Two Check
============================================

CONCEPT:
  Powers of two have EXACTLY one set bit (1, 10, 100, 1000...). The
  trick x & (x-1) clears the lowest set bit — for a power of two that's
  the ONLY bit, so the result is 0. Guard with n > 0: zero and negatives
  are not powers of two, and 0 & -1 == 0 would lie.

PROBLEM:
  Write a function `is_power_of_two(n: int) -> bool` returning True iff
  n is a power of two (1, 2, 4, 8, ...). One line suffices — no loops,
  no math.log.

TRY THIS INPUT:
  ```python
  print(is_power_of_two(1))
  print(is_power_of_two(16))
  print(is_power_of_two(3))
  print(is_power_of_two(0))
  print(is_power_of_two(-8))
  print(is_power_of_two(1024))
  ```

EXPECTED OUTPUT:
  ```
  True
  True
  False
  False
  False
  True
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
