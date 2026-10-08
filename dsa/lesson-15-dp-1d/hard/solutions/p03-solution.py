"""
SOLUTION: Partition Equal Subset Sum (Hard)
============================================
Reduce to subset-sum: two equal halves exist iff some subset sums to
total // 2. Boolean DP over reachable sums.

reachable[s] = can we make sum s using each element at most once.
Iterate s DOWNWARD (target..x) — iterating upward would let one
element contribute multiple times (that would be UNBOUNDED knapsack).
"""


def can_partition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 == 1:
        return False                       # odd total can never split
    target = total // 2
    reachable = [False] * (target + 1)
    reachable[0] = True                    # empty subset sums to 0
    for x in nums:
        for s in range(target, x - 1, -1):  # DOWN: 0/1 usage per element
            if reachable[s - x]:
                reachable[s] = True
        if reachable[target]:              # early exit
            return True
    return reachable[target]


if __name__ == "__main__":
    assert can_partition([1, 5, 11, 5]) is True
    assert can_partition([1, 2, 3, 5]) is False
    assert can_partition([1, 2, 5]) is False
    assert can_partition([1, 1]) is True
    assert can_partition([100]) is False
    assert can_partition([2, 2, 3, 5]) is False
    assert can_partition([3, 3, 3, 4, 5]) is True    # [3,3,3]=9? no: [4,5]=9 vs [3,3,3]=9
    print("All tests passed!")
