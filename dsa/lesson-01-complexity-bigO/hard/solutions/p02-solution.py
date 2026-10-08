"""
SOLUTION: Fib Call Count (Hard)
==============================
Naive fib: T(n) = 1 + T(n-1) + T(n-2) -> call count grows like 2^n.
fib(5) = 15 calls, fib(10) = 177 calls, fib(50) ~ a trillion.
"""
def fib_with_count(n: int) -> tuple:
    calls = [0]                    # mutable counter visible in inner scope

    def fib(k):
        calls[0] += 1              # every call counts, including this one
        if k < 2:
            return k
        return fib(k - 1) + fib(k - 2)

    return fib(n), calls[0]

if __name__ == "__main__":
    assert fib_with_count(0) == (0, 1)
    assert fib_with_count(1) == (1, 1)
    assert fib_with_count(5) == (5, 15)
    assert fib_with_count(10) == (55, 177)
    print("All tests passed!")
