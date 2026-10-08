# 03 — Mutable vs immutable built-in types

> **Interview question:** "Which built-in types are mutable and which are immutable — and why does it matter for function arguments?"
> **What the interviewer is really testing:** Whether you understand that Python passes *object references* into functions — so a mutable argument can be changed under the caller's feet.

## Theory — what it is

**Mutable** = you can change the object's contents *in place* without creating a new object: `list`, `dict`, `set`, `bytearray`. `lst.append(x)` modifies the same object; `id(lst)` stays the same. **Immutable** = the object's value can never change after creation: `int`, `float`, `str`, `tuple`, `frozenset`, `bool`, `bytes`, `None`. "Changing" an immutable — `x = x + 1` — builds a *new* object and rebinds the name; `id(x)` changes.

Now the function-argument part. Python's argument passing is best described as **"pass by object reference"** (a.k.a. pass-by-assignment): the parameter name inside the function binds to the *same object* the caller passed — no copy is made. Two consequences:

1. **Mutating** the object through the parameter (`items.append(...)`, `d[k] = v`) is visible to the caller — same object, both names see it.
2. **Rebinding** the parameter name (`items = items + [x]`, `n = n + 1`) only moves the *local* name to a new object — the caller's name still points at the original.

So "can a function change my variable?" depends on whether the *object* is mutable — not on any Python passing mode.

A third consequence: **hashability**. Dict keys and set members must be immutable (roughly) — because lookup relies on the hash staying constant. `d[[1,2]] = x` raises `TypeError: unhashable type: 'list'`. If a list could be a key and then mutated, its hash would change and the entry would be lost inside the table.

## Why it was needed

Immutability is a **safety and correctness** feature, not a limitation. If dict keys could change after insertion, lookups would silently fail. If strings were mutable, sharing one string object across a program (which interning relies on) would be dangerous. Immutability makes objects safe to share without copying — `name = "akash"` can be passed anywhere with zero defensive copies.

Mutability exists for **performance**: `list.append` is amortized O(1) because it mutates in place; if lists were immutable, every append would copy the whole list (O(n)) — that's what happens with `tuple + tuple`. The split gives you both: cheap in-place updates when you want them, safe shareable values when you don't.

## Where it's used in a real project

- **Function signatures:** libraries document "this function mutates `df` in place" (pandas `sort_values(inplace=True)`) vs returns a copy — the mutable/immutable contract is API design.
- **Dict keys / set members:** tuples as composite keys — `prices[(symbol, date)]`; you can't use a list.
- **Default arguments:** immutable defaults (`None`, `0`, `""`) are safe; a mutable default is shared across calls (see file 04).
- **`frozen=True` dataclasses / `NamedTuple`:** making config objects immutable so they can be hashed, cached, and safely shared between threads.

## Diagram

```
Caller:  nums ──► [1, 2]          count ──► 5
                    │                    │
def f(lst, n):      │                    │
         lst ───────┘         n ─────────┘        (same objects, new names)

  lst.append(99)   → mutates the ONE list → caller sees [1, 2, 99]
  n = n + 1        → n ──► 6 (new object) → caller's count still 5

dict key rule:
  { (1,2): "ok" }   ✓ tuple is immutable -> hash never changes
  { [1,2]: "x"  }   ✗ TypeError: unhashable type: 'list'
```

## Code — explained

```python
def mutate(lst, n):
    lst.append(99)      # in-place mutation — caller WILL see it
    n = n + 1           # rebinding a local name — caller will NOT

nums = [1, 2]
count = 5
mutate(nums, count)
print(nums)     # [1, 2, 99]
print(count)    # 5

# proof that "changing" an int makes a NEW object:
x = 10
print(id(x) == id(x + 1))   # False — x+1 is a different object; x is still 10
```

1. `lst` and caller's `nums` are two names for one list object; `append` mutates the object itself, so the caller's `nums` shows `99`.
2. `n = n + 1` computes a *new* int `6` and rebinds the local name `n` — the caller's `count` name still points to `5`. Immutable objects can only ever be "replaced," never edited.
3. The `id` check proves immutability concretely: `x + 1` produced a different object; `x` itself is untouched.
4. Interview shorthand: **"Python passes references to objects, and the parameter is just a new name for the same object."** Mutation shows through; rebinding doesn't.

## Problems

### Easy — predict the output
**Problem:** Predict what this prints, and explain which line mutates vs rebinds.
```python
def grow(lst, n):
    lst.append(n)
    n = n * 10

nums = [1]
x = 5
grow(nums, x)
print(nums, x)
```
**Try this input:** (the snippet above)
**Expected output:** `[1, 5] 5`
**Solution:**
```python
def grow(lst, n):
    lst.append(n)
    n = n * 10

nums = [1]
x = 5
grow(nums, x)
print(nums, x)   # [1, 5] 5
```
**Logic explained:**
1. `lst.append(n)` appends `5` to the shared list object → caller's `nums` becomes `[1, 5]`.
2. `n = n * 10` makes a new int `50` and rebinds the *local* `n`; caller's `x` still points at `5`.
3. So `print(nums, x)` → `[1, 5] 5`: the list mutation leaked out, the int "change" did not.

### Medium — return, don't mutate
**Problem:** A teammate wrote `add_item` so it appends to the caller's list — causing spooky bugs where one call site corrupts another's data. Rewrite it as `append_new(lst, item)` that returns a **new** list and leaves the input untouched.
**Try this input:** `orig = [1, 2]`; `new = append_new(orig, 3)`
**Expected output:**
```
[1, 2]
[1, 2, 3]
```
**Solution:**
```python
def append_new(lst, item):
    return lst + [item]     # builds a NEW list; input never touched

orig = [1, 2]
new = append_new(orig, 3)
print(orig)   # [1, 2]
print(new)    # [1, 2, 3]
```
**Logic explained:**
1. `lst + [item]` creates a fresh list object — the immutable-style, "return a new value" contract.
2. `orig` is unmodified, so any other code holding `orig` can't be surprised — this is the whole point of immutability-by-convention.
3. Alternative: `lst.copy() + [item]` or `[*lst, item]`. (`lst.append` + `return lst` would be the bug — it mutates the shared object.)

### Hard — freeze it so it can be a dict key
**Problem:** You need to use structured data (nested lists/dicts/sets) as a dict key or set member, but mutables are unhashable. Write `freeze(obj)` that recursively converts: `list`→`tuple`, `dict`→sorted `tuple` of `(key, frozen_value)` pairs, `set`→`frozenset`, anything else→itself. Prove it by using a frozen structure as a dict key.
**Try this input:** `data = [1, [2, 3], {"a": 4}]`
**Expected output:**
```
(1, (2, 3), (('a', 4),))
hit
```
**Solution:**
```python
def freeze(obj):
    if isinstance(obj, list):
        return tuple(freeze(x) for x in obj)
    if isinstance(obj, dict):
        return tuple(sorted((k, freeze(v)) for k, v in obj.items()))
    if isinstance(obj, set):
        return frozenset(freeze(x) for x in obj)
    return obj                          # int/str/etc: already immutable

data = [1, [2, 3], {"a": 4}]
key = freeze(data)
print(key)                              # (1, (2, 3), (('a', 4),))
seen = {key: "hit"}
print(seen[freeze([1, [2, 3], {"a": 4}])])   # hit
```
**Logic explained:**
1. Recursion converts every nested mutable into an immutable twin, so the result is hashable end-to-end.
2. Dicts become sorted `(key, value)` tuples — sorting makes the frozen form order-independent (dicts compare order-insensitively, tuples don't).
3. `seen[key]` works because two frozen copies of equal data produce equal tuples — this is why immutability and hashing go together.
4. This is the real trick behind `functools.lru_cache` argument hashing and "canonical form" dedup in data pipelines.

## The 30-second interview answer

"Mutable types — list, dict, set, bytearray — can be edited in place; immutable types — int, float, str, tuple, frozenset — can't, so 'modifying' one creates a new object. It matters for function args because Python binds the parameter name to the *same object* the caller passed: mutating it inside the function is visible outside, while reassigning the name is not. It also drives hashability — only immutable objects can be dict keys or set members, since their hash must stay constant — and it's why mutable default arguments are a bug."

## Follow-up trap

**"Are tuples really immutable?"** Mostly — but a tuple can *contain* a mutable object: `t = (1, [2])`. You can't reassign `t[1]`, but `t[1].append(3)` works fine — the tuple is immutable, its contents aren't. Even weirder: `t[1] += [3]` **both** mutates the list **and** raises `TypeError` (the append happens, then the attempted store-back fails — the list still grew!). Second trap: *"so immutables are always safe to share?"* — yes for contents, but beware assuming identity: `x += 1` on an int rebinds, while `lst += [1]` on a list mutates in place (it calls `__iadd__`, i.e. `extend`). Same `+=` operator, opposite behavior — that's the sharpest version of this question.
