"""SOLUTION: Compose (Hard)"""
def compose(f, g):
    def composed(x):
        return f(g(x))
    return composed

if __name__ == "__main__":
    h = compose(lambda x: x + 1, lambda x: x * 2)
    assert h(3) == 7  # (3*2)+1
    print("All tests passed!")
