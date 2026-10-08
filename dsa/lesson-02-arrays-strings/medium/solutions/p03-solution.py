"""
SOLUTION: Product Except Self (Medium)
==============================
Pass 1: out[i] = product of everything LEFT of i.
Pass 2: multiply in product of everything RIGHT of i.
O(n) time, no division — zeros handled for free.
"""
def product_except_self(nums: list) -> list:
    n = len(nums)
    out = [1] * n
    left = 1
    for i in range(n):             # left-products
        out[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1): # right-products
        out[i] *= right
        right *= nums[i]
    return out

if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([2, 3, 4]) == [12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print("All tests passed!")
