"""SOLUTION: divide with pytest.raises (Medium)"""
import pytest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

if __name__ == "__main__":
    assert divide(10, 2) == 5.0
    try:
        divide(1, 0)
        assert False
    except ZeroDivisionError:
        pass
    print("All tests passed!")
