# 08 — Partition: Keepers Left, Movers Right

> 4-minute read. Same read/write idea, new keeper rule.

## The idea, plain words

Chapter 07's keeper rule was "different from the previous keeper." Now
the rule is a **condition**: "keep every non-zero." Same machinery —
`fast` scans, `slow` writes keepers — then fill the leftover tail.

**Move all zeros to the end** (keeping other elements' order):

- Pass 1: write every non-zero at `slow`, advancing `slow`.
- Pass 2: fill `slow` to the end with zeros.

Real-life version: **sorting laundry as you pull it from the basket.**
Keepers go straight onto the shelf at the next free slot; zeros are the
socks you toss in a pile — you deal with them at the end.

## In code

```python
def move_zeros(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:          # keeper?
            nums[slow] = nums[fast]  # write at next free slot
            slow += 1
    for i in range(slow, len(nums)): # fill the tail
        nums[i] = 0
    return nums

print(move_zeros([0, 1, 0, 3, 12]))
```

Output:

```
[1, 3, 12, 0, 0]
```

## Hand trace — `[0, 1, 0, 3, 12]`

```
W=0   F → [0, 1, 0, 3, 12]    F=0: 0 → skip (not a keeper)
W=0      F → [0, 1, 0, 3, 12]  F=1: 1 → write@0 → [1, 1, 0, 3, 12] W=1
W=1         F → [1, 1, 0, 3, 12]  F=2: 0 → skip
W=1            F → [1, 1, 0, 3, 12]  F=3: 3 → write@1 → [1, 3, 0, 3, 12] W=2
W=2               F → [1, 3, 0, 3, 12]  F=4: 12 → write@2 → [1, 3, 12, 3, 12] W=3
tail fill: positions 3,4 get 0 → [1, 3, 12, 0, 0]  done
```

## Why it exists

The **partition** idea — "split the array into group A in front, group B
behind" — generalizes dedup: any yes/no test can drive the write pointer.
The famous three-way version (**Dutch national flag**: sort 0s/1s/2s into
three regions) uses *two* write boundaries — `low` and `high` — while a
scanner walks between them. Same family, one extra pointer. You'll meet
it in interviews; the core is already in your hands.

## Where it's used

Move-zeros, remove-element-in-place, "evens before odds," pivot
partitioning inside quicksort — and the backward version (write from the
**end**) powers merge-sorted-in-place in `hard/p02` (see chapter 11).

## Common mistake

Two, and they're both in the trace above:

- Forgetting the **tail fill** — you'd return `[1, 3, 12, 3, 12]` with
  stale `3, 12` where the zeros belong.
- Overwriting an element `fast` hasn't read yet. It's safe here because
  `slow ≤ fast` always — the write slot chases the reader, never leads it.
  Writing *forward* into unread territory is the bug; a `slow` that trails
  `fast` can't do that.

## Your turn

Trace `move_zeros([2, 0, 0, 4])`. What does the array look like after
pass 1 (before the tail fill)?

<details><summary>Answer</summary>
F=0: 2 → write@0 (no visible change), W=1. F=1,2: zeros → skip.
F=3: 4 → write@1 → `[2, 4, 0, 4]`, W=2. Then tail fill → `[2, 4, 0, 0]`.
The stale `4` at index 3 is exactly why pass 2 exists.
</details>

---

**← Prev** [07 — Read & write pointers](07-read-write-pointers.md) ·
**Next →** [09 — Two pointers vs hashing](09-vs-hashing.md)
