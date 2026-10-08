"""
SOLUTION: XOR Single Number (Easy)
==================================
XOR every element — pairs cancel (a^a=0), the loner survives.
O(n) time, O(1) space.
"""
def single_number(nums):
    result = 0
    for x in nums:
        result ^= x
    return result

if __name__ == "__main__":
    assert single_number([2,2,1]) == 1
    assert single_number([4,1,2,1,2]) == 4
    assert single_number([1]) == 1
    assert single_number([-1,-1,-2]) == -2
    assert single_number([7,3,5,3,5]) == 7
    print("All tests passed!")
