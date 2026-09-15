"""SOLUTION: Even Squares Generator Expression (Easy)"""
even_squares = (x * x for x in range(0, 21, 2))

if __name__ == "__main__":
    result = list(even_squares)
    assert result == [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
    print("All tests passed!")
