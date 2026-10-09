# 13 — Space Complexity (the "and what about memory?" question)

> 4-minute read.

## The idea, plain words

Time complexity counts *steps*. **Space complexity counts extra memory** —
the new variables, lists, dicts you create, measured against n the same way.

Interviewers follow EVERY "what's the time?" with "...and the space?"
Same notation, different thing being counted.

## The three shapes you'll see

```python
def sum_list(nums):          # O(1) space
    total = 0                # one extra variable — same memory at any n
    for x in nums:
        total += x
    return total
```

```python
def doubled(nums):           # O(n) space
    out = []                 # this list GROWS with the input
    for x in nums:
        out.append(x * 2)
    return out               # n items in → n items of new memory
```

```python
def pairs_table(nums):       # O(n²) space — rare but exists
    table = []
    for a in nums:
        for b in nums:
            table.append((a, b))   # stores n² tuples!
    return table
```

## Why it exists

RAM is finite. An algorithm can be perfectly fast yet die by holding
n² things in memory. There's also a **trade-off** you'll use constantly:
spending O(n) extra space (a set/dict) to *save* time — that's what made
`dedup_fast` O(n) instead of O(n²) in the last chapter. Memory for speed:
the standard deal.

## Where it's used

- "Solve in place" = O(1) extra space required (two-pointer tricks, lesson 04)
- Recursion depth counts too — 1000-deep recursion = O(n) stack memory
- Caching/memoizing = deliberately trading space for time (lesson 15)

## The hidden stack cost

```python
def countdown(n):
    if n == 0: return
    countdown(n - 1)         # n frames deep on the call stack → O(n) space!
```

Every recursive call parks a frame in memory. `fib(10000)` doesn't just
take time — it can blow Python's ~1000 frame limit.

## Your turn

```python
def even_only(nums):
    return [x for x in nums if x % 2 == 0]
```

Time AND space?

<details><summary>Answer</summary>
Time O(n) — one pass. Space O(n) worst case — if ALL items are even,
the new list is size n.
</details>

---

**← Prev** [12 — Best/worst/average](12-best-worst-average.md) ·
**Next →** [14 — Amortized: why append is "O(1)"](14-amortized-append.md)
