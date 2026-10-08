"""
SOLUTION: XOR Two Single Numbers (Medium)
=========================================
xor_all = a ^ b. Its lowest set bit (xor & -xor) is a bit where a and b
differ → splitting the array by it puts a and b in different groups and
each duplicate pair in the same group. XOR each group → the two loners.
O(n) time, O(1) space.
"""
def single_numbers(nums):
    xor_all = 0
    for x in nums:
        xor_all ^= x                     # = a ^ b
    diff = xor_all & -xor_all            # lowest bit where a and b differ
    a = 0
    for x in nums:
        if x & diff:                     # one group: contains exactly one loner
            a ^= x
    return [a, a ^ xor_all]              # b = a ^ (a ^ b)

if __name__ == "__main__":
    assert sorted(single_numbers([1,2,1,3,2,5])) == [3,5]
    assert sorted(single_numbers([-1,0])) == [-1,0]
    assert sorted(single_numbers([0,1])) == [0,1]
    assert sorted(single_numbers([1,2,3,4,1,2,3,7])) == [4,7]
    assert sorted(single_numbers([4,4,7,7,3,1])) == [1,3]
    print("All tests passed!")
