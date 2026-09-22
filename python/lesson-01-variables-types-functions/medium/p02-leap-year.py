"""
LESSON 01 — Variables, Types & Functions
MEDIUM P02 — Leap Year
============================================

CONCEPT:
  Some yes/no questions need several conditions checked in a specific
  order. A year is a leap year if it's divisible by 4 — EXCEPT century
  years (divisible by 100), which are leap years only if also divisible
  by 400. Checking the most specific rule first (400) makes the logic
  simple.

PROBLEM:
  Write a function `is_leap_year(year: int) -> bool` that returns
  True if `year` is a leap year. Rules: divisible by 400 -> True;
  else divisible by 100 -> False; else divisible by 4 -> True;
  otherwise -> False.

TRY THIS INPUT:
  ```python
  print(is_leap_year(2000))
  print(is_leap_year(1900))
  print(is_leap_year(2024))
  ```

EXPECTED OUTPUT:
  ```
  True
  False
  True
  ```

CHECK: python3 check.py medium/p02
"""
def is_leap_year(year:int)->bool:
    if year % 400==0:
        return True
    elif year % 100==0:
        return False
    elif year % 4==0:
        return True
    else:
        return False

print(is_leap_year(2000))
print(is_leap_year(1900))
print(is_leap_year(2024))