"""SOLUTION: Infinite Fibonacci (Medium)"""
from itertools import islice

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    first_10 = list(islice(fibonacci(), 10))
    assert first_10 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    print("All tests passed!")
