"""SOLUTION: Safe Divide with Custom Error (Hard)"""
class DivideByZeroError(Exception):
    pass

def safe_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric")
    if b == 0:
        raise DivideByZeroError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    assert safe_divide(10, 2) == 5.0
    try:
        safe_divide(1, 0)
        assert False
    except DivideByZeroError:
        pass
    try:
        safe_divide("a", 1)
        assert False
    except TypeError:
        pass
    print("All tests passed!")
