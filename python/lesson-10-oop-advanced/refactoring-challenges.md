# Lesson 10 — Refactoring Challenges

## Refactor 01 (Easy): Inheritance for Code Reuse
### Before
```python
class Stack(list):
    def push(self, x): self.append(x)
    # exposes sort, reverse, insert — breaks stack contract
```
### After
```python
class Stack:
    def __init__(self): self._data = []
    def push(self, x): self._data.append(x)
    def pop(self): return self._data.pop()
    def peek(self): return self._data[-1]
```

## Refactor 02 (Medium): No Abstract Class
### Before
```python
class Shape:
    def area(self): pass  # does nothing, subclass must override
```
### After
```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
```

## Refactor 03 (Hard): Deep Inheritance
### Before
```python
class A: def method(self): ...
class B(A): def method(self): ...
class C(B): def method(self): ...
class D(C): def method(self): ...
```
### After
```python
# Use composition instead
class D:
    def __init__(self):
        self.a = A()
        self.b = B()
    def method(self):
        return self.a.method() or self.b.method()
```
