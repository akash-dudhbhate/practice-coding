# Lesson 09 — OOP Basics

## What you'll learn
- Defining classes and creating instances.
- `__init__` and `self`.
- Instance vs class attributes.
- Instance methods, `__str__`/`__repr__`, encapsulation.
- Static and class methods.

## Lesson

A class bundles data (attributes) with behavior (methods).

### Basic class
```python
class Dog:
    species = "Canis familiaris"   # class attribute

    def __init__(self, name):
        self.name = name           # instance attribute

    def bark(self):
        return f"{self.name} says Woof!"

d = Dog("Rex")
d.bark()   # "Rex says Woof!"
```

### Methods & dunder
```python
def __str__(self):
    return f"Dog({self.name})"

@classmethod
def from_dict(cls, data):
    return cls(data["name"])
```

### Key rules
- `self` is always the first parameter of instance methods.
- Initialize mutable per-instance data in `__init__`, NOT as a class attribute.
- `_name` = "internal" by convention; `__name` = name-mangled.
- `@classmethod` uses `cls`; `@staticmethod` uses neither.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete solution from scratch below** (function signature + body) to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.py` — `Rectangle` class: `__init__(width, height)`, method `area()` returning width*height, method `perimeter()`.
2. `easy/p02-solve.py` — `Counter` class: `__init__()` sets count to 0; `increment()` adds 1; `get()` returns current count.
3. `easy/p03-solve.py` — `Book` class: `__init__(title, author)`, `__str__` returns `"Title by Author"`.

### Medium
4. `medium/p01-solve.py` — `BankAccount` class: `__init__(owner, balance=0)`, `deposit(amount)`, `withdraw(amount)` (raise `ValueError` if insufficient funds), `__str__` returns `"Owner: $balance"`.
5. `medium/p02-solve.py` — `Stack` class (list-based): `push(item)`, `pop()` (raise `IndexError` if empty), `peek()`, `is_empty()`, `__len__`.
6. `medium/p03-solve.py` — `Temperature` class: `__init__(celsius)`; `@classmethod from_fahrenheit(f)`; `@staticmethod to_fahrenheit(c)`; instance method `fahrenheit()`.

### Hard
7. `hard/p01-solve.py` — `ShoppingCart` class: holds list of `(name, price)` items; `add_item(name, price)`, `total()`, `remove_item(name)` (removes first match), `__str__` lists items and total.
8. `hard/p02-solve.py` — `Student` class with class attribute `count` tracking total students; `__init__(name, grades=[])` (avoid mutable-default bug); `add_grade(g)`; `average()`; `@classmethod get_count()`.
9. `hard/p03-solve.py` — `Library` class composed of `Book` objects (from easy p03): `add_book(book)`, `find_by_author(author)` returning a list, `__len__`, `__str__` summarizing the collection.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python <filename>` to test with your own inputs.
- When done, tell me and I'll review. Say **"give me next task"** to advance to the next lesson.
