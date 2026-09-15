"""
SOLUTION: Sum List (Easy)
==========================
Return the sum of all numbers in a list (no built-in sum()).
"""
def sum_list(nums: list) -> int:
    total = 0
    for n in nums:
        total += n
    return total

if __name__ == "__main__":
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([]) == 0
    assert sum_list([-1, 1]) == 0
    print("All tests passed!")
