"""
LESSON 01 — Variables, Types & Functions
MEDIUM P03 — Count Vowels
============================================

CONCEPT:
  A string is a sequence of characters, so a `for` loop visits each
  character one at a time. Keep a counter variable, add 1 whenever the
  character is a vowel, and return the counter at the end — this
  "loop and accumulate" pattern shows up everywhere.

PROBLEM:
  Write a function `count_vowels(text: str) -> int` that returns the
  number of vowels (a, e, i, o, u) in `text`. The count must be
  case-insensitive, so 'A' counts just like 'a'.

TRY THIS INPUT:
  ```python
  print(count_vowels("hello"))
  print(count_vowels("AEIOU"))
  print(count_vowels("xyz"))
  ```

EXPECTED OUTPUT:
  ```
  2
  5
  0
  ```

CHECK: python3 check.py medium/p03
"""

def count_vowels(text:str)->int:
    count =0
    for char in text.lower():
        if char in "aeiou":
            count +=1
            return count
print(count_vowels("hello"))
print(count_vowels("AEIOU"))
print(count_vowels("xyz"))
