"""SOLUTION: Vector Class (Medium)"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    assert (v1 + v2) == Vector(4, 6)
    assert (v2 - v1) == Vector(2, 2)
    print("All tests passed!")
