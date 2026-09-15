"""
SOLUTION: Is Prime (Hard)
==========================
Check if a number is prime.
"""
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    assert is_prime(2) == True
    assert is_prime(7) == True
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(13) == True
    print("All tests passed!")
