"""
SOLUTION: Koko Eating Bananas (Medium)
============================================
Search the answer: speed k in [1, max(piles)].
hours(k) = sum(ceil(pile / k)) is a DECREASING function of k.
Find the smallest k where hours(k) <= h.
ceil(p / k) = (p + k - 1) // k — no floats, no math.ceil needed.
"""
def min_eating_speed(piles: list, h: int) -> int:
    def hours_needed(k):
        return sum((p + k - 1) // k for p in piles)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours_needed(mid) <= h:
            hi = mid               # fast enough — try slower
        else:
            lo = mid + 1           # too slow — eat faster
    return lo

if __name__ == "__main__":
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
    assert min_eating_speed([1], 1) == 1
    assert min_eating_speed([312884470], 312884469) == 2
    print("All tests passed!")
