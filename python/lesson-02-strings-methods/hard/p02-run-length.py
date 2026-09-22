"""
LESSON 02 — Strings & String Methods
HARD P02 — Run-Length Encoding
============================================

CONCEPT:
  Run-length encoding compresses repeated characters into char+count
  pairs. Walking the string while comparing each character to the
  previous one lets you count runs — when the character changes, you
  flush the run and reset the counter.

PROBLEM:
  Write a function `run_length_encode(s: str) -> str` that compresses a
  string using run-length encoding: "aaabbc" -> "a3b2c1". Every run gets
  a count, even a single character ("abc" -> "a1b1c1"). Empty -> "".

TRY THIS INPUT:
  ```python
  print(run_length_encode("aaabbc"))
  print(run_length_encode("abc"))
  print(run_length_encode("aaaa"))
  ```

EXPECTED OUTPUT:
  ```
  a3b2c1
  a1b1c1
  a4
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
