"""SOLUTION: Calculator Package (Hard)"""
# Simulated package in one file

# basic_ops module
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# advanced_ops module
import math

def power(a, b): return a ** b
def sqrt(a): return math.sqrt(a)
def factorial(n): return math.factorial(n)

# __init__.py equivalent — expose all at package level
__all__ = ["add", "sub", "mul", "div", "power", "sqrt", "factorial"]

if __name__ == "__main__":
    assert add(2, 3) == 5
    assert sub(5, 2) == 3
    assert mul(3, 4) == 12
    assert div(10, 2) == 5.0
    assert power(2, 3) == 8
    assert sqrt(16) == 4.0
    assert factorial(5) == 120
    print("All tests passed!")
