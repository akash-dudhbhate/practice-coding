# Lesson 09 — Concepts Explained (OOP Basics)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Class

**What:** A class is a blueprint for creating objects. It defines what attributes (data) and methods (behavior) every instance of that type will have.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"

d = Dog("Rex")       # create an instance (object)
d.bark()             # "Rex says Woof!"
d.name               # "Rex"  (attribute access)
```

**Why it exists:** When you have many things of the same kind (10 dogs, 100 users, 1000 products), a class lets you define the shape and behavior once and create as many instances as you need. It bundles data with the operations that act on it.

**Where it's used:** Modeling real-world entities (User, Product, Order), data structures (Stack, Queue), game entities, UI components, almost every non-trivial program.

**What goes wrong without it:**
- You use parallel dicts/lists to represent objects → no methods, no type safety, easy to misspell keys, logic scattered.
- Code that should be together (a user and its actions) is spread across many functions → hard to maintain.
- No way to enforce that every "user" has the required fields.

---

## `__init__` and `self`

**What:** `__init__` is the constructor — it runs when you create an instance, setting up its initial state. `self` refers to the current instance.

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # instance attribute
        self.age = age

p = Person("Akash", 25)
# __init__ runs automatically; self is p
p.name   # "Akash"
p.age    # 25
```

**Why it exists:** Every object needs initialization — set its starting data, validate inputs, open resources. `__init__` guarantees that setup happens at creation time. `self` lets methods refer to the specific instance they're operating on.

**Where it's used:** Every class that holds data. The constructor is where you set up the object's state.

**What goes wrong without it:**
- Forgetting `self`: `def __init__(name, age):` → `TypeError: __init__() missing 1 required positional argument`. The instance is always passed as the first arg automatically.
- `name = name` instead of `self.name = name` → creates a local variable that's discarded; the attribute is never set → `AttributeError` later.
- Forgetting to define `__init__` → instances have no initial attributes; you must set them manually (error-prone).

---

## Instance Attributes vs Class Attributes

**What:** Instance attributes belong to each object (unique per instance). Class attributes belong to the class itself (shared by all instances).

```python
class Car:
    wheels = 4              # class attribute — shared by ALL cars
    count = 0               # class attribute — tracks total cars

    def __init__(self, brand):
        self.brand = brand  # instance attribute — unique per car
        Car.count += 1

c1 = Car("Toyota")
c2 = Car("Honda")
c1.brand       # "Toyota"  (instance)
c2.brand       # "Honda"   (instance)
c1.wheels      # 4  (class attribute, accessed via instance)
Car.wheels     # 4  (class attribute, accessed via class)
Car.count      # 2
```

**Why it exists:** Some data is the same for every instance (all cars have 4 wheels) — that's a class attribute, defined once. Some data differs per instance (brand) — that's an instance attribute. Separating them avoids redundant copies.

**Where it's used:** Constants (`wheels`, `species`), counters (how many instances exist), default values shared across instances.

**What goes wrong without it:**
- **Mutable class attribute bug**: `class X: items = []` — ALL instances share the SAME list. `x1.items.append(1)` affects `x2.items` too. Fix: initialize in `__init__` as `self.items = []`.
- Setting `c1.wheels = 3` creates an INSTANCE attribute that shadows the class attribute for `c1` only — `c2.wheels` is still 4. This surprises people.
- Forgetting `Car.count += 1` should reference the class (`Car.count`), not `self.count`, which would create an instance attribute.

---

## Instance Methods

**What:** A method is a function defined inside a class that operates on an instance. The first parameter is always `self` (the instance).

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
        return self.balance

acct = BankAccount("Akash", 100)
acct.deposit(50)     # 150
acct.withdraw(30)    # 120
```

**Why it exists:** Methods bundle behavior with the data it operates on. Instead of free functions `deposit(acct, 50)`, you write `acct.deposit(50)` — clearer and ensures the right object is used.

**Where it's used:** Every class that has behavior — `list.append`, `str.upper`, your own domain logic.

**What goes wrong without it:**
- Forgetting `self` in the method signature → `TypeError: takes 0 positional arguments but 1 was given` (Python passes the instance automatically).
- Calling `BankAccount.deposit(50)` without an instance → missing `self`. Call on an instance: `acct.deposit(50)`.
- Methods that mutate state without validation → invalid states (negative balance). Validate inside methods.

---

## `__str__` and `__repr__`

**What:** `__str__` controls what `print(obj)` and `str(obj)` show (user-friendly). `__repr__` controls what `repr(obj)` and the REPL show (developer-friendly, ideally unambiguous).

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

p = Point(3, 4)
print(p)      # (3, 4)         <- __str__
p             # Point(3, 4)    <- __repr__ (in REPL)
str(p)        # "(3, 4)"
repr(p)       # "Point(3, 4)"
```

**Why it exists:** Without these, printing an object shows `<__main__.Point object at 0x7f...>` — useless. Defining them makes objects readable in logs, debugging, and the REPL.

**Where it's used:** Debugging, logging, displaying objects to users, collections of objects.

**What goes wrong without it:**
- No `__str__` → ugly memory-address output in logs; hard to debug.
- `__repr__` that isn't unambiguous (e.g., returns same as `__str__`) → harder to reconstruct objects from output.
- If only `__repr__` is defined, it's used as fallback for `str()` too. If only `__str__`, `repr` falls back to the ugly default.

---

## Encapsulation (Public vs "Private")

**What:** Python uses convention: a leading underscore (`_x`) means "internal, don't touch." A double leading underscore (`__x`) triggers name mangling to reduce accidental clashes.

```python
class Account:
    def __init__(self, balance):
        self._balance = balance   # "protected" by convention
        self.__secret = "pin"     # name-mangled to _Account__secret

    def get_balance(self):        # controlled access
        return self._balance

a = Account(100)
a._balance          # works, but convention says don't access directly
# a.__secret         # AttributeError
a._Account__secret  # works (mangled) — Python doesn't truly hide
```

**Why it exists:** Encapsulation protects internal state from being broken by external code. You expose safe methods (`get_balance`) and hide the raw field so callers can't put it in an invalid state.

**Where it's used:** Any class with invariants to protect — balance can't go negative, email must be valid, internal caches shouldn't be touched.

**What goes wrong without it:**
- Directly mutating `account.balance = -999` bypasses validation → invalid state.
- Overusing `__` name mangling → makes subclassing and testing harder. Prefer single `_` for "internal."
- Python doesn't enforce privacy — it's a convention. Relying on it for security is a mistake.

---

## Static & Class Methods

**What:** `@staticmethod` is a method that doesn't need the instance or class. `@classmethod` receives the class as the first argument (`cls`), not an instance.

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def to_fahrenheit(c):
        return c * 9/5 + 32      # doesn't need an instance

    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5/9)   # creates an instance (alternative constructor)

Temperature.to_fahrenheit(100)        # 212.0  (no instance needed)
t = Temperature.from_fahrenheit(212)  # Temperature(100.0)
```

**Why it exists:** Some methods logically belong to a class but don't need instance data (utility functions, alternative constructors). Static methods are plain functions in the class namespace; class methods can create instances (factory pattern).

**Where it's used:** Alternative constructors (`dict.fromkeys`), utility helpers, factory methods in inheritance hierarchies.

**What goes wrong without it:**
- Using `@staticmethod` when you need `cls` to create instances → can't build the right subclass type.
- Forgetting `@classmethod` decorator but using `cls` → `cls` isn't passed; `TypeError`.
- Putting functions that don't use the class as static methods when they'd be clearer as module-level functions.

---

## Object Composition vs "God Class"

**What:** Build complex objects from simpler objects (composition) rather than one giant class with everything.

```python
class Engine:
    def start(self): return "vroom"

class Wheel:
    def rotate(self): return "spinning"

class Car:
    def __init__(self):
        self.engine = Engine()    # composed
        self.wheels = [Wheel() for _ in range(4)]

    def drive(self):
        return self.engine.start() + " " + ", ".join(w.rotate() for w in self.wheels)
```

**Why it exists:** A class doing 50 things is unmaintainable. Composition lets each part have one job; you combine them. "Prefer composition over inheritance" is a key OOP principle.

**Where it's used:** Building systems from components — a `User` has an `Address`, a `Order` has `LineItem`s, a `Car` has an `Engine`.

**What goes wrong without it:**
- God classes: one class with 2000 lines and 50 methods → impossible to test, understand, or change.
- Tight coupling: everything knows everything → changing one part breaks many.
- Hard to test in isolation because dependencies are baked in, not injected.
