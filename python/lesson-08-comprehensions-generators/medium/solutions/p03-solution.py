"""SOLUTION: Even Squares (Medium)"""
def even_squares(n):
    return [i * i for i in range(n) if (i * i) % 2 == 0]

if __name__ == "__main__":
    assert even_squares(5) == [0, 4, 16]
    print("All tests passed!")
