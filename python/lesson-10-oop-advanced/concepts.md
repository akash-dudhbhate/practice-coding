# Lesson 10 — Concepts Explained (OOP Advanced)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Inheritance

**What:** Inheritance lets a class (child) reuse attributes and methods from another class (parent). The child gets everything the parent has, plus can add or override.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):           # Dog inherits from Animal
    def speak(self):          # override the parent method
        return f"{self.name} says Woof!"

d = Dog("Rex")
d.speak()  # "Rex says Woof!"  — uses Dog's version, not Animal's
```

**Why it exists:** Without inheritance, you'd copy-paste the same code into every class. A Dog, Cat, and Cow all have a name and can speak — inheritance lets them share the common parts (Animal) and customize the different parts (speak).

**Where it's used:** Frameworks (Django models, Flask views, unittest TestCase), game entities (Character → Player/Enemy), UI components (BaseButton → PrimaryButton), exception hierarchies (Exception → ValueError → CustomError).

**What goes wrong without it:**
- Code duplication — every class redefines `__init__`, `name`, common methods.
- Fix a bug in one class, forget to fix it in the other 10 identical classes.
- No polymorphism — you can't write code that works with "any Animal" because there's no shared parent.
- Deep inheritance chains (5+ levels) become hard to understand — prefer composition over deep inheritance.

---

## super()

**What:** `super()` lets a child class call methods from its parent class. Most commonly used in `__init__` to run the parent's initialization before adding the child's.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)    # call Animal.__init__ first
        self.breed = breed        # then add Dog-specific attribute

d = Dog("Rex", "Labrador")
d.name   # "Rex"      — set by Animal.__init__ via super()
d.breed  # "Labrador"  — set by Dog.__init__
```

**Why it exists:** Without `super()`, the child's `__init__` would completely replace the parent's. The parent's attributes would never get set. `super()` lets you extend the parent's behavior instead of replacing it.

**Where it's used:** Every time a child class needs to add to (not replace) the parent's initialization or methods.

**What goes wrong without it:**
- Forgetting `super().__init__()` → parent's attributes are never set → `AttributeError` when you try to access `self.name`.
- Calling `super()` after using `self` → `self` isn't fully initialized yet → subtle bugs.
- In multiple inheritance, `super()` follows MRO (Method Resolution Order) — not calling it in one class breaks the chain for others.

---

## Polymorphism

**What:** Polymorphism means "same interface, different behavior." Different classes can have the same method name, and you can call it without knowing which class you're dealing with.

```python
class Dog:
    def speak(self): return "Woof"
class Cat:
    def speak(self): return "Meow"
class Cow:
    def speak(self): return "Moo"

def make_sound(animal):
    return animal.speak()    # works for ANY animal with a speak() method

make_sound(Dog())  # "Woof"
make_sound(Cat())  # "Meow"
make_sound(Cow())  # "Moo"
```

**Why it exists:** Without polymorphism, you'd write `if type == "dog": return "Woof"` elif `type == "cat": ...` — a giant if/else chain that grows with every new animal. Polymorphism lets you add new types without changing existing code.

**Where it's used:** Every framework — Django's ORM (different model types, same query interface), Python's `len()` (works on strings, lists, dicts — they all implement `__len__`), file-like objects (strings, files, buffers all have `.read()`).

**What goes wrong without it:**
- Giant if/else type-checking chains — add a new type, edit 10 functions.
- `isinstance()` checks everywhere — brittle, hard to maintain.
- Can't swap implementations (e.g., swap SQLite for PostgreSQL) without rewriting code.

---

## Method Overriding

**What:** A child class redefines a method from the parent to change its behavior. The child's version replaces the parent's.

```python
class Shape:
    def area(self):
        return 0  # default: no area

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):           # override Shape.area
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):           # override Shape.area
        return self.w * self.h
```

**Why it exists:** The parent defines a default behavior ("shapes have an area"). Each child customizes it for its specific shape. Overriding lets you provide specialized behavior while keeping the same method signature.

**Where it's used:** Template method pattern (parent defines the algorithm, children override specific steps), framework hooks (override `save()` in Django models to add custom logic).

**What goes wrong without it:**
- All shapes return 0 for area — useless.
- Forgetting to override → child uses parent's default → wrong results.
- Changing the method signature (adding parameters) → breaks polymorphism — calling `shape.area()` fails for some shapes.

---

## @property Decorator

**What:** `@property` turns a method into something that looks like an attribute. You access it without parentheses.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius    # private convention (underscore)

    @property
    def area(self):              # accessed as circle.area, NOT circle.area()
        return 3.14 * self._radius ** 2

c = Circle(5)
c.area      # 78.5  — looks like an attribute, computed on the fly
```

You can also add a setter:
```python
    @area.setter
    def area(self, value):
        self._radius = (value / 3.14) ** 0.5
```

**Why it exists:** Without `@property`, you'd either: (a) make `area` a method (users must call `circle.area()` — ugly), or (b) compute and store `area` in `__init__` (goes stale if radius changes). `@property` gives clean attribute syntax with computed values.

**Where it's used:** Computed attributes (area, perimeter, full_name from first+last), validation on assignment, read-only attributes, backward compatibility (changing a method to a property without breaking callers).

**What goes wrong without it:**
- Stale cached values — `__init__` computes `area` once, then `radius` changes but `area` doesn't update.
- No validation — `circle.radius = -5` is accepted silently. With a property setter, you can reject negative values.
- Forgetting `@property` → users must call `circle.area()` → inconsistent API if some attributes are properties and others are methods.

---

## Dunder Methods (Magic Methods)

**What:** Dunder (double underscore) methods let your class work with Python's built-in operations — `+`, `==`, `len()`, `str()`, `[]`, etc.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):           # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):            # v1 == v2
        return self.x == other.x and self.y == other.y

    def __str__(self):                  # str(v) or print(v)
        return f"Vector({self.x}, {self.y})"

    def __len__(self):                  # len(v)
        return int((self.x**2 + self.y**2) ** 0.5)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v1 + v2     # Vector(4, 6)   — uses __add__
print(v1)   # Vector(1, 2)   — uses __str__
len(v2)     # 5              — uses __len__
```

**Why it exists:** Without dunder methods, you'd write `v1.add(v2)`, `v1.equals(v2)`, `v1.to_string()` — verbose and non-Pythonic. Dunder methods let your objects work with Python's native syntax (`+`, `==`, `print`, `len`, `for`, `in`).

**Where it's used:** Custom data types (vectors, matrices, money, dates), ORM models (`__str__` for display), collections (`__len__`, `__getitem__` for indexing), comparison (`__lt__`, `__gt__` for sorting).

**What goes wrong without it:**
- `print(my_object)` → `<__main__.MyClass object at 0x7f...>` — useless. Need `__str__`.
- `v1 + v2` → `TypeError: unsupported operand type`. Need `__add__`.
- `len(my_collection)` → `TypeError: object has no len()`. Need `__len__`.
- Sorting custom objects without `__lt__` → `TypeError: '<' not supported`.

---

## Class Methods (@classmethod) vs Static Methods (@staticmethod)

**What:**
- `@classmethod` — receives the CLASS as first argument (`cls`), not an instance. Can create instances.
- `@staticmethod` — receives NEITHER class nor instance. Just a function that lives in the class namespace.

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):        # cls = User (the class)
        name, age = data.split(",")
        return cls(name, int(age))     # creates a User instance

    @staticmethod
    def is_valid_age(age):              # no cls, no self
        return age >= 0 and age <= 150

User.from_string("Akash,25")   # User("Akash", 25) — alternative constructor
User.is_valid_age(25)          # True — utility function
```

**Why it exists:** `@classmethod` is for alternative constructors (creating instances from different input formats). `@staticmethod` is for utility functions that are logically related to the class but don't need instance/class data.

**Where it's used:** `@classmethod` — factory methods (Django's `Model.objects.create()`), alternative constructors (`datetime.fromtimestamp()`). `@staticmethod` — validation helpers, utility functions (`Math.max()` in other languages).

**What goes wrong without it:**
- Using `@staticmethod` when you need to create instances → can't call `cls()` → wrong decorator.
- Using `@classmethod` when you don't need class data → unnecessary `cls` parameter → confusing.
- Forgetting `@classmethod` → method expects `self` but you pass the class → `TypeError`.

---

## Abstract Base Classes (ABC)

**What:** ABCs define a contract — methods that child classes MUST implement. If a child doesn't implement them, Python raises an error.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass                    # no implementation — just the contract

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r ** 2
    def perimeter(self): return 2 * 3.14 * self.r

# Shape()        # ERROR — can't instantiate abstract class
# Circle(5)      # OK — implemented both abstract methods
```

**Why it exists:** Without ABCs, a child class might forget to implement `area()` — the bug only shows up when someone calls it. ABCs catch this at instantiation time, before it causes runtime errors.

**Where it's used:** Frameworks and libraries that define interfaces — Django's abstract models, Python's `collections.abc` (Iterable, Sized, Mapping), plugin architectures.

**What goes wrong without it:**
- Child class forgets to implement a method → `AttributeError` at runtime (hard to debug) instead of `TypeError` at instantiation (easy to debug).
- No way to enforce that all subclasses have the same interface — polymorphism breaks silently.
- Can't prevent direct instantiation of a base class that's meant to be subclassed only.

---

## Composition vs Inheritance

**What:** Composition means "has-a" (a Car has-an Engine) instead of "is-a" (a Dog is-an Animal). You include objects as attributes instead of inheriting.

```python
# Composition (has-a)
class Engine:
    def start(self): return "Vroom!"

class Car:
    def __init__(self):
        self.engine = Engine()    # Car HAS an Engine
    def start(self):
        return self.engine.start()

# vs Inheritance (is-a) — would be wrong here:
# class Car(Engine):  # Car IS an Engine? No, that doesn't make sense.
```

**Why it exists:** Inheritance creates tight coupling — changing the parent breaks all children. Composition is flexible — you can swap the Engine for an ElectricEngine without changing Car. "Favor composition over inheritance" is a core OOP principle.

**Where it's used:** Strategy pattern (swap algorithms), dependency injection (swap implementations), game entities (Entity has Components), Django (model has fields, not inherits from field types).

**What goes wrong without it:**
- Deep inheritance chains (Vehicle → Car → SportsCar → RaceCar) → changing Vehicle breaks everything below.
- Wrong "is-a" relationships: `class Stack(list)` — a Stack is NOT a list (it shouldn't allow random access), but inheritance exposes all list methods.
- Can't change behavior at runtime — inheritance is fixed at class definition. Composition lets you swap components dynamically.

---

## Encapsulation (Private Attributes)

**What:** Encapsulation hides internal data from outside access. Python uses convention: `_name` (protected — don't touch), `__name` (name-mangled — harder to touch).

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # private (name-mangled)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.__balance     # AttributeError — can't access directly
account._BankAccount__balance  # works but you SHOULDN'T (name mangling)
account.get_balance() # 100 — the proper way
```

**Why it exists:** Without encapsulation, anyone can set `account.balance = -1000` — bypassing validation. Encapsulation forces access through methods where you can validate, log, and protect data.

**Where it's used:** Any class with internal state that shouldn't be modified directly — bank accounts, database connections, configuration objects, game state.

**What goes wrong without it:**
- `account.balance = -1000` → invalid state, no validation → bugs, security issues.
- Internal implementation changes break external code — if `balance` is public, you can't rename it without breaking everyone who uses `account.balance`.
- Python's "private" is by convention, not enforced — `_name` is "protected" (accessible but you shouldn't), `__name` is "private" (name-mangled, harder but still accessible). Don't rely on it for security.

---

## Multiple Inheritance & MRO

**What:** A class can inherit from multiple parents. Python uses MRO (Method Resolution Order) to decide which parent's method to use.

```python
class A:
    def greet(self): return "A"

class B(A):
    def greet(self): return "B"

class C(A):
    def greet(self): return "C"

class D(B, C):       # multiple inheritance
    pass

D().greet()          # "B" — MRO is D → B → C → A
D.__mro__            # (D, B, C, A, object) — the order
```

**Why it exists:** Sometimes a class genuinely needs features from multiple sources — a `FlyingCar` inherits from both `Car` and `Aircraft`. Multiple inheritance lets you combine capabilities.

**Where it's used:** Mixins (small reusable classes that add one feature), Django's model inheritance, Tkinter widgets.

**What goes wrong without it:**
- Diamond problem: `D` inherits from `B` and `C`, both inherit from `A`. Which `A` method does `D` get? Python's MRO (C3 linearization) resolves this, but it can be confusing.
- Calling `super()` in multiple inheritance — the order matters. If one parent doesn't call `super()`, the chain breaks.
- Overuse → "spaghetti inheritance" — impossible to trace which method comes from where. Prefer composition for complex cases.
