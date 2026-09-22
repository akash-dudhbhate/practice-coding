"""
LESSON 01 — Variables, Types & Functions
EASY P01 — Max of Two Numbers
============================================

CONCEPT:
  A function takes inputs (parameters) and gives back a result with
  `return`. To compare two values you use an `if` statement: if the
  first is bigger, return it, otherwise return the second.

PROBLEM:
  Write a function `max_of_two(a: int, b: int) -> int` that returns
  the larger of the two integers. If they are equal, return either one.
  Do NOT use the built-in max() — write the comparison yourself.

TRY THIS INPUT:
  ```python
  print(max_of_two(3, 7))
  print(max_of_two(10, 5))
  print(max_of_two(4, 4))
  ```

EXPECTED OUTPUT:
  ```
  7
  10
  4
  ```

CHECK: python3 check.py easy/p01
"""
a=10
b=2
def max_of_two(a,b):
    if a>b: 
        return a
    else:
        return b
    
print(max_of_two(a, b))




