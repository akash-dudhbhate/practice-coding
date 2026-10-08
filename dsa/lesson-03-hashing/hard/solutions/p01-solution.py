"""
SOLUTION: Longest Consecutive Sequence (Hard) — O(n)
===================================================
Key insight: only start counting a run at a RUN START — a number x
where (x - 1) is not in the set. Then extend x, x+1, x+2... Every
number is looked at O(1) times across the whole algorithm -> O(n).
"""
def longest_consecutive(nums: list) -> int:
    s = set(nums)
    best = 0
    for x in s:
        if x - 1 not in s:          # x starts a run
            length = 1
            while x + length in s:  # extend the run
                length += 1
            best = max(best, length)
    return best

if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    assert longest_consecutive([1, 2, 0, 1]) == 3
    assert longest_consecutive([7]) == 1
    print("All tests passed!")
