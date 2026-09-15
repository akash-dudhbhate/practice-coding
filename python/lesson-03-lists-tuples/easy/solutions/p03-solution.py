"""
SOLUTION: Contains (Easy)
==========================
Return True if target is in the list (no 'in' operator — loop manually).
"""
def contains(items: list, target) -> bool:
    for item in items:
        if item == target:
            return True
    return False

if __name__ == "__main__":
    assert contains([1, 2, 3], 2) == True
    assert contains([1, 2, 3], 5) == False
    assert contains([], 1) == False
    print("All tests passed!")
