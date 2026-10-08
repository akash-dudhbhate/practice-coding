# 02 — `is` vs `==`, and small-object interning

> **Interview question:** "What's the difference between `is` and `==`? And why does `a is b` work for 256 but sometimes not for 1000?"
> **What the interviewer is really testing:** Whether you understand identity vs equality, and that CPython pre-creates (interns) small objects — so `is` can "accidentally" be True.

## Theory — what it is

`==` asks "do these two objects have the same **value**?" It calls `a.__eq__(b)`, which classes can override — lists compare element-by-element, strings compare character-by-character. `is` asks a narrower question: "are these the **same object** in memory?" It compares `id(a) == id(b)` — essentially the memory address in CPython. Identical objects are always equal; equal objects are not necessarily identical.

So why does `a is b` sometimes surprise you? **Interning** — CPython caches and reuses certain objects so it doesn't create duplicates. Two big cases: **small integers** — every int from -5 to 256 is created once at startup and reused forever, so `a = 256; b = 256` makes both names point to the *same* object. And **strings** — strings that look like identifiers (letters/digits/underscore) typed as literals are usually interned automatically.

For 1000 there's no guarantee — it's outside the small-int cache. *However*, there's a second trap: when two identical literals appear in the **same code block**, the compiler **constant-folds** them into one object anyway, so `x = 1000; y = 1000` in one function can still be `is`-True. The reliable demo is building the second int at **runtime** (`int("1000")`), which forces a fresh object.

## Why it was needed

`is` exists because "same value" and "same thing" are genuinely different questions. A sentinel like `None` or `sentinel = object()` works *because* there's exactly one of them — `x is sentinel` is the only correct test. It's also a free O(1) pointer comparison, while `==` on a million-element list walks every element.

Interning exists for **speed and memory**: small ints (-5..256) are used constantly (loop counters, indexes), so pre-creating ~260 objects once beats allocating millions. String interning makes dict-key and attribute-name lookups faster — equal strings that are the *same object* can short-circuit on pointer equality.

## Where it's used in a real project

- **None checks:** `if x is None:` — the idiomatic test. `==` could be hijacked by a weird `__eq__`.
- **Sentinel defaults:** `MISSING = object()` to distinguish "argument not passed" from "argument passed as None" — used by `dataclasses.MISSING`, `functools`, argparse internals.
- **Identity caches / memoization:** ORMs keep identity maps so two queries for row 5 return the *same* object (`is`-comparable).
- **Enum members:** `Color.RED is Color.RED` — enums are singletons by design; `is` is the recommended comparison.

## Diagram

```
a ──────────► int 256 ◄────────── b      a == b -> True   a is b -> True
                (pre-created, interned — ONE object)

x ──────────► int 1000                    x == y -> True
y ──────────► int 1000   (built at runtime: TWO objects)  x is y -> False

p ──────────► list [1, 2]                 p == q -> True
q ──────────► list [1, 2]   (two lists, same contents)    p is q -> False

n1 ─────────► None ◄────────── n2         singleton: n1 is n2 -> True
```

## Code — explained

```python
a = 256
b = 256
print(a == b, a is b)          # True True   — 256 is interned, ONE object

x = 1000
y = int("100" + "0")           # built at runtime -> guaranteed NEW object
print(x == y, x is y)          # True False  — equal value, different object

p = [1, 2]
q = [1, 2]
print(p == q, p is q)          # True False  — lists are never interned

s1 = "hello"
s2 = "hello"
print(s1 is s2)                # True        — identifier-like literal: interned

s3 = "hello world!"            # space+punct: not auto-interned
s4 = "hello " + "world!"[:6]   # ... runtime-built version
```

1. `a` and `b` both bind to the pre-created int object 256 — same value *and* same identity.
2. `int("100" + "0")` computes `1000` at runtime, allocating a fresh object — so `is` is `False` even though `==` is `True`. (Using the literal `y = 1000` in the same block could still fold to the same object — runtime construction is the reliable way to force the difference.)
3. Lists are mutable and never interned — two literals are always two objects.
4. `"hello"` looks like an identifier, so CPython interns the literal — `s1 is s2` is `True`.
5. The golden rule: compare **values** with `==`, compare **singletons/sentinels** (`None`, `True`, `False`, `object()` markers, enum members) with `is`. Never use `is` for ints/strings — the True you see is an implementation accident.

## Problems

### Easy — predict the output
**Problem:** Without running it, predict what this prints — then verify. Explain each line in terms of value vs identity.
```python
a = 256
b = 256
print(a == b, a is b)
c = [1, 2]
d = [1, 2]
print(c == d, c is d)
```
**Try this input:** (the snippet above)
**Expected output:**
```
True True
True False
```
**Solution:**
```python
a = 256
b = 256
print(a == b, a is b)   # True True
c = [1, 2]
d = [1, 2]
print(c == d, c is d)   # True False
```
**Logic explained:**
1. `a == b`: both hold the value 256 → `True`. `a is b`: 256 is in the interned range (-5..256) → both names point to the *same* pre-made object → `True`.
2. `c == d`: list `__eq__` compares element-by-element → `True`. `c is d`: each literal creates a new list object → `False`.
3. The asymmetry is the lesson: `==` answers "same contents?", `is` answers "same object?".

### Medium — the MISSING sentinel
**Problem:** `dict.get(key, default)` can't tell "key absent" from "value was None" if you default to `None`. Write `get_or(d, key)` that returns a unique sentinel when the key is missing, so callers can test `result is MISSING`.
**Try this input:** `cfg = {"host": "localhost"}`; call `get_or(cfg, "host")` then `get_or(cfg, "port")`
**Expected output:**
```
localhost
True
False
```
**Solution:**
```python
MISSING = object()              # one unique object, created once

def get_or(d, key):
    return d.get(key, MISSING)

cfg = {"host": "localhost"}
r1 = get_or(cfg, "host")
r2 = get_or(cfg, "port")
print(r1)                # localhost
print(r2 is MISSING)     # True
print(r1 is MISSING)     # False
```
**Logic explained:**
1. `object()` creates a guaranteed-unique object — nothing else in the program can equal it by identity, so it's a perfect sentinel.
2. `d.get(key, MISSING)` returns the sentinel *object itself* when the key is absent — the caller checks identity with `is`.
3. `r2 is MISSING` works only because the same singleton object flows back out — `==` against a fresh `object()` would never match.
4. This is exactly how `dataclasses.MISSING` and many library APIs distinguish "not provided" from "None".

### Hard — interning to dedupe strings
**Problem:** You load millions of repeated strings (e.g., a `"country"` column). Use `sys.intern` to guarantee that equal strings share one object, and prove it: build two equal-but-distinct strings at runtime, show `is` is `False`, intern both, show the interned results are the same object.
**Try this input:** `s1 = "".join(["hello", " ", "world!"])` and `s2 = "".join(["hello ", "world!"])`
**Expected output:**
```
True False
True
```
**Solution:**
```python
import sys

s1 = "".join(["hello", " ", "world!"])   # 'hello world!' — built at runtime
s2 = "".join(["hello ", "world!"])       # same VALUE, different object
print(s1 == s2, s1 is s2)                # True False

s1i = sys.intern(s1)
s2i = sys.intern(s2)
print(s1i is s2i)                        # True
```
**Logic explained:**
1. `str.join` builds a *new* string each call, and `"hello world!"` contains a space and `!`, so it's not identifier-like and isn't auto-interned — two equal objects exist → `==` True, `is` False.
2. `sys.intern(s)` registers `s` in CPython's internal string table and returns *the* canonical object for that value; the second intern of an equal string returns the same object.
3. After interning, `s1i is s2i` is `True` — downstream comparisons can use fast pointer equality, and memory holds one copy.
4. Real-world use: pandas/dedup pipelines intern repeated low-cardinality strings to save RAM and speed up dict lookups.

## The 30-second interview answer

"`==` compares values — it calls `__eq__`, which classes can customize. `is` compares identity — whether two names point to the same object in memory, basically `id(a) == id(b)`. The 256-vs-1000 quirk is interning: CPython pre-creates ints from -5 to 256 and reuses them forever, and also interns identifier-looking string literals, so `is` can be True by accident for those. Outside that — or when the object is built at runtime — `is` is False even when `==` is True. Rule of thumb: `==` for values, `is` only for singletons like `None`, sentinels, and enum members."

## Follow-up trap

**"So is `a is b` ever safe to rely on for ints?"** Only for documented singletons — `None`, `True`, `False`, `Ellipsis`, `NotImplemented`. Small-int interning (-5..256) is a CPython implementation detail, not a language guarantee, and constant folding means even big literals in the same code block can share an object — the behavior differs between a script, the REPL (each line compiled separately!), and PyPy. Second trap: *"what does `==` do if `__eq__` isn't defined?"* — it falls back to `object.__eq__`, which is identity comparison. Third: defining `__eq__` without `__hash__` makes your class unhashable — Python sets `__hash__` to `None` so you can't accidentally put a "equal but different" object in a set.
