"""
LESSON 01 — Variables, Types & Functions
EASY P03 — Celsius to Fahrenheit
============================================

CONCEPT:
  Arithmetic in Python works like a calculator: * for multiply, / for
  divide, + for add. Dividing ints with / produces a float, which is
  exactly what you want for a temperature conversion formula.

PROBLEM:
  Write a function `celsius_to_fahrenheit(c: float) -> float` that
  converts a Celsius temperature to Fahrenheit using the formula
  F = C * 9 / 5 + 32 and returns the result.

TRY THIS INPUT:
  ```python
  print(celsius_to_fahrenheit(0))
  print(celsius_to_fahrenheit(100))
  print(celsius_to_fahrenheit(-40))
  ```

EXPECTED OUTPUT:
  ```
  32.0
  212.0
  -40.0
  ```

CHECK: python3 check.py easy/p03
"""

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(-40))
