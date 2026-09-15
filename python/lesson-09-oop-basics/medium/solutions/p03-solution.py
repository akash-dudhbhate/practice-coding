"""SOLUTION: Temperature Class (Medium)"""
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5 / 9)

    @staticmethod
    def to_fahrenheit(c):
        return c * 9 / 5 + 32

    def fahrenheit(self):
        return self.to_fahrenheit(self.celsius)

if __name__ == "__main__":
    t = Temperature(100)
    assert t.fahrenheit() == 212.0
    t2 = Temperature.from_fahrenheit(32)
    assert abs(t2.celsius - 0) < 0.01
    print("All tests passed!")
