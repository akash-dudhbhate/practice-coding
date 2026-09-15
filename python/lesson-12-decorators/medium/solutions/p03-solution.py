"""SOLUTION: @validate_positive Decorator (Medium)"""
def validate_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Argument must be positive, got {arg}")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(width, height):
    return width * height

if __name__ == "__main__":
    assert calculate_area(4, 5) == 20
    try:
        calculate_area(-1, 5)
        assert False
    except ValueError:
        pass
    print("All tests passed!")
