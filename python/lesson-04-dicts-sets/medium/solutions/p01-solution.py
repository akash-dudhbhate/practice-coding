"""
SOLUTION: Merge Dicts (Medium)
================================
Merge two dicts; d2 values override d1. Don't mutate inputs.
"""
def merge_dicts(d1: dict, d2: dict) -> dict:
    return {**d1, **d2}

if __name__ == "__main__":
    assert merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}
    assert merge_dicts({}, {"a": 1}) == {"a": 1}
    print("All tests passed!")
