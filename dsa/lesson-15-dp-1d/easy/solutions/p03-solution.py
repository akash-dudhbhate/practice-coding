"""
SOLUTION: Tribonacci (Easy)
============================
T(n) = T(n-1) + T(n-2) + T(n-3) — the same recipe, three cells back.
Guard n < 3 before allocating so the base-case writes don't overflow.
"""


def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1
    a, b, c = 0, 1, 1               # T(0), T(1), T(2)
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c


if __name__ == "__main__":
    assert tribonacci(0) == 0
    assert tribonacci(1) == 1
    assert tribonacci(2) == 1
    assert tribonacci(3) == 2
    assert tribonacci(4) == 4
    assert tribonacci(10) == 149
    assert tribonacci(25) == 1389537
    assert tribonacci(37) == 2082876103
    print("All tests passed!")
