# lesson-10-oop-advanced — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Missing super().__init__()
```python
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        self.num_doors = num_doors
```
<details><summary>Answer</summary>
**Bug:** Parent's `__init__` not called — `make`, `model`, `year` never set.
**Fix:** `super().__init__(make, model, year); self.num_doors = num_doors`.
</details>

## Debug 02 (Medium): Property without setter
```python
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    @property
    def area(self):
        return self.w * self.h

r = Rectangle(4, 5)
r.area = 20
```
<details><summary>Answer</summary>
**Bug:** `@property` without `@area.setter` makes area read-only. `r.area = 20` → AttributeError.
**Fix:** Remove the assignment (area is computed) or add a setter.
</details>

## Debug 03 (Hard): Wrong MRO
```python
class A:
    def speak(self): return "A"
class B(A):
    def speak(self): return "B"
class C(A):
    def speak(self): return "C"
class D(B, C):
    pass
D().speak()
```
<details><summary>Answer</summary>
Returns `"B"` — MRO (Method Resolution Order) is D → B → C → A. Python uses C3 linearization. `D().speak()` finds `B.speak()` first.
</details>

---

## Common Mistakes — the traps learners hit

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

---

## Refactoring Challenges — make working code better

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

---

## Approach Comparison — different ways to solve it

## Problem: Stack Implementation

### Approach 1: Inheritance (is-a)
```python
class Stack(list):
    def push(self, item): self.append(item)
    def pop(self): return super().pop()
    def peek(self): return self[-1]
```
**Cons:** Exposes ALL list methods (sort, reverse, insert). Users can break the stack.

### Approach 2: Composition (has-a)
```python
class Stack:
    def __init__(self):
        self._data = []
    def push(self, item): self._data.append(item)
    def pop(self): return self._data.pop()
    def peek(self): return self._data[-1]
```
**Pros:** Only exposes stack methods. Internal list is hidden. Can't be broken.

**Winner:** Approach 2 (composition) — "favor composition over inheritance" (Gang of Four).

---

## Problem: Temperature Class

### Approach 1: Methods
```python
class Temperature:
    def __init__(self, c):
        self.c = c
    def to_f(self): return self.c * 9/5 + 32
    def to_k(self): return self.c + 273.15
```
Usage: `t.to_f()` — looks like a function call.

### Approach 2: Properties
```python
class Temperature:
    def __init__(self, c):
        self.c = c
    @property
    def f(self): return self.c * 9/5 + 32
    @property
    def k(self): return self.c + 273.15
```
Usage: `t.f` — looks like an attribute. More natural.

**Winner:** Approach 2 (properties) — computed attributes feel like data, not function calls.
