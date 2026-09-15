"""SOLUTION: Fibonacci Generator (Hard)"""
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    assert list(fibonacci_gen(6)) == [0, 1, 1, 2, 3, 5]
    assert list(fibonacci_gen(0)) == []
    assert list(fibonacci_gen(1)) == [0]
    print("All tests passed!")
