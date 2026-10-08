# 07 — Shallow vs deep copy: when `list.copy()` still bites you

> **Interview question:** "I did `b = a.copy()` — why did mutating `b` still change `a`?"
> **What the interviewer is really testing:** Whether you know `copy()` duplicates only the *outer* container — the elements inside are still shared references. Nested mutables need `copy.deepcopy`.

## Theory — what it is

Python has **two levels of copying**, and the everyday tools only do the shallow one:

- **Shallow copy** — `a.copy()`, `a[:]`, `list(a)`, `dict(a)`, `copy.copy(a)` — builds a **new outer container**, then fills it with **references to the same inner objects**. One level deep, that's it.
- **Deep copy** — `copy.deepcopy(a)` — recursively walks the whole object graph and duplicates **every** object it finds. The result is fully independent.

So for `a = [[1, 2], [3, 4]]`, `b = a.copy()` gives `b` its own list object — but `b[0]` and `a[0]` are the *same* inner list. `b[0].append(99)` mutates shared state; `a` sees it too. But `b[0] = [9]` — *rebinding a slot* — is safe, because the outer lists really are separate.

When shallow copy is fine: **flat containers of immutables** — `[1, 2, 3].copy()`, `("a", "b")` — the elements can't be mutated, so sharing them is harmless. The trap only appears with **nested mutables**: lists in lists, dicts in dicts, objects in dicts.

Two subtleties worth knowing:

- `deepcopy` preserves **aliasing topology**: if `a = [x, x]` (same `x` twice), `deepcopy(a)` gives `[x', x']` — one *new* object referenced twice, not two copies. It uses a memo dict to track already-copied objects, which also makes it safe on cyclic structures.
- `copy.copy` on an **immutable container returns the original** — `copy.copy((1, 2))` is the same tuple; no need to copy what can't change. But a tuple *containing* a list is effectively mutable: `t = ([1], [2]); t[0].append(9)` mutates the shared list inside.

## Why it was needed

Copying is expensive — duplicating a whole nested structure on every `a.copy()` or `a[:]` would waste memory and time for the common case where you just want an independent *outer* container. Python gives you the **cheap default** (shallow) and makes you ask explicitly for the **expensive guarantee** (deep).

`deepcopy` exists because "fully clone this structure" is a real need — test fixtures, undo history, retrying with a mutated config. Its costs are real too: it can be 10–100× slower, and it **fails on uncopyable objects** — open files, sockets, locks, generators. Custom classes can hook it via `__copy__` / `__deepcopy__` dunders to control what gets duplicated.

## Where it's used in a real project

- **Copying config dicts before mutating:** `cfg = base_config.copy()` then `cfg["db"]["pool"] = 5` — *still mutates `base_config`!* The nested `"db"` dict is shared. Classic bug.
- **Test fixtures:** deepcopy a template payload per test so mutations don't leak between tests.
- **Undo / snapshots / retries:** snapshot state before a risky operation — must be deep or the "snapshot" mutates along with the original.
- **API boundaries:** defensive copies of parsed JSON before handing to code that mutates it.
- **The `[[]]*n` trap** (file 40) is the same disease — references copied, object shared — one level earlier, at construction time.

## Diagram

```
a = [[1, 2], [3, 4]]

SHALLOW:  b = a.copy()
          a ──> [ref, ref] ──┬──> [1, 2] <── shared!
          b ──> [ref, ref] ──┘   (b[0] is a[0] == True)

          b[0].append(9)  →  a becomes [[1,2,9],[3,4]]   OUCH
          b[1] = [0]      →  a unaffected                (rebind is safe)

DEEP:     c = copy.deepcopy(a)
          c ──> [ref, ref] ──┬──> NEW [1, 2]
                             └──> NEW [3, 4]           nothing shared
```

## Code — explained

```python
import copy

a = [[1, 2], [3, 4]]
b = a.copy()              # shallow: new OUTER list, same INNER lists

b[0].append(99)
print(a)                  # [[1, 2, 99], [3, 4]]   <- a changed!
print(a[0] is b[0])       # True — literally the same inner object

b[1] = [0]                # rebinding a slot touches only b's outer list
print(a)                  # [[1, 2, 99], [3, 4]]   <- inner [3,4] still intact
print(b)                  # [[1, 2, 99], [0]]

c = copy.deepcopy(a)      # fully independent clone
c[0].append(7)
print(a[0])               # [1, 2, 99] — unaffected
print(c[0] is a[0])       # False

flat = [1, 2, 3]          # shallow copy is ENOUGH for flat immutables
g = flat.copy()
g.append(4)
print(flat)               # [1, 2, 3] — ints can't be mutated, sharing is safe
```

1. `a.copy()` allocates a new list but copies the *references* — `b[0] is a[0]` is `True`. One inner list, two paths to it.
2. `b[0].append(99)` mutates the shared inner list → `a` shows `[[1, 2, 99], [3, 4]]`. This is the bite.
3. `b[1] = [0]` is **rebinding**, not mutation — it writes a new reference into `b`'s outer slot, which is genuinely separate. `a` is unaffected. Mutate = shared; rebind = safe.
4. `deepcopy` builds a parallel structure — `c[0] is a[0]` is `False`, so `c` mutates in isolation.
5. `flat.copy()` is a real, sufficient copy because ints are immutable — you can't `.append` to an int, so sharing the elements never shows.

## Problems

### Easy — predict the output
**Problem:** What prints, and why does `x` change?
```python
x = [[1], [2]]
y = x.copy()
y[0].append(5)
print(x, y)
```
**Try this input:** (the snippet above)
**Expected output:** `[[1, 5], [2]] [[1, 5], [2]]`
**Solution:**
```python
x = [[1], [2]]
y = x.copy()        # new outer list, same inner lists
y[0].append(5)      # mutates the SHARED inner list
print(x, y)         # [[1, 5], [2]] [[1, 5], [2]] — identical!
```
**Logic explained:**
1. `x.copy()` is shallow — `y` gets its own outer list but `y[0] is x[0]`.
2. `y[0].append(5)` mutates that shared `[1]` — both names see `[[1, 5], [2]]`.
3. Fix depends on depth: `y = [row[:] for row in x]` or `y = copy.deepcopy(x)`.

### Medium — clone the user records
**Problem:** `clone_users` must return an independent copy of a list of user dicts so callers can edit freely. The naive `.copy()` still leaks edits into the original. Fix it.
**Try this input:** `users = [{"name": "a"}, {"name": "b"}]`; clone it, set `clone[0]["name"] = "z"`, print both.
**Expected output:** original unchanged — `[{'name': 'a'}, {'name': 'b'}]` and `[{'name': 'z'}, {'name': 'b'}]`
**Solution:**
```python
import copy

def clone_users(users):
    return copy.deepcopy(users)          # or [dict(u) for u in users] for FLAT dicts

users = [{"name": "a"}, {"name": "b"}]
clone = clone_users(users)
clone[0]["name"] = "z"
print(users)    # [{'name': 'a'}, {'name': 'b'}] — protected
print(clone)    # [{'name': 'z'}, {'name': 'b'}]
```
**Logic explained:**
1. `users.copy()` only clones the list — the dicts inside are shared, so `clone[0]["name"] = "z"` would rewrite the original's dict too.
2. `[dict(u) for u in users]` copies each dict — works here because the dicts are flat (string values are immutable).
3. `deepcopy` is the safe general answer: if a dict held `"tags": ["x"]`, `dict(u)` would still share the `tags` list — the same trap one level deeper. When in doubt about depth, `deepcopy`.

### Hard — implement `deep_copy` yourself
**Problem:** Without importing `copy`, write `deep_copy(x)` that recursively clones nested lists and dicts (leaf values are immutable). Prove independence on a nested structure.
**Try this input:** `src = {"rows": [[1], [2]], "meta": {"v": 1}}` — deep-copy it, append `9` to `copy_["rows"][0]`, then print `src` and `copy_`.
**Expected output:** `{'rows': [[1], [2]], 'meta': {'v': 1}}` / `{'rows': [[1, 9], [2]], 'meta': {'v': 1}}`
**Solution:**
```python
def deep_copy(x):
    if isinstance(x, list):
        return [deep_copy(i) for i in x]
    if isinstance(x, dict):
        return {deep_copy(k): deep_copy(v) for k, v in x.items()}
    return x                    # leaf: int, str, etc. — safe to share

src = {"rows": [[1], [2]], "meta": {"v": 1}}
copy_ = deep_copy(src)
copy_["rows"][0].append(9)
print(src)     # {'rows': [[1], [2]], 'meta': {'v': 1}}
print(copy_)   # {'rows': [[1, 9], [2]], 'meta': {'v': 1}}
print(copy_["rows"] is src["rows"])   # False
```
**Logic explained:**
1. Recursion mirrors the structure: a list returns a new list of deep-copied items; a dict returns a new dict of deep-copied keys/values.
2. Anything else — ints, strings, `None` — is returned as-is; immutables are always safe to share.
3. Every container in the result is freshly allocated, so `copy_["rows"] is src["rows"]` is `False` and mutations can't cross over.
4. Real `deepcopy` adds two things this skips: a **memo** dict (so `a = [x, x]` stays `[x', x']` — shared stays shared — and cyclic structures don't recurse forever) and `__deepcopy__` hooks for custom classes.

## The 30-second interview answer

"`a.copy()` — and `a[:]`, `list(a)`, `copy.copy` — are all *shallow*: they allocate a new outer container but copy *references* to the elements, so nested mutables are still shared. With `a = [[1,2],[3,4]]`, `b = a.copy(); b[0].append(9)` mutates `a` too — `b[0] is a[0]`. Rebinding a slot is safe; mutating a shared element isn't. `copy.deepcopy` walks the whole graph recursively and duplicates everything — fully independent, but slower, and it fails on uncopyable objects like file handles. For flat containers of immutables, shallow copy is all you need — sharing ints and strings can't bite because they can't be mutated."

## Follow-up trap

**"Does `deepcopy` break shared references?"** — no, it *preserves* them: `x = [1]; a = [x, x]` deep-copies to `[x', x']` with `b[0] is b[1]` still `True` — a memo dict maps each original to its single clone. That's also what lets `deepcopy` survive cyclic structures (an object that contains itself) without infinite recursion. Second trap: *"`t = ([1], [2])` is a tuple — safe to share?"* — no! A tuple containing mutables is effectively mutable: `t[0].append(9)` mutates the list inside, and `copy.copy(t)` returns the *same* tuple (tuples are "immutable" so shallow copy skips them — hiding the shared list). Third: *"which is faster?"* — shallow by far; `deepcopy` can be 10–100× slower on big structures, which is why you reach for it deliberately, not by default.
