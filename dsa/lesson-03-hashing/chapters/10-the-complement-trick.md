# 10 — The Complement Trick (two-sum, the #1 pattern)

> 6-minute read. If you learn one hashing pattern, learn this one.

## The idea, plain words

Problem: *find two numbers in the list that add to `target`.*

Brute force tries every pair — O(n²). The trick: **don't search for the
partner — compute it.** For each `x`, the partner it needs is exactly
`target - x`. So keep a dict of everything you've passed, and ask:
*"have I already seen the complement?"*

```python
def two_sum(nums, target):
    seen = {}                          # value -> index
    for i, x in enumerate(nums):
        need = target - x              # the partner x is looking for
        if need in seen:               # did the past already hold it?
            return [seen[need], i]
        seen[x] = i                    # check FIRST, then remember
    return []

print(two_sum([2, 7, 11, 15], 9))
```

```
[0, 1]
```

## Walk it by hand — nums = [2, 7, 11, 15], target = 9

```
i=0   x=2    need=7    seen={}       -> miss, store  ->  seen={2:0}
i=1   x=7    need=2    seen={2:0}    -> HIT! return [0, 1]
```

Two elements in, one pass, done — the O(n²) pair-search became O(n).

## Why it exists

This is the seen-set trick upgraded: the map remembers not just values
but **value → index**, so a "yes" also tells you *where*. The move —
*store the past so each new element can instantly query it* — unlocks
dozens of interview problems.

## Where it's used

Two-sum and every cousin: "pair with difference k", "two entries sum to
price", subarray sums (chapter 11 applies it to running totals). When a
problem says "find two items that relate", reach for a map.

## Common mistakes

- `if need in nums:` — `nums` is a list → O(n) lookup → O(n²) total.
  The complement must be checked against the **map**, not the input.
- Storing `seen[x]` *before* checking: `two_sum([3], 6)` would let 3
  pair with itself and wrongly return `[0, 0]`. Check first, add second.
- Returning values when the problem wants **indices** — that's why the
  dict stores `x -> i`, not just x.

## Your turn

Trace `two_sum([1, 5, 3], 8)` by hand. What gets returned?

<details><summary>Answer</summary>
i=0: x=1, need=7, miss → seen={1:0}.
i=1: x=5, need=3, miss → seen={1:0, 5:1}.
i=2: x=3, need=5 → 5 is in seen at index 1 → return `[1, 2]`.
</details>

---

**← Prev** [09 — Keys can't change](09-keys-cant-change.md) ·
**Next →** [11 — Running totals in a map](11-running-totals-in-a-map.md)
