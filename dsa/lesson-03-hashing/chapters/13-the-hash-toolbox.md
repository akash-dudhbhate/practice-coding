# 13 — The Hash Toolbox (which tool for which task)

> 4-minute read. Ties every chapter together. Bookmark this page.

## The whole lesson on one card

| Task | Tool | Cost |
|------|------|------|
| "Is X in my collection?" | `x in my_set` | O(1) per check |
| Count how many of each | `dict` + `.get(x, 0)` / `Counter` | O(n) total |
| Find a pair summing to k | complement map, value → index | O(n) |
| Group equivalent items | `dict.setdefault(key, []).append` | O(n) |
| Remove duplicates | `set(items)` | O(n) |
| Count subarrays summing to k | prefix-sum frequency map | O(n) |
| Cache with "evict oldest" | dict + doubly-linked list | O(1) per op |

## The decision shortcut

When you read a problem, ask one question:

> **"Is there a hidden search inside a loop?"**

- *"check if seen / exists / contains"* → **set**
- *"how many times"* → **counting dict / Counter**
- *"find two that combine to k"* → **complement map**
- *"put equivalents together"* → **dict of lists with a signature key**
- *"subarray sums to exactly k"* → **prefix-sum map**

Every one of those swaps an O(n²) brute force for O(n) time plus O(n)
memory. That swap *is* the lesson.

## One last honesty check

The two things hashing can't do — worth saying out loud in interviews:

1. **No ordering tricks** — dicts can't hand you min/max/sorted order
   (that's sorting, heaps, BSTs — later lessons).
2. **No inequalities** — "sum ≥ k" or "closest to k" won't fit a hash.
   Hashing answers *exact* matches only.

## Practice ladder — name the tool

1. "Does the array contain any duplicates?"
2. "Return the most frequent element."
3. "Indices of two numbers that add to target."
4. "Group all the anagrams together."
5. "How many subarrays sum to k?"

<details><summary>Answers</summary>
1. seen set — or just `len(set(nums)) != len(nums)`.
2. counting dict / `Counter` (ch.06).
3. complement map, value → index (ch.10).
4. dict of lists keyed by sorted letters (ch.07).
5. prefix-sum frequency map seeded with `{0: 1}` (ch.11).
</details>

## What you now know

How a hash function maps keys to slots, why collisions are handled by
buckets, why lookups are O(1) *on average*, what sets are, and the four
patterns — counting, grouping, seen-set, complement — that turn O(n²)
brute forces into O(n) passes. Plus the honest limits: keys must be
immutable, hashing does exact matches only, and ordering needs a second
structure.

**That's the whole lesson.** Now go make `check.py` happy.

---

**← Prev** [12 — Remembering order](12-remembering-order-lru.md) ·
Done with concepts? → Open `task-explanation.md` and solve `easy/p01` next.
