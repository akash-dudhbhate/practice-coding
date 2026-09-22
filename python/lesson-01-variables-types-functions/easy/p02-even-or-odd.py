"""
LESSON 01 — Variables, Types & Functions
EASY P02 — Even or Odd
============================================

CONCEPT:
  The modulo operator % gives the remainder of a division. An even
  number divided by 2 has remainder 0, so `n % 2 == 0` is True exactly
  when n is even. Booleans (True/False) are values you can return
  directly from a function.

PROBLEM:
  Write a function `is_even(n: int) -> bool` that returns True if n
  is even and False if n is odd.


"""
def even_or_odd(num):
 if num% 2==0 :
  return "even"
 else :
  return "odd"
print(even_or_odd(10))
print(even_or_odd(7))
