"""SOLUTION: Student with Class Counter (Hard)"""
class Student:
    count = 0

    def __init__(self, name, grades=None):
        self.name = name
        self.grades = list(grades) if grades else []
        Student.count += 1

    def add_grade(self, g):
        self.grades.append(g)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    @classmethod
    def get_count(cls):
        return cls.count

if __name__ == "__main__":
    Student.count = 0  # reset
    s1 = Student("Akash", [90, 80])
    s2 = Student("Dev")
    assert Student.get_count() == 2
    s2.add_grade(70)
    assert s2.average() == 70
    print("All tests passed!")
