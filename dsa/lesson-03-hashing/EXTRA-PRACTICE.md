# lesson-03-hashing — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: Membership cost
```python
nums = list(range(100000))
target = 99999
print(target in nums)    # (A)
s = set(nums)
print(target in s)       # (B)
```
Which is faster, (A) or (B)? Roughly how much?

<details><summary>Answer</summary>
**(B)** is ~100,000× faster. `in` on a list is a linear scan O(n); `in` on a set
is a hash lookup O(1). Converting to a set costs O(n) once — worth it for
repeated lookups.
</details>

---

## Check 02: .get() vs []
```python
d = {"a": 1}
print(d.get("b", 0))
print(d["b"])
```
What happens (2 lines)?

<details><summary>Answer</summary>
```
0
KeyError
```
`.get(key, default)` returns the default for missing keys; `d[key]` raises
`KeyError`. In counting loops always use `.get(x, 0)` or `defaultdict`.
</details>

---

## Check 03: Set dedup
```python
nums = [3, 1, 3, 2, 1]
print(set(nums))
print(len(set(nums)))
```
What prints?

<details><summary>Answer</summary>
```
{1, 2, 3}
3
```
A set keeps unique values only — duplicates vanish silently. If you need to know
*how many* duplicates there were, use a dict/Counter, not a set.
</details>

---

## Check 04: Unhashable keys
```python
d = {}
d[[1, 2]] = "x"
```
What happens?
- (A) stores it fine
- (B) TypeError
- (C) works but lookup fails later

<details><summary>Answer</summary>
**(B) TypeError: unhashable type: 'list'**. Dict keys must be immutable. Convert
to a tuple: `d[(1, 2)] = "x"`.
</details>

---

## Check 05: Two-sum order matters
```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        seen[x] = i
        if target - x in seen:
            return [seen[target - x], i]
    return []

print(two_sum([3], 6))
```
What prints — and what's the bug?

<details><summary>Answer</summary>
`[0, 0]` — **wrong**. Storing `x` before checking lets the element pair with
itself (3 needs 3, and 3 is "seen" at index 0). Always check the complement
FIRST, then store. Correct version returns `[]`.
</details>

---

## Check 06: Prefix-sum seed
```python
def subarray_sum(nums, k):
    count, prefix, freq = 0, 0, {}   # no {0: 1} seed!
    for x in nums:
        prefix += x
        count += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1
    return count

print(subarray_sum([3, 1], 4))
```
Expected answer is 1 (`[3,1]` sums to 4). What does this print?

<details><summary>Answer</summary>
`0` — **bug**. Without `{0: 1}` in `freq`, subarrays that start at index 0 are
never counted. The empty prefix (sum 0) must be seeded once.
</details>

---

## Debug Exercises — find and fix the bug

> Fix the broken code. Find bugs mentally before running.

---

## Debug 01 (Easy): Count frequencies — KeyError

```python
def count_frequencies(items):
    counts = {}
    for x in items:
        counts[x] += 1
    return counts
```

**Hint:** What happens on the very first item?

<details><summary>Answer</summary>

**Bug:** `counts[x] += 1` on a missing key raises `KeyError`.
**Fix:** `counts[x] = counts.get(x, 0) + 1` or use `defaultdict(int)`.
</details>

---

## Debug 02 (Medium): Find duplicates — duplicates reported twice

```python
def find_duplicates(nums):
    seen = set()
    dupes = []
    for x in nums:
        if x in seen:
            dupes.append(x)
        seen.add(x)
    return sorted(dupes)
```

**Hint:** `find_duplicates([5, 5, 5, 5])` returns `[5, 5, 5]`. Should be `[5]`.

<details><summary>Answer</summary>

**Bug:** `dupes` is a list — every repeat appends again.
**Fix:** make `dupes` a `set()` and `.add(x)`, then `return sorted(dupes)`.
</details>

---

## Debug 03 (Medium): Two-sum — pairs with itself

```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        seen[x] = i
        if target - x in seen:
            return [seen[target - x], i]
    return []
```

**Hint:** Same trap as Check 05 — store order.

<details><summary>Answer</summary>

**Bug:** storing `x` before checking lets `x` pair with itself when
`target == 2*x` (and the dict isn't yet populated for earlier index anyway).
**Fix:** check `if target - x in seen` first, then `seen[x] = i`.
</details>

---

## Debug 04 (Hard): Longest consecutive — recounting runs

```python
def longest_consecutive(nums):
    s = set(nums)
    best = 0
    for x in s:
        length = 1
        while x + length in s:
            length += 1
        best = max(best, length)
    return best
```

**Hint:** It returns the right answer... but what's the complexity? Is it still O(n)?

<details><summary>Answer</summary>

**Bug (performance, not correctness):** every number starts a walk, so a run of
length L is walked L times — O(n²) on inputs like `[1,2,3,...,n]`.
**Fix:** only extend when `x - 1 not in s` (x is a run start):
```python
if x - 1 not in s:
    length = 1
    while x + length in s:
        length += 1
    best = max(best, length)
```
</details>

---

## Debug 05 (Hard): LRU — get() doesn't refresh recency

```python
class LRUCache:
    def __init__(self, cap):
        self.cap = cap
        self.data = {}          # key -> value
        self.order = []         # order[-1] = most recent

    def get(self, key):
        return self.data.get(key, -1)     # BUG: order not updated

    def put(self, key, value):
        if key in self.order:
            self.order.remove(key)
        self.data[key] = value
        self.order.append(key)
        if len(self.data) > self.cap:
            old = self.order.pop(0)
            del self.data[old]
```

**Hint:** `c.get(1); c.put(3,...)` — which key should be evicted?

<details><summary>Answer</summary>

**Bug:** `get` returns the value but doesn't move the key to the most-recent
end, so a *used* key gets evicted. Two issues: recency not refreshed on read,
and `self.order` as a list makes `remove`/`pop(0)` O(n) — real LRU needs a
doubly-linked list + node dict for O(1).
**Fix:** on `get`, move the key/node to the front (head) of the ordering
structure before returning the value.
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: `x in list` inside a loop
```python
# WRONG — O(n) lookup inside O(n) loop = O(n²)
for x in nums:
    if x in results_list:   # list membership
        ...

# CORRECT
seen = set(results_list)
for x in nums:
    if x in seen:           # O(1)
        ...
```

## Mistake 02: counts[x] += 1 on missing key
```python
# WRONG — KeyError
counts[x] += 1

# CORRECT
counts[x] = counts.get(x, 0) + 1
```

## Mistake 03: Using a set when you need counts or indices
```python
# WRONG — set forgets how many times / where
seen = set(nums)   # can't answer "first index of x" or "count of x"

# CORRECT — dict remembers
first_index = {}
for i, x in enumerate(nums):
    first_index.setdefault(x, i)
```

## Mistake 04: Mutable objects as keys
```python
# WRONG — TypeError
groups[[1, 2]] = "x"

# CORRECT — freeze to tuple
groups[tuple(sorted([2, 1]))] = "x"
```

## Mistake 05: Forgetting the {0: 1} prefix seed
```python
# WRONG — misses subarrays that start at index 0
freq = {}

# CORRECT
freq = {0: 1}
```

## Mistake 06: Modifying a dict/set while iterating it
```python
# WRONG — RuntimeError: dictionary changed size during iteration
for k in d:
    if d[k] == 0:
        del d[k]

# CORRECT — iterate a snapshot or rebuild
d = {k: v for k, v in d.items() if v != 0}
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Manual dedup loop
### Before
```python
def find_duplicates(nums):
    dupes = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and nums[i] not in dupes:
                dupes.append(nums[i])
    return sorted(dupes)
```
### Problems
1. O(n²) pairwise comparison — hashing does it in O(n)
2. `nums[i] not in dupes` is another hidden linear scan

### After
```python
def find_duplicates(nums):
    seen, dupes = set(), set()
    for x in nums:
        if x in seen:
            dupes.add(x)
        seen.add(x)
    return sorted(dupes)
```

---

## Refactor 02 (Medium): Brute-force two-sum
### Before
```python
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```
### Problems
1. O(n²) — n=10⁵ means ~5·10⁹ comparisons

### After
```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
```

---

## Refactor 03 (Hard): Subarray sum with recomputed sums
### Before
```python
def subarray_sum(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i:j+1]) == k:
                count += 1
    return count
```
### Problems
1. O(n³) — `sum()` re-scans each slice inside nested loops

### After
```python
def subarray_sum(nums, k):
    count, prefix, freq = 0, 0, {0: 1}
    for x in nums:
        prefix += x
        count += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1
    return count
```

---

## Approach Comparison — different ways to solve it

## Problem: Two Sum

### Approach 1: Brute force
```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```
**Pros:** Zero extra memory, obvious. **Cons:** O(n²) — fails for large n.

### Approach 2: Sort + two pointers
```python
# requires tracking original indices — extra bookkeeping
```
**Pros:** O(n log n), O(1) extra space if indices unneeded. **Cons:** loses
original positions; still slower than hashing.

### Approach 3: Complement hash map
```python
seen = {}
for i, x in enumerate(nums):
    if target - x in seen:
        return [seen[target - x], i]
    seen[x] = i
```
**Pros:** O(n) time, returns indices naturally. **Cons:** O(n) space.

**Winner:** Approach 3 — the canonical interview answer.

---

## Problem: Group Anagrams

### Approach 1: Sorted-string key
```python
key = "".join(sorted(w))     # O(k log k) per word, k = word length
```
**Pros:** Simple, readable. **Cons:** sorting each word costs k log k.

### Approach 2: Count-signature key
```python
key = tuple(counts)          # 26-tuple of letter counts — O(k) per word
```
**Pros:** O(k) instead of O(k log k); scales for long words. **Cons:** more
code; language-specific alphabet.

**Winner:** Approach 1 for clarity (words are usually short); Approach 2 in
interviews if asked to optimize.

---

## Problem: First Unique Character

### Approach 1: Count + second scan
```python
freq = {}
for c in s: freq[c] = freq.get(c, 0) + 1
for i, c in enumerate(s):
    if freq[c] == 1: return i
return -1
```
**Pros:** O(n), dead simple. **Cons:** two passes.

### Approach 2: Single pass with index map
```python
first = {}
for i, c in enumerate(s):
    first[c] = i if c not in first else -1  # -1 marks "seen twice"
return min((i for i in first.values() if i >= 0), default=-1)
```
**Pros:** one pass over the string. **Cons:** second pass over dict anyway;
more code for no real gain.

**Winner:** Approach 1 — clarity beats micro-optimization.
