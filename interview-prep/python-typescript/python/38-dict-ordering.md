# 38 — Dict ordering guarantee since 3.7 — what changed (compact dict)

> **Interview question:** "Do Python dicts preserve insertion order? What changed in Python 3.7?"
> **What the interviewer is really testing:** Whether you know the compact-dict redesign (3.6 implementation, 3.7 language guarantee) and its side benefits.

## Theory — what it is

Since Python 3.7, `dict` **guarantees** that iteration order equals insertion order: the order in which you put keys in is the order they come out in `for k in d`, `d.keys()`, `d.items()`. Before 3.7 this was *not* promised — in older CPython the order was arbitrary and depended on hash values and table size.

Technically the change landed in **CPython 3.6** as an implementation detail (the "compact dict" designed by Raymond Hettinger), and was promoted to an official **language guarantee** in 3.7 — meaning every conforming Python must behave this way forever. So if you write code on 3.6 that relies on order, it works in CPython but wasn't officially promised until 3.7.

The mechanism: the dict keeps **two arrays**. One is a dense array of entries — `(hash, key, value)` triples — stored in insertion order. The other is a sparse array of *indices* (the actual hash table) that points into the dense array. Iterating just walks the dense array front to back, so order comes out for free. A bonus: entries are packed tightly, so dicts use ~20-50% less memory than the old design.

## Why it was needed

The old dict stored entries directly inside the sparse hash table. Iterating meant scanning the whole table including thousands of empty slots — wasteful memory and no meaningful order. JSON configs, CSV rows, `**kwargs`, and database records all *naturally* have an order, and losing it forced people to use `collections.OrderedDict` — which worked but was slower, used more memory, and was an extra import for something people wanted 90% of the time.

Compact dict solved both problems at once: ordered iteration as a free side effect, plus a large memory win. It's a great interview point because it's a real engineering tradeoff — slightly more indirection on lookup (one extra array hop) in exchange for ordering and much better cache/memory behavior.

## Where it's used in a real project

- **Deterministic serialization:** `json.dumps(d)` now emits keys in the order you built them — important for diffing generated config files or golden tests.
- **Deduplicating while keeping order:** `list(dict.fromkeys(items))` — the classic "unique but ordered" one-liner.
- **Ordered kwargs:** `def f(**kw)` receives keyword args in the caller's order — matters for builders like `select(**{col: 1 ...})`.
- **CSV/DB row order:** `csv.DictReader` rows and ORM records keep column order.

## Diagram

```
Old dict (pre-3.6):  entries live IN the sparse table
  [ - | - | k2,v2 | - | - | - | k1,v1 | - ]   order = wherever hash landed

Compact dict (3.6+):
  sparse index table:  [ 1 | - | 0 | - | 2 ]   (hash table, holds indices)
                           |       |     |
                           v       v     v
  dense entries:     [ k1,v1 ][ k2,v2 ][ k3,v3 ]   (insertion order kept here)

Iteration = walk dense array left -> right  =>  guaranteed order
```

## Code — explained

```python
d = {}
d["b"] = 1
d["a"] = 2
d["c"] = 3
print(list(d))              # ['b', 'a', 'c'] — insertion order, guaranteed

# deletion then re-insertion puts the key at the END
del d["b"]
d["b"] = 9
print(list(d))              # ['a', 'c', 'b']

# equality ignores order, but iteration doesn't
d2 = {"b": 9, "a": 2, "c": 3}   # same content, different insertion order
print(d == d2)              # True — same keys/values
print(list(d) == list(d2))  # False — ['a','c','b'] != ['b','a','c']

# classic ordered dedupe
print(list(dict.fromkeys([3, 1, 3, 2, 1])))   # [3, 1, 2]
```

1. `list(d)` shows keys come out in insertion order — this is the guarantee.
2. After `del d["b"]` and re-adding, `"b"` appends to the dense array's end.
3. `d == d2` compares content only; dict equality was never order-sensitive.
4. `dict.fromkeys` builds a dict from the list (duplicates collapse, first position wins) — then `list()` pulls the ordered keys back out.

## Problems

### Easy — first unique character, ordered
**Problem:** Return the first character that appears exactly once, using a dict.
**Try this input:** `"swiss"`
**Expected output:** `w`
**Solution:**
```python
def first_unique(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in counts:            # iterates in first-seen order — guaranteed
        if counts[ch] == 1:
            return ch

print(first_unique("swiss"))
# w
```
**Logic explained:**
1. First pass counts every character (O(1) dict updates).
2. Second pass iterates the dict — because order is guaranteed, the first count-1 key found is the first-appearing unique character.
3. Without the ordering guarantee you'd need `enumerate(s)` for a second scan; with it, one dict loop suffices.

### Medium — dedupe keeping order
**Problem:** Remove duplicates from a list while preserving first-occurrence order.
**Try this input:** `[5, 2, 5, 8, 2, 1]`
**Expected output:** `[5, 2, 8, 1]`
**Solution:**
```python
def dedupe(items):
    return list(dict.fromkeys(items))

print(dedupe([5, 2, 5, 8, 2, 1]))
# [5, 2, 8, 1]
```
**Logic explained:**
1. `dict.fromkeys(items)` inserts each item as a key; duplicates overwrite the same bucket, so only the first insertion position survives.
2. Dict keys are unique AND ordered — exactly the properties we need.
3. `list()` converts the ordered keys back. O(n) total vs O(n^2) for `x not in result` list scans.

### Hard — LRU cache skeleton using dict ordering
**Problem:** Implement `get`/`put` on an LRU cache of capacity N using dict ordering (no OrderedDict). `get` marks the key most-recently-used; `put` evicts the least-recently-used when full.
**Try this input:** capacity 2; `put(1,1); put(2,2); get(1); put(3,3); get(2)`
**Expected output:** `get(1)` -> `1`; after `put(3,3)`, `get(2)` -> `-1` (2 was evicted)
**Solution:**
```python
class LRU:
    def __init__(self, cap):
        self.cap = cap
        self.d = {}                    # order: oldest ... newest

    def get(self, k):
        if k not in self.d:
            return -1
        self.d[k] = self.d.pop(k)      # re-insert -> moves to newest end
        return self.d[k]

    def put(self, k, v):
        if k in self.d:
            self.d.pop(k)              # refresh position
        self.d[k] = v                  # newest goes last
        if len(self.d) > self.cap:
            oldest = next(iter(self.d))  # first key = least recently used
            self.d.pop(oldest)

c = LRU(2)
c.put(1, 1); c.put(2, 2)
print(c.get(1))     # 1
c.put(3, 3)         # evicts 2
print(c.get(2))     # -1
```
**Logic explained:**
1. Because dict order = insertion order, the "newest" key is always at the end and the "oldest" at the front.
2. `d[k] = d.pop(k)` deletes and re-inserts — moving the key to the end in O(1).
3. `next(iter(self.d))` grabs the first (least-recently-used) key without scanning.
4. Everything is O(1); this is exactly why the ordering guarantee made `OrderedDict` mostly redundant.

## The 30-second interview answer

"Yes — since Python 3.7, insertion order is an official language guarantee; it actually arrived in CPython 3.6 via the compact-dict redesign. The dict stores entries in a dense array in insertion order, plus a sparse hash table of indices pointing into it. Iterating walks the dense array, so order is preserved for free, and it uses substantially less memory than the old design. Practically, it means `dict.fromkeys` gives ordered deduplication, `**kwargs` preserves call order, and `OrderedDict` is mostly obsolete. One caveat: equality still ignores order — `{a:1,b:2} == {b:2,a:1}` is True."

## Follow-up trap

**"So is OrderedDict completely dead?"** No — three edge cases remain: `OrderedDict.move_to_end()` (explicit reordering), order-sensitive equality (`OrderedDict(a=1,b=2) != OrderedDict(b=2,a=1)`), and `popitem(last=False)` for pops from either end. If they ask *"what happens on delete?"* — the entry is marked deleted in the dense array; re-inserting the same key sends it to the end, and the array is compacted on resize.
