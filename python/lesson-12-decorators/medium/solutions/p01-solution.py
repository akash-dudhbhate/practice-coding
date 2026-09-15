"""SOLUTION: @repeat(n) Decorator (Medium)"""
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("hi")
    return "done"

if __name__ == "__main__":
    assert greet() == "done"
    print("All tests passed!")
