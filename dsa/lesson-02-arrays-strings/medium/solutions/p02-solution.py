"""
SOLUTION: Move Zeros In-Place (Medium)
==============================
Write pointer: copy non-zeros forward in order, then fill tail with 0s.
O(n) time, O(1) space — the list is mutated, not replaced.
"""
def move_zeros(nums: list) -> None:
    w = 0                          # write pointer: next slot for non-zero
    for x in nums:                 # read pointer scans every element
        if x != 0:
            nums[w] = x
            w += 1
    while w < len(nums):           # fill the tail with zeros
        nums[w] = 0
        w += 1

if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]; move_zeros(a); assert a == [1, 3, 12, 0, 0]
    b = [0, 0, 1]; move_zeros(b); assert b == [1, 0, 0]
    c = [1, 2, 3]; move_zeros(c); assert c == [1, 2, 3]
    d = []; move_zeros(d); assert d == []
    print("All tests passed!")
