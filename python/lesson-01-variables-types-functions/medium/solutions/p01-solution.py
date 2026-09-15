"""
SOLUTION: Max of Three (Medium)
================================
Reuse max_of_two to find the max of three numbers.
"""
def max_of_two(a: int, b: int) -> int:
    return a if a >= b else b

def max_of_three(a: int, b: int, c: int) -> int:
    return max_of_two(max_of_two(a, b), c)

if __name__ == "__main__":
    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(5, 1, 4) == 5
    assert max_of_three(2, 8, 3) == 8
    print("All tests passed!")
