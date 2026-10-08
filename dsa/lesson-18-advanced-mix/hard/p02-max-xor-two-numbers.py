"""
LESSON 18 — Advanced Mix
HARD P02 — Max XOR of Two Numbers (Bitwise Trie)
============================================

CONCEPT:
  O(n^2) pairwise XOR dies at n = 10^5. Insert every number into a trie
  as a path of BITS (most significant first); then for each x, walk the
  trie preferring the OPPOSITE bit at each level — greedy, because a
  flipped high bit contributes more than all lower bits combined. Each
  walk is <= 32 steps → O(32n).

PROBLEM:
  Write a function `find_maximum_xor(nums: list[int]) -> int` returning
  the maximum XOR of any pair (including a number with itself, though
  the max never needs it). Non-negative ints. Fewer than 2 elements
  returns 0.

TRY THIS INPUT:
  ```python
  print(find_maximum_xor([3,10,5,25,2,8]))
  print(find_maximum_xor([0]))
  print(find_maximum_xor([2,4]))
  print(find_maximum_xor([8,10,2]))
  print(find_maximum_xor([14,70,53,83,49,91,36,80,92,51,66,70]))
  ```

EXPECTED OUTPUT:
  ```
  28
  0
  6
  10
  127
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
