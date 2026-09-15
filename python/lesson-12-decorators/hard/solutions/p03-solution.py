"""SOLUTION: Stacked Decorators (Hard)"""
import time

def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[TIMER] {func.__name__} took {time.time()-start:.4f}s")
        return result
    return wrapper

@log
@timer
def process(n):
    time.sleep(0.05)
    return n * 2

if __name__ == "__main__":
    result = process(5)
    assert result == 10
    print("All tests passed!")
