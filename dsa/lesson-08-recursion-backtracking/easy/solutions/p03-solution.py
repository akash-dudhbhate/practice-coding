"""
SOLUTION: Power Recursively (Easy)
==============================
Contract: returns base^exp. Base: exp == 0 -> 1. Shrink: exp - 1.
(The O(log exp) halving variant lives in EXTRA-PRACTICE.md.)
"""
def power(base, exp: int):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

if __name__ == "__main__":
    assert power(2, 10) == 1024
    assert power(2, 0) == 1
    assert power(3, 3) == 27
    assert power(5, 1) == 5
    assert power(7, 2) == 49
    assert power(10, 4) == 10000
    print("All tests passed!")
