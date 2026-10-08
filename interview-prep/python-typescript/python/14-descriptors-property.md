# 14 — Descriptors and `@property` Under the Hood

> **Interview question:** "What is a descriptor? How does `@property` work under the hood?"
> **What the interviewer is really testing:** Whether you know that attribute access isn't a dict lookup — it's a protocol — and that `property` is just a class implementing it.

## Theory — what it is

A **descriptor** is any object that defines one or more of:

- `__get__(self, obj, objtype)` — runs when the attribute is *read*
- `__set__(self, obj, value)` — runs when the attribute is *assigned*
- `__delete__(self, obj)` — runs on `del obj.attr`

When a descriptor sits as a **class attribute**, it hijacks attribute access. `obj.x` doesn't just do `obj.__dict__["x"]` — Python first checks whether `type(obj).__dict__["x"]` is a descriptor, and if so calls its `__get__`.

**Precedence rule** (worth memorizing): a descriptor with `__set__`/`__delete__` (a *data* descriptor) wins over the instance `__dict__`; a `__get__`-only descriptor (a *non-data* descriptor) loses to it. That's why `obj.x = 5` can shadow a non-data descriptor but can't bypass a `property` setter.

`property` is just a **built-in descriptor class**. `@property def area(self)` is literally `area = property(area)` — an object with `__get__` that calls your function. Adding `@area.setter` gives the same object a `__set__`, making it a data descriptor.

## Why it was needed

Without descriptors, you can't intercept attribute access — you'd have to expose methods (`obj.get_price()`, `obj.set_price(x)`) like Java. Descriptors let a class attach validation, lazy loading, unit conversion, or logging to a plain-looking attribute. `property` exists because writing a full descriptor class for "validate this one field" is boilerplate — `property` is the 90% case packaged nicely.

## Where it's used in a real project

- **Validation**: `product.price = -5` raising `ValueError` — the field *looks* like a plain attribute.
- **Computed attributes**: `circle.area` recomputed on each read; ORMs use this heavily (`user.full_name`).
- **Lazy loading**: a descriptor that fetches a value on first access and caches it (e.g., `lazy_property` — below).
- **Framework magic**: Django/SQLAlchemy model fields are descriptors — `user.email` actually emits SQL.

## Diagram

```
obj.x = 5                read: obj.x
    |                        |
    v                        v
is type(obj).x a       is type(obj).x a
data descriptor?       descriptor?
    |                        |
 yes -> x.__set__       yes -> x.__get__(obj, cls)
       (obj, 5)              |
    |                   non-data only:
    |                   obj.__dict__["x"] wins
 no  -> obj.__dict__         |
       ["x"] = 5        no -> obj.__dict__["x"]
                             (or class default)
```

## Code — explained

A descriptor by hand — validates that `price` stays positive:

```python
class Positive:
    def __set_name__(self, owner, name):
        self.name = name                     # learns it's called "price"

    def __get__(self, obj, objtype=None):
        if obj is None:                      # accessed on the CLASS
            return self
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be positive")
        obj.__dict__[self.name] = value      # store in the INSTANCE dict

class Product:
    price = Positive()                       # ONE descriptor, shared by all instances
    def __init__(self, price):
        self.price = price                   # routed through __set__!

p = Product(10)
print(p.price)                               # 10
# p.price = -3   -> ValueError: price must be positive
```

And the same behavior via `property` — notice it *is* a descriptor:

```python
class Product:
    def __init__(self, price):
        self.price = price

    @property                                # == price = property(price)
    def price(self):
        return self._price

    @price.setter                            # gives the property a __set__
    def price(self, value):
        if value <= 0:
            raise ValueError("price must be positive")
        self._price = value                  # note: _price, not price (no recursion!)
```

Line-by-line:

1. `price = Positive()` — the descriptor lives on the **class**; instances share it. Values go into each instance's `__dict__`, keyed by the attribute name.
2. `__set_name__` (Python 3.6+) tells the descriptor which attribute name it manages, for nice error messages and storage keys.
3. `obj is None` in `__get__` — `Product.price` (class access) should return the descriptor itself, not a value.
4. `self._price` in the property — writing `self.price` inside the setter would recurse forever; the underscore attribute is the storage.
5. `Product.price` with `property` returns the *property object* — `Product.price.__get__(p, Product)` is literally what `p.price` expands to.

## Problems

### Easy — Computed property
**Problem:** Give `Rectangle` a read-only `area` property.
**Try this input:**
```python
r = Rectangle(3, 4)
print(r.area)
r.area = 99
```
**Expected output:**
```
12
AttributeError: can't set attribute 'area'
```
**Solution:**
```python
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    @property
    def area(self):
        return self.w * self.h

r = Rectangle(3, 4)
print(r.area)      # 12
# r.area = 99      # AttributeError — no setter defined
```
**Logic explained:**
1. `@property` builds a descriptor with only `__get__`... but `property` *always* defines `__set__` too (which raises `AttributeError` if no setter was added) — so it's a data descriptor and can't be shadowed.
2. `r.area` calls `Rectangle.area.__get__(r)` → `r.w * r.h` → `12`, recomputed fresh each read.

### Medium — Validated setter
**Problem:** `Person.age` must reject non-int and negative values.
**Try this input:**
```python
p = Person(30)
p.age = 31
print(p.age)
# p.age = -1  -> ValueError
```
**Expected output:** `31`
**Solution:**
```python
class Person:
    def __init__(self, age):
        self.age = age                    # goes through the setter

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("age must be an int")
        if value < 0:
            raise ValueError("age must be >= 0")
        self._age = value

p = Person(30)
p.age = 31
print(p.age)           # 31
```
**Logic explained:**
1. `self.age = age` in `__init__` routes through the setter — validation applies from birth.
2. Getter returns the private `self._age`; never touch `self.age` inside the methods or you'd recurse.
3. Setter validates type then range, then stores.

### Hard — Lazy caching descriptor
**Problem:** Implement `lazy_property` — a **non-data** descriptor that computes a value once, caches it in the instance dict, and never recomputes. Prove it caches.
**Try this input:**
```python
class Report:
    calls = 0

    @lazy_property
    def heavy(self):
        Report.calls += 1
        return 42

r = Report()
print(r.heavy, r.heavy, Report.calls)
```
**Expected output:** `42 42 1`
**Solution:**
```python
class lazy_property:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__          # key for the instance cache

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = self.func(obj)             # compute once...
        obj.__dict__[self.name] = value    # ...store in the INSTANCE dict
        return value

class Report:
    calls = 0

    @lazy_property
    def heavy(self):
        Report.calls += 1
        return 42

r = Report()
print(r.heavy, r.heavy, Report.calls)      # 42 42 1
```
**Logic explained:**
1. First `r.heavy` → `__get__` runs `func`, stores `42` into `r.__dict__["heavy"]`.
2. `lazy_property` has **no `__set__`** — it's a *non-data* descriptor, so the instance dict entry now shadows it.
3. Second `r.heavy` → `obj.__dict__["heavy"]` wins; `__get__` never runs again. `calls` stays `1`. This is exactly how `functools.cached_property` works.

## The 30-second interview answer

"A descriptor is an object implementing `__get__`, `__set__`, or `__delete__` — when it's a class attribute, Python routes attribute access through those methods instead of a plain dict lookup. `property` is a built-in descriptor: `@property def x` is `x = property(x)`, and `@x.setter` adds the `__set__`, making it a data descriptor that instance assignment can't bypass. Data descriptors beat `obj.__dict__`; non-data descriptors lose to it — which is how `cached_property` caches. Functions, methods, and `staticmethod` are all descriptors too — `__get__` is what binds `self`."

## Follow-up trap

**"Why does this descriptor recurse forever?"**

```python
def __set__(self, obj, value):
    obj.price = value          # BUG: calls this same __set__ again!
```

Writing `obj.<same name>` inside `__set__`/`__get__` re-triggers the descriptor → infinite recursion. Store in `obj.__dict__[name]` or a differently-named attribute (`obj._price`). The matching trap in `__get__` is `return obj.price` — same infinite loop.

Also know the precedence gotcha cold: `instance.attr = x` on a class with a `@property` **raises AttributeError** (data descriptor), but on a `__get__`-only descriptor it silently *shadows* it — that's the whole difference between data and non-data.
