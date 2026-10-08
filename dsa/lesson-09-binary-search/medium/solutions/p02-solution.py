"""
SOLUTION: Minimum Capacity to Ship Packages in D Days (Medium)
============================================
Search the answer: capacity C in [max(weights), sum(weights)].
feasible(C) = "can we ship in <= days days?" — simulate loading:
greedily fill each day until the next package would overflow.
Bigger C never needs more days → monotone → binary search the
smallest feasible C.
"""
def min_ship_capacity(weights: list, days: int) -> int:
    def feasible(cap):
        needed, load = 1, 0
        for w in weights:
            if load + w > cap:     # doesn't fit today — new day
                needed += 1
                load = 0
            load += w
        return needed <= days

    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid               # works — try smaller
        else:
            lo = mid + 1           # too small — need more capacity
    return lo

if __name__ == "__main__":
    assert min_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    assert min_ship_capacity([3, 2, 2, 4, 1, 4], 3) == 6
    assert min_ship_capacity([1, 2, 3, 1, 1], 4) == 3
    assert min_ship_capacity([5], 1) == 5
    assert min_ship_capacity([10, 50, 100, 200, 40], 3) == 200
    print("All tests passed!")
