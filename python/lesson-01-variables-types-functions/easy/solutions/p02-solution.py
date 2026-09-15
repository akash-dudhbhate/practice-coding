"""
SOLUTION: Even or Odd (Easy)
=============================
Return True if even, False if odd.
"""
def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == "__main__":
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    assert is_even(-2) == True
    print("All tests passed!")
