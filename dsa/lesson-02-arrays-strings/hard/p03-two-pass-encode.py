"""
LESSON 02 — Arrays & Strings
HARD P03 — Two-Pass Encode
============================================

CONCEPT:
  Two-pass string transform: pass 1 counts every character (frequency
  dict), pass 2 builds the output labeling each DISTINCT character
  (in first-appearance order) with its total count. Build with join —
  += on strings in a loop is O(n^2).

PROBLEM:
  Write a function `encode_with_freq(text: str) -> str` returning
  "<char><count>" pairs concatenated, where each character appears
  once, in the order it was FIRST seen.

TRY THIS INPUT:
  ```python
  print(encode_with_freq("aabca"))
  print(encode_with_freq("zzz"))
  print(encode_with_freq("ab"))
  print(encode_with_freq(""))
  ```

EXPECTED OUTPUT:
  ```
  a3b1c1
  z3
  a1b1

  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
