# 12 — Dunder Methods: `__repr__`, `__eq__`, `__len__`, `__getitem__`, `__enter__/__exit__`

> **Interview question:** "What are dunder methods? Explain `__repr__`, `__eq__`, `__len__`, `__getitem__`, and `__enter__`/`__exit__`."
> **What the interviewer is really testing:** Do you know how Python's built-in syntax (`print`, `==`, `len()`, `[]`, `with`) maps onto methods — i.e., can you make your own objects behave like built-ins?

## Theory — what it is

**Dunder** = "double underscore" — methods like `__len__` that Python calls *implicitly* when you use operators or built-ins. You almost never call `obj.__len__()` yourself; you call `len(obj)` and Python dispatches it.

The mapping for the ones asked about:

| You write...      | Python calls...            | Purpose                                        |
|-------------------|----------------------------|------------------------------------------------|
| `print(obj)`, `repr(obj)` | `obj.__repr__()`   | unambiguous string form — for *developers*     |
| `a == b`          | `a.__eq__(b)`              | equality by value instead of identity          |
| `len(obj)`        | `obj.__len__()`            | size of a container-like object                |
| `obj[i]`          | `obj.__getitem__(i)`       | indexing (and slicing, and even iteration!)    |
| `with obj:`       | `obj.__enter__()` / `obj.__exit__(...)` | setup/teardown around a block  |

The philosophy: **your objects should feel like Python objects**. If your class is a collection, `len()` and `for x in obj` should just work.

## Why it was needed

Without dunders, every class would be a second-class citizen. `==` would only compare memory addresses (`a is b`), so `Money(10) == Money(10)` would be `False`. `print(obj)` would show `<__main__.Money object at 0x7f...>`. There'd be no `with` statement, no indexing custom containers, no `len()`. Dunder methods are the *protocol* that lets user code plug into the language's syntax — that's the whole "Python data model."

## Where it's used in a real project

- **`__repr__`**: logging and debugging — `repr` is what appears in tracebacks, the REPL, and f-strings via `{obj!r}`.
- **`__eq__`**: comparing domain objects (`User(id=1) == User(id=1)`), and test assertions.
- **`__len__` / `__getitem__`**: wrappers around data — a `Deck` of cards, a `ResultSet`, a `Matrix`.
- **`__enter__`/`__exit__`**: `open()`, DB transactions, locks, timers — guaranteed cleanup.

## Diagram

```
          your syntax                    your class
   print(obj)  --------->  __repr__  ->  "Playlist('rock', 3 songs)"
   a == b      --------->  __eq__    ->  True / False / NotImplemented
   len(obj)    --------->  __len__   ->  int >= 0
   obj[i]      --------->  __getitem__ -> item at i
   with obj:   --------->  __enter__ ->  the resource
      ...body...
   (block ends)--------->  __exit__  ->  cleanup, suppress or propagate errors
```

## Code — explained

```python
class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = list(songs)

    def __repr__(self):                    # what devs see in logs/REPL
        return f"Playlist({self.name!r}, {self.songs!r})"

    def __len__(self):                     # enables len(pl)
        return len(self.songs)

    def __getitem__(self, i):              # enables pl[0], pl[1:3], iteration
        return self.songs[i]

    def __eq__(self, other):               # enables pl1 == pl2
        if not isinstance(other, Playlist):
            return NotImplemented          # let Python try the other side
        return self.name == other.name and self.songs == other.songs

pl = Playlist("rock", ["a", "b", "c"])
print(pl)            # Playlist('rock', ['a', 'b', 'c'])
print(len(pl))       # 3
print(pl[1])         # 'b'
print(pl[1:])        # ['b', 'c'] — slices work for free
for s in pl:         # iteration works via __getitem__ fallback!
    print(s)
```

Line-by-line:

1. `__repr__` should ideally look like constructor code (`Playlist(...)`) — rule of thumb: `repr` is for developers, `str` for end users.
2. `__len__` must return a non-negative int; `bool(pl)` also falls back to it (empty → `False`).
3. `__getitem__` receives the index — including a `slice` object for `pl[1:]` — and we just delegate to the inner list.
4. **Bonus behavior**: with `__getitem__` but no `__iter__`, Python iterates by trying `obj[0]`, `obj[1]`, ... until `IndexError`. Our `for` loop works without ever defining `__iter__`.
5. `__eq__` returning `NotImplemented` (not `False`!) tells Python "try the reflected operation" — the polite way to say "I can't compare to that type."

## Problems

### Easy — `__repr__`
**Problem:** Give `Book` a `__repr__` that shows title and author.
**Try this input:**
```python
b = Book("Dune", "Herbert")
print(repr(b))
```
**Expected output:** `Book('Dune', 'Herbert')`
**Solution:**
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r})"

b = Book("Dune", "Herbert")
print(repr(b))     # Book('Dune', 'Herbert')
```
**Logic explained:**
1. `{x!r}` inside an f-string calls `repr(x)` — quoting strings automatically.
2. Format like valid constructor code: readable, unambiguous, copy-pasteable into a REPL.

### Medium — `__len__` + `__getitem__` + `__eq__`
**Problem:** Implement `Basket` so `len(b)`, `b[i]`, iteration, and `b1 == b2` (same items, any order? — no: exact same list) all work.
**Try this input:**
```python
b1 = Basket(["apple", "pear"])
b2 = Basket(["apple", "pear"])
print(len(b1), b1[0], b1 == b2)
```
**Expected output:** `2 apple True`
**Solution:**
```python
class Basket:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, i):
        return self.items[i]

    def __eq__(self, other):
        if not isinstance(other, Basket):
            return NotImplemented
        return self.items == other.items

b1 = Basket(["apple", "pear"])
b2 = Basket(["apple", "pear"])
print(len(b1), b1[0], b1 == b2)   # 2 apple True
```
**Logic explained:**
1. `len(b1)` → `__len__` → `2`.
2. `b1[0]` → `__getitem__(0)` → `'apple'`.
3. `b1 == b2` → `__eq__` compares the wrapped lists element-wise → `True`.
4. `NotImplemented` for foreign types keeps `==` from lying about unknown comparisons.

### Hard — Context-manager dunders
**Problem:** Implement `Timer`, usable as `with Timer(): ...`, that prints `elapsed: Xs` when the block exits — even if the block raises.
**Try this input:**
```python
with Timer():
    sum(range(1_000_000))
```
**Expected output:** `elapsed: 0.0Xs` (some small float, e.g. `elapsed: 0.014s`)
**Solution:**
```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self                      # becomes the `as` variable if used

    def __exit__(self, exc_type, exc, tb):
        print(f"elapsed: {time.time() - self.start:.3f}s")
        return False                     # False = don't suppress exceptions

with Timer():
    sum(range(1_000_000))
```
**Logic explained:**
1. `with Timer()` constructs the object and calls `__enter__` — we record start time and return `self`.
2. The block runs.
3. On exit — normal OR via exception — `__exit__` runs with `(exc_type, exc, traceback)`; all `None` if no error.
4. Returning `False` (falsy) means "propagate any exception"; returning `True` would swallow it — a subtle, dangerous power.

## The 30-second interview answer

"Dunder methods are hooks that connect my classes to Python syntax: `len(obj)` calls `__len__`, `obj[i]` calls `__getitem__`, `a == b` calls `__eq__`, `repr` calls `__repr__`, and `with` uses `__enter__`/`__exit__`. `__repr__` is the developer-facing string, ideally looking like constructor code; `__eq__` gives value equality and should return `NotImplemented` for foreign types; `__getitem__` alone even enables iteration via the sequence protocol; and `__exit__` runs on block exit — even on exceptions — and can suppress them by returning truthy."

## Follow-up trap

**"You defined `__eq__` — can you put your objects in a `set` now?"** — Trick: **no**. Defining `__eq__` without `__hash__` sets `__hash__` to `None`, making instances unhashable (`TypeError`). If objects must be dict keys or set members, either define `__hash__` consistent with `__eq__` (equal objects → equal hashes), or add `__hash__ = None`... wait, no — set `@dataclass(eq=True, frozen=True)` or define `__hash__` explicitly. Another common probe: **`__repr__` vs `__str__`** — `__str__` is the pretty, user-facing version; if only `__repr__` exists, `print` falls back to it.
