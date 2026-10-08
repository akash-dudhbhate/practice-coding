# 11 — `__init__` vs `__new__`

> **Interview question:** "What's the difference between `__init__` and `__new__`? When would you ever touch `__new__`?"
> **What the interviewer is really testing:** Whether you understand that object creation is a two-step process — and that `__init__` is *not* a constructor in the Java sense.

## Theory — what it is

When you write `obj = MyClass("x")`, Python does **two** things, in order:

1. `__new__(cls, ...)` — a static method that **creates** the object (allocates it) and returns it. This is the real "constructor."
2. `__init__(self, ...)` — receives the already-created object as `self` and **initializes** it (sets attributes). It must return `None`.

Think of building a house: `__new__` pours the concrete and erects the frame (a new object exists); `__init__` paints the walls and moves in furniture (the object gets its state). 99% of the time the default `object.__new__` does the creating fine, so you only ever write `__init__` — which is why people mistakenly call `__init__` "the constructor."

Jargon check: a **static method** is a function on a class that doesn't get `self` — `__new__` gets the *class* (`cls`) instead, because no instance exists yet when it runs.

## Why it was needed

If creation and initialization were one step, you'd have no hook for cases where **what gets created** depends on logic — or where the object can't be modified after creation:

- **Immutable types** (`int`, `str`, `tuple`): you can't fix the value inside `__init__`, because by then the immutable object already exists. Subclassing `str` requires `__new__`.
- **Singletons / object reuse**: `__new__` can return a cached existing object instead of building a new one.
- **Factories**: `__new__` can return an instance of a *different* class entirely.

Without `__new__` as a separate hook, none of these patterns would be possible.

## Where it's used in a real project

- **Singleton pattern**: a `Settings` or `DBConnection` class that must have exactly one instance.
- **Subclassing `str`/`tuple`/`int`**: e.g., a `LowerStr` that always stores lowercase, or a `SortedTuple`.
- **Factory by argument**: `Pet("dog")` returns a `Dog` instance while `Pet("cat")` returns a `Cat`.
- **Frameworks/metaclasses**: ORMs and plugin systems override `__new__` to control instance creation.

## Diagram

```
MyClass("x")
     |
     v
+-------------------+       +------------------------+
| __new__(cls, "x") |       | __init__(self, "x")    |
|  creates object,  |  -->  |  receives that object  |
|  RETURNS it       |       |  sets attributes on it |
+-------------------+       |  returns None          |
                            +------------------------+
 Rule: __init__ runs ONLY if __new__ returned
 an instance of cls (or a subclass). Otherwise skipped.
```

## Code — explained

```python
class Demo:
    def __new__(cls, name):
        print("1. __new__ runs — creating the object")
        return super().__new__(cls)        # delegate allocation to object

    def __init__(self, name):
        print("2. __init__ runs — object already exists:", self)
        self.name = name

d = Demo("bob")
# Output:
# 1. __new__ runs — creating the object
# 2. __init__ runs — object already exists: <Demo object ...>
```

Line-by-line:

1. `Demo("bob")` — Python calls `Demo.__new__(Demo, "bob")` first.
2. `super().__new__(cls)` — `object.__new__` actually allocates the instance; you almost never allocate memory yourself.
3. Python checks: is the returned object an instance of `Demo`? Yes → it calls `__init__` with the same `"bob"` argument.
4. `__init__` just stores state. Whatever it returns is ignored (returning a value raises `TypeError`).

## Problems

### Easy — Predict the order
**Problem:** What prints when you run this?
```python
class A:
    def __new__(cls):
        print("new")
        return super().__new__(cls)
    def __init__(self):
        print("init")

a = A()
```
**Try this input:** run the code.
**Expected output:**
```
new
init
```
**Solution:** (the code above *is* the answer)
**Logic explained:**
1. `A()` triggers `A.__new__` first — `"new"` prints.
2. `super().__new__(cls)` returns a real `A` instance.
3. Since it *is* an `A`, `__init__` runs — `"init"` prints. Order is always new → init.

### Medium — Singleton
**Problem:** Implement `Singleton` so every "instance" is the same object.
**Try this input:**
```python
a = Singleton()
b = Singleton()
print(a is b)
```
**Expected output:** `True`
**Solution:**
```python
class Singleton:
    _instance = None                     # class-level cache

    def __new__(cls):
        if cls._instance is None:        # first call only:
            cls._instance = super().__new__(cls)   # build one object
        return cls._instance             # every call returns THE object

a = Singleton()
b = Singleton()
print(a is b)                            # True
```
**Logic explained:**
1. `__new__` checks the class attribute `_instance`.
2. First call: nothing cached → allocate via `super().__new__` and store it on the class.
3. Every later call: skip creation entirely, return the cached object. `__init__` still runs each time (worth mentioning — it would re-initialize state, so real singletons often guard `__init__` too).

### Hard — Immutable subclass
**Problem:** Make `SortedTuple`, a subclass of `tuple` that stores its items sorted — no matter what order they're passed in. You cannot sort inside `__init__` because tuples are immutable by then.
**Try this input:**
```python
t = SortedTuple([3, 1, 2])
print(t)
print(t[0] + t[2])
```
**Expected output:**
```
(1, 2, 3)
4
```
**Solution:**
```python
class SortedTuple(tuple):
    def __new__(cls, items):
        # transform the data BEFORE the immutable object is born
        return super().__new__(cls, sorted(items))

t = SortedTuple([3, 1, 2])
print(t)              # (1, 2, 3)
print(t[0] + t[2])    # 4
```
**Logic explained:**
1. `tuple` is immutable — once `super().__new__` builds it, its contents are frozen. So sorting must happen at creation time.
2. `sorted(items)` produces `[1, 2, 3]` and we pass *that* into `tuple.__new__`.
3. `__init__` isn't needed at all — `tuple`'s default is fine.
4. Same technique works for `str` (e.g., force lowercase) and `int` (e.g., clamp to a range).

## The 30-second interview answer

"`__new__` creates and returns the instance; `__init__` initializes it after it exists. When I call `MyClass()`, Python runs `__new__` first, then calls `__init__` only if `__new__` returned an instance of that class. I reach for `__new__` in three cases: singletons (return a cached object), subclassing immutables like `str` or `tuple` (transform data before the frozen object exists), and factories that return a different class. Day to day, `object.__new__` is fine and I only write `__init__`."

## Follow-up trap

**"If `__new__` returns an object of a different class, does `__init__` still run?"** — No. `__init__` only runs when the returned object is an instance of the class being constructed. This is exactly how factory-style `__new__` methods work: `Pet("dog")` returns a fully-formed `Dog`, and `Pet.__init__` is skipped. Related gotcha they may probe: `__init__` must return `None` — returning a value raises `TypeError`.
