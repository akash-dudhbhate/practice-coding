"""
SOLUTION: Invert Dict (Medium)
================================
Swap keys and values. Keep last key for duplicate values.
"""
def invert_dict(d: dict) -> dict:
    return {v: k for k, v in d.items()}

if __name__ == "__main__":
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert invert_dict({}) == {}
    print("All tests passed!")
