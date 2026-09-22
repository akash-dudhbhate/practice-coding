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

# TODO: Write your complete solution from scratch below (function signature + body).
#       Remove this TODO line when done.
"""

# a=2024
# b=2021
# if a%400==0 or a%4==0:
#     print("a is leap year")
# else:
#     print("b is leap year")
    
#  output:   a is leap year

# logic behind it: we use logical operater "or " so 1 st condition a is divided by 400 is false and a is divided by 4 is true
# so or means both value are f then it return f otherwise True
# here f or t=t then codition is ru and prints a is leap year

a=2024
b=2021
if a%400==0 and a%4==0:
    print("a is leap year")
else:
    print("b is leap year")
    
#  output:b is leap year
#  bcoz weused and operator   
