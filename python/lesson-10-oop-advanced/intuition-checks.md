# Lesson 10 — Intuition Checks

## Check 01: super()
```python
class A:
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        print("B")
        super().__init__()
B()
```
<details><summary>Answer</summary>
Prints `B` then `A`. `super().__init__()` calls the parent's init.
</details>

## Check 02: isinstance
```python
class Animal: pass
class Dog(Animal): pass
d = Dog()
print(isinstance(d, Dog))
print(isinstance(d, Animal))
print(isinstance(d, Cat))  # NameError or False?
```
<details><summary>Answer</summary>
`True`, `True`, `NameError` (Cat not defined). `isinstance` checks the entire inheritance chain.
</details>

## Check 03: Abstract Class
```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
s = Shape()
```
<details><summary>Answer</summary>
**TypeError** — can't instantiate an abstract class. Must subclass and implement `area()`.
</details>

## Check 04: @classmethod vs @staticmethod
```python
class MyClass:
    @classmethod
    def cls_method(cls):
        return cls.__name__
    @staticmethod
    def static_method():
        return "static"
```
<details><summary>Answer</summary>
`cls_method` receives the CLASS as first arg (can create instances). `static_method` receives nothing (like a regular function in a class namespace).
</details>

## Check 05: __eq__
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
print(p1 is p2)
```
<details><summary>Answer</summary>
`True`, `False` — `==` uses `__eq__` (compares values). `is` checks identity (same object in memory).
</details>
