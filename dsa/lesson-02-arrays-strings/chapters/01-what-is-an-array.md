# 01 — What is an array, really?

> 4-minute read. One idea only.

## The idea, plain words

An **array** is a row of boxes sitting side by side in the computer's
memory. Each box holds one value, and each box has a position number
called its **index**.

Real-life version: **a row of mailboxes**. Box 0, box 1, box 2... each
holds one letter, and the mail carrier finds any box instantly by its
number — no digging through the others.

```python
nums = [3, 1, 4, 1, 5]
```

In memory it looks like this — five boxes in a row, numbered:

```
value:   [ 3 | 1 | 4 | 1 | 5 ]
index:     0   1   2   3   4
```

## Why does the index start at 0?

Because the index is **not "which box" — it's "how many boxes to skip."**

- `nums[0]` = "start at the first box, skip 0" → `3`
- `nums[2]` = "start at the first box, skip 2" → `4`

The computer stores where the row *starts*, then walks `index` steps
forward. Skipping 0 lands on the first box — so the first index is 0.
Last box of a 5-item array? `nums[4]`, not `nums[5]`. Always
`len(nums) - 1`.

## Try it

```python
nums = [3, 1, 4, 1, 5]
print(nums[0])     # -> 3   (skip 0 boxes)
print(nums[2])     # -> 4   (skip 2 boxes)
print(nums[4])     # -> 5   (the last box)
print(len(nums))   # -> 5   (how many boxes total)
```

## Why it exists

Programs constantly need "the i-th thing" — the 3rd score, the 100th
pixel, today's temperature. Arrays exist so that request is one quick
calculation instead of a treasure hunt. The next chapter shows why that
makes arrays blazingly fast.

## Where it's used

Everywhere. Python `list`s, strings (coming in chapter 04), rows of a
grid, pixels in an image — any time you reach into a sequence by
position, you're indexing an array.

## Common mistake

Thinking `nums[1]` is the *first* element. It's the **second** — index
1 means "skip 1 box." First is `nums[0]`. This one trips up every
beginner; it's called an **off-by-one error**.

## Your turn

```python
temps = [70, 72, 68, 75]
```

What does `temps[3]` print? What is `len(temps)`? What's the index of
the *last* box?

<details><summary>Answer</summary>
`temps[3]` is `75` (skip 3 boxes). `len(temps)` is `4`. Last index is
`3` — always `len - 1`, never `len`.
</details>

---

**Next →** [02 — Why is `nums[5000]` as fast as `nums[0]`?](02-why-indexing-is-o1.md)
