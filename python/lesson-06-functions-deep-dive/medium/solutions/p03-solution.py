"""SOLUTION: Apply Func (Medium)"""
def apply_func(func, items):
    return [func(item) for item in items]

if __name__ == "__main__":
    assert apply_func(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]
    assert apply_func(str, [1, 2]) == ["1", "2"]
    print("All tests passed!")
