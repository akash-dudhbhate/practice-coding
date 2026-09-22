"""
PROBLEM: FizzBuzz (Hard)
========================

CONCEPT: Loops, conditionals, combining multiple conditions, order of checks.

# See concepts.md in this lesson folder for detailed explanations (WHY/WHERE/WHAT-GOES-WRONG).

"""

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))