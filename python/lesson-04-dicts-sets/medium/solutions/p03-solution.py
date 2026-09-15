"""
SOLUTION: Common Elements (Medium)
====================================
Return sorted list of elements in BOTH lists using set intersection.
"""
def common_elements(a: list, b: list) -> list:
    return sorted(set(a) & set(b))

if __name__ == "__main__":
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert common_elements([1], [2]) == []
    assert common_elements([], []) == []
    print("All tests passed!")
