"""
LESSON 12 — Heaps
EASY P03 — Top-K Frequent Words
============================================

CONCEPT:
  Top-K on a computed key (frequency), with a TIEBREAK. Heap entries
  compare lexicographically, so push tuples where element order IS
  the sort order: (-freq, word) puts high frequency first and
  alphabetical order second — negating the count turns "most
  frequent" into "smallest heap entry."

PROBLEM:
  Write `top_k_frequent_words(words, k) -> list[str]` — the k most
  frequent words. Higher frequency first; ties break alphabetically
  (ascending). Assume k <= number of distinct words.

TRY THIS INPUT:
  ```python
  print(top_k_frequent_words(["i","love","leetcode","i","love","coding"], 2))
  print(top_k_frequent_words(["i","love","leetcode","i","love","coding"], 3))
  print(top_k_frequent_words(["the","day","is","sunny","the","the","the",
                              "sunny","is","is"], 4))
  ```

EXPECTED OUTPUT:
  ```
  ['i', 'love']
  ['i', 'love', 'coding']
  ['the', 'is', 'sunny', 'day']
  ```

CHECK: python3 check.py easy/p03
"""

import heapq
from collections import Counter

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
