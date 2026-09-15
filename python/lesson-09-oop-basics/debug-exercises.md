# Lesson 09 — Debug Exercises

## Debug 01 (Easy): Missing `self`
```python
class Dog:
    def __init__(name, age):
        name = name
        age = age

    def bark():
        return "Woof!"
```
<details><summary>Answer</summary>
**Bug:** Missing `self` parameter. Python methods need `self` as first param.
**Fix:** `def __init__(self, name, age): self.name = name; self.age = age` and `def bark(self):`.
</details>

## Debug 02 (Medium): Assigning Instead of Setting Attribute
```python
class Rectangle:
    def __init__(self, width, height):
        width = width
        height = height
```
<details><summary>Answer</summary>
**Bug:** `width = width` just reassigns the local variable, doesn't set the attribute. Need `self.width = width`.
**Fix:** `self.width = width; self.height = height`.
</details>

## Debug 03 (Hard): Mutable Class Attribute
```python
class Student:
    grades = []
    def add_grade(self, g):
        self.grades.append(g)

s1 = Student()
s2 = Student()
s1.add_grade(90)
print(s2.grades)
```
<details><summary>Answer</summary>
**Bug:** `grades = []` is a CLASS attribute, shared by all instances. `s2.grades` prints `[90]` — s1's grade!
**Fix:** Move to `__init__`: `self.grades = []`.
</details>
