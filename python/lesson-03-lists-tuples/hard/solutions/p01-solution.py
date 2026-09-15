"""
SOLUTION: Flatten (Hard)
=========================
Flatten a list that may contain sub-lists (one level deep).
"""
def flatten(nested: list) -> list:
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result

if __name__ == "__main__":
    assert flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten([1, [2], 3]) == [1, 2, 3]
    assert flatten([]) == []
    print("All tests passed!")
