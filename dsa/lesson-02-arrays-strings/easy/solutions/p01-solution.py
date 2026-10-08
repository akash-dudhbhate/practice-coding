"""
SOLUTION: Running Sum (Easy)
==============================
Carry a total, append after each element -> one pass, O(n).
"""
def running_sum(nums: list) -> list:
    out = []
    total = 0
    for x in nums:
        total += x
        out.append(total)
    return out

if __name__ == "__main__":
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_sum([5]) == [5]
    assert running_sum([]) == []
    assert running_sum([1, -1, 1, -1]) == [1, 0, 1, 0]
    print("All tests passed!")
