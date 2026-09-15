"""SOLUTION: Flatten 2D (Medium)"""
def flatten(matrix):
    return [item for row in matrix for item in row]

if __name__ == "__main__":
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten([]) == []
    print("All tests passed!")
