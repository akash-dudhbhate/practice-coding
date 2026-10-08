"""
LESSON 18 — Advanced Mix
EASY P03 — Count Set Bits (Brian Kernighan's trick)
============================================

CONCEPT:
  n & (n-1) removes exactly one 1-bit per iteration — the lowest one.
  Loop until n is 0 and count iterations: you do ONE step per set bit,
  not one per bit position. For n treated as a 32-bit integer, mask
  with 0xFFFFFFFF so negative inputs behave.

PROBLEM:
  Write a function `hamming_weight(n: int) -> int` returning the number
  of 1-bits in n's binary representation (treat n as an unsigned 32-bit
  integer). Use the n &= n-1 loop — not bin(n).count('1').

TRY THIS INPUT:
  ```python
  print(hamming_weight(11))       # 1011
  print(hamming_weight(128))      # 10000000
  print(hamming_weight(0))
  print(hamming_weight(255))      # 11111111
  print(hamming_weight(2147483647))
  ```

EXPECTED OUTPUT:
  ```
  3
  1
  0
  8
  31
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
