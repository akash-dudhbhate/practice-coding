"""
SOLUTION: Next Greater Element (Medium)
==========================================
Monotonic stack of indices (values decreasing top-down). A new element
pops every index it's greater than — the pop moment IS the answer.
Leftovers keep -1. Each index pushed/popped once → O(n).
"""
def next_greater(nums):
    ans = [-1] * len(nums)
    stack = []                          # indices waiting for an answer
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            ans[stack.pop()] = x        # x is their next greater
        stack.append(i)
    return ans

if __name__ == "__main__":
    assert next_greater([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
    assert next_greater([1, 2, 3, 4]) == [2, 3, 4, -1]
    assert next_greater([4, 3, 2, 1]) == [-1, -1, -1, -1]
    assert next_greater([5, 5, 5]) == [-1, -1, -1]
    assert next_greater([]) == []
    assert next_greater([7]) == [-1]
    print("All tests passed!")
