"""SOLUTION: @timer Decorator (Easy)"""
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "done"

if __name__ == "__main__":
    assert slow_function() == "done"
    print("All tests passed!")
