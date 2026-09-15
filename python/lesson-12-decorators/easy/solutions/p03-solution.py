"""SOLUTION: @log_call Decorator (Easy)"""
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

if __name__ == "__main__":
    assert add(2, 3) == 5
    print("All tests passed!")
