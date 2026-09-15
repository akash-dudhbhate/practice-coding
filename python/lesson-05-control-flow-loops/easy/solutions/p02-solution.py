"""
SOLUTION: Sum Range (Easy)
===========================
Sum all integers from start to stop inclusive using a for loop.
"""
def sum_range(start: int, stop: int) -> int:
    total = 0
    for i in range(start, stop + 1):
        total += i
    return total

if __name__ == "__main__":
    assert sum_range(1, 5) == 15
    assert sum_range(0, 0) == 0
    assert sum_range(-2, 2) == 0
    print("All tests passed!")
