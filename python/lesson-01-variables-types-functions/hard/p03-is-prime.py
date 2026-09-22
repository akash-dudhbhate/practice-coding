"""
LESSON 01 — Variables, Types & Functions
HARD P03 — Is Prime
============================================

CONCEPT:
  A prime number is only divisible by 1 and itself, so to test n you
  check whether anything from 2 up to n-1 divides it evenly. Edge
  cases matter here: numbers below 2 (0, 1, negatives) are not prime.
  You only need to check divisors up to the square root of n — if a
  bigger divisor existed, its partner would already have been found.

PROBLEM:
  Write a function `is_prime(n: int) -> bool` that returns True if n
  is prime and False otherwise. Remember: 0, 1, and negative numbers
  are NOT prime; 2 IS prime.

TRY THIS INPUT:
  ```python
  print(is_prime(7))
  print(is_prime(1))
  print(is_prime(4))
  print(is_prime(13))
  ```

EXPECTED OUTPUT:
  ```
  True
  False
  False
  True
  ```

CHECK: python3 check.py hard/p03
"""

def is_prime(n:int)-> bool:
    if n<=1:
        return False

    for i in range(2,n):
        if n %i == 0:
            return False
    return True


print(is_prime(7))
print(is_prime(1))
print(is_prime(4))
print(is_prime(13))
