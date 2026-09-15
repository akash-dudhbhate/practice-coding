"""SOLUTION: @CountCalls Class Decorator (Hard)"""
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    return "hi"

if __name__ == "__main__":
    say_hi()
    say_hi()
    say_hi()
    assert say_hi.count == 3
    print("All tests passed!")
