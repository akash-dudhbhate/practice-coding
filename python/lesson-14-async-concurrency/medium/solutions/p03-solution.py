"""SOLUTION: ProcessPoolExecutor (Medium)"""
from concurrent.futures import ProcessPoolExecutor

def square(n):
    return n * n

if __name__ == "__main__":
    nums = list(range(1, 21))
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(square, nums))
    assert results == [n * n for n in range(1, 21)]
    print("All tests passed!")
