"""SOLUTION: Sum All with *args (Easy)"""
def sum_all(*nums):
    total = 0
    for n in nums:
        total += n
    return total

if __name__ == "__main__":
    assert sum_all(1, 2, 3) == 6
    assert sum_all() == 0
    assert sum_all(10) == 10
    print("All tests passed!")
