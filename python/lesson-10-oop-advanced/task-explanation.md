# Lesson 10 — OOP Advanced

## What you'll learn
- Inheritance and super()
- Polymorphism and method overriding
- @property decorator (getters/setters)
- Dunder methods (__add__, __str__, __eq__, __len__)
- @classmethod and @staticmethod
- Abstract base classes (ABC)
- Composition vs inheritance
- Encapsulation (private attributes)
- Multiple inheritance and MRO

## Lesson

Advanced OOP builds on the basics (lesson 09) to create flexible, reusable, and professional-grade class designs.

### Inheritance + super()
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call parent init
        self.breed = breed
```

### Polymorphism
```python
def make_sound(animal):
    return animal.speak()  # works for any animal with speak()
```

### @property
```python
class Circle:
    @property
    def area(self):
        return 3.14 * self._radius ** 2
# circle.area (no parentheses)
```

### Dunder methods
```python
def __str__(self): return f"MyClass({self.value})"
def __eq__(self, other): return self.value == other.value
def __add__(self, other): return MyClass(self.value + other.value)
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Create a Vehicle class with make/model/year. Create a Car subclass that adds num_doors and overrides a `display()` method.
2. `easy/p02-solve.py` — Create a Rectangle class with @property for area and perimeter.
3. `easy/p03-solve.py` — Create a Student class with __str__ that returns "Student: Name (Grade)".

### Medium
4. `medium/p01-solve.py` — Create a Vector class with __add__, __sub__, __eq__, and __str__.
5. `medium/p02-solve.py` — Create a BankAccount class with private __balance, deposit/withdraw methods with validation, and @property getter for balance.
6. `medium/p03-solve.py` — Create an abstract Shape class with abstract area() and perimeter(). Implement Circle and Square subclasses.

### Hard
7. `hard/p01-solve.py` — Create a class hierarchy: Employee → Manager (adds team list, override salary calculation) and Developer (adds programming_languages list).
8. `hard/p02-solve.py` — Create a Stack class using composition (has-a list, not is-a list). Only expose push, pop, peek, is_empty, size — no direct list access.
9. `hard/p03-solve.py` — Create a Book class with @property for "is_available" (based on borrowed flag), a @classmethod "from_string" that parses "Title|Author|ISBN", and @staticmethod "is_valid_isbn" that checks length is 10 or 13.

### How to work
- Write your complete solution from scratch below the TODO marker.
- Remove the TODO line when done.
- Run `python <filename>` to test.
