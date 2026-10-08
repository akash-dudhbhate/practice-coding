"""
SOLUTION: Count Subarrays Summing to K (Hard) — O(n)
===================================================
Prefix sums + frequency map. A subarray ending at the current index
sums to k exactly when a PAST prefix equals (prefix - k). Seed
{0: 1} so subarrays starting at index 0 are counted. Query before
recording the new prefix (matters when k == 0).
"""
def subarray_sum(nums: list, k: int) -> int:
    count = 0
    prefix = 0
    freq = {0: 1}                 # the empty prefix
    for x in nums:
        prefix += x
        count += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1
    return count

if __name__ == "__main__":
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([1, -1, 0], 0) == 3
    assert subarray_sum([1], 0) == 0
    assert subarray_sum([], 0) == 0
    assert subarray_sum([0, 0, 0], 0) == 6
    print("All tests passed!")
