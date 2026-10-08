"""
SOLUTION: Jump Game — Is the End Reachable? (Medium)
====================================================
Track `reach` = farthest index any path can land on. You can stand at i
only if i <= reach; then extend reach = max(reach, i + nums[i]).
If i > reach ever occurs, that index is stranded → False.
O(n) time, O(1) space.
"""
def can_jump(nums):
    reach = 0
    for i, x in enumerate(nums):
        if i > reach:                    # can't even stand here
            return False
        reach = max(reach, i + x)
    return True

if __name__ == "__main__":
    assert can_jump([2,3,1,1,4]) == True
    assert can_jump([3,2,1,0,4]) == False    # the 0 at index 3 is a wall
    assert can_jump([0]) == True
    assert can_jump([2,0,0]) == True         # can jump over zeros
    assert can_jump([1,1,0,1]) == False
    assert can_jump([1,0,1,0]) == False
    assert can_jump([4,0,0,0,0]) == True
    print("All tests passed!")
