"""
LESSON 02 — Arrays & Strings
MEDIUM P01 — Range Sum Queries
============================================

CONCEPT:
  Prefix sums: build P once (P[i] = sum of first i elements) in O(n),
  then answer sum(i..j inclusive) = P[j+1] - P[i] in O(1) per query.
  Re-summing per query is O(q*n); prefix sums make it O(n + q).

PROBLEM:
  Write a function `answer_queries(nums: list, queries: list) -> list`
  that returns a list of sums, one per (i, j) tuple in `queries`.
  Ranges are INCLUSIVE. Build the prefix array ONCE.

TRY THIS INPUT:
  ```python
  print(answer_queries([1, 2, 3, 4, 5], [(0, 2)]))
  print(answer_queries([1, 2, 3, 4, 5], [(0, 2), (1, 4), (2, 2)]))
  print(answer_queries([1, 2, 3, 4, 5], [(0, 4)]))
  ```

EXPECTED OUTPUT:
  ```
  [6]
  [6, 14, 3]
  [15]
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
