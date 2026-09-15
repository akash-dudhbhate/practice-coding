"""SOLUTION: Squares Comprehension (Easy)"""
def squares(n):
    return [i * i for i in range(n)]

if __name__ == "__main__":
    assert squares(4) == [0, 1, 4, 9]
    assert squares(0) == []
    print("All tests passed!")
