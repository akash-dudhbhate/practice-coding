"""
LESSON 02 — Strings & String Methods
MEDIUM P02 — Count Words
============================================

CONCEPT:
  .split() with no arguments splits on ANY run of whitespace, so multiple
  spaces and leading/trailing gaps are handled for free. len() on the
  resulting list gives the word count.

PROBLEM:
  Write a function `count_words(sentence: str) -> int` that returns the
  number of words in `sentence`. Extra spaces around or between words
  shouldn't throw off the count. Empty string -> 0.

TRY THIS INPUT:
  ```python
  print(count_words("Hello world"))
  print(count_words("  one  two  three  "))
  print(count_words(""))
  ```

EXPECTED OUTPUT:
  ```
  2
  3
  0
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
