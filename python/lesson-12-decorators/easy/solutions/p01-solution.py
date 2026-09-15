"""SOLUTION: @shout Decorator (Easy)"""
def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() if isinstance(result, str) else result
    return wrapper

@shout
def greet(name):
    return f"hello {name}"

if __name__ == "__main__":
    assert greet("world") == "HELLO WORLD"
    print("All tests passed!")
