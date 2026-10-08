"""
LESSON 02 — Arrays & Strings
EASY P03 — Char Frequency
============================================

CONCEPT:
  Tally characters in a dict during one scan — O(n). The alternative,
  calling text.count(c) per character, rescans the string each time
  and is O(n^2).

PROBLEM:
  Write a function `char_freq(text: str) -> dict` returning a dict
  mapping each character to its count (case-sensitive).

TRY THIS INPUT:
  ```python
  print(char_freq("aab"))
  print(char_freq("hello"))
  print(char_freq(""))
  ```

EXPECTED OUTPUT:
  ```
  {'a': 2, 'b': 1}
  {'h': 1, 'e': 1, 'l': 2, 'o': 1}
  {}
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
