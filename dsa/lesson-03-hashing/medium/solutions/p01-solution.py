"""
SOLUTION: Two Sum — Complement Lookup (Medium)
==============================================
seen maps value -> index. For each x, check if target - x was already
seen. Check BEFORE storing so an element can't pair with itself
(e.g. two_sum([3], 6) must return []).
"""
def two_sum(nums: list, target: int) -> list:
    seen = {}                      # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []

if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 5, 9], 20) == []
    assert two_sum([3], 6) == []
    print("All tests passed!")
