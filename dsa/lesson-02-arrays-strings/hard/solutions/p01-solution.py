"""
SOLUTION: Subarray Sum Equals K (Hard)
==============================
prefix[i..j] = P[j+1] - P[i] = k  <=>  P[i] = P[j+1] - k.
Keep a dict of seen prefix counts; at each prefix, ask how many
earlier prefixes equal P - k. Seed {0: 1} for subarrays at index 0.
O(n) time, O(n) space.
"""
def count_subarray_sum(nums: list, k: int) -> int:
    seen = {0: 1}                  # the empty prefix sums to 0, once
    P = 0
    count = 0
    for x in nums:
        P += x
        count += seen.get(P - k, 0)
        seen[P] = seen.get(P, 0) + 1
    return count

if __name__ == "__main__":
    assert count_subarray_sum([1, 1, 1], 2) == 2
    assert count_subarray_sum([1, 2, 3], 3) == 2
    assert count_subarray_sum([1, -1, 0], 0) == 3
    assert count_subarray_sum([1], 1) == 1
    print("All tests passed!")
