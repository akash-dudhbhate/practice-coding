# 06 — Any range-sum in one subtraction

> 5-minute read. This is where the prefix sum earns its name.

## The idea, plain words

Question: "sum of `nums[i]` through `nums[j]`?" With the checkpoint
list `P` from chapter 05, the answer is **one subtraction**:

```
sum(i..j)  =  P[j+1] - P[i]
```

Why does subtracting work? `P[j+1]` is "everything up to and including
j." `P[i]` is "everything before i." Take the first, remove the second
— what's left is exactly `i` through `j`.

Real-life version: **odometer math**. Trip distance = odometer now
minus odometer at the start. You don't re-measure the road.

## Trace it with real numbers

```python
nums = [1, 2, 3, 4, 5]
P = [0, 1, 3, 6, 10, 15]      # built last chapter: P[i] = first i elements
```

Question: sum of indices 1..3 → `2 + 3 + 4`.

```
want:        [ 1 | 2 | 3 | 4 | 5 ]     indices 1..3
                 └───── sum this ─┘

P[4] = 10   = everything through index 3  = 1+2+3+4
P[1] =  1   = everything before index 1   = 1
P[4]-P[1] = 9 = 2+3+4                     <- exactly what we wanted
```

```python
print(P[4] - P[1])   # -> 9  (two lookups + one minus, no loop)
```

Same trick, different range — indices 0..2 → `1+2+3 = 6`:

```python
print(P[3] - P[0])   # -> 6 - 0 = 6
```

See why the leading `0` matters? `P[0]` gives "sum before index 0 = 0"
a home — ranges starting at 0 work for free.

## The payoff: one build, unlimited queries

```python
def range_sum(P, i, j):       # P built ONCE, O(n)
    return P[j + 1] - P[i]    # every query O(1)

nums = [1, 2, 3, 4, 5]
P = [0]
for x in nums:
    P.append(P[-1] + x)

for (i, j) in [(0, 2), (1, 4), (2, 2)]:
    print(i, j, "->", range_sum(P, i, j))
# -> 0 2 -> 6
# -> 1 4 -> 14
# -> 2 2 -> 3
```

Three queries, zero loops over `nums`. With a thousand queries: naive
re-summing is O(1000·n); this is O(n + 1000). That's the whole trick —
**precomputation trading space for time**.

## Why it exists

Dashboards and problems ask range questions over and over ("sales
Tuesday→Friday", "sum of last k days"). Answering each by scanning is
fine once, wasteful a thousand times. Pay O(n) once; every question
after is two array reads and a minus.

## Where it's used

Range-sum queries (medium/p01!), sliding statistics, image regions in
2D, and — in chapter 12 — turned inside-out with a dict to hunt for
subarrays summing to `k`.

## Common mistake — THE prefix-sum bug

Off-by-one between `P[i]` and `P[i+1]`. There is exactly one
convention worth memorizing:

> `P[0] = 0`, `P[i]` = sum of first `i` elements.
> Then `sum(i..j inclusive) = P[j+1] - P[i]`. **Always.**

If a range answer is wrong by one element, it's this. Check `P[0]` and
the `+1` before touching anything else.

## Your turn

With `nums = [2, 5, 1, 8]` and `P = [0, 2, 7, 8, 16]`: what is
`sum(1..3)` using one subtraction? Say the indices before computing.

<details><summary>Answer</summary>
`P[4] - P[1]` = `16 - 2` = `14`. Check: 5+1+8 = 14.
The `+1` on j is the part beginners drop — `P[j+1]`, not `P[j]`.
</details>

---

**← Prev** [05 — Running totals: pay once, remember forever](05-running-totals.md) ·
**Next →** [07 — Change the list, or build a new one?](07-in-place-vs-new-list.md)
