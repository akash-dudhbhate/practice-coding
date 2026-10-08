"""
LESSON 05 — Sliding Window
HARD P02 — Longest Substring With At Most K Distinct Characters
============================================

CONCEPT:
  Variable window whose validity is "number of distinct characters
  <= k". Window state is a count dict; the window is invalid when
  len(count) > k. Critical detail: when a count hits 0 during shrink,
  DELETE the key so len(count) stays truthful.

PROBLEM:
  Write a function `length_of_longest_k_distinct(s: str, k: int) -> int`
  that returns the length of the longest substring containing at most
  k distinct characters. If k == 0 or s is empty, return 0.

TRY THIS INPUT:
  ```python
  print(length_of_longest_k_distinct("eceba", 2))
  print(length_of_longest_k_distinct("aa", 1))
  print(length_of_longest_k_distinct("abcadcacacaca", 3))
  print(length_of_longest_k_distinct("aabbcc", 2))
  ```

EXPECTED OUTPUT:
  ```
  3
  2
  11
  4
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
