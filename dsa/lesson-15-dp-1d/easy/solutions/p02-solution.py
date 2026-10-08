"""
SOLUTION: Climbing Stairs (Easy)
=================================
ways(i) = ways(i-1) + ways(i-2): your last move was a 1-step or a
2-step. Fibonacci shifted by one. Rolling variables give O(1) space.
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2                     # ways(1), ways(2)
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8
    assert climb_stairs(10) == 89
    assert climb_stairs(45) == 1836311903
    print("All tests passed!")
