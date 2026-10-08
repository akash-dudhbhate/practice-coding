# 22 — `abc.ABC` vs duck typing

> **Interview question:** "What are abstract base classes in Python, and when would you use one instead of relying on duck typing?"
> **What the interviewer is really testing:** Do you understand that Python is duck-typed by default — and can you name the concrete cases where an ABC adds safety duck typing can't?

## Theory — what it is

**Duck typing** is Python's default philosophy: "if it walks like a duck and quacks like a duck, it is a duck." You don't declare that an object *is* a `Drawable` — you just call `obj.draw()` and it either works or raises `AttributeError` at runtime. No base class needed; any object with the right methods is acceptable.

An **abstract base class (ABC)** is a class you can't instantiate directly — it exists to define a *required interface* for subclasses. You make one with `abc.ABC` (or `metaclass=abc.ABCMeta`) and mark methods with `@abstractmethod`. A subclass that forgets to implement an abstract method **cannot be instantiated** — Python raises `TypeError` at object-creation time, not later when the missing method is called.

Two extra ABC superpowers: **virtual subclasses** via `register()` (declare that an unrelated class satisfies the interface without inheriting), and the built-in ABCs in `collections.abc` (`Iterable`, `Sized`, `Sequence`, `Mapping`…) that power `isinstance` checks like `isinstance(x, Iterable)`.

## Why it was needed

Pure duck typing fails *late*. If your plugin system requires `.render()` and a contributor's class defines `.render()` plus a needed `.teardown()` they forgot — you only find out when `teardown` is called, possibly deep in production. An ABC converts "runtime typo discovered in prod" into **"TypeError at import/instantiation time"** — failing fast is the entire point.

ABCs also *document intent*: `class Storage(ABC)` with abstract `save`/`load` tells implementers exactly what the contract is — no doc-digging. And they enable **structural `isinstance` checks**: `collections.abc.Iterable` lets you ask "can I loop over this?" without caring what concrete type it is.

Without ABCs, teams simulate interfaces with base classes raising `NotImplementedError` — which *does* work but only fails when the method is *called*, not when the object is created, and gives no `isinstance` semantics.

## Where it's used in a real project

- **Plugin/extension architectures**: `class Exporter(ABC)` with abstract `export()` — teammates write `CSVExporter`, `PDFExporter`; the framework instantiates them knowing the contract is satisfied.
- **`isinstance` checks on capabilities**: `isinstance(x, collections.abc.Sized)` before calling `len(x)`; `isinstance(f, collections.abc.Callable)`.
- **Frameworks you already use**: `collections.abc`, `numbers.Number`, `typing.Protocol`'s runtime-checkable variant, Django/DRF base classes, `abc`-based repository patterns.
- **Enforcing team contracts** in large codebases where duck-typing mistakes are expensive — a CI check that fails at instantiation beats a 2am pager.

## Diagram

```
DUCK TYPING                        ABC
─────────────                      ─────────────────────────
def save(thing):                   class Storage(ABC):
    thing.save(data)   # works        @abstractmethod
    # crashes LATER if               def save(self, d): ...
    # .save missing                  def load(self): ...

                                   class Disk(Storage):
                                       def save(self, d): ...
                                       # forgot load()!

                                   Disk()  → TypeError NOW:
                                   "Can't instantiate abstract
                                    class Disk with abstract
                                    method load"
fail time: whenever the            fail time: at instantiation —
missing method is called           before bad object exists
```

## Code — explained

```python
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> bool:
        """Deliver message; return True on success."""

    def notify_all(self, users):          # concrete method: shared logic OK
        return [self.send(u) for u in users]

# Notifier()                          # TypeError: abstract class

class EmailNotifier(Notifier):
    def send(self, message):
        print(f"email: {message}")
        return True

class BrokenNotifier(Notifier):           # forgot send()
    pass

print(EmailNotifier().send("hi"))         # email: hi / True
try:
    BrokenNotifier()
except TypeError as e:
    print("TypeError:", e)

# isinstance works — and so does duck typing alongside it
print(isinstance(EmailNotifier(), Notifier))   # True
```

1. `class Notifier(ABC)` marks this as abstract — `Notifier()` itself raises `TypeError: Can't instantiate abstract class Notifier with abstract method send`.
2. `@abstractmethod` on `send` declares: "every concrete subclass MUST define this." Subclasses can add docstrings/type hints freely.
3. ABCs can mix abstract and **concrete** methods — `notify_all` gives all subclasses shared behavior for free (the Template Method pattern).
4. `EmailNotifier` implements `send` → instantiates fine. `BrokenNotifier` doesn't → `TypeError` *at the `()` call*, printing something like `Can't instantiate abstract class BrokenNotifier with abstract method send`.
5. `isinstance(EmailNotifier(), Notifier)` is `True` — ABCs give you normal `isinstance` semantics, which pure duck typing can't (a duck-typed object has no declared type to check against).

## Problems

### Easy — define and subclass an ABC
**Problem:** Create an ABC `Shape` with abstract method `area()`. Implement `Square(side)`. Show that instantiating `Shape` itself fails.
**Try this input:**
```python
print(Square(4).area())
try:
    Shape()
except TypeError as e:
    print("failed")
```
**Expected output:**
```
16
failed
```
**Solution:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

print(Square(4).area())
try:
    Shape()
except TypeError:
    print("failed")
```
**Logic explained:**
1. `Shape(ABC)` + `@abstractmethod` makes `area` a required contract.
2. `Square` fulfills it → `Square(4).area()` returns `16`.
3. `Shape()` raises `TypeError` — you can't instantiate an interface, only implementations. The `try/except` catches it and prints `failed`.

### Medium — catch a missing method at instantiation
**Problem:** Define ABC `Parser` with abstract `parse(text)` and `filetype()`. Write `CsvParser` implementing both, and `JsonParser` that "forgets" `filetype`. Show which instantiation fails and with what error type.
**Try this input:**
```python
print(CsvParser().parse("a,b"))
try:
    JsonParser()
except TypeError as e:
    print(type(e).__name__)
```
**Expected output:**
```
['a', 'b']
TypeError
```
**Solution:**
```python
from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def parse(self, text):
        pass

    @abstractmethod
    def filetype(self):
        pass

class CsvParser(Parser):
    def parse(self, text):
        return text.split(",")
    def filetype(self):
        return "csv"

class JsonParser(Parser):
    def parse(self, text):
        import json
        return json.loads(text)
    # filetype() forgotten!

print(CsvParser().parse("a,b"))
try:
    JsonParser()
except TypeError as e:
    print(type(e).__name__)
```
**Logic explained:**
1. `CsvParser` implements both abstract methods → instantiates; `parse("a,b")` → `['a', 'b']`.
2. `JsonParser` misses `filetype` → `JsonParser()` raises `TypeError` immediately — *before* any parsing runs. That's the ABC guarantee.
3. With duck typing, this bug would surface only when `filetype()` was eventually called — possibly much later, far from the real mistake.

### Hard — ABC + register() for virtual subclassing
**Problem:** Without touching `list`, make `isinstance([], Serializable)` return `True` using `ABC.register`. Then write a `dump(obj)` function that accepts anything `isinstance`-of `Serializable` and calls `.serialize()` — and show a non-serializable object is rejected with a clean error.
**Try this input:**
```python
print(dump(123))
try:
    dump(object())
except TypeError:
    print("rejected")
```
**Expected output:**
```
<int:123>
rejected
```
**Solution:**
```python
from abc import ABC, abstractmethod

class Serializable(ABC):
    @abstractmethod
    def serialize(self):
        pass

class IntBox(Serializable):
    def __init__(self, n):
        self.n = n
    def serialize(self):
        return f"<int:{self.n}>"

def dump(obj):
    if not isinstance(obj, Serializable):
        raise TypeError("not serializable")
    return obj.serialize()

print(dump(IntBox(123)))
try:
    dump(object())
except TypeError:
    print("rejected")

# register() — make an existing class a 'virtual' subclass:
Serializable.register(str)
print(isinstance("hi", Serializable))   # True
```
**Logic explained:**
1. `IntBox` is a normal ABC subclass implementing `serialize` → `dump(IntBox(123))` returns `<int:123>`.
2. `dump` guards with `isinstance` — `object()` isn't a `Serializable` → clean `TypeError` instead of an `AttributeError` deep inside `obj.serialize()`.
3. `Serializable.register(str)` declares `str` a **virtual subclass** — `isinstance("hi", Serializable)` becomes `True` *without* `str` inheriting anything or defining `serialize`. Note: `isinstance` says yes, but calling `.serialize()` on `str` would still fail — register is a promise, not enforcement. That's the key subtlety of virtual subclassing.

## The 30-second interview answer

"Duck typing is Python's default: call the method, and if it exists it works — no declarations needed. An ABC makes the contract explicit: `abc.ABC` plus `@abstractmethod` means a subclass that forgets a required method raises `TypeError` at instantiation time, failing fast instead of blowing up in production. I use ABCs for plugin interfaces, framework extension points, and anywhere a missing method would be a costly late failure — plus `collections.abc` gives `isinstance` checks like `isinstance(x, Iterable)`. ABCs can also carry shared concrete methods. The trade-off: ABCs add a base-class dependency, so for simple internal code duck typing is still the Pythonic default — I reach for ABCs at boundaries where the contract matters."

## Follow-up trap

**"What about `typing.Protocol` — isn't that the modern answer?"** Yes, and knowing it separates seniors from juniors. `Protocol` gives *static* duck typing: mypy checks that your object has the right methods *without inheriting* anything — no runtime base class at all. Rules of thumb: **duck typing** for trivial internal code, **Protocol** when you want type-checker-enforced contracts without coupling, **ABC** when you need runtime `isinstance`, shared concrete methods, or instantiation-time enforcement. Second trap: *"does `register()` enforce the interface?"* — No! `register` is an unchecked promise; `isinstance` will lie if the registered class doesn't actually implement the methods. And: *"can an ABC have a constructor/state?"* — yes, `__init__` works normally, subclasses just call `super().__init__()`.
