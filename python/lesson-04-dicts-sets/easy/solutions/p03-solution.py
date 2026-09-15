"""
SOLUTION: Unique Items (Easy)
==============================
Return list of unique items preserving order, using a set for tracking.
"""
def unique_items(items: list) -> list:
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    assert unique_items([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert unique_items([]) == []
    print("All tests passed!")
