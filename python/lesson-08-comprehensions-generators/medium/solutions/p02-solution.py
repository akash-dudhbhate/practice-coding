"""SOLUTION: Sum Squares Generator (Medium)"""
def sum_squares(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    assert sum_squares(4) == 0 + 1 + 4 + 9
    assert sum_squares(0) == 0
    print("All tests passed!")
