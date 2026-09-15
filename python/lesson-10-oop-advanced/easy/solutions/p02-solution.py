"""SOLUTION: Rectangle with @property (Easy)"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == "__main__":
    r = Rectangle(4, 5)
    assert r.area == 20
    assert r.perimeter == 18
    print("All tests passed!")
