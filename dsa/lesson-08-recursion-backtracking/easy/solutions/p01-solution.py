"""
SOLUTION: Sum Digits Recursively (Easy)
==============================
Contract: returns an int digit-sum. Base: n == 0 -> 0.
Shrink: n // 10 drops the last digit; n % 10 is this level's piece.
"""
def sum_digits(n: int) -> int:
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

if __name__ == "__main__":
    assert sum_digits(1234) == 10
    assert sum_digits(0) == 0
    assert sum_digits(999) == 27
    assert sum_digits(7) == 7
    assert sum_digits(10001) == 2
    print("All tests passed!")
