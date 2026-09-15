"""SOLUTION: factorial with parametrize (Easy)"""
import pytest

def factorial(n):
    if n < 0:
        raise ValueError("Negative input")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (3, 6),
])
def test_factorial(n, expected):
    assert factorial(n) == expected

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

if __name__ == "__main__":
    for n, exp in [(0, 1), (1, 1), (5, 120), (3, 6)]:
        assert factorial(n) == exp
    try:
        factorial(-1)
        assert False
    except ValueError:
        pass
    print("All tests passed!")
