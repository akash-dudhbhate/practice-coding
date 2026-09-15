# Lesson 10 — Common Mistakes

## Mistake 01: Forgetting super().__init__()
```python
# WRONG — parent attributes not set
class Child(Parent):
    def __init__(self, child_arg):
        self.child_arg = child_arg

# CORRECT
class Child(Parent):
    def __init__(self, parent_arg, child_arg):
        super().__init__(parent_arg)
        self.child_arg = child_arg
```

## Mistake 02: Deep inheritance hierarchies
```python
# AVOID — hard to maintain
class A: pass
class B(A): pass
class C(B): pass
class D(C): pass
class E(D): pass

# PREFER — composition over inheritance
class E:
    def __init__(self):
        self.a = A()
        self.b = B()
```

## Mistake 03: Not using abstract classes
```python
# WRONG — can instantiate incomplete class
class Shape:
    def area(self):
        pass  # does nothing

# CORRECT — can't instantiate without implementing
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
```

## Mistake 04: Overriding without calling super
```python
# WRONG — parent behavior lost
class Child(Parent):
    def method(self):
        # does something but parent's method is never called

# CORRECT
class Child(Parent):
    def method(self):
        super().method()  # extend, don't replace
        # additional behavior
```

## Mistake 05: Using inheritance for code reuse only
```python
# WRONG — Dog doesn't "is-a" Runnable, it "has-a" ability to run
class Runnable:
    def run(self): ...
class Dog(Runnable): ...

# BETTER — composition or mixin
class Dog:
    def run(self): ...  # if all dogs run
# or
class Dog:
    def __init__(self):
        self.movement = Runnable()  # composition
```
