# 05 — LEGB name resolution order

> **Interview question:** "When Python sees a variable name, how does it decide which value it means?"
> **What the interviewer is really testing:** Whether you know the LEGB search order — Local, Enclosing, Global, Built-in — and the `UnboundLocalError` trap it creates.

## Theory — what it is

When code uses a name like `x`, Python searches up to **four scopes** in a fixed order, and the **first match wins**:

- **L — Local:** names defined inside the *current function* (parameters + anything assigned in the body).
- **E — Enclosing:** names in any *outer functions* wrapping this one — only exists for nested functions; this is where closures get their captured variables.
- **G — Global:** names defined at *module level* (top of the `.py` file) — really "module scope," not program-wide.
- **B — Built-in:** Python's own names — `len`, `print`, `sum`, `Exception` — the last resort.

If none of the four has the name → `NameError`.

The crucial gotcha: **assignment decides scope for the whole function**. If a function body contains `x = ...` *anywhere* — even after a line that reads `x` — Python classifies `x` as local for the *entire* function at compile time. So this fails:

```python
x = 10
def f():
    print(x)    # UnboundLocalError! x is "local" here...
    x = 20      # ...because this assignment makes it local everywhere in f
```

`print(x)` looks for local `x` before the assignment ran → `UnboundLocalError` (not `NameError` — the name *exists* in the local table, just unbound). To write a global from inside a function you must declare `global x`; to write an enclosing variable, `nonlocal x`. Reading needs no declaration — only writing does.

## Why it was needed

Without a fixed order, every name lookup would be ambiguous — does `len` mean your local variable or the built-in? LEGB makes shadowing **predictable**: the nearest enclosing scope wins, which matches intuition ("local variables trump globals") and lets you reuse common names (`id`, `list`, `type`) locally without breaking the built-ins everywhere else.

The "assignment marks it local" rule exists for the same reason: it prevents a stray assignment deep in a function from silently overwriting a module-global — a huge source of action-at-a-distance bugs. Python forces you to *say* `global` when you mean global.

## Where it's used in a real project

- **Closures & decorators:** a decorator's `wrapper` reads variables from the enclosing `decorator` scope — E of LEGB is what makes `functools.wraps`-style decorators work.
- **`nonlocal` counters/state:** factory functions like `make_counter()` keep private state in the enclosing scope — the OOP-free way to encapsulate.
- **`global` for module config:** `global DEBUG` in a `configure()` function; also module-level caches/connection pools mutated via `global`.
- **The accidental-shadowing bug:** `list = [1,2]` at module top → every later `list(...)` call in the module breaks. Linters flag "redefines built-in" for exactly this.

## Diagram

```
        ┌─────────────────────────── Built-in ───────────────────────────┐
        │   len, print, range, Exception ...            (searched LAST)   │
        │  ┌──────────────────────── Global ──────────────────────────┐  │
        │  │  x = "G",   module-level functions, imports               │  │
        │  │  ┌──────────────── Enclosing ──────────────────────────┐ │  │
        │  │  │  def outer():   x = "E"   (captured by closures)    │ │  │
        │  │  │  ┌────────────── Local ───────────────────────────┐ │ │  │
        │  │  │  │  def inner():  x = "L"   (searched FIRST)      │ │ │  │
        │  │  │  └────────────────────────────────────────────────┘ │ │  │
        │  │  └────────────────────────────────────────────────────┘ │  │
        │  └────────────────────────────────────────────────────────┘  │
        └──────────────────────────────────────────────────────────────┘

   lookup walks outward:  L → E → G → B,  first hit wins
   assignment in a body  →  name is LOCAL for that whole body
```

## Code — explained

```python
x = "global"                       # G

def outer():
    x = "enclosing"                # E
    def inner():
        x = "local"                # L
        return x
    return inner()

print(outer())                     # local   — inner's own x wins
print(x)                           # global  — module x untouched

# shadowing a builtin — legal but dangerous:
len = 5
def demo():
    return len                     # finds GLOBAL len=5 ... before builtin!
print(demo())                      # 5
```

1. `inner()` returns its **local** `x` (`"local"`) — L wins over E and G.
2. `print(x)` at module level finds the **global** — the nested assignments never touched it; each `x` lived in its own scope.
3. `len = 5` shadows the **built-in** `len` at global scope — inside `demo()`, LEGB finds the global `5` before reaching B. This is why shadowing builtins is dangerous: it works silently until something calls the real `len()`.
4. Note the asymmetry: `outer()`'s `x` and `inner()`'s `x` are three *different* objects sharing a name — resolution picks by proximity, never by "the real one."

## Problems

### Easy — which x wins?
**Problem:** Predict the output — which `x` does each `print` see, and which LEGB scope supplied it?
```python
x = "G"
def outer():
    x = "E"
    def inner():
        x = "L"
        return x
    return inner()
print(outer(), x)
```
**Try this input:** (the snippet above)
**Expected output:** `L G`
**Solution:**
```python
x = "G"
def outer():
    x = "E"
    def inner():
        x = "L"
        return x
    return inner()
print(outer(), x)   # L G
```
**Logic explained:**
1. `inner()` returns its **local** `x` = `"L"` — first scope searched, first hit wins.
2. The enclosing `x = "E"` is *skipped* because L already matched — that's the point of ordered resolution.
3. `print(..., x)` at module level sees **global** `"G"` — neither function's assignment leaked outward.

### Medium — fix the UnboundLocalError
**Problem:** This fails — write the working version so `bump()` increments a module-level counter, and call it three times.
```python
count = 0
def bump():
    count += 1        # UnboundLocalError: 'count' is local but never bound
    return count
```
**Try this input:** `bump(); bump(); bump()`
**Expected output:** `1 2 3`
**Solution:**
```python
count = 0
def bump():
    global count      # declare: writes go to module scope
    count += 1
    return count

print(bump(), bump(), bump())   # 1 2 3
```
**Logic explained:**
1. `count += 1` is really `count = count + 1` — an *assignment*, so Python marked `count` local for the whole function; reading it before the assignment raised `UnboundLocalError`.
2. `global count` tells the compiler "don't make this local — resolve it in module scope," so the read finds the global `0` and the write updates it.
3. Without `global`, *reading* a global is fine — it's only *writing* that triggers local classification. That's the asymmetry that surprises people.

### Hard — nonlocal counter factory
**Problem:** Write `make_counter()` returning a `step` function that remembers how many times *it* was called — each counter independent. Use `nonlocal`, not `global`.
**Try this input:** `a = make_counter(); b = make_counter()` then `a(); a(); b(); a()`
**Expected output:** `1 2 1 3`
**Solution:**
```python
def make_counter():
    n = 0                    # enclosing scope variable
    def step():
        nonlocal n           # write to outer's n, not a new local
        n += 1
        return n
    return step

a = make_counter()
b = make_counter()
print(a(), a(), b(), a())   # 1 2 1 3
```
**Logic explained:**
1. Each call to `make_counter` creates a *fresh* `n` in its own enclosing scope — `a` and `b` capture different `n`s, hence independent counts.
2. `nonlocal n` tells `step` "assign to the enclosing function's `n`" — without it, `n += 1` would create a local `n` and fail with `UnboundLocalError` (same trap as Medium).
3. `b()` prints `1` because `b`'s `n` was untouched by `a`'s calls; the final `a()` prints `3` continuing `a`'s own count.
4. This is a **closure** — `step` carries a reference to `make_counter`'s scope even after `make_counter` returned. LEGB's E is literally what a closure captures.

## The 30-second interview answer

"Python resolves names by searching four scopes in order: Local — inside the current function; Enclosing — outer functions for nested defs; Global — the module; Built-in — things like `len` and `print`. First match wins, then it raises `NameError`. The important subtlety: if a function assigns a name anywhere, that name is local for the *whole* function — so reading it before the assignment gives `UnboundLocalError`, even if a global exists. You opt out with `global` for module scope or `nonlocal` for enclosing scope — `nonlocal` is what powers closures like counter factories and decorators."

## Follow-up trap

**"Why `UnboundLocalError` and not `NameError`?"** — because the name *is* in the function's local symbol table (the compiler put it there due to the later assignment); it's just not bound to a value yet. `NameError` means "not found anywhere"; `UnboundLocalError` means "found locally, but empty." Second trap: *"does `if False: x = 5` make `x` local?"* — yes! Scope is decided at **compile time** from the *presence* of an assignment, not whether it runs — `print(x)` above it still raises `UnboundLocalError`. Third: *"what about `for i in ...` or `except E as e`?"* — loop targets are normal locals; and `e` is auto-deleted after the `except` block, which surprises people in list comprehensions over exception handlers.
