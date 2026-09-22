"""
PROBLEM: Even or Odd (Easy)
============================

CONCEPT: Variables, types, functions, modulo operator.

# See concepts.md in this lesson folder for detailed explanations (WHY/WHERE/WHAT-GOES-WRONG).

"""

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_or_odd(10))
print(even_or_odd(7))