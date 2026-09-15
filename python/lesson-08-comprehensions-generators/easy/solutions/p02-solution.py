"""SOLUTION: Evens Comprehension (Easy)"""
def evens(nums):
    return [n for n in nums if n % 2 == 0]

if __name__ == "__main__":
    assert evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert evens([1, 3, 5]) == []
    print("All tests passed!")
