"""
PROBLEM: Leap Year (Medium)
===========================

CONCEPT: Conditionals, boolean logic, combining multiple conditions.

# See concepts.md in this lesson folder for detailed explanations (WHY/WHERE/WHAT-GOES-WRONG).

# TODO: Write your complete solution from scratch below (function signature + body).
#       Remove this TODO line when done.
"""

# a=2024
# b=2021
# if a%400==0 or a%4==0:
#     print("a is leap year")
# else:
#     print("b is leap year")
    
#  output:   a is leap year

# logic behind it: we use logical operater "or " so 1 st condition a is divided by 400 is false and a is divided by 4 is true
# so or means both value are f then it return f otherwise True
# here f or t=t then codition is ru and prints a is leap year

a=2024
b=2021
if a%400==0 and a%4==0:
    print("a is leap year")
else:
    print("b is leap year")
    
#  output:b is leap year
#  bcoz weused and operator   