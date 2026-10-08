# 25 — MRO; what `super()` actually resolves to in multiple inheritance

> **Interview question:** "What is the MRO in Python, and what does `super()` actually call in multiple inheritance?"
> **What the interviewer is really testing:** The common misconception that `super()` means "my parent" — it doesn't. It means "next in the MRO chain," which may be a *sibling* class.

## Theory — what it is

**MRO (Method Resolution Order)** is the linear order Python searches when you call a method on a class with multiple parents. For `class D(B, C)`, when you call `d.method()`, Python doesn't just check `D` then its parents — it computes a single ordered list (`D.__mro__`) and walks it in order, using the first match.

Python uses the **C3 linearization** algorithm — the same one Dylan uses. The rules in plain English: (1) a class comes before its parents, (2) parents keep the order listed (`class D(B, C)` → B before C), (3) a class appears *once*, after all classes that need it. For the "diamond" `D(B,C)` where `B(A)` and `C(A)`, the MRO is `D → B → C → A → object` — `A` comes *last*, after everything that inherits it.

**`super()` is not "the parent class."** `super()` inside `D.m` means "the next class *after D* in the MRO of the *actual object's* class." If you call `super()` inside `B.m` but the object is a `D`, it looks at `D`'s MRO and finds what's after `B` — which is `C`, not `A`. This is **cooperative multiple inheritance**: `super()` lets every class in the chain contribute, then pass the baton to the next, ending at `object`.

## Why it was needed

Single inheritance is trivial — walk up the parent chain until you hit a match. Multiple inheritance creates the **diamond problem**: `D(B,C)`, `B(A)`, `C(A)` — if both `B` and `C` override `A.save()`, which does `D` use? And if `D.save()` calls `super().save()`, does `B.save` then `C.save` then `A.save` all run, or does `A.save` run twice (once via B, once via C)?

Without C3 + `super()`, you get either ambiguity or double-calls. C3 gives a single, predictable order where every class runs **exactly once**; `super()` is the mechanism that walks it. The classic payoff: a `LoggingMixin` can `super().__init__(*a, **kw)` and *cooperate* — each class in the chain adds its behavior then hands off, so `D()` initializes B's part, C's part, and A's part exactly once, in order.

## Where it's used in a real project

- **Mixins**: `class MyView(LoginRequiredMixin, DetailView)` — each mixin adds one behavior (auth check, serialization) then `super()` hands off to the next. This is the dominant real-world use of cooperative MI (Django, DRF).
- **Framework hierarchies**: Django's `Model` and form classes use MI + `super()` so framework code and your code both initialize.
- **Debugging**: `print(D.__mro__)` or `D.mro()` is the tool when "which method is actually being called?" — especially when a mixin silently overrides something.
- **`super()` in `__init__`** chains: every class calls `super().__init__(*args, **kwargs)` so the whole chain initializes — the cooperative-inheritance contract.

## Diagram

```
Diamond:                       MRO for D:
        A                      D → B → C → A → object
       / \
      B   C                    d.method() search order:
       \ /                     1.D  2.B  3.C  4.A  5.object
        D

super() is NOT "parent" —
inside B.save() with a D instance:
  B's "next" in D.__mro__ is C (a sibling!), not A
  so super().save() in B calls C.save, which calls A.save
  → A runs ONCE, after B and C — the cooperative chain
```

## Code — explained

```python
class A:
    def who(self):
        return "A"

class B(A):
    def who(self):
        return "B"

class C(A):
    def who(self):
        return "C"

class D(B, C):
    pass

print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
print(D().who())          # B — first match in MRO

# super() walks the MRO, not "the parent"
class A2:
    def go(self):
        print("A", end=" ")

class B2(A2):
    def go(self):
        print("B", end=" ")
        super().go()       # in D2's MRO, after B2 comes C2!

class C2(A2):
    def go(self):
        print("C", end=" ")
        super().go()

class D2(B2, C2):
    def go(self):
        print("D", end=" ")
        super().go()

D2().go()                 # D B C A — each ran ONCE, in MRO order
```

1. `D(B, C)` means "check B before C" — `D.__mro__` prints `D, B, C, A, object`. `D().who()` returns `"B"` — B is first in the chain after D.
2. The `super()` example is the payoff: `D2().go()` prints `D B C A`. Inside `B2.go`, `super()` does *not* call `A2` (B2's only parent) — it calls `C2`, because in `D2.__mro__` (which is `D2, B2, C2, A2, object`), the class after `B2` is `C2`.
3. `super()` is resolved against **the type of `self`** (`type(self).__mro__`), not the class the code is written in. `self` is a `D2`, so every `super()` walks `D2`'s MRO.
4. Each class ran exactly once — C3 guarantees no double-visits even in diamonds. That's why `A` appears once at the end, not once per path.
5. `super().go()` inside `C2` reaches `A2` — the last user-defined class — and `A2.go` has no `super()` call, ending the chain cleanly before `object`.

## Problems

### Easy — read the MRO
**Problem:** Given `class X`, `class Y(X)`, `class Z(X)`, `class W(Y, Z)` — predict `W.__mro__` order and what `W().m()` returns when `Y` and `Z` both define `m` returning their letter.
**Try this input:**
```python
print([c.__name__ for c in W.__mro__])
print(W().m())
```
**Expected output:**
```
['W', 'Y', 'Z', 'X', 'object']
Y
```
**Solution:**
```python
class X:
    pass

class Y(X):
    def m(self):
        return "Y"

class Z(X):
    def m(self):
        return "Z"

class W(Y, Z):
    pass

print([c.__name__ for c in W.__mro__])
print(W().m())
```
**Logic explained:**
1. MRO: `W` first, then its parents in declared order — `Y` before `Z` (because `W(Y, Z)` lists Y first).
2. `X` comes *after* both `Y` and `Z` — C3 places a shared parent after all classes that inherit it.
3. `W().m()` → `"Y"`: `W` has no `m`, next in MRO is `Y`, which has `m` — first match wins; `Z`'s `m` is never reached.

### Medium — cooperative `__init__`
**Problem:** Build `Base` plus mixins `Log` and `Auth`, and `class View(Log, Auth, Base)`. Each `__init__` prints its name then calls `super().__init__()`. Show all run exactly once in MRO order.
**Try this input:**
```python
View()
```
**Expected output:**
```
Log
Auth
Base
```
**Solution:**
```python
class Base:
    def __init__(self):
        print("Base")

class Log:
    def __init__(self):
        print("Log")
        super().__init__()     # hands to NEXT in View's MRO: Auth

class Auth:
    def __init__(self):
        print("Auth")
        super().__init__()     # hands to Base

class View(Log, Auth, Base):
    pass                       # inherits the whole chain

View()
```
**Logic explained:**
1. `View.__mro__` = `View, Log, Auth, Base, object`. `View()` calls `Log.__init__` (first match after View).
2. `Log` prints "Log", then `super().__init__()` — resolved against `type(self)` = `View` → next after `Log` is `Auth`.
3. `Auth` prints "Auth", `super()` → `Base`; `Base` prints "Base" and stops (no super call — the chain ends before `object`).
4. Each initializer ran once, in order — cooperative MI working. If `Log` had called `Base.__init__(self)` directly instead of `super()`, `Auth` would be skipped and `Base` could run twice.

### Hard — the forgotten super()
**Problem:** `MixinA` and `MixinB` both wrap `process()` to add logging, and `Worker(MixinA, MixinB)` uses them — but `MixinA.process` calls `MixinB` *directly* instead of `super()`. Show what breaks (MixinA runs, chain stops early / double-calls), then fix with `super()`.
**Try this input:**
```python
print(BadWorker().process("job"))
print(Worker().process("job"))
```
**Expected output:**
```
[A] MixinA before job
[B] MixinB before job
core job
[A] MixinA before job
[B] MixinB before job
core job
```
Wait — a cleaner demonstration: have `BadMixinA.process` call `MixinB.process(self, x)` directly (hardcoding the "parent"), so it works for `Worker` but breaks if `Worker` adds a mixin between them, or calls it twice. Simplest correct demo: `MixinA` calls `super()`, `MixinB` forgets `super()` → `Core.process` never runs.
**Solution:**
```python
class Core:
    def process(self, x):
        return f"core {x}"

class MixinA(Core):
    def process(self, x):
        print(f"[A] MixinA before {x}")
        return super().process(x)

class MixinB(Core):
    def process(self, x):
        print(f"[B] MixinB before {x}")
        return super().process(x)

class BadMixinB(Core):
    def process(self, x):
        print(f"[B] MixinB before {x}")
        return f"core {x}"      # forgot super() — chain CUT

class BadWorker(MixinA, BadMixinB):
    pass

class Worker(MixinA, MixinB):
    pass

print(BadWorker().process("job"))   # MixinB runs but Core's part skipped
print(Worker().process("job"))      # full chain: A → B → core
```
**Logic explained:**
1. `BadWorker.__mro__` = `BadWorker, MixinA, BadMixinB, Core, object`. `process` → `MixinA` (prints A) → `super()` → `BadMixinB` (prints B) — but `BadMixinB` returns a hardcoded string *without* calling `super()`, so `Core.process` is never reached.
2. `Worker` (both mixins call `super()`): `MixinA` → `super()` → `MixinB` → `super()` → `Core` → returns "core job" up the chain.
3. The rule: **every class in a cooperative chain must call `super()`** — even ones that think they're "last" — because `super()` means "next in *the object's* MRO," which depends on the concrete class being instantiated, not the class you're writing. `MixinB` might be last today and middle tomorrow.
4. Real-world corollary: always `super().__init__(*args, **kwargs)` and pass through `*args, **kwargs` so later classes' params reach them.

## The 30-second interview answer

"MRO is the linear order Python searches for methods in multiple inheritance, computed by the C3 algorithm — a class before its parents, parents in declared order, each class once. The key insight: `super()` doesn't mean 'my parent' — it means 'the next class in the MRO of the *actual object*.' So inside `B.method`, with a `D(B, C)` instance, `super()` calls `C` — a sibling — because in `D`'s MRO, `C` follows `B`. This enables cooperative multiple inheritance: every class calls `super()` to hand off to the next, so in a diamond each class runs exactly once, ending at `object`. I use `Class.__mro__` to debug 'which method runs' questions, and in mixins I always call `super().__init__(*args, **kwargs)` so the chain isn't broken."

## Follow-up trap

**"Why does `super()` inside `B` call `C`, not `A` — isn't `B`'s parent `A`?"** This is the whole question. `super()` takes zero args in py3 but is secretly `super(ThisClass, self)` — and it uses **`self`'s class's MRO**, starting after `ThisClass`. With `self` being a `D` (MRO `D, B, C, A`), `super()` inside `B`'s method looks at position-after-B in `D`'s MRO → `C`. It is *not* "B's parent." Second trap: *"what breaks the cooperative chain?"* — a class that doesn't call `super()` (cuts the chain), or that hardcodes `Parent.method(self)` instead of `super()` (skips siblings, can double-call in diamonds). Third: *"inconsistent MRO"* — `class C(A, B)` where `A(B)` is impossible order → `TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B` — C3 can't satisfy both "A before B" and "B before its parent A."
