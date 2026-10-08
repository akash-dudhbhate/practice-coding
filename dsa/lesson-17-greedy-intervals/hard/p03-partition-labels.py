"""
LESSON 17 — Greedy & Intervals
HARD P03 — Partition Labels
============================================

CONCEPT:
  Intervals in disguise: each letter "owns" the range [first index,
  last index] it spans. A part can end only when every letter seen so
  far has finished — i.e., when i reaches the maximum last-index of the
  letters inside it. Precompute last[c]; sweep while extending the
  partition's right edge greedily — same "track the boundary" move as
  Jump Game II.

PROBLEM:
  Write a function `partition_labels(s: str) -> list[int]` that splits s
  into as many parts as possible such that each letter appears in AT
  MOST one part, and returns the list of part sizes in order. Concatenating
  the parts must give back s.

TRY THIS INPUT:
  ```python
  print(partition_labels("ababcbacadefegdehijhklij"))
  print(partition_labels("eccbbbbdec"))
  print(partition_labels("a"))
  print(partition_labels("abac"))
  ```

EXPECTED OUTPUT:
  ```
  [9, 7, 8]
  [10]
  [1]
  [3, 1]
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
