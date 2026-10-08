# Lesson 03 — Concepts Explained (Hashing: Dict & Set Patterns)

> Read this before solving the problems. Each concept explains:
> **What it is** · **Why it exists** · **Where it's used** · **What goes wrong** without it.
> Then a worked example with real numbers, code, and expected output.

---

## How Hashing Gives O(1) Lookup

**What it is:** A `dict` (and a `set`) in Python is a *hash table*. When you store
`d["apple"] = 3`, Python runs `hash("apple")` to get a number, uses that number to
pick a slot (a "bucket") in an internal array, and puts the value there. Later,
`"apple" in d` re-computes the same hash, jumps straight to the same bucket, and
finds the answer — no scanning.

```
d["apple"] = 3

hash("apple")  ->  some big number  ->  bucket index 5
internal array:  [ _ , _ , _ , _ , _ , ("apple", 3) , _ , _ ]
                                          ^
"apple" in d -> hash again -> jump to bucket 5 -> found!  O(1)
```

**Why it exists:** Without hashing, "is this item in my collection?" means a linear
scan — O(n) per lookup. With hashing it's O(1) *on average*, so a whole pass over
n items with n lookups costs O(n) instead of O(n²).

**Where it's used:** Deduplication, counting, "seen this before" checks, caches,
indexes, grouping — basically any problem whose brute force is a nested loop asking
"have I seen X / does Y exist".

**What goes wrong without it:**
- `x in my_list` is a hidden O(n) scan. Doing it inside a loop over n items makes
  the whole program O(n²) — 10⁶ items means ~10¹² comparisons. Program hangs.
- Two different keys can land in the same bucket ("collision"). Python handles
  collisions internally, so you never see them — just know O(1) is *average*, not
  magic.
- Hashing trades space for time: you pay O(n) extra memory to make lookups O(1).

**Worked example (real numbers):**

```python
names = ["amit", "sara", "amit", "john", "sara", "amit"]
seen = set()
for n in names:
    if n in seen:          # O(1) per check — 6 checks total
        print(f"{n}: duplicate")
    else:
        seen.add(n)
        print(f"{n}: new")
```

Expected output:
```
amit: new
sara: new
amit: duplicate
john: new
sara: duplicate
amit: duplicate
```

Same check with `seen = []` (a list) still works but each `in` scans the list —
fine for 6 items, fatal for 6 million.

---

## Counting with a Dict (and Counter)

**What it is:** Use a dict where the *key* is the item and the *value* is how many
times you've seen it. Walk the data once, bump counts. Python's
`collections.Counter` is the same idea pre-packaged.

```python
counts = {}
for x in ["a", "b", "a"]:
    counts[x] = counts.get(x, 0) + 1   # .get(key, default) avoids KeyError

from collections import Counter
Counter(["a", "b", "a"])   # Counter({'a': 2, 'b': 1})
```

**Why it exists:** "How many times does each thing appear?" is the most common
sub-problem in all of hashing — frequency tables, voting, histograms, dedup-with-count.

**Where it's used:** Word counts, finding duplicates, "most frequent element",
checking whether two strings are anagrams (equal frequency tables), inventory tally.

**What goes wrong without it:**
- `counts[x] += 1` on a missing key → `KeyError`. Use `counts.get(x, 0)`, a
  `try/except`, or `collections.defaultdict(int)` which auto-creates `0`.
- Counting by sorting + scanning runs in O(n log n) and destroys order. A dict
  count is O(n) and keeps first-seen information available.
- Counter objects compare by content, not identity: `Counter("ab") == Counter("ba")`
  is `True` — handy for anagram checks.

**Worked example (real numbers):**

```python
items = ["pen", "book", "pen", "pen", "book"]
counts = {}
for x in items:
    counts[x] = counts.get(x, 0) + 1
print(counts)
print(max(counts, key=counts.get))   # most frequent
```

Expected output:
```
{'pen': 3, 'book': 2}
pen
```

---

## Set Membership: "Have I Seen This Before?"

**What it is:** A `set` stores unique items with O(1) membership tests. The classic
loop pattern is: keep a `seen` set, for each item ask "is it in seen?" — if yes,
it's a repeat; if no, add it.

```python
seen = set()
for x in nums:
    if x in seen:
        ...   # x is a duplicate
    seen.add(x)
```

**Why it exists:** Sets forget duplicates automatically (`{1, 1, 2}` is `{1, 2}`)
and answer membership in O(1). Two superpowers: *deduplication* and *memory* of
what you've already processed.

**Where it's used:** Detecting duplicates, computing intersections/unions
(`a & b`, `a | b`), tracking visited nodes in graph traversal, "does this input
contain a repeat".

**What goes wrong without it:**
- Using a list for `seen` → `x in seen` is O(n) → whole algorithm O(n²).
- `set()` removes order information you might need — a set can't tell you the
  *first* occurrence's index. For that, store values in a dict as you go.
- Sets swallow duplicates silently: `len(set([1,1,2]))` is `2`. If you need
  counts, you need a dict/Counter, not a set.

**Worked example (real numbers):**

```python
nums = [4, 3, 2, 4, 3, 5]
seen = set()
dupes = set()
for x in nums:
    if x in seen:
        dupes.add(x)
    seen.add(x)
print(sorted(dupes))
```

Expected output:
```
[3, 4]
```

Walk it: 4 new → 3 new → 2 new → 4 seen (dupe) → 3 seen (dupe) → 5 new.
dupes = {3, 4}.

---

## The Complement Lookup Pattern (Two-Sum)

**What it is:** The single most important hashing pattern. When a problem asks
"find two items that relate to each other" (a + b = target), don't compare every
pair. For each item `x`, compute what its *partner* must be (`target - x`) and ask
the hash set/map: "have I seen the partner already?"

```python
seen = {}                    # value -> index
for i, x in enumerate(nums):
    need = target - x        # the complement
    if need in seen:
        return [seen[need], i]
    seen[x] = i
```

**Why it exists:** Brute force checks every pair: O(n²) time. The complement trick
makes one pass: O(n) time, O(n) space. This exact move — *store the past in a hash
map so each new element can instantly query it* — unlocks dozens of problems.

**Where it's used:** Two-sum, pair-difference, "two entries sum to k" in finance/
shopping data, and it's the seed of the prefix-sum pattern below.

**What goes wrong without it:**
- Checking `target - x in nums` where `nums` is a list → O(n) lookup → O(n²) total.
  Convert the "past" to a dict/set.
- Storing into `seen` *before* checking can let an element pair with itself:
  `two_sum([3], 6)` must not return `[0, 0]`. Check first, then add.
- Returning values when the problem wants indices — store `x -> index`, not just x.

**Worked example (real numbers):** `nums = [2, 7, 11, 15]`, `target = 9`.

```
i=0  x=2   need=7   seen={}          -> miss, store {2:0}
i=1  x=7   need=2   seen={2:0}       -> HIT! return [0, 1]
```

```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []

print(two_sum([2, 7, 11, 15], 9))
```

Expected output:
```
[0, 1]
```

---

## Grouping by a Key

**What it is:** Instead of mapping item → count, map a *computed key* → a list of
items that share it. For anagrams the key is the sorted letters; for "index of each
value" the key is the value itself; for "students by grade" the key is the grade.

```python
groups = {}
for w in words:
    key = "".join(sorted(w))        # "eat", "tea", "ate" -> "aet"
    groups.setdefault(key, []).append(w)
```

**Why it exists:** Many problems are really "bucket the items by some property".
A dict of lists does it in one pass: O(total work) instead of comparing every item
to every other item — O(n²).

**Where it's used:** Group anagrams, group transactions by user, index maps
(value → list of positions), bucketing by date/category, deduplicating by a
normalized form (e.g., lowercase email).

**What goes wrong without it:**
- `groups[key].append(w)` on a missing key → `KeyError`. Use
  `groups.setdefault(key, []).append(w)` or `defaultdict(list)`.
- Picking a bad key: using `w` itself groups nothing (each word its own bucket).
  The key must capture the *equivalence* you want — sorted letters, lowercase form,
  value mod k, etc.
- Dict order = insertion order. If the answer needs sorted output, sort the groups
  explicitly — never rely on dict ordering for correctness.

**Worked example (real numbers):**

```python
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}
for w in words:
    key = "".join(sorted(w))
    groups.setdefault(key, []).append(w)
print(list(groups.values()))
```

Expected output:
```
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

Keys produced: "aet" (3 words), "ant" (2 words), "abt" (1 word).

---

## Hash Keys Must Be Immutable (+ the Sorting-as-Key Trick)

**What it is:** Only *immutable* objects can be dict keys / set members — numbers,
strings, tuples of immutables. Lists and dicts can't, because a hash must never
change while the object lives in the table. When your natural key is a list, freeze
it: convert to a tuple.

```python
d[[1, 2]] = "x"        # TypeError: unhashable type: 'list'
d[(1, 2)] = "x"        # OK — tuple is immutable

key = tuple(sorted(word))   # list -> sorted -> tuple: a stable "signature"
```

**Why it exists:** Hash tables need the hash to be a permanent fingerprint. If a
key could mutate after insertion, its bucket would be wrong forever — lookups would
randomly fail. Python enforces this by making mutable types unhashable.

**Where it's used:** Grid coordinates `(r, c)` as dict keys, sorted-tuple
signatures for anagrams, caching function results keyed by `(arg1, arg2)`, memoization.

**What goes wrong without it:**
- `seen.add([1, 2])` → `TypeError: unhashable type: 'list'`. Convert to tuple first.
- `sorted(w)` returns a *list* — `tuple(sorted(w))` or `"".join(sorted(w))` makes
  it hashable. `"".join(sorted("tea"))` → `"aet"`.
- Tuples containing mutables are still unhashable: `(1, [2])` fails. Every level
  must be immutable.

**Worked example (real numbers):**

```python
sig = {}
for w in ["tea", "eat", "bat"]:
    key = "".join(sorted(w))
    sig.setdefault(key, []).append(w)
print(sig)
```

Expected output:
```
{'aet': ['tea', 'eat'], 'abt': ['bat']}
```

---

## Prefix-Sum Hashing (Subarray Sums)

**What it is:** Keep a running total `prefix` as you scan, and store how many times
each prefix value has occurred. A subarray `i..j` sums to `k` exactly when
`prefix[j] - prefix[i-1] == k`, i.e. `prefix[i-1] == prefix[j] - k`. So at each
position, ask the map: "have I seen `prefix - k` before? Each occurrence means one
valid subarray ending here." Seed the map with `{0: 1}` so subarrays starting at
index 0 count.

```python
count = 0
prefix = 0
freq = {0: 1}                      # empty prefix
for x in nums:
    prefix += x
    count += freq.get(prefix - k, 0)   # every past prefix equal to prefix-k works
    freq[prefix] = freq.get(prefix, 0) + 1
```

**Why it exists:** "Count subarrays with sum k" brute-forces O(n²) — every start,
every end. Prefix sums turn each subarray question into an O(1) lookup question —
the complement pattern applied to running totals.

**Where it's used:** Subarray-sum-k, subarrays divisible by k (prefix mod k),
balanced 0/1 subarrays (treat 0 as -1), "continuous range sum" analytics.

**What goes wrong without it:**
- Forgetting `{0: 1}`: a subarray `[2, -2]` (prefix hits k exactly) is missed —
  the "empty prefix" must count once.
- Storing the *new* prefix before checking lets a zero-length subarray count when
  k == 0 — order matters: query first, then record.
- Trying this on "subarray with sum ≥ k" fails — hashing only works for exact
  equality. Inequalities need sorted structures or sliding windows (when all values
  are non-negative).

**Worked example (real numbers):** `nums = [1, -1, 0]`, `k = 0`.

```
prefix=0        freq={0:1}
x=1   prefix=1   need 1-0=1   miss     freq={0:1, 1:1}      count=0
x=-1  prefix=0   need 0-0=0   hit x1   freq={0:2, 1:1}      count=1  ([1,-1])
x=0   prefix=0   need 0-0=0   hit x2   freq={0:3, 1:1}      count=3  ([1,-1,0],[0])
```

Expected output: `3`

---

## Hash Map + Ordering = LRU-Style Designs

**What it is:** A dict gives O(1) lookup but no notion of "oldest" or "most recent".
Combine a dict (key → node) with a doubly-linked list (usage order, most-recent at
the head) and you get a structure where *both* lookup and reordering are O(1):
move a node to the head on every access; evict the tail when full. That's an LRU
(Least Recently Used) cache.

```
dict: {1 -> node(1), 2 -> node(2), 3 -> node(3)}
list: head <-> 3 <-> 1 <-> 2 <-> tail     # 3 most recent, 2 evicted next
```

**Why it exists:** Caches must answer "is this key stored?" fast AND "what do I
throw away when full?" fast. A dict alone can't order; a list alone can't look up.
Together they cover each other's weakness.

**Where it's used:** CPU/page caches, browser history, memoization with bounded
memory, `functools.lru_cache`, database buffers.

**What goes wrong without it:**
- Dict alone: eviction would scan all entries for "oldest" → O(n) per evict.
- List alone: `get` scans → O(n). The whole point is O(1) for both.
- Forgetting to update order on `get` — LRU means *recently used*, and a read
  counts as a use.
- `put` on an existing key must refresh its value AND its position — a common bug
  is updating the value but leaving it near the tail.

**Worked example (real numbers):** capacity 2.

```
put(1,1) put(2,2)  -> cache holds {1,2}   order: 2,1
get(1)             -> returns 1           order: 1,2   (1 now most recent)
put(3,3)           -> evicts 2            cache {1,3}
get(2)             -> -1 (miss)
```

Expected output: `1`, then `-1`.

---

## Quick Reference

| Task | Tool | Cost |
|------|------|------|
| membership test | `x in my_set` | O(1) |
| counting | `dict` + `.get(x, 0)` / `Counter` | O(n) total |
| find pair summing to k | complement map value→index | O(n) |
| group equivalent items | `dict.setdefault(key, []).append` | O(n·k) |
| dedup | `set()` | O(n) |
| subarray sum == k | prefix-sum frequency map | O(n) |
| cached get/put with eviction | dict + doubly-linked list | O(1) each |
