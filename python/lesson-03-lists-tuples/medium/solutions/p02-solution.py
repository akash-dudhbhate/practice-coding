"""
SOLUTION: Sort By Length (Medium)
==================================
Sort strings by length (shortest first) using sorted() with key.
"""
def sort_by_length(words: list) -> list:
    return sorted(words, key=len)

if __name__ == "__main__":
    assert sort_by_length(["apple", "hi", "cat"]) == ["hi", "cat", "apple"]
    assert sort_by_length([]) == []
    assert sort_by_length(["same", "four"]) == ["same", "four"]
    print("All tests passed!")
