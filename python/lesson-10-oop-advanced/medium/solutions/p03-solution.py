"""SOLUTION: Abstract Shape (Medium)"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

if __name__ == "__main__":
    c = Circle(5)
    assert abs(c.area() - 78.54) < 1
    s = Square(4)
    assert s.area() == 16
    print("All tests passed!")
