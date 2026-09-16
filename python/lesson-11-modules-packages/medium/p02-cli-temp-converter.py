"""
LESSON 11 — Modules & Packages
MEDIUM P02 — CLI Temperature Converter
============================================

CONCEPT:
  `sys.argv` gives your script access to command-line arguments:
  `sys.argv[0]` is the script name, the rest are the arguments the user
  typed. Combined with `__name__ == "__main__"` this is how small CLI
  tools are built.

PROBLEM:
  Write two functions:
    - `celsius_to_fahrenheit(c)` — returns c * 9 / 5 + 32
    - `fahrenheit_to_celsius(f)` — returns (f - 32) * 5 / 9
  Then add a `__main__` block that reads a temperature and a unit
  (C or F) from `sys.argv` and prints the converted value with 1 decimal,
  e.g. `python3 p02-*.py 100 C` prints `212.0 F`.

TRY THIS INPUT:
  ```python
  print(f"{celsius_to_fahrenheit(100):.1f} F")
  print(f"{fahrenheit_to_celsius(32):.1f} C")
  ```

EXPECTED OUTPUT:
  ```
  212.0 F
  0.0 C
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
