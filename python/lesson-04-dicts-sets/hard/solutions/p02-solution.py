"""
SOLUTION: Set Difference (Hard)
=================================
Return dict with only_a and only_b (symmetric difference split).
"""
def set_difference(a: list, b: list) -> dict:
    set_a, set_b = set(a), set(b)
    return {
        "only_a": sorted(set_a - set_b),
        "only_b": sorted(set_b - set_a),
    }

if __name__ == "__main__":
    assert set_difference([1, 2, 3], [2, 3, 4]) == {"only_a": [1], "only_b": [4]}
    print("All tests passed!")
