"""
SOLUTION: Max of Two Numbers (Easy)
====================================
Return the larger of two integers without using built-in max().
"""
def max_of_two(a: int, b: int) -> int:
    if a >= b:
        return a
    return b

# Test
if __name__ == "__main__":
    assert max_of_two(3, 7) == 7
    assert max_of_two(10, 5) == 10
    assert max_of_two(4, 4) == 4
    print("All tests passed!")
