"""
SOLUTION: Next Greater Element — Circular (Medium)
==================================================
Stack of indices with decreasing values; nums[j] resolves every index
it dominates. Loop 2n for wraparound, index with i % n, but push only
on the first lap (i < n). O(n).
"""
def next_greater_elements(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []                              # indices, values decreasing
    for i in range(2 * n):
        j = i % n
        while stack and nums[stack[-1]] < nums[j]:
            ans[stack.pop()] = nums[j]
        if i < n:                           # push only during the first lap
            stack.append(i)
    return ans

if __name__ == "__main__":
    assert next_greater_elements([1,2,1]) == [2,-1,2]
    assert next_greater_elements([1,2,3,4,3]) == [2,3,4,-1,4]
    assert next_greater_elements([5,4,3,2,1]) == [-1,5,5,5,5]
    assert next_greater_elements([1,2,3,2,1]) == [2,3,-1,3,2]
    assert next_greater_elements([3]) == [-1]
    assert next_greater_elements([2,2,2]) == [-1,-1,-1]   # strictly greater → none
    print("All tests passed!")
