"""
SOLUTION: Reverse List (Easy)
==============================
Return a new list with elements in reverse order (don't mutate input).
"""
def reverse_list(items: list) -> list:
    return items[::-1]

if __name__ == "__main__":
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list([]) == []
    original = [1, 2, 3]
    reverse_list(original)
    assert original == [1, 2, 3]  # not mutated
    print("All tests passed!")
