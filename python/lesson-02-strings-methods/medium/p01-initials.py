"""
LESSON 02 — Strings & String Methods
MEDIUM P01 — Get Initials
============================================

CONCEPT:
  .split() breaks a string into a list of words, and indexing word[0]
  grabs the first letter of each. .join() then glues those letters back
  into one string — a common split-process-join pipeline.

PROBLEM:
  Write a function `get_initials(name: str) -> str` that takes a full
  name and returns the initials in uppercase. "John Doe" -> "JD".
  Extra whitespace between names should be handled; empty input -> "".

TRY THIS INPUT:
  ```python
  print(get_initials("John Doe"))
  print(get_initials("Akash  Dev"))
  print(get_initials("single"))
  ```

EXPECTED OUTPUT:
  ```
  JD
  AD
  S
  ```

CHECK: python3 check.py medium/p01
"""


def get_initials(name:str)->str:
    words = name.split()
    initials =""

    for word in words:
        initials  += word[0].upper()

    return initials

print(get_initials("John Doe"))
print(get_initials("Akash  Dev"))
print(get_initials("single"))
print(get_initials("Utkarsaha Narsale"))
print(get_initials("Madhuri Mukhekar "))
print(get_initials("Divya Hilal"))