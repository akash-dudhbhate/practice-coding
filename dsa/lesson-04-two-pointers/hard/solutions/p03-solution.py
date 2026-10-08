"""
SOLUTION: 4-Sum (Hard)
======================
Sort, fix nums[i] and nums[j], two-pointer the rest for
target - nums[i] - nums[j]. Skip duplicate i, j values and duplicate
pair values so no quadruplet repeats. O(n^3).
"""
def four_sum(nums: list, target: int) -> list:
    nums = sorted(nums)
    result = []
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            L, R = j + 1, n - 1
            while L < R:
                s = nums[i] + nums[j] + nums[L] + nums[R]
                if s == target:
                    result.append([nums[i], nums[j], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
                elif s < target:
                    L += 1
                else:
                    R -= 1
    return result

if __name__ == "__main__":
    assert four_sum([1, 0, -1, 0, -2, 2], 0) == [
        [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]
    ]
    assert four_sum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
    assert four_sum([], 0) == []
    assert four_sum([1, 2, 3], 6) == []
    print("All tests passed!")
