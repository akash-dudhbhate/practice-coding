# 05 — Running totals: pay once, remember forever

> 5-minute read. First technique of the lesson — read slowly.

## The idea, plain words

A **running total** (its fancy name: *prefix sum*) is just "the sum so
far." While walking through the list once, you keep adding — and you
**write down each total**. Now you have a second list that remembers
every checkpoint.

Real-life version: **your bank statement's running balance**. Each row
shows the balance *after* that transaction — nobody recomputes it by
re-adding every transaction since the account opened.

## Build one by hand

```python
nums = [1, 2, 3, 4, 5]
```

Walk it left to right, keeping `total`:

```
x = 1   total = 0 + 1 = 1    checkpoints: [1]
x = 2   total = 1 + 2 = 3    checkpoints: [1, 3]
x = 3   total = 3 + 3 = 6    checkpoints: [1, 3, 6]
x = 4   total = 6 + 4 = 10   checkpoints: [1, 3, 6, 10]
x = 5   total = 10 + 5 = 15  checkpoints: [1, 3, 6, 10, 15]
```

`checkpoint[i]` = sum of `nums[0]` through `nums[i]`. That took **one
pass — O(n)** — and now every partial sum is memorized.

## The convention that prevents bugs

Real code stores the checkpoints **shifted by one**, starting with 0:

```python
nums = [1, 2, 3, 4, 5]
P = [0]                      # "sum of the first 0 elements" = 0
for x in nums:
    P.append(P[-1] + x)      # each new entry = last entry + this element
print(P)                     # -> [0, 1, 3, 6, 10, 15]
```

```
index i:      0   1   2   3   4   5
P[i]:       [ 0 | 1 | 3 | 6 | 10| 15 ]
              ^   ^               ^
              |   |               |
            empty sum(1)      sum(1..5)
```

Read it as: **`P[i]` = sum of the first `i` elements.**

- `P[0]` = sum of first 0 elements = `0`
- `P[3]` = sum of first 3 elements = `1+2+3` = `6`
- `P[5]` = sum of first 5 elements = `15`

Note `P` has **n+1** entries — one extra slot for the empty sum. That
leading `0` is doing real work; the next chapter shows why.

## Why it exists

Because "sum of these elements" questions repeat. Re-adding from
scratch every time is wasted work — a checkpoint list pays O(n) **once**
and remembers forever. Next chapter turns this into O(1) range-sum
queries, which is where it becomes a superpower.

## Where it's used

Running balances, "total so far" dashboards, cumulative counts,
"rainfall this year through July" — and the hard problem in this lesson
(subarray-sum-equals-k) is built directly on it.

## Common mistake

Dropping the leading `0` and starting `P` at `nums[0]`. Then "sum of
everything before index i" has nowhere to live, and the range formula
next chapter breaks on index 0. Always start with `P = [0]`.

## Your turn

Build `P` (with the leading 0) for `nums = [3, 1, 4]`. What is `P`?

<details><summary>Answer</summary>
`P = [0, 3, 4, 8]`.
`P[0]=0`, `P[1]=0+3=3`, `P[2]=3+1=4`, `P[3]=4+4=8`.
Check: `P[3]` = sum of all 3 elements = 3+1+4 = 8.
</details>

---

**← Prev** [04 — Strings: arrays you can't write to](04-strings-immutable-arrays.md) ·
**Next →** [06 — Any range-sum in one subtraction](06-range-sum-one-subtraction.md)
