# 24 — Singleton in Python — and why it's usually a bad idea

> **Interview question:** "How do you implement a singleton in Python — and why is it usually a bad idea?"
> **What the interviewer is really testing:** Whether you can implement it (they want to see `__new__` or a decorator) AND whether you know *why modern Python avoids it* — global state, testability, hidden coupling.

## Theory — what it is

A **singleton** is a class designed so only **one instance** ever exists — every call to `Class()` returns the same object. The classic uses: a shared cache, a config object, a connection pool — "exactly one of these should exist app-wide."

The three common Python implementations:

1. **`__new__` override** — `__new__` is the method that actually *creates* the object (`__init__` only initializes it). Cache the instance on the class and return it.
2. **Module-level instance** — just create `config = Config()` at module top and `import` it everywhere. Python modules are themselves singletons (imported once, cached in `sys.modules`).
3. **Decorator/metaclass** — wrap `__call__` to cache instances.

The Pythonic answer is usually #2 — it's explicit, simple, and doesn't fight the language.

## Why it was needed — and why it backfires

Singletons solve "I need shared state accessible from everywhere." The failure modes:

1. **Hidden global state** — a singleton is a global variable wearing an OOP costume. Any code anywhere can mutate it; debugging "who changed this?" is painful.
2. **Untestable** — tests can't swap in a fake; a test that mutates the singleton leaks state into the next test (test pollution, ordering-dependent failures).
3. **Hidden coupling** — `Foo()` deep in a function secretly depends on global config; the function's signature lies about its dependencies.
4. **Concurrency bugs** — naive `__new__` singletons aren't thread-safe (two threads can both create instances); you need locks.

The modern fix is **dependency injection**: create one `Config` in `main()`, pass it to whoever needs it. Same single instance — but explicit, testable, no global magic. "Singleton as a pattern" → "one instance as a policy."

## Where it's used in a real project

- **Legitimate-ish**: read-only config loaded once (`settings = Settings()` in a module), connection pools, registries.
- **What you'd actually see**: module-level constants/objects (`db = create_engine(...)`, `logger = logging.getLogger(__name__)`), FastAPI's `lru_cache`-cached settings.
- **What replaces it**: dependency injection (pass `config` explicitly), Flask's `g`/`app` context, `functools.lru_cache` on a factory.

## Diagram

```
WITHOUT singleton               WITH singleton
┌─────┐ ┌─────┐                 ┌─────┐ ┌─────┐
│ a() │ │ b() │                 │ a() │ │ b() │
└──┬──┘ └──┬──┘                 └──┬──┘ └──┬──┘
   │Cfg()  │Cfg()  → 2 objects     │Cfg()  │Cfg()
   ▼       ▼                        └──┬──┘
┌──────┐ ┌──────┐                      ▼
│cfg#1 │ │cfg#2│  different!     ┌──────────┐
└──────┘ └──────┘                 │ cfg #1   │  SAME object both times
                                   └──────────┘
DI fix: main() makes cfg once, passes it to a(cfg), b(cfg)
— no global, tests can pass a fake cfg.
```

## Code — explained

```python
# --- 1. __new__ singleton ---
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)                 # True — same object
a.x = 42
print(b.x)                    # 42 — shared state

# --- 2. Pythonic way: module-level instance ---
# settings.py:
#   class Config: ...
#   config = Config()          # THE one instance; import it

# --- 3. functools.lru_cache factory (modern DI-ish) ---
from functools import lru_cache

class Config:
    def __init__(self):
        self.debug = False

@lru_cache(maxsize=1)
def get_config():
    return Config()

c1 = get_config()
c2 = get_config()
print(c1 is c2)               # True — cached single instance
```

1. `__new__` runs before `__init__` and returns the object — caching `cls._instance` means every `Singleton()` call returns that same object. `a is b` → `True`, and `a.x = 42` is visible as `b.x`.
2. **Subtle bug in naive `__new__`**: `__init__` still runs *every call* — `Singleton()` re-runs `__init__` on the cached instance, re-setting fields. Real implementations guard with `if not hasattr(self, '_initialized')`.
3. **Thread-safety gap**: two threads could both see `_instance is None` and create two objects — production code needs `threading.Lock`. (The GIL doesn't save you — the check-then-create isn't atomic.)
4. Module-level `config = Config()` is the simplest true singleton: Python caches modules in `sys.modules`, so every `from settings import config` gets the same object. No `__new__` tricks.
5. `lru_cache(maxsize=1)` on `get_config()` is the modern pattern: one cached instance, but callers ask a *function* — easy to swap in tests (`get_config.cache_clear()` or inject a fake).

## Problems

### Easy — verify identity
**Problem:** Implement a `__new__`-based `Cache` singleton. Show two "instances" are the same object and that setting a key on one is visible on the other.
**Try this input:**
```python
c1 = Cache()
c2 = Cache()
print(c1 is c2)
c1.data["k"] = 1
print(c2.data["k"])
```
**Expected output:**
```
True
1
```
**Solution:**
```python
class Cache:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = {}
        return cls._instance

c1 = Cache()
c2 = Cache()
print(c1 is c2)
c1.data["k"] = 1
print(c2.data["k"])
```
**Logic explained:**
1. First `Cache()` call: `_instance` is `None` → create object, attach `data = {}`, cache it.
2. Second call: `_instance` exists → return it. `c1 is c2` → `True`.
3. `c1.data["k"] = 1` mutates the shared dict → `c2.data["k"]` is `1`. The `data` init is inside the `if` so it only runs once — avoiding the re-init bug.

### Medium — the test-pollution problem
**Problem:** Show why a singleton makes tests order-dependent: a `FeatureFlags` singleton where test A enables a flag and test B sees the leftover state. Then show the DI fix — pass flags in.
**Try this input:**
```python
def test_a():
    flags.enable("dark_mode")
    print(flags.is_on("dark_mode"))

def test_b():
    print(flags.is_on("dark_mode"))   # sees test A's change!

test_a()
test_b()
```
**Expected output:**
```
True
True
```
**Solution:**
```python
class FeatureFlags:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.flags = set()
        return cls._instance

    def enable(self, name):
        self.flags.add(name)

    def is_on(self, name):
        return name in self.flags

flags = FeatureFlags()

def test_a():
    flags.enable("dark_mode")
    print(flags.is_on("dark_mode"))

def test_b():
    print(flags.is_on("dark_mode"))   # polluted by test_a!

test_a()
test_b()

# DI fix: drop the singleton — plain class, inject a fresh one per test
class PlainFlags:
    def __init__(self):
        self.flags = set()
    def enable(self, name):
        self.flags.add(name)
    def is_on(self, name):
        return name in self.flags

def test_b_fixed(flags):
    print(flags.is_on("dark_mode"))

test_b_fixed(PlainFlags())   # False — fresh instance, deterministic
```
**Logic explained:**
1. `test_a` mutates the singleton's `flags` set; `test_b` sees `"dark_mode"` still on — order-dependent, a classic singleton test smell.
2. With DI, `test_b_fixed(PlainFlags())` gets a brand-new object — the output is `False` no matter what ran before. Each test owns its state.
3. Interview takeaway: singletons trade convenience for hidden shared state — tests are where that debt comes due. Dropping `__new__` and injecting dependencies removes the whole class of bug.

### Hard — thread-safe singleton with double-checked locking
**Problem:** Implement a `__new__` singleton that is safe under threads — two threads calling `Db()` concurrently must get the same object, and construction must happen exactly once.
**Try this input:**
```python
import threading
results = []
def make():
    results.append(Db())
ts = [threading.Thread(target=make) for _ in range(10)]
[t.start() for t in ts]
[t.join() for t in ts]
print(all(r is results[0] for r in results))
```
**Expected output:** `True`
**Solution:**
```python
import threading

class Db:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:            # fast path: no lock needed
            with cls._lock:                  # only lock when creating
                if cls._instance is None:    # re-check inside the lock
                    cls._instance = super().__new__(cls)
        return cls._instance

import threading as _t
results = []
def make():
    results.append(Db())
ts = [_t.Thread(target=make) for _ in range(10)]
[t.start() for t in ts]
[t.join() for t in ts]
print(all(r is results[0] for r in results))
```
**Logic explained:**
1. **Double-checked locking**: the outer `if` lets threads skip locking once the instance exists (fast path); the inner `if` inside `with cls._lock` catches the race — a second thread that waited on the lock sees `_instance` already set and doesn't re-create.
2. Without the lock, two threads could both pass `if cls._instance is None` before either finishes `super().__new__` — creating two objects and breaking the singleton.
3. The GIL does *not* make check-then-create atomic — bytecode can switch threads between the check and the assignment. The lock is required. (This is a great detail to mention in interviews.)

## The 30-second interview answer

"A singleton guarantees one instance per process. The classic implementation overrides `__new__` to cache and return the same object; the Pythonic version is just a module-level instance — modules are already singletons via `sys.modules` caching. But it's usually a bad idea: a singleton is a global variable in OOP clothing — hidden shared state that's hard to test (test pollution), hard to reason about (who mutated it?), and not thread-safe without locks. The modern answer is dependency injection — create one instance in `main` and pass it to callers — or `functools.lru_cache` on a factory for cached-once construction with an easy test seam. I'd only reach for a real singleton for read-only config or a connection pool, and even then I'd prefer passing it explicitly."

## Follow-up trap

**"Ok, so implement a *thread-safe* singleton — and does `__init__` still run every call?"** Two traps in one. Thread-safety: show double-checked locking (as in the Hard problem) — the naive `if cls._instance is None` races under threads, and the GIL doesn't make check-then-create atomic. `__init__` trap: yes, `Singleton()` calls `__init__` on the cached instance *every time* — fields get re-initialized. Fix: guard with `if getattr(self, '_initialized', False): return` then set `self._initialized = True`. Final trap: *"what about `__new__` vs metaclass vs decorator?"* — metaclass `__call__` override is the cleanest "enforced" singleton (intercepts the call itself); decorator wraps the class; `__new__` is the classic. For interviews, `__new__` + acknowledgment of the module-level pattern is the expected answer.
