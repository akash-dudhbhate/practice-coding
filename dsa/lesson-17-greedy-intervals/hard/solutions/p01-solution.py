"""
SOLUTION: Jump Game II — Minimum Jumps (Hard)
===========================================
`boundary` = farthest index reachable with the jumps spent so far.
`farthest` = farthest reachable if we spend ONE more. Sweep; when i hits
`boundary` we MUST commit another jump. Loop only to n-2 — the last
index doesn't need a jump of its own. O(n) time, O(1) space.
"""
def jump(nums):
    jumps = boundary = farthest = 0
    for i in range(len(nums) - 1):          # last index needs no jump
        farthest = max(farthest, i + nums[i])
        if i == boundary:                   # exhausted current jump's range
            jumps += 1
            boundary = farthest
    return jumps

if __name__ == "__main__":
    assert jump([2,3,1,1,4]) == 2
    assert jump([2,3,0,1,4]) == 2
    assert jump([1,1,1,1]) == 3
    assert jump([0]) == 0
    assert jump([1,2,3]) == 2
    assert jump([4,1,1,1,1,1]) == 2          # reach-in-one-bound still needs a landing jump
    assert jump([7,0,9,6,9,6,1,7,9,0,1,2,9]) == 2
    print("All tests passed!")
