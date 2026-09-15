# Lesson 09 — Common Mistakes

## Mistake 01: Forgetting `self`
```python
# WRONG
def set_name(name):
    self.name = name

# CORRECT
def set_name(self, name):
    self.name = name
```

## Mistake 02: Class attribute for instance data
```python
# WRONG — shared across instances
class Student:
    grades = []

# CORRECT — per instance
class Student:
    def __init__(self):
        self.grades = []
```

## Mistake 03: Not using __str__
```python
# WRONG — unreadable default
class User:
    def __init__(self, name):
        self.name = name
print(user)  # <__main__.User at 0x...>

# CORRECT
class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"User({self.name})"
```

## Mistake 04: Directly accessing private attributes
```python
class Account:
    def __init__(self):
        self.__balance = 0

acc = Account()
acc.__balance = 1000  # WRONG — bypasses validation
# Actually creates a NEW attribute, doesn't modify __balance
```

## Mistake 05: Not using properties for computed values
```python
# WRONG — stored, can get out of sync
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.area = w * h  # doesn't update if w or h changes

# CORRECT — computed on access
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    @property
    def area(self):
        return self.w * self.h
```
