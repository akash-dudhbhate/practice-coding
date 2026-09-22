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

# TODO: Write your complete solution from scratch below (function signature + body).
#       Remove this TODO line when done.
"""

# celcius=40
# Fahrenheit=celcius * 9 / 5 + 32
# print(Fahrenheit)


c=20
def celsius_to_fahrenheit(c):
    f = c * 9 / 5 + 32
    return f

print(celsius_to_fahrenheit(c))

# output=68.0
