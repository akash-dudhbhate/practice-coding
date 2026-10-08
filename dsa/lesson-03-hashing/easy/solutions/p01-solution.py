"""
SOLUTION: Count Frequencies (Easy)
==================================
Build a dict item -> count in one pass using .get() to default to 0.
"""
def count_frequencies(items: list) -> dict:
    counts = {}
    for x in items:
        counts[x] = counts.get(x, 0) + 1
    return counts

if __name__ == "__main__":
    assert count_frequencies(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}
    assert count_frequencies([7, 7, 7]) == {7: 3}
    assert count_frequencies([]) == {}
    assert count_frequencies(["x"]) == {"x": 1}
    print("All tests passed!")
