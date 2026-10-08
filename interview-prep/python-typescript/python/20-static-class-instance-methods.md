# 20 — `@staticmethod` vs `@classmethod` vs instance method — when each

> **Interview question:** "What's the difference between a static method, a class method, and an instance method in Python?"
> **What the interviewer is really testing:** Do you understand what each one *receives implicitly* (`self` vs `cls` vs nothing) and when that actually matters?

## Theory — what it is

All three are functions defined inside a class body; they differ only in **what Python automatically passes as the first argument** when you call them.

An **instance method** is the default. Its first parameter is `self` — the specific object the method was called on. Python fills it in automatically: `obj.m(x)` really means `Class.m(obj, x)`. Use it whenever the method needs to read or change that object's own data (`self.name`, `self.balance`).

A **`@classmethod`** takes `cls` — the *class itself* — as the first argument, filled in automatically whether you call it on the class (`C.m()`) or an instance (`obj.m()`). Its signature job is **alternative constructors** (`User.from_dict(d)`, `datetime.now()`), because `cls(...)` calls the constructor of whatever class it was invoked on — which keeps subclassing working.

A **`@staticmethod`** takes nothing implicitly. It's just a plain function namespaced inside a class. It can't touch `self` or `cls`. Use it when a function logically *belongs* to the class (it's about the class's domain) but needs no state — utilities, validators, helpers.

## Why it was needed

Without `@classmethod`, every class would have exactly one way to build objects — `__init__` — and subclassing would break. If `Date.from_string("2024-01-01")` were a staticmethod that did `return Date(...)`, a subclass `MyDate.from_string(...)` would still return a `Date`, not a `MyDate`. `cls` fixes this: it always points at the class the method was called on.

Without `@staticmethod`, you'd have two bad options: (a) put helper functions at module top-level where they're divorced from the class they relate to, or (b) make them instance methods with a useless `self` parameter — which misleads readers into thinking the method needs object state. Static methods say "this is related to the class but touches no state," which is both honest and slightly faster (no bound-method creation).

## Where it's used in a real project

- **classmethod**: alternative constructors — `dict.fromkeys()`, `datetime.fromtimestamp()`, `User.from_json(payload)`, factory methods that must work with subclasses.
- **classmethod**: accessing/mutating *class-level* state shared by all instances — e.g., a `cls.registry` that tracks all subclasses, or a class counter.
- **staticmethod**: pure helpers — `Order.is_valid_email(email)`, `Geometry.area_of_circle(r)`, `Parser.strip_whitespace(s)`.
- **instance method**: everything that reads/writes one object's fields — `account.withdraw(50)`, `user.full_name()`, `cart.add_item(item)`.

## Diagram

```
                    what gets passed automatically?
class C:                    call on class C  call on obj c=C()
├─ def m(self):      self →   C.m() ✘error    c.m()  → self=c
├─ @classmethod            ├─  C.cm() → cls=C   c.cm() → cls=C (the class!)
│    def cm(cls):   cls  ──┘  always receives the CLASS
└─ @staticmethod                C.sm() → nothing  c.sm() → nothing
     def sm():        (none)    works like a plain function

Use for:
self → read/write ONE object's fields   (obj.balance)
cls  → build objects, touch class state (User.from_csv)
none → pure helper namespaced in class  (Validator.is_email)
```

## Code — explained

```python
class Temperature:
    freezing_c = 0  # class attribute: shared by all instances

    def __init__(self, celsius):
        self.celsius = celsius          # instance attribute

    # --- instance method: needs THIS object's data ---
    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    # --- classmethod: alternative constructor, gets cls ---
    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5 / 9)    # cls(...) respects subclasses

    # --- staticmethod: pure helper, no self/cls ---
    @staticmethod
    def is_valid_celsius(c):
        return -273.15 <= c <= 1_000_000

t = Temperature(100)
print(t.to_fahrenheit())                    # 212.0
print(Temperature.from_fahrenheit(32).celsius)  # 0.0
print(Temperature.is_valid_celsius(-300))   # False

# classmethod respects subclasses — staticmethod would not
class Kelvin(Temperature):
    pass
k = Kelvin.from_fahrenheit(212)
print(type(k).__name__, k.celsius)          # Kelvin 100.0
```

1. `to_fahrenheit(self)` is an instance method — `t.to_fahrenheit()` secretly calls `Temperature.to_fahrenheit(t)`, so `self.celsius` is `100`.
2. `@classmethod from_fahrenheit(cls, f)` receives the class. `Temperature.from_fahrenheit(32)` → `cls` is `Temperature` → `cls(0.0)` builds a new `Temperature`.
3. `@staticmethod is_valid_celsius(c)` gets nothing implicit — it's a plain function living in the class namespace. Called on the class or an instance identically.
4. The subclass demo is the payoff: `Kelvin.from_fahrenheit(212)` sets `cls = Kelvin`, so `cls(...)` builds a `Kelvin`, not a `Temperature`. A staticmethod version would have hardcoded `Temperature(...)` and broken this.
5. Note `freezing_c` is a *class attribute* — reachable via `cls` in classmethods, `self` in instance methods, but **not** at all in staticmethods.

## Problems

### Easy — which decorator?
**Problem:** You have `class Circle` storing `radius`. Add a method `area()` that returns `π·r²`, and a method `unit_circle()` that returns a `Circle` of radius 1. Which decorator (if any) does each need?
**Try this input:**
```python
c = Circle(2)
print(round(c.area(), 2))
print(Circle.unit_circle().radius)
```
**Expected output:**
```
12.57
1
```
**Solution:**
```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):                    # instance method: needs self.radius
        return math.pi * self.radius ** 2

    @classmethod
    def unit_circle(cls):              # classmethod: builds a cls instance
        return cls(1)

c = Circle(2)
print(round(c.area(), 2))
print(Circle.unit_circle().radius)
```
**Logic explained:**
1. `area` reads `self.radius` — per-object data — so it's a plain instance method.
2. `unit_circle` constructs a `Circle` but is called on the *class* (`Circle.unit_circle()`), so it must be a `@classmethod` with `cls` — `cls(1)` calls `__init__(1)`.
3. If `unit_circle` were a `@staticmethod` doing `Circle(1)`, subclasses like `UnitCircle` would get back the wrong type.

### Medium — track instances with class state
**Problem:** Create a `User` class that counts how many users have been created. Expose `User.count()` (classmethod) and a staticmethod `User.is_valid_name(name)` that returns True for non-empty strings under 50 chars.
**Try this input:**
```python
u1 = User("alice")
u2 = User("bob")
print(User.count())
print(User.is_valid_name(""))
print(User.is_valid_name("carol"))
```
**Expected output:**
```
2
False
True
```
**Solution:**
```python
class User:
    _count = 0                       # class attribute, shared

    def __init__(self, name):
        if not User.is_valid_name(name):
            raise ValueError("bad name")
        self.name = name
        User._count += 1

    @classmethod
    def count(cls):
        return cls._count

    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and 0 < len(name) < 50

u1 = User("alice")
u2 = User("bob")
print(User.count())
print(User.is_valid_name(""))
print(User.is_valid_name("carol"))
```
**Logic explained:**
1. `_count` lives on the class, not instances — `User._count += 1` bumps it for everyone.
2. `count` is a `@classmethod` because it reads class state (`cls._count`) and needs no instance.
3. `is_valid_name` is a `@staticmethod` — it's a pure check on the argument alone; no `self`, no `cls`. `__init__` calls it as `User.is_valid_name(name)` for validation.

### Hard — polymorphic factory
**Problem:** Write `Shape.from_string(s)` that parses `"circle 2"` or `"square 3"` and returns a `Circle` or `Square` instance (both subclasses of `Shape`) — each with an `area()` method. The factory must live on `Shape` and dispatch correctly.
**Try this input:**
```python
print(round(Shape.from_string("circle 2").area(), 2))
print(Shape.from_string("square 3").area())
print(type(Shape.from_string("circle 1")).__name__)
```
**Expected output:**
```
12.57
9
Circle
```
**Solution:**
```python
import math

class Shape:
    _kinds = {}                       # registry: name → subclass

    def __init_subclass__(cls, **kw):
        super().__init_subclass__(**kw)
        Shape._kinds[cls.__name__.lower()] = cls

    @classmethod
    def from_string(cls, s):
        name, size = s.split()
        subclass = cls._kinds[name.lower()]
        return subclass(float(size))

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2

class Square(Shape):
    def __init__(self, s):
        self.s = s
    def area(self):
        return self.s ** 2

print(round(Shape.from_string("circle 2").area(), 2))
print(Shape.from_string("square 3").area())
print(type(Shape.from_string("circle 1")).__name__)
```
**Logic explained:**
1. `__init_subclass__` runs automatically each time a `Shape` subclass is defined, registering it in `Shape._kinds` — a real-world plugin pattern.
2. `from_string` is a `@classmethod` because it must be callable on `Shape` (no instance exists yet) and needs access to class data (`cls._kinds`).
3. It splits `"circle 2"` → looks up `Circle` → calls `Circle(2.0)` → returns the right subclass instance, whose `area()` is polymorphic.
4. This is exactly why `cls` matters: the factory works even if renamed or subclassed, and adding a `Triangle(Shape)` later needs zero changes to `from_string`.

## The 30-second interview answer

"The difference is what Python passes implicitly as the first argument. Instance methods get `self` — one specific object — so use them for anything reading or writing that object's fields. `@classmethod` gets `cls`, the class itself, so it's for alternative constructors like `User.from_dict` and for touching class-level state — crucially, `cls` respects subclassing, so `cls(...)` builds the right type. `@staticmethod` gets nothing — it's just a function namespaced inside the class for helpers that relate to the class but need no state. A rule of thumb: if it doesn't need `self`, don't give it `self`; if it builds or touches the class, use `cls`; if it's pure, make it static."

## Follow-up trap

**"Can you call a staticmethod/classmethod on an instance? What happens?"** Yes — `obj.static_m()` and `obj.class_m()` both work fine. The trap is the second half: for a classmethod called on an instance, `cls` is still the *class of the instance* (`type(obj)`), not the instance — so `Kelvin().from_fahrenheit()` returns a `Kelvin`. And for a staticmethod, `obj.sm()` is just sugar — no `self` is passed; `obj.sm()` == `C.sm()`. Bonus trap: *"why does `staticmethod` exist at all — why not a module function?"* — namespacing and intent: `Date.from_ordinal` inside `Date` says "this belongs to Date's API"; a free function `parse_date_ordinal` floats loose. Also, `staticmethod` used to matter before Python 3 for unbound-method rules — today it's purely organizational, which is a fine answer.
