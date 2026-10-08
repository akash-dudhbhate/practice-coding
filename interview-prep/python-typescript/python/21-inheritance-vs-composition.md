# 21 — Inheritance vs composition — when does inheritance become the wrong choice?

> **Interview question:** "When should you use inheritance vs composition?"
> **What the interviewer is really testing:** Whether you know the "is-a vs has-a" heuristic — and more importantly, the *failure modes* of inheritance (fragile base class, deep hierarchies) that made "favor composition over inheritance" a famous rule.

## Theory — what it is

**Inheritance** (`class Dog(Animal)`) makes a child class automatically get all of a parent's methods and attributes. It models an **"is-a"** relationship: a `Dog` *is an* `Animal`. The child can override parent methods and call them via `super()`.

**Composition** means a class *contains* other objects and delegates work to them. It models a **"has-a"** relationship: a `Car` *has an* `Engine`. Instead of inheriting `Engine`'s methods, `Car` holds `self.engine = Engine()` and calls `self.engine.start()` when needed.

The famous design guideline is **"favor composition over inheritance"** (from *Design Patterns*, 1994). It doesn't mean "never inherit" — it means inheritance is a strong coupling tool that's easy to misuse, so reach for it only when the relationship truly is "is-a" and the parent is designed to be extended.

**Liskov Substitution Principle (LSP)** is the test: if `B` inherits `A`, then anywhere code expects an `A`, a `B` must work correctly. If a `Square` inherits `Rectangle` but breaks when you `set_width` independently of height, LSP is violated — inheritance was the wrong choice.

## Why it was needed

Inheritance was sold as "code reuse," but it creates the **strongest coupling** in OOP: the child is welded to the parent's implementation, not just its interface. Three concrete breakages:

1. **Fragile base class problem**: change the parent's internals and every child can silently break — even if the parent's public API is unchanged. The child may have relied on which parent method calls which other method.
2. **Deep hierarchies**: `A → B → C → D` means to understand `D` you must hold all of `A..C` in your head. Debugging "where does this method actually live" becomes archaeology (see MRO problems, file 25).
3. **Wrong taxonomy**: real domains resist clean trees. `class Penguin(Bird)` — but `Bird.fly()`? Now you're overriding `fly` to raise `NotImplementedError`, which is LSP violation and a code smell screaming "wrong hierarchy."

Composition avoids all three: you depend only on the contained object's *public interface*, you can swap it at runtime (`car.engine = ElectricEngine()`), and testing is easy (inject a fake engine). You trade a bit of boilerplate (delegation methods) for flexibility — usually a good trade.

## Where it's used in a real project

- **Inheritance is right**: framework extension points designed for it — `class MyView(APIView)`, `class MyTest(unittest.TestCase)`, `class MyError(Exception)`, `class MyHandler(BaseHTTPRequestHandler)`. The parent is *built* to be subclassed.
- **Inheritance is right**: true "is-a" with shared interface — `class Circle(Shape)` where every `Shape` must have `.area()`.
- **Composition is right**: plugging in behavior — a `ReportGenerator` *has a* `Formatter` (CSV or PDF injected); a `Repository` *has a* `Database`; a `Service` *has a* `Logger`/`HttpClient`.
- **Composition is right**: swapping strategies at runtime or in tests — pass `FakeStorage` in tests, `S3Storage` in prod.

## Diagram

```
INHERITANCE (is-a)                COMPOSITION (has-a)
┌─────────┐                       ┌──────────────┐
│ Animal  │                       │    Car       │
│ speak() │                       │ ┌──────────┐ │
└────┬────┘                       │ │ Engine   │ │
     │ "is-a"                     │ │ start()  │ │
┌────┴────┐                       │ └──────────┘ │
│  Dog    │  gets speak() free    │ start() {    │
│ bark()  │                       │   engine.start() }  delegates
└─────────┘                       └──────────────┘
coupled to Animal's guts          coupled only to Engine's interface
can't change parent at runtime    swap engine anytime:
                                  car.engine = FakeEngine() in tests
```

## Code — explained

```python
# --- INHERITANCE done wrong: Stack "is-a" list? ---
class BadStack(list):
    def push(self, item):
        self.append(item)

s = BadStack()
s.push(1)
s.insert(0, 99)          # inherited method bypasses stack discipline!
print(s)                 # [99, 1] — stack invariant broken

# --- COMPOSITION fixes it: Stack HAS a list ---
class Stack:
    def __init__(self):
        self._items = []          # hidden internal list

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)

st = Stack()
st.push(1); st.push(2)
print(st.pop(), len(st))          # 2 1 — no way to break the invariant

# --- Composition for swappable behavior ---
class ConsoleLogger:
    def log(self, msg): print(f"LOG: {msg}")

class Service:
    def __init__(self, logger):   # inject dependency
        self.logger = logger
    def run(self):
        self.logger.log("running")

Service(ConsoleLogger()).run()    # LOG: running
```

1. `BadStack(list)` inherits *every* `list` method — including `insert`, which lets callers break the "last-in-first-out" rule. Inheritance exposed 30+ methods we never wanted.
2. `Stack` *has* a list but exposes only `push`/`pop`/`len` — the invariant can't be broken from outside. This is "composition over inheritance" literally.
3. `Service` takes a `logger` via the constructor (**dependency injection**). In tests you'd pass a `FakeLogger` that records calls instead of printing — no monkey-patching needed.
4. Notice the delegation cost: `Stack` had to define `__len__` manually. That's the price of composition — worth it when the alternative is exposing a broken interface.

## Problems

### Easy — is-a or has-a?
**Problem:** For each pair, say whether inheritance or composition fits: (a) `Dog`/`Animal`, (b) `Car`/`Engine`, (c) `Manager`/`Employee`, (d) `Team`/`Player`.
**Try this input:** N/A — reasoning question. Then implement (d) with composition: `Team` has players and a method `total_skill()`.
**Expected output:**
```
15
```
**Solution:**
```python
# (a) is-a → inheritance  (b) has-a → composition
# (c) is-a → inheritance  (d) has-a → composition

class Player:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []                 # HAS players — composition

    def add(self, player):
        self.players.append(player)

    def total_skill(self):
        return sum(p.skill for p in self.players)

t = Team("Tigers")
t.add(Player("amy", 7))
t.add(Player("bo", 8))
print(t.total_skill())
```
**Logic explained:**
1. `Dog`/`Animal` and `Manager`/`Employee` are true "is-a" — a Manager *is* an Employee with extras; inheritance is safe because LSP holds.
2. `Car`/`Engine` and `Team`/`Player` are "has-a" — a car isn't an engine, a team isn't a player. Composing keeps interfaces honest.
3. `Team` delegates: `total_skill` iterates its contained `Player` objects rather than inheriting anything.

### Medium — refactor inheritance to composition
**Problem:** A dev wrote `class JsonReport(dict)` that inherits `dict` to "reuse" storage. It breaks because `dict` methods like `.update()` bypass the report's validation. Refactor to composition: keep a private dict, expose `set_field(key, value)` (rejects non-string keys) and `to_json()`.
**Try this input:**
```python
r = JsonReport()
r.set_field("title", "Q1")
r.set_field("views", 100)
print(r.to_json())
```
**Expected output:** `{"title": "Q1", "views": 100}`
**Solution:**
```python
import json

class JsonReport:
    def __init__(self):
        self._data = {}                    # HAS a dict — not IS a dict

    def set_field(self, key, value):
        if not isinstance(key, str):
            raise TypeError("keys must be strings")
        self._data[key] = value

    def to_json(self):
        return json.dumps(self._data)

r = JsonReport()
r.set_field("title", "Q1")
r.set_field("views", 100)
print(r.to_json())
```
**Logic explained:**
1. Inheriting `dict` would leak `.update()`, `.pop()`, `__setitem__` — all skipping the string-key check. Inheritance gave *too much*.
2. Composition holds `self._data` privately; only the two curated methods touch it. Validation can't be bypassed.
3. `json.dumps` produces `{"title": "Q1", "views": 100}` — insertion order preserved (dicts ordered since 3.7).

### Hard — strategy pattern via composition
**Problem:** Build a `Checkout` that *has a* `PaymentStrategy`. Implement `CardPayment` and `PaypalPayment` strategies, each with `pay(amount)` returning a receipt string. Show swapping the strategy at runtime — impossible to do cleanly if `Checkout` inherited from one payment class.
**Try this input:**
```python
c = Checkout(CardPayment("4111"))
print(c.complete(50))
c.strategy = PaypalPayment("a@b.com")
print(c.complete(30))
```
**Expected output:**
```
Paid 50 via card 4111
Paid 30 via paypal a@b.com
```
**Solution:**
```python
class CardPayment:
    def __init__(self, number):
        self.number = number
    def pay(self, amount):
        return f"Paid {amount} via card {self.number}"

class PaypalPayment:
    def __init__(self, email):
        self.email = email
    def pay(self, amount):
        return f"Paid {amount} via paypal {self.email}"

class Checkout:
    def __init__(self, strategy):
        self.strategy = strategy          # HAS a payment strategy
    def complete(self, amount):
        return self.strategy.pay(amount)  # delegates

c = Checkout(CardPayment("4111"))
print(c.complete(50))
c.strategy = PaypalPayment("a@b.com")     # swapped at runtime!
print(c.complete(30))
```
**Logic explained:**
1. `Checkout` doesn't inherit `CardPayment` — it *contains* any object with a `.pay(amount)` method (duck typing, no base class needed).
2. Swapping `c.strategy` mid-flight changes behavior — with inheritance, `Checkout` would be frozen as one payment type forever.
3. This is the **Strategy pattern**: composition + a common informal interface. It's how real code handles "same job, many ways" — formatters, storage backends, auth providers.
4. Bonus testability: in tests inject a `FakePayment` that always succeeds — no network, no card numbers.

## The 30-second interview answer

"Inheritance models 'is-a', composition models 'has-a' — but the deeper point is coupling. Inheritance binds the child to the parent's *implementation*, which creates the fragile-base-class problem: parent changes can silently break children, and deep hierarchies hide where behavior actually lives. I use inheritance only for true 'is-a' where the parent is designed for extension — framework base classes, exceptions, test cases. For 'has-a' or interchangeable behavior — services with loggers, checkouts with payment strategies — I compose and inject dependencies, which also makes testing trivial. The Liskov test is my sanity check: if a child can't be substituted wherever the parent is expected, inheritance was wrong — like `Square` inheriting `Rectangle` or `Penguin` inheriting a flying `Bird`."

## Follow-up trap

**"So is inheritance bad? Should we never use it?"** No — the trap is overcorrecting. Inheritance is right when the parent is *designed* to be extended (abstract base classes, template-method hooks) and the relationship is genuinely substitutable. Good examples: `Exception` subclasses, `unittest.TestCase`, Django `Model`, ABCs. Also know the middle options Python gives: **mixins** (small inheritance for one focused capability, e.g., `JsonMixin`), and `functools` delegation like `collections.UserDict` when you *do* want dict-like behavior safely. If asked "how do you get code reuse without inheritance" — composition + delegation, or plain functions; most "reuse" needs were really "share a helper," which a module-level function solves with zero coupling.
