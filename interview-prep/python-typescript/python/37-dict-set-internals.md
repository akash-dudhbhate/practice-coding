# 37 — How dict/set are implemented (hash tables); why lookup is O(1)

> **Interview question:** "How are Python dicts and sets implemented under the hood, and why is lookup O(1)?"
> **What the interviewer is really testing:** Whether you understand hashing, buckets, and collision handling — not just that "dicts are fast."

## Theory — what it is

A `dict` and a `set` in CPython are both built on a **hash table**. A hash table is an array of slots (called *buckets*) plus a function called a **hash function** that turns a key into an integer. `hash("name")` might return `81231`; the table takes that integer modulo the table size to pick a bucket index — `81231 % 8 = 7` — and stores the key/value there.

Lookup is O(1) ("constant time" — same speed whether there are 10 keys or 10 million) because you never search. You hash the key, jump straight to the bucket, and grab the value. It is like going directly to drawer #7 instead of opening every drawer. The hash function and array indexing both take the same fixed amount of work regardless of size.

Two keys can land in the same bucket — that is a **collision**. CPython handles collisions with **open addressing**: if bucket 7 is occupied by a different key, it probes other buckets (using a perturbation scheme on the hash bits) until it finds the key or an empty slot. When the table gets too full (about 2/3), Python **resizes** it — allocates a bigger table and rehashes everything — to keep collisions rare and lookups near-instant.

A `set` is literally a dict with keys but dummy values. Everything above applies to `set` membership tests (`x in s`) exactly the same way.

## Why it was needed

Without hashing, finding "is this key present?" means scanning every element — O(n) like a list. Checking `user_id in banned_ids` on a list of a million IDs takes a million comparisons per check. With a set, it is one hash plus one array read. That is the difference between a web request taking 2 seconds and 0.000002 seconds.

The design also forces a rule that beginners trip on: **keys must be hashable** — immutable and with a stable hash. A `list` cannot be a dict key because if you mutated it, its hash would change and the key would be "lost" in the wrong bucket forever.

## Where it's used in a real project

- **Caching / memoization:** `cache[key] = result` — `functools.lru_cache` is a dict under the hood.
- **Counting and grouping:** `collections.Counter`, grouping records by `record["country"]`.
- **Deduplication:** `set(emails)` to strip duplicates before sending notifications.
- **Fast membership filters:** `if user.id in blocked_ids` where `blocked_ids` is a set, not a list.
- **JSON / config / DB rows:** every `json.loads` result and ORM row maps to dicts.

## Diagram

```
hash("cat") = 41  ->  41 % 8 = 1  --+
                                    v
        bucket:  [0]   [1]         [2]   [3]   [4]   [5]   [6]   [7]
                  ---  "cat":4     ---   ---   ---   ---   ---   "dog":9
                              ^
hash("dog") = 95 -> 95 % 8 = 7 --+      (no searching, straight to slot)

Collision: hash("eel") % 8 = 1, but bucket 1 has "cat"
  -> probe next slots until empty or matching key is found
```

## Code — explained

```python
d = {}                 # empty dict — a hash table with 8 slots to start
d["cat"] = 4           # hash("cat") picks a bucket; stores ("cat", 4) there
d["dog"] = 9           # different hash -> different bucket

print(d["cat"])        # 4 — hashes "cat" again, jumps to same bucket, O(1)

s = {1, 2, 3}          # set = dict with keys only
print(2 in s)          # True — hash(2), jump to bucket, found
print(9 in s)          # False — hash(9), bucket empty, stop

# why lists can't be keys:
# d[[1, 2]] = "x"      # TypeError: unhashable type: 'list'
```

1. `d = {}` allocates a small hash table (compact dict — see file 38).
2. `d["cat"] = 4` calls `hash("cat")`, takes `% table_size` to find the bucket, and stores the key and value together (the key is stored too, so collisions can be checked).
3. `d["cat"]` repeats the hash — it always lands in the same place because the hash is deterministic.
4. `2 in s` on the set does the identical bucket jump; no iteration happens.
5. The commented-out line shows the hashability rule: mutable objects can't be keys.

## Problems

### Easy — build a frequency dict
**Problem:** Count how many times each word appears in a list using a dict.
**Try this input:** `["a", "b", "a", "c", "b", "a"]`
**Expected output:** `{'a': 3, 'b': 2, 'c': 1}`
**Solution:**
```python
def count_words(words):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts

print(count_words(["a", "b", "a", "c", "b", "a"]))
# {'a': 3, 'b': 2, 'c': 1}
```
**Logic explained:**
1. `counts.get(w, 0)` does one O(1) lookup; returns 0 if the word isn't stored yet.
2. Each word is hashed twice total (get + set) — still O(1) per word, O(n) for the whole list.
3. A list-of-tuples approach would be O(n^2); the hash table keeps it linear.

### Medium — two-sum with a set/dict
**Problem:** Given a list of numbers and a target, return the indices of two numbers that add to the target. Do it in one pass.
**Try this input:** `nums = [2, 7, 11, 15], target = 9`
**Expected output:** `(0, 1)`
**Solution:**
```python
def two_sum(nums, target):
    seen = {}                     # value -> index
    for i, n in enumerate(nums):
        if target - n in seen:    # O(1) hash lookup instead of rescanning
            return (seen[target - n], i)
        seen[n] = i

print(two_sum([2, 7, 11, 15], 9))
# (0, 1)
```
**Logic explained:**
1. For each number `n`, the partner we need is `target - n`.
2. `target - n in seen` is an O(1) hash lookup — this is exactly why dicts exist.
3. If found, return the stored index plus the current index.
4. Otherwise record `n -> i` so future numbers can find it. Total time O(n) instead of the brute-force O(n^2).

### Hard — group anagrams
**Problem:** Group words that are anagrams of each other (same letters, different order).
**Try this input:** `["eat", "tea", "tan", "ate", "nat", "bat"]`
**Expected output:** `[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]` (group order may vary)
**Solution:**
```python
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = tuple(sorted(w))    # sorted letters = canonical key
        groups[key].append(w)
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```
**Logic explained:**
1. `"eat"` and `"tea"` both sort to `('a','e','t')` — anagrams share a key.
2. The tuple is hashable (a list wouldn't be!) so it can be a dict key.
3. `defaultdict(list)` auto-creates an empty list for unseen keys — one O(1) lookup per word.
4. Sorting each word is O(k log k); total O(n · k log k), far better than pairwise comparison.

## The 30-second interview answer

"Dicts and sets are hash tables: the key goes through a hash function, the result modulo the table size picks a bucket, and the value is stored there. Lookup is O(1) because you hash once and jump straight to the slot — no scanning. Collisions are handled by open addressing — Python probes other buckets until it finds the key or an empty slot. When the table fills past about two-thirds, it resizes and rehashes. A set is just a dict with keys and no values, which is why `in` on a set is O(1). And that's also why keys must be immutable — a mutable key could change its hash and get lost."

## Follow-up trap

**"What's the worst-case time, and when does it happen?"** The worst case is O(n) — if every key collides into the same bucket (adversarial hash flooding, or a pathological `__hash__`). Python mitigated real-world hash-flooding attacks with SipHash-based randomized string hashing (PYTHONHASHSEED). Also expect: *"Can a tuple be a dict key?"* — yes, but only if everything inside it is hashable: `(1, 2)` yes, `([1], 2)` no.
