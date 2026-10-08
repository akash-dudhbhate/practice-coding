"""
SOLUTION: Find Duplicates (Easy)
================================
Track `seen` values; when a value is already in `seen`, record it in
`dupes` (a set, so triple+ repeats report once). Return sorted.
"""
def find_duplicates(nums: list) -> list:
    seen = set()
    dupes = set()
    for x in nums:
        if x in seen:
            dupes.add(x)
        else:
            seen.add(x)
    return sorted(dupes)

if __name__ == "__main__":
    assert find_duplicates([4, 3, 2, 4, 3, 5]) == [3, 4]
    assert find_duplicates([1, 2, 3]) == []
    assert find_duplicates([5, 5, 5, 5]) == [5]
    assert find_duplicates([]) == []
    print("All tests passed!")
