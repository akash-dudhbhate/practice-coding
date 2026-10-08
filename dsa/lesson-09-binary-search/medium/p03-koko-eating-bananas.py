"""
LESSON 09 — Binary Search
MEDIUM P03 — Koko Eating Bananas
============================================

CONCEPT:
  Another "search the answer": eating speed k is in
  [1, max(piles)]. Hours needed = sum(ceil(pile / k)) — a
  DECREASING function of k: faster speed → fewer hours. Find the
  smallest k where total hours <= h.

PROBLEM:
  Write `min_eating_speed(piles: list, h: int) -> int`: the minimum
  integer speed (bananas/hour) at which Koko finishes all piles
  within `h` hours. Each hour she eats from ONE pile; if a pile
  has fewer than k bananas she finishes it and waits.

TRY THIS INPUT:
  ```python
  print(min_eating_speed([3, 6, 7, 11], 8))
  print(min_eating_speed([30, 11, 23, 4, 20], 5))
  print(min_eating_speed([30, 11, 23, 4, 20], 6))
  ```

EXPECTED OUTPUT:
  ```
  4
  30
  23
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
