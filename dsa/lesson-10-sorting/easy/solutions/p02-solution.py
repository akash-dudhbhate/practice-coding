"""
SOLUTION: Sort With a Custom Key (Easy)
============================================
Return a tuple from key= and Python compares element-wise:
length first, alphabetical order as the tiebreak — one call,
no manual comparator needed.
"""
def sort_by_length(words: list) -> list:
    return sorted(words, key=lambda w: (len(w), w))

if __name__ == "__main__":
    assert sort_by_length(["banana", "kiwi", "apple", "fig", "cherry"]) == \
        ["fig", "kiwi", "apple", "banana", "cherry"]
    assert sort_by_length(["bb", "aa", "c"]) == ["c", "aa", "bb"]
    assert sort_by_length([]) == []
    assert sort_by_length(["same", "size"]) == ["same", "size"]
    # stability demo: equal keys keep input order
    assert sorted(["b1", "a2", "c3"], key=len) == ["b1", "a2", "c3"]
    print("All tests passed!")
