"""
SOLUTION: Group By Parity (Hard)
=================================
Group numbers by even/odd. Handle empty input.
"""
def group_by_parity(nums: list) -> dict:
    result = {"even": [], "odd": []}
    for n in nums:
        if n % 2 == 0:
            result["even"].append(n)
        else:
            result["odd"].append(n)
    return result

if __name__ == "__main__":
    assert group_by_parity([1, 2, 3, 4]) == {"even": [2, 4], "odd": [1, 3]}
    assert group_by_parity([]) == {"even": [], "odd": []}
    print("All tests passed!")
