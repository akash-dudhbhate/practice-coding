# lesson-04-dicts-sets — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Dict vs List Lookup
```python
d = {i: i for i in range(10000)}
l = list(range(10000))

# Which is faster?
# A: `9999 in d`
# B: `9999 in l`
```
Which is faster?

<details><summary>Answer</summary>
**A is much faster.** Dict lookup is O(1) (hash table). List lookup is O(n) (scans each element). For 10000 items, dict is ~10000× faster for worst case.
</details>

## Check 02: Dict Ordering
```python
d = {"c": 1, "a": 2, "b": 3}
print(list(d.keys()))
```
What prints? (Python 3.7+)

<details><summary>Answer</summary>
```
['c', 'a', 'b']
```
Since Python 3.7, dicts maintain insertion order. Before 3.7, order was arbitrary.
</details>

## Check 03: Set Operations
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)
print(a | b)
print(a - b)
```
What prints (3 lines)?

<details><summary>Answer</summary>
```
{2, 3}
{1, 2, 3, 4}
{1}
```
`&` = intersection, `|` = union, `-` = difference.
</details>

## Check 04: Dict Get with Default
```python
d = {"a": 1}
print(d.get("b", 0))
print(d.get("a", 0))
print(d["b"])
```
What happens (3 lines)?

<details><summary>Answer</summary>
```
0
1
KeyError
```
`.get(key, default)` returns default if key missing. `d[key]` raises KeyError if missing.
</details>

## Check 05: Set from String
```python
s = set("hello")
print(s)
print(len(s))
```
What prints (2 lines)?

<details><summary>Answer</summary>
```
{'h', 'e', 'l', 'o'}
4
```
`set("hello")` creates a set of UNIQUE characters. 'l' appears twice in "hello" but once in the set.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Word Count — Not Lowercasing
```python
def word_count(text):
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
```
**Hint:** "The" and "the" should be the same word.

<details><summary>Answer</summary>
**Bug:** Doesn't lowercase. `word_count("The the")` returns `{"The": 1, "the": 1}` instead of `{"the": 2}`.
**Fix:** `words = text.lower().split()`.
</details>

## Debug 02 (Medium): Has Key — Wrong Check
```python
def has_key(d, key):
    return d.get(key) is not None
```
**Hint:** What if the value IS None?

<details><summary>Answer</summary>
**Bug:** If the key exists but its value is `None`, `d.get(key)` returns `None`, and `is not None` is False — so it says the key doesn't exist. `has_key({"a": None}, "a")` returns False!
**Fix:** `return key in d` or `return d.get(key, sentinel) is not sentinel` where sentinel is a unique object.
</details>

## Debug 03 (Hard): Invert Dict — Duplicate Values Lost
```python
def invert_dict(d):
    return {v: k for k, v in d.items()}
```
**Hint:** What if two keys have the same value?

<details><summary>Answer</summary>
**Bug:** If values aren't unique, later keys overwrite earlier ones. `invert_dict({"a": 1, "b": 1})` returns `{1: "b"}` — "a" is lost silently.
**Fix (if acceptable):** Document that last key wins. **Fix (if need all):** Return `{v: [k1, k2]}` with lists.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Using `in` on dict checks values instead of keys
```python
d = {"a": 1, "b": 2}
# WRONG — checks values, not keys
if 1 in d:  # False! checks keys
# CORRECT
if "a" in d:  # True
if 1 in d.values():  # True — but slower
```

## Mistake 02: Modifying dict while iterating
```python
# WRONG — RuntimeError
d = {"a": 1, "b": 2}
for key in d:
    if d[key] == 1:
        del d[key]

# CORRECT — iterate over a copy
for key in list(d.keys()):
    if d[key] == 1:
        del d[key]
```

## Mistake 03: Using dict when you need a list of pairs
```python
# WRONG — keys must be hashable, loses duplicates
d = {["a", 1], ["b", 2]}  # TypeError — list not hashable

# CORRECT — use list of tuples
pairs = [("a", 1), ("b", 2)]
```

## Mistake 04: Not using defaultdict
```python
# VERBOSE
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

# BETTER — defaultdict
from collections import defaultdict
counts = defaultdict(int)
for word in words:
    counts[word] += 1
```

## Mistake 05: Using set for ordered data
```python
# WRONG — sets are unordered
unique_ordered = set([3, 1, 2])  # {1, 2, 3} — order lost!

# CORRECT — use dict.fromkeys (preserves order)
unique_ordered = list(dict.fromkeys([3, 1, 2]))  # [3, 1, 2]
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Manual Key Check
### Before
```python
def add_to_dict(d, key, value):
    if key in d:
        d[key] = d[key] + value
    else:
        d[key] = value
```
### After
```python
def add_to_dict(d, key, value):
    d[key] = d.get(key, 0) + value
```

## Refactor 02 (Medium): Manual Counting
### Before
```python
def count_words(text):
    counts = {}
    for word in text.split():
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts
```
### After
```python
from collections import Counter
def count_words(text):
    return dict(Counter(text.split()))
```

## Refactor 03 (Hard): Nested Dict Access
### Before
```python
def get_value(data):
    if data is not None:
        if "user" in data:
            if "name" in data["user"]:
                return data["user"]["name"]
    return None
```
### After
```python
def get_value(data):
    return data.get("user", {}).get("name")
```

---

## Approach Comparison — different ways to solve it

## Problem: Word Count

### Approach 1: Manual loop with .get()
```python
def word_count(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```

### Approach 2: defaultdict
```python
from collections import defaultdict
def word_count(text):
    counts = defaultdict(int)
    for word in text.lower().split():
        counts[word] += 1
    return dict(counts)
```

### Approach 3: Counter
```python
from collections import Counter
def word_count(text):
    return dict(Counter(text.lower().split()))
```

**Winner:** Approach 3 (Counter) — built for exactly this. One line, tested, fast.

---

## Problem: Unique Items (order-preserving)

### Approach 1: Set + loop
```python
def unique_items(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```

### Approach 2: dict.fromkeys()
```python
def unique_items(items):
    return list(dict.fromkeys(items))
```

**Winner:** Approach 2 — one line, preserves order, O(n).
