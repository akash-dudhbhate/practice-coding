"""
LESSON 02 — Strings & String Methods
EASY P01 — Count Vowels
============================================

CONCEPT:
  Strings are sequences of characters, so you can loop over them one
  character at a time. Checking membership in a set like {'a','e','i','o','u'}
  is a fast way to ask "is this character a vowel?".

PROBLEM:
  Write a function `count_vowels(text: str) -> int` that returns the
  number of vowels (a, e, i, o, u) in `text`, case-insensitive.

TRY THIS INPUT:
  ```python
  print(count_vowels("hello"))
  print(count_vowels("AEIOU"))
  print(count_vowels("rhythm"))
  ```

EXPECTED OUTPUT:
  ```
  2
  5
  0
  ```

CHECK: python3 check.py easy/p01
"""
def count_vowels(text:str)->int:
    count =0
    for char in text.lower():
        if char in "aeiou":
            count +=1
            return count
print(count_vowels("hello"))
print(count_vowels("AEIOU"))
print(count_vowels("rhythm"))
