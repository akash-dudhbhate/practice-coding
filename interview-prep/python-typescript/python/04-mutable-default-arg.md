# 04 — The mutable default argument bug

> **Interview question:** "What's wrong with `def f(x, items=[])`? Why does it happen and how do you fix it?"
> **What the interviewer is really testing:** Whether you know default values are evaluated ONCE at function-definition time and shared across all calls.

## Theory — what it is

`def` is an **executable statement**. When Python runs the line `def f(x, items=[]):`, it evaluates the default expressions **once**, right then, and stores the resulting objects inside the function object — you can see them at `f.__defaults__`. The list `[]` is created one time, at definition time.

Every call that omits `items` gets **that same list object** — not a fresh `[]`. So if the function body mutates it (`items.append(x)`), the mutation accumulates across calls. Call 1 leaves `[1]` in the shared list; call 2 starts from `[1]` and appends → `[1, 2]`. The "default" has memory.

The fix is a **sentinel**: default to `None` (immutable, unique, meaningful) and create the fresh list inside the body:

```python
def f(x, items=None):
    if items is None:
        items = []        # new list created on EVERY call
    items.append(x)
    return items
```

## Why it was needed

Why does Python evaluate defaults once, at `def` time? Two reasons. **Performance:** if defaults were re-evaluated per call, every call would pay the cost of building them — and expressions like `def log(msg, level=logging.INFO)` would re-lookup `logging.INFO` constantly. **Semantics:** defaults being part of the function *object* makes them introspectable (`f.__defaults__`, `inspect.signature`) and lets them act as captured state — decorators and closures rely on this.

Without the once-only rule, though, nothing breaks — the design is a deliberate tradeoff, and the "bug" is really a **leaky abstraction**: it looks like the default is per-call, but it's per-definition. Languages that re-evaluate per call (e.g., JavaScript's `= []` in params) hide this entirely; Python exposes it, so you must know it.

## Where it's used in a real project

- **The classic bug:** `def add_tag(tag, tags=[])` in request handlers — user A's tags leak into user B's response. A real class of security-adjacent bugs in web apps.
- **Legitimate use — memoization:** `def fib(n, _memo={})` exploits the shared dict as a free cache that persists across calls.
- **Legitimate use — loop-variable capture:** `funcs = [lambda x, i=i: x + i for i in range(3)]` — the `i=i` default snapshots `i` at definition time, fixing the late-binding closure bug.
- **`None` sentinel pattern everywhere:** `def connect(host, opts=None)` — the single most common signature convention in library code.

## Diagram

```
def f(x, items=[]):          runs ONCE at def time
                  │
                  ▼
   function object f ──► __defaults__ = ( [] ,)   ← ONE shared list
                                            ▲
   f(1) ──► items.append(1) ──► list = [1] ─┤ same object!
   f(2) ──► items.append(2) ──► list = [1,2]┘

fix:  __defaults__ = ( None ,)   ← immutable sentinel
   f(1) ──► items = []  (fresh) ──► [1]
   f(2) ──► items = []  (fresh) ──► [2]
```

## Code — explained

```python
def buggy(item, items=[]):
    items.append(item)
    return items

print(buggy(1))              # [1]        — looks fine
print(buggy(2))              # [1, 2]     — surprise: remembers call 1!
print(buggy.__defaults__)    # ([1, 2],)  — the shared list, living in the function

def fixed(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(fixed(1))              # [1]
print(fixed(2))              # [2]        — fresh list each call
print(fixed(3, ["x"]))       # ['x', 3]   — caller-supplied list still works
```

1. `buggy(1)` appends `1` to the default list stored in `__defaults__` → `[1]`.
2. `buggy(2)` receives the **same** list object — now `[1]`, appends → `[1, 2]`.
3. `buggy.__defaults__` proves it: the default *is* a real, mutated object stored on the function.
4. `fixed` uses `None` (immutable — can never accumulate state) and builds a brand-new `[]` inside the body on each call.
5. Bonus: `fixed(3, ["x"])` shows the fix preserves the intended behavior when a caller *does* pass a list.

## Problems

### Easy — predict the accumulation
**Problem:** Predict the output of three calls to this buggy function — and say *why* the second call doesn't return just `['b']`.
```python
def add(item, items=[]):
    items.append(item)
    return items

print(add("a"))
print(add("b"))
print(add("c"))
```
**Try this input:** (the snippet above)
**Expected output:**
```
['a']
['a', 'b']
['a', 'b', 'c']
```
**Solution:**
```python
def add(item, items=[]):
    items.append(item)
    return items

print(add("a"))   # ['a']
print(add("b"))   # ['a', 'b']
print(add("c"))   # ['a', 'b', 'c']
```
**Logic explained:**
1. `[]` is created once when `def` executes; it's stored in `add.__defaults__`.
2. Every call without `items` reuses that same object, and `append` mutates it in place — so results accumulate.
3. `add("b")` doesn't return `['b']` because the default list already holds `'a'` from call 1.

### Medium — fix the registry
**Problem:** Fix `register` so each call gets a fresh group when none is given, while a caller-provided list is still appended to. Verify both paths.
**Try this input:** `register("ann")`, `register("bob")`, then `team = []; register("cat", team); register("dan", team); print(team)`
**Expected output:**
```
['ann']
['bob']
['cat', 'dan']
```
**Solution:**
```python
def register(name, group=None):
    if group is None:
        group = []          # fresh list per call
    group.append(name)
    return group

print(register("ann"))    # ['ann']
print(register("bob"))    # ['bob']  — no leakage from previous call
team = []
register("cat", team)
register("dan", team)
print(team)               # ['cat', 'dan']  — caller's list used correctly
```
**Logic explained:**
1. `None` is immutable, so it can't accumulate state — it's the standard "no argument given" sentinel.
2. The `if group is None: group = []` line creates a *new* list object on every defaulted call.
3. When the caller passes `team`, we append to their list — intentional shared mutation, which is correct because the caller owns it.

### Hard — exploit the bug on purpose (memoization)
**Problem:** Instead of fixing the shared default, *use* it: write memoized `fib(n, _memo={})` so repeated calls reuse cached results. Compute `fib(10)` and `fib(30)`.
**Try this input:** `fib(10)`, `fib(30)`
**Expected output:**
```
55
832040
```
**Solution:**
```python
def fib(n, _memo={}):
    if n in _memo:
        return _memo[n]
    if n < 2:
        return n
    _memo[n] = fib(n - 1) + fib(n - 2)
    return _memo[n]

print(fib(10))   # 55
print(fib(30))   # 832040 — instant, because the shared _memo persists
```
**Logic explained:**
1. `_memo={}` is the same dict across every call — normally a bug, here a free persistent cache.
2. `if n in _memo` short-circuits recursion: each `n` is computed once, turning exponential `O(2^n)` into linear `O(n)`.
3. `fib(30)` returns `832040` instantly even though naive recursion would need ~2.7 million calls.
4. The `_` prefix signals "private — callers shouldn't pass this." (In production you'd use `functools.lru_cache`, but this demonstrates you *understand* the mechanism rather than fearing it.)

## The 30-second interview answer

"The default `items=[]` is evaluated once when the `def` statement executes — the list object is stored in `f.__defaults__` and every call that omits the argument shares that same list. So appends accumulate across calls, which looks like the function 'remembering' state. The fix is `items=None` plus `if items is None: items = []` inside the body, creating a fresh list per call. It's not a random quirk — it's a consequence of `def` being an executable statement — and the same mechanism is exploited legitimately for memoization and for capturing loop variables with `i=i`."

## Follow-up trap

**"Is `def f(x=expensive())` also evaluated once?"** Yes — *all* defaults are, including function calls: `def log(ts=datetime.now())` stamps every log with the **import-time** timestamp, not the call time — a real production bug. Second trap: *"so immutable defaults are always fine?"* — `def f(n=0)` is safe not because it's re-evaluated but because ints can't be mutated in place. Third, the subtle one: *"what about `def f(items=[])` where the function only reads, never mutates?"* — technically safe but still fragile: any future edit that mutates, or any caller inspecting `f.__defaults__`, reawakens the bug. Use `None` anyway — it's free.
