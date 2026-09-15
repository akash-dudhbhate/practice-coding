"""SOLUTION: Vehicle and Car Inheritance (Easy)"""
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display(self):
        return f"{super().display()} ({self.num_doors} doors)"

if __name__ == "__main__":
    c = Car("Toyota", "Camry", 2020, 4)
    assert "2020 Toyota Camry" in c.display()
    assert "4 doors" in c.display()
    print("All tests passed!")
