"""
LESSON 09 — OOP Basics
MEDIUM P03 — Temperature Class
============================================

CONCEPT:
  `@classmethod` gets the class itself (`cls`) — perfect for
  alternate constructors. `@staticmethod` is a plain function that
  lives on the class for namespacing.

PROBLEM:
  Write a class `Temperature` with `__init__(self, celsius)`, a
  classmethod `from_fahrenheit(f)` that builds a Temperature from a
  Fahrenheit value, a staticmethod `to_fahrenheit(c)` converting
  Celsius to Fahrenheit, and an instance method `fahrenheit()`.

TRY THIS INPUT:
  ```python
  t = Temperature(100)
  print(t.fahrenheit())
  t2 = Temperature.from_fahrenheit(32)
  print(round(t2.celsius))
  ```

EXPECTED OUTPUT:
  ```
  212.0
  0
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
