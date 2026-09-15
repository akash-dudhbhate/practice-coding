"""SOLUTION: Student __str__ (Easy)"""
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Student: {self.name} ({self.grade})"

if __name__ == "__main__":
    s = Student("Akash", "A")
    assert str(s) == "Student: Akash (A)"
    print("All tests passed!")
