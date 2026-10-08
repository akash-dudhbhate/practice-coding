"""
LESSON 12 — Heaps
HARD P03 — Reorganize String
============================================

CONCEPT:
  Rearrange so no two adjacent chars are equal. Greedy: always place
  the most frequent remaining char — a max-heap on (freq, char).
  The guardrail: you may NOT place the char you just placed — hold
  it aside for one step, push it back next round. Impossibility is
  decided by pigeonhole: max_freq > (len(s)+1)//2 means even perfect
  alternation can't separate the copies.

PROBLEM:
  Write `reorganize_string(s) -> str` — any valid rearrangement,
  or "" if impossible.

TRY THIS INPUT:
  ```python
  print(reorganize_string("aab"))
  print(reorganize_string("aaab"))
  print(reorganize_string("aaabbc"))
  print(reorganize_string(""))
  ```

EXPECTED OUTPUT:
  ```
  aba          (or any valid arrangement)
               ("" — impossible: 3 a's can't be separated in length 4)
  ababca       (or any valid arrangement)
               ("" — empty in, empty out)
  ```

CHECK: python3 check.py hard/p03
  (The checker validates properties: same letters, no adjacent
   dupes — OR "" exactly when the task is provably impossible.)
"""

import heapq
from collections import Counter

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
