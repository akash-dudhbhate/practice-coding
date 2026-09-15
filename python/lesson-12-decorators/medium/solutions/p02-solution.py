"""SOLUTION: @cache Decorator (Medium)"""
def cache(func):
    _cache = {}
    def wrapper(*args):
        if args in _cache:
            return _cache[args]
        result = func(*args)
        _cache[args] = result
        return result
    return wrapper

@cache
def slow_square(n):
    print(f"  computing {n}...")
    return n * n

if __name__ == "__main__":
    assert slow_square(4) == 16
    assert slow_square(4) == 16  # cached, no print
    print("All tests passed!")
