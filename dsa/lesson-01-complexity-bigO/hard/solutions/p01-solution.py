"""
SOLUTION: Measured Dedup (Hard)
==============================
Naive dedup scans `result` per element -> O(n^2) comparisons.
Set dedup does one O(1) lookup per element -> O(n) checks.
Same output, very different op counts.
"""
def dedup_naive(nums: list) -> tuple:
    result = []
    ops = 0
    for x in nums:
        found = False
        for y in result:          # hidden inner loop!
            ops += 1              # count EVERY element comparison
            if x == y:
                found = True
                break
        if not found:
            result.append(x)
    return result, ops

def dedup_set(nums: list) -> tuple:
    seen = set()
    result = []
    ops = 0
    for x in nums:
        ops += 1                  # one membership check = 1 op
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result, ops

if __name__ == "__main__":
    assert dedup_naive([1, 2, 2, 3]) == ([1, 2, 3], 5)
    assert dedup_set([1, 2, 2, 3]) == ([1, 2, 3], 4)
    assert dedup_naive([1, 2, 3, 4, 5]) == ([1, 2, 3, 4, 5], 10)
    assert dedup_set([1, 2, 3, 4, 5]) == ([1, 2, 3, 4, 5], 5)
    print("All tests passed!")
