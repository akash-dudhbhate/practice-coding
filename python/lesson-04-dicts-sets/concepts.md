# Lesson 04 — Concepts Explained (Dictionaries & Sets)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Dictionary

**What:** A dictionary is an unordered (insertion-ordered since Python 3.7) collection of key-value pairs. Keys must be unique and hashable; values can be anything.

```python
person = {"name": "Akash", "age": 25, "city": "LA"}
person["name"]          # "Akash"  (access by key)
person["age"] = 26      # update value
person["email"] = "a@b.com"  # add new key-value
del person["city"]      # remove a key

len(person)             # 3
"name" in person        # True  (check if key exists)
```

**Why it exists:** You constantly need to look up a value by a name/label, not by position. "Given a username, find the user." Lists force you to scan every item (O(n)); dicts find a key in constant time (O(1)) using a hash table.

**Where it's used:** Config settings, JSON/API data, caches, counting frequencies, mapping IDs to records, representing objects/rows.

**What goes wrong without it:**
- You store parallel lists (`names = [...]`, `ages = [...]`) and keep them in sync manually — index bugs are inevitable.
- Lookup becomes O(n) — searching 1 million records one by one is slow.
- `KeyError: 'name'` — accessing a missing key crashes. Use `.get()` or `in` first.

---

## .get, .keys, .values, .items

**What:** The core dict methods for safe access and iteration.

```python
person = {"name": "Akash", "age": 25}

person.get("name")          # "Akash"
person.get("email")         # None  (no crash if missing)
person.get("email", "none") # "none"  (default value)

person.keys()    # dict_keys(['name', 'age'])
person.values()  # dict_values(['Akash', 25])
person.items()   # dict_items([('name', 'Akash'), ('age', 25)])

for key, value in person.items():
    print(key, value)
```

**Why it exists:** Direct `d[key]` crashes on missing keys. `.get()` returns a default instead. `.keys()/.values()/.items()` let you iterate over the parts you need without building intermediate lists.

**Where it's used:** Safe lookups (`config.get("timeout", 30)`), iterating config, transforming dicts, building reports from key-value data.

**What goes wrong without it:**
- `d["missing"]` → `KeyError` crashes your program. `.get("missing")` returns `None` gracefully.
- Iterating a dict directly (`for x in d`) gives keys only — confusing if you expected values or pairs. Use `.items()` for pairs.
- Modifying a dict while iterating over it → `RuntimeError: dictionary changed size during iteration`. Iterate over `list(d.items())` if you must modify.

---

## Dict Comprehension & Building Patterns

**What:** Concise ways to build dicts, plus the `setdefault`/`defaultdict` counting pattern.

```python
# Dict comprehension
squares = {n: n*n for n in range(4)}   # {0:0, 1:1, 2:4, 3:9}

# Counting pattern with setdefault
counts = {}
for word in ["a", "b", "a", "c", "b", "a"]:
    counts[word] = counts.get(word, 0) + 1
# counts -> {"a": 3, "b": 2, "c": 1}

# setdefault
d = {}
d.setdefault("k", []).append(1)   # d -> {"k": [1]}
d.setdefault("k", []).append(2)   # d -> {"k": [1, 2]}
```

**Why it exists:** Building dicts from data is extremely common (grouping, counting, indexing). These patterns make it one line instead of a verbose loop with conditionals.

**Where it's used:** Frequency counting, grouping items by key, inverting a dict, filtering dict entries.

**What goes wrong without it:**
- `counts[word] += 1` on a missing key → `KeyError`. You must use `.get(word, 0)` or `setdefault` or `defaultdict`.
- Verbose manual loops are error-prone and hard to read.

---

## Set

**What:** A set is an unordered collection of UNIQUE, hashable items.

```python
colors = {"red", "green", "blue"}
colors.add("yellow")
colors.add("red")      # no effect — already present
"red" in colors        # True  (O(1) membership test)

nums = set([1, 2, 2, 3, 3, 3])   # {1, 2, 3}  (dedupe)
len(nums)             # 3
```

**Why it exists:** When you only care about "is this item present?" or "give me the unique items," a set is faster (O(1) lookup) and clearer than a list (O(n) lookup). It automatically enforces uniqueness.

**Where it's used:** Removing duplicates, membership testing, tracking "seen" items, mathematical set operations (union, intersection).

**What goes wrong without it:**
- Checking `item in big_list` on a 1-million-item list is slow (O(n)). `item in big_set` is O(1).
- Deduplicating with a list (`if x not in result: result.append(x)`) is O(n²). `list(set(items))` is O(n).
- Sets are unordered — if order matters, you can't rely on a set. Use a dict (ordered) or `dict.fromkeys()`.
- Sets only hold hashable items — you can't put a list in a set (`TypeError: unhashable type: 'list'`).

---

## Set Operations

**What:** Mathematical set operations: union, intersection, difference, symmetric difference.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # {1, 2, 3, 4, 5, 6}  union (in either)
a & b    # {3, 4}              intersection (in both)
a - b    # {1, 2}              difference (in a, not b)
a ^ b    # {1, 2, 5, 6}        symmetric difference (in one, not both)

a.issubset(b)    # False
a.isdisjoint(b)  # False (they share 3,4)
```

**Why it exists:** Many real problems are literally set problems: "users who bought both A and B" (intersection), "users in A but not B" (difference), "all users across groups" (union). Operators make these one-liners.

**Where it's used:** Tag systems, permission checks (does user have ANY of these roles?), finding common/different elements, deduping across sources.

**What goes wrong without it:**
- Hand-writing intersection with nested loops is O(n*m) and buggy.
- Confusing `-` (difference) with `^` (symmetric difference) gives wrong results.
- `a | b` creates a NEW set; `a.update(b)` modifies `a` in place. Mixing them up mutates data unexpectedly.

---

## frozenset

**What:** An immutable version of a set. Once created, you can't add or remove items. Because it's immutable and hashable, it can be used as a dict key or a member of another set.

```python
fs = frozenset([1, 2, 3])
# fs.add(4)   # AttributeError — immutable
{fs: "value"}    # OK — frozenset is hashable, can be a dict key
{fs, frozenset([4,5])}  # OK — can be a set member
```

**Why it exists:** Regular sets are mutable and unhashable, so they can't be keys or set members. `frozenset` fills that gap — a constant set you can safely share and use as a key.

**Where it's used:** Caching keyed by a set of options, representing fixed groups (e.g., a set of allowed permissions), as dict keys when the key is a collection.

**What goes wrong without it:**
- Trying to use a set as a dict key → `TypeError: unhashable type: 'set'`. Use `frozenset`.
- Using a regular set where immutability is expected → another part of code mutates it, breaking logic that assumed it was fixed.

---

## Hashability (Why Keys Must Be Hashable)

**What:** A hashable object has a `__hash__` value that never changes during its lifetime and compares equal to other equal objects. Immutable built-ins (int, str, tuple-of-hashables, frozenset) are hashable. Mutable ones (list, dict, set) are not.

```python
hash("hello")     # some int — strings are hashable
hash((1, 2, 3))   # tuples of hashables are hashable
# hash([1, 2, 3]) # TypeError — lists are unhashable

d = {}
d["name"] = 1     # OK — str key
d[(1, 2)] = 3     # OK — tuple key
# d[[1, 2]] = 3   # TypeError — list key not allowed
```

**Why it exists:** Dicts and sets use a hash table for O(1) lookup. The hash must stay constant; if a key's hash changed after insertion, the dict could never find it again. That's why keys must be immutable (hashable).

**Where it's used:** Any time you use a dict or set — the keys/elements must be hashable.

**What goes wrong without it:**
- `TypeError: unhashable type: 'list'` when you try to use a list as a key — convert to a tuple first.
- Putting a mutable object in a set, then mutating it elsewhere, would "lose" the item in the hash table. Python prevents this by forbidding mutable keys entirely.

---

## Choosing Between List, Dict, and Set

**What:** A quick decision guide.

```python
# LIST: ordered, duplicates OK, access by index
scores = [90, 85, 90, 70]

# DICT: lookup by key, unique keys
user_by_id = {101: "Akash", 102: "Sam"}

# SET: unique items, membership testing, set math
tags = {"python", "web", "api"}
```

**Why it exists:** Picking the right structure determines correctness and performance. Wrong choice = slow code or wrong results.

**Where it's used:** Every data-modeling decision in a program.

**What goes wrong without it:**
- Using a list for lookups → O(n) instead of O(1); program slows to a crawl at scale.
- Using a set when order/duplicates matter → lost order, lost duplicates, wrong output.
- Using a dict when a list suffices → wasted memory, more complex code.
