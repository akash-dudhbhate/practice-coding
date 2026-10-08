"""
SOLUTION: Fibonacci, Memoized (Easy)
=====================================
Naive recursion recomputes fib(k) exponentially many times. A cache
(dict or @lru_cache) makes each fib(k) compute once: O(n) time.
The bottom-up / rolling-variable versions are equivalent.
"""
from functools import lru_cache


# Option A: top-down memoization
@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# Option B: bottom-up table (O(n) space)
def fib_table(n: int) -> int:
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# Option C: rolling variables (O(1) space)
def fib_rolling(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    for fn in (fib, fib_table, fib_rolling):
        assert fn(0) == 0
        assert fn(1) == 1
        assert fn(2) == 1
        assert fn(7) == 13
        assert fn(10) == 55
        assert fn(30) == 832040
        assert fn(50) == 12586269025
    print("All tests passed!")
