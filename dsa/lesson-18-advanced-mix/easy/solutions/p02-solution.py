"""
SOLUTION: Power of Two Check (Easy)
===================================
Powers of two have exactly one set bit → n & (n-1) erases it → 0.
Guard with n > 0: 0 and negatives are not powers of two.
"""
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

if __name__ == "__main__":
    assert is_power_of_two(1) == True
    assert is_power_of_two(16) == True
    assert is_power_of_two(3) == False
    assert is_power_of_two(0) == False       # the guard earns its keep
    assert is_power_of_two(-8) == False
    assert is_power_of_two(1024) == True
    assert is_power_of_two(6) == False       # 110 has two set bits
    print("All tests passed!")
