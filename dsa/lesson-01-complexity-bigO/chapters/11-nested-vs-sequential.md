# 11 — Nested vs Side-by-Side Loops: the #1 confusion

> 4-minute read. This is where most beginners slip — nail it once.

## The idea, plain words

- **Loops side by side → ADD:** O(n) + O(n) = O(n). Two passes, still linear.
- **Loops nested → MULTIPLY:** O(n) × O(n) = O(n²). The inner runs n times *per outer round*.

The question is always: **"does the inner loop restart for every outer
iteration?"** Yes → multiply. No → add.

## Side by side — adds

```python
def two_passes(nums):                # O(n)
    for x in nums:
        print(x)                     # n steps
    for x in nums:
        print(x * 2)                 # n more steps
# 2n total → drop constant → O(n)
```

The second loop starts AFTER the first finishes. Nothing multiplied.

## Nested — multiplies

```python
def all_pairs(nums):                 # O(n²)
    for a in nums:                   # n rounds
        for b in nums:               # inner runs a FULL n per round
            print(a, b)
```

The inner loop isn't "another loop after" — it's **inside**. Outer says:
"for each a..." and the inner replies "...do the whole list again."
n outer rounds × n inner steps = n².

## The sneaky version — hidden inner loop

`in`, `count`, `index`, `max`, `sum` on a **list** are secretly a full scan.
Inside a `for`, each one is a hidden inner loop:

```python
def dedup_slow(nums):                # LOOKS like O(n)
    result = []
    for x in nums:                   # n rounds
        if x not in result:          # hidden scan of result — up to n!
            result.append(x)
    return result                    # actually O(n²)
```

```python
def dedup_fast(nums):                # truly O(n)
    seen = set()
    for x in nums:
        if x not in seen:            # set lookup = O(1) — no hidden scan
            seen.add(x)
    return list(seen)
```

Same job. The `set` version is ~1000× faster at n = 10,000. The only
difference: `in` on a **list** scans; `in` on a **set** hashes.

## Your turn

```python
for a in nums:
    print(a)
print(sum(nums))                     # sum() = hidden pass
for a in nums:
    for b in nums:
        print(a - b)
```

Three parts. Total Big-O?

<details><summary>Answer</summary>
O(n²). The parts are n + n + n² → add them → n² dominates.
The two "linear" pieces don't save the nested one.
</details>

---

**← Prev** [10 — n log n & 2ⁿ](10-onlogn-and-2n.md) ·
**Next →** [12 — Best, worst, average case](12-best-worst-average.md)
