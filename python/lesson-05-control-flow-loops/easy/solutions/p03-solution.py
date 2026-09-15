"""
SOLUTION: Count Down (Easy)
=============================
Return a list counting down from n to 1 using a while loop.
"""
def count_down(n: int) -> list:
    result = []
    while n > 0:
        result.append(n)
        n -= 1
    return result

if __name__ == "__main__":
    assert count_down(3) == [3, 2, 1]
    assert count_down(1) == [1]
    assert count_down(0) == []
    print("All tests passed!")
