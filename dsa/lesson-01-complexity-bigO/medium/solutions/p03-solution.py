"""
SOLUTION: Early Exit Comparisons (Medium)
==============================
Linear search stops the moment it finds the target — best case O(1),
worst case O(n). Count each comparison actually performed.
"""
def count_comparisons(nums: list, target) -> int:
    ops = 0
    for x in nums:
        ops += 1
        if x == target:
            break          # early exit = best case
    return ops

if __name__ == "__main__":
    assert count_comparisons([5, 9, 2, 7], 5) == 1
    assert count_comparisons([5, 9, 2, 7], 7) == 4
    assert count_comparisons([5, 9, 2, 7], 99) == 4
    assert count_comparisons([], 1) == 0
    print("All tests passed!")
