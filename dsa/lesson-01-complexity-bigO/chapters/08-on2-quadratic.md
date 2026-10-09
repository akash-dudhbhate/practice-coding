# 08 — O(n²): Quadratic Time — the one everyone warns you about

> 6-minute read. Take this one slowly — it's the chapter that matters most.

## The idea, plain words

`O(n²)` means: **every item has to interact with every other item.**

Real-life version: **a group photo where everyone shakes hands with
everyone.** 5 people → each shakes 4 hands → 5×4 = 20 handshakes
(10 unique pairs). 100 people → ~5,000 handshakes. The guests grow linearly,
the work grows *squared*.

In code it happens whenever a **loop sits inside a loop** over the same data.

## Watch it happen — hand count

```python
nums = [1, 2, 3]          # n = 3

for a in nums:            # outer: 3 rounds
    for b in nums:        # inner: 3 steps PER round
        print(a, b)
```

```
a=1 → inner runs: (1,1) (1,2) (1,3)      ← 3 steps
a=2 → inner runs: (2,1) (2,2) (2,3)      ← 3 steps
a=3 → inner runs: (3,1) (3,2) (3,3)      ← 3 steps
                                          total = 9 = 3²
```

Now scale it — this is the part to *feel*:

| n (items) | n² steps | at ~10 billion ops/sec |
|-----------|----------|------------------------|
| 100 | 10,000 | instant |
| 10,000 | 100,000,000 | ~0.01 sec |
| 100,000 | 10,000,000,000 | ~1 sec |
| 1,000,000 | 1,000,000,000,000 | ~100 sec |

**Doubling n quadruples the work.** n=100 → 10,000 steps, n=200 → 40,000.
That's the n² shape: the curve gets steeper and steeper.

## Why it exists

Some problems genuinely need all-pairs work (comparing every element to
every other). But MOST of the time n² is an accident — you nested loops
because it was easy to write, not because the problem required it.
The classic fix: a dict/set turns the inner "search" into O(1) → total O(n).

## Where it's used / when it's fine

- Fine: n is small (< ~1,000), or the problem truly is all-pairs.
- Not fine: interviews and real data — n² on 100k+ items is the bug.

```python
# accidental n² — "for each element, scan the whole list"
for x in nums:
    if x in other_list:        # `in` on a list secretly scans all of it!
        ...
```

## Your turn

```python
for a in nums:          # n
    print(a)
for a in nums:          # n
    for b in nums:      # n
        print(a + b)
```

Total Big-O?

<details><summary>Answer</summary>
`O(n²)` — first part is n, second is n² → n + n² → drop the small term.
The one nested section makes the WHOLE function quadratic.
</details>

---

**← Prev** [07 — O(n): linear](07-on-linear.md) ·
**Next →** [09 — O(log n): halving](09-ologn-halving.md)
