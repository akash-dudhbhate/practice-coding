"""
SOLUTION: Multiplication Table (Medium)
=========================================
Return an n x n multiplication table as list of lists.
"""
def multiplication_table(n: int) -> list:
    return [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]

if __name__ == "__main__":
    assert multiplication_table(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    assert multiplication_table(1) == [[1]]
    print("All tests passed!")
