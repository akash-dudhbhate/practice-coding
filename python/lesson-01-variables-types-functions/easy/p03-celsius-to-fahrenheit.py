"""
PROBLEM: Celsius to Fahrenheit (Easy)
=====================================

CONCEPT: Variables, types, functions, arithmetic, return values.

# See concepts.md in this lesson folder for detailed explanations (WHY/WHERE/WHAT-GOES-WRONG).

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