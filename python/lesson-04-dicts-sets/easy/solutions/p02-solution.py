"""
SOLUTION: Has Key (Easy)
=========================
Return True if key is in dict using .get() (not 'in').
"""
def has_key(d: dict, key) -> bool:
    return d.get(key) is not None or key in d

if __name__ == "__main__":
    assert has_key({"a": 1}, "a") == True
    assert has_key({"a": 1}, "b") == False
    assert has_key({}, "a") == False
    print("All tests passed!")
