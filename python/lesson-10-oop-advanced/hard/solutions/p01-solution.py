"""SOLUTION: Employee Hierarchy (Hard)"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, team=None):
        super().__init__(name, salary)
        self.team = team or []

    def calculate_salary(self):
        return self.salary + len(self.team) * 100  # bonus per team member

class Developer(Employee):
    def __init__(self, name, salary, languages=None):
        super().__init__(name, salary)
        self.languages = languages or []

    def calculate_salary(self):
        return self.salary + len(self.languages) * 50  # bonus per language

if __name__ == "__main__":
    m = Manager("Alice", 80000, ["Bob", "Carol"])
    assert m.calculate_salary() == 80200
    d = Developer("Dave", 70000, ["Python", "JS"])
    assert d.calculate_salary() == 70100
    print("All tests passed!")
