# 23 — `@dataclass`, `frozen=True`, vs plain class vs NamedTuple

> **Interview question:** "What is a dataclass? How does `@dataclass(frozen=True)` compare to a plain class or a NamedTuple?"
> **What the interviewer is really testing:** Do you know the boilerplate a dataclass eliminates, and can you pick the right tool for "a bag of fields"?

## Theory — what it is

A **dataclass** (Python 3.7+) is a regular class decorated with `@dataclass` where you declare fields as *annotated class attributes*. The decorator auto-generates `__init__`, `__repr__`, and `__eq__` for you — the three methods that make up ~90% of "data holder" boilerplate.

```python
@dataclass
class Point:
    x: float
    y: float
# is roughly: def __init__(self, x, y): self.x=x; self.y=y
#           + __repr__ → "Point(x=1, y=2)"
#           + __eq__   → compares all fields
```

**`frozen=True`** makes instances *immutable*: after construction, assigning to a field raises `FrozenInstanceError`. This also makes the object hashable (usable as dict keys / set members) if fields are hashable.

A **`NamedTuple`** (`from typing import NamedTuple`) is a *tuple* subclass with named fields — immutable by nature, comparable, iterable, indexable (`p[0]` works). A **plain class** gives you full control but you write `__init__`/`__repr__`/`__eq__` yourself.

The decision rule: **dataclass** for mutable or customized data objects; **`frozen=True`** when you want value-object semantics (hashable, safe to share); **NamedTuple** when you need tuple behavior (unpacking, indexing, interop with tuple-expecting APIs); **plain class** when the object has real behavior/invariants beyond holding fields.

## Why it was needed

Before dataclasses, writing a simple "record" meant ~15 lines of repetitive `__init__` plus remembering `__repr__` (for readable logs) and `__eq__` (for tests comparing objects). People either wrote the boilerplate, used `namedtuple` (which forces immutability + tuple indexing you may not want), or pulled in `attrs` (the library dataclasses were modeled on).

The subtle killer: **mutable default fields**. `def __init__(self, items=[])` is the classic bug — dataclasses solve it with `field(default_factory=list)`, which calls `list` fresh for each instance. Dataclasses also play well with type checkers (annotations are real), slots (`slots=True` for memory savings), and ordering (`order=True` generates `<`, `<=` etc.).

## Where it's used in a real project

- **Config/settings objects**: `@dataclass(frozen=True) class DbConfig: host: str; port: int` — immutable, hashable, printable.
- **API/domain models**: `User`, `Order`, `InvoiceLine` — auto `__eq__` makes test assertions `assert result == Order(...)` trivial.
- **DTOs between layers**: request/response objects, parsed-CSV rows, message payloads.
- **Value objects as dict keys**: `frozen=True` `Coordinate` can be a dict key for caching/geo-lookups — a plain class can't (unhashable unless you write `__hash__`).

## Diagram

```
                mutable?   fields?   __init__/   hashable?   unpackable
                             typed    repr/eq      by default   like tuple
                                   auto?
plain class     yes        manual    manual      no           no
@dataclass      yes        yes       YES         no           no
@dataclass      no         yes       YES         YES          no
 (frozen=True)
NamedTuple      no         yes       YES         YES          YES
                                  (it's a tuple)
```

## Code — explained

```python
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int
    tags: list = field(default_factory=list)   # NOT [] — see below

u = User("amy", 30)
print(u)                          # User(name='amy', age=30, tags=[])
print(u == User("amy", 30))       # True — auto __eq__
u.tags.append("admin")            # mutable: fine

@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(1, 2)
# p.x = 9    # FrozenInstanceError — immutable!
print(hash(p) is not None)        # True — hashable, dict-key-able

from typing import NamedTuple
class Color(NamedTuple):
    r: int
    g: int
    b: int

c = Color(255, 0, 0)
print(c.r, c[0])                  # 255 255 — named AND indexed
r, g, b = c                       # tuple unpacking works
print(r, g, b)                    # 255 0 0
```

1. `@dataclass` on `User` auto-writes `__init__(name, age, tags=[])`, `__repr__`, `__eq__` — all from the three annotated lines.
2. `field(default_factory=list)` is critical: `tags: list = []` would be a `ValueError` at class-creation time (dataclasses *forbid* mutable defaults via `=`); `default_factory` calls `list()` fresh per instance.
3. `u == User("amy", 30)` → `True` because generated `__eq__` compares all fields — a plain class would need `u is u` identity or a hand-written `__eq__`.
4. `frozen=True` on `Point`: `p.x = 9` raises `FrozenInstanceError`. Immutability → auto `__hash__` → `hash(p)` works, so `Point` can be a dict key/set member.
5. `Color(NamedTuple)` gives named access `c.r` **plus** tuple powers: indexing `c[0]` and unpacking `r, g, b = c`. A dataclass can't be unpacked like that (it's not a tuple).
6. Plain class equivalent of `User` would need ~15 lines: `def __init__`, `def __repr__`, `def __eq__` — all manual, all bug-prone.

## Problems

### Easy — basic dataclass
**Problem:** Create a `Book` dataclass with `title: str`, `author: str`, `pages: int = 0`. Print one and check equality with an identical instance.
**Try this input:**
```python
b1 = Book("Dune", "Herbert", 412)
print(b1)
print(b1 == Book("Dune", "Herbert", 412))
```
**Expected output:**
```
Book(title='Dune', author='Herbert', pages=412)
True
```
**Solution:**
```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int = 0

b1 = Book("Dune", "Herbert", 412)
print(b1)
print(b1 == Book("Dune", "Herbert", 412))
```
**Logic explained:**
1. `@dataclass` generates `__init__` accepting positional args in field order.
2. `pages` has a default `0` — fields with defaults must come *after* fields without.
3. `print` uses generated `__repr__`; `==` uses generated `__eq__` comparing all fields → `True`.

### Medium — mutable default + frozen
**Problem:** Model a frozen `Point(x, y)` used as dict keys, and a mutable `Path` dataclass holding a list of points — using `default_factory` for the list. Add `Path.add(point)`.
**Try this input:**
```python
p = Path()
p.add(Point(0, 0))
p.add(Point(3, 4))
print(p.points)
d = {Point(0, 0): "origin"}
print(d[Point(0, 0)])
```
**Expected output:**
```
[Point(x=0, y=0), Point(x=3, y=4)]
origin
```
**Solution:**
```python
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Point:
    x: float
    y: float

@dataclass
class Path:
    points: list = field(default_factory=list)

    def add(self, point):
        self.points.append(point)

p = Path()
p.add(Point(0, 0))
p.add(Point(3, 4))
print(p.points)
d = {Point(0, 0): "origin"}
print(d[Point(0, 0)])
```
**Logic explained:**
1. `Point` is `frozen=True` → immutable + hashable → usable as dict key. `d[Point(0,0)]` finds `"origin"` because equal `Point`s hash equally.
2. `Path.points` uses `default_factory=list` — each `Path()` gets a *fresh* list (avoiding the shared-mutable-default bug).
3. `Path` is a normal mutable dataclass — `add` mutates `self.points` fine. If `Path` were frozen, `add` would raise.

### Hard — ordering + post-init validation
**Problem:** Create a frozen `Version` dataclass (`major`, `minor`, `patch`) that supports `<`/`==` ordering (`order=True`) and validates in `__post_init__` that all fields are non-negative ints — raising `ValueError` otherwise. Sort a list of versions.
**Try this input:**
```python
vs = [Version(1, 10, 0), Version(1, 2, 3), Version(2, 0, 0)]
print([str(v) for v in sorted(vs)])
try:
    Version(1, -1, 0)
except ValueError:
    print("rejected")
```
**Expected output:**
```
['1.2.3', '1.10.0', '2.0.0']
rejected
```
**Solution:**
```python
from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int
    patch: int

    def __post_init__(self):
        for f in (self.major, self.minor, self.patch):
            if not isinstance(f, int) or f < 0:
                raise ValueError("bad version")

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"

vs = [Version(1, 10, 0), Version(1, 2, 3), Version(2, 0, 0)]
print([str(v) for v in sorted(vs)])
try:
    Version(1, -1, 0)
except ValueError:
    print("rejected")
```
**Logic explained:**
1. `order=True` generates `<`, `<=`, `>`, `>=` comparing fields as a tuple `(major, minor, patch)` — so `1.2.3 < 1.10.0` correctly (2 < 10 in `minor`).
2. `frozen=True` makes versions hashable and safe to share as dict keys.
3. `__post_init__` runs right after the generated `__init__` — the hook for validation when the object is fully constructed. `Version(1,-1,0)` raises `ValueError` before the object escapes.
4. `sorted` uses generated `<`; `str()` uses our `__str__` → clean `1.2.3` output. Without `order=True`, `sorted` would raise `TypeError: '<' not supported`.

## The 30-second interview answer

"A dataclass auto-generates `__init__`, `__repr__`, and `__eq__` from annotated fields — eliminating the boilerplate of data-holder classes. `frozen=True` makes instances immutable and hashable, giving value-object semantics so they work as dict keys. Versus NamedTuple: a NamedTuple is a real tuple — indexable, unpackable, always immutable — while a dataclass is a normal class that's easier to mutate, add methods to, and customize. Versus a plain class: the dataclass is the plain class minus ~15 lines of boilerplate, plus safety features like `field(default_factory=list)` that kill the mutable-default-argument bug. I default to dataclasses for data objects, reach for `frozen=True` when sharing them, and NamedTuple only when I specifically need tuple behavior or interop."

## Follow-up trap

**"What can't a dataclass do / what are the gotchas?"** Know three: (1) **mutable defaults are rejected** — `items: list = []` is a `ValueError` at class creation; you *must* use `field(default_factory=list)`. (2) **frozen + mutable field = trap**: `frozen=True` only blocks *rebinding* — a frozen dataclass holding a `list` still lets you `obj.items.append(x)`! True immutability needs immutable fields (tuple, not list). (3) **`eq=True` + mutable fields = unhashable**: by default dataclasses set `__hash__ = None` when `eq=True`, so a plain `@dataclass` can't be a dict key — you need `frozen=True` (or `eq=False`, dangerous). Bonus trap: *"dataclass vs pydantic?"* — pydantic validates/coerces at runtime (e.g. `"123"` → `123`); dataclasses only *annotate* — `User("amy", "thirty")` happily stores a string in `age: int`. For untrusted input, pydantic; for internal typed data, dataclass.
