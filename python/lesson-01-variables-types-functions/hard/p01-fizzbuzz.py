"""
LESSON 01 — Variables, Types & Functions
HARD P01 — FizzBuzz
============================================

CONCEPT:
  When several conditions can be true at once, the ORDER of your
  if/elif checks matters. A number divisible by both 3 and 5 (like 15)
  must be handled before the single-divisor checks, or it will be
  caught by the wrong branch first.

PROBLEM:
  Write a function `fizzbuzz(n: int) -> list` that returns a list of
  strings for the numbers 1 to n: multiples of 3 become "Fizz",
  multiples of 5 become "Buzz", multiples of both become "FizzBuzz",
  and every other number becomes its own string (e.g. 1 -> "1").

TRY THIS INPUT:
  ```python
  print(fizzbuzz(5))
  print(fizzbuzz(3))
  ```

EXPECTED OUTPUT:
  ```
  ['1', '2', 'Fizz', '4', 'Buzz']
  ['1', '2', 'Fizz']
  ```

CHECK: python3 check.py hard/p01
"""
def fizzbuzz(n:int)-> list:
    result =[]
    for i in range(1,n+1):
        if i % 3== 0 and i % 5==0:
            result.append("FizzBuzz")
        elif i% 3==0:
            result.append ("Fizz")
        elif i % 5==0:
            result.append ("Buzz")
        else:
             result.append (str(i))
    return result
print(fizzbuzz(5))
print(fizzbuzz(3))