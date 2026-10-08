"""
SOLUTION: 3-Sum (Medium)
========================
Sort. Fix nums[i]; two-pointer the remainder for -nums[i].
Skip duplicate i values and advance both pointers past duplicate
values after a hit so no triplet repeats.
"""
def three_sum(nums: list) -> list:
    nums = sorted(nums)
    result = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue                      # same fixed value -> same triplets
        L, R = i + 1, n - 1
        while L < R:
            s = nums[i] + nums[L] + nums[R]
            if s == 0:
                result.append([nums[i], nums[L], nums[R]])
                L += 1
                R -= 1
                while L < R and nums[L] == nums[L - 1]:
                    L += 1                # skip duplicate pair values
                while L < R and nums[R] == nums[R + 1]:
                    R -= 1
            elif s < 0:
                L += 1
            else:
                R -= 1
    return result

if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([]) == []
    print("All tests passed!")
