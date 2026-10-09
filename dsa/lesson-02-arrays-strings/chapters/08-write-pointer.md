# 08 — The write-pointer trick

> 5-minute read. How in-place edits stay safe.

## The idea, plain words

Problem: you're **reading** a list while **writing** into the same
list. How do you not trip over your own feet?

Answer: two pointers — two variables holding positions.

- **Read pointer** (`x` in a `for` loop): scans every element, always
  moves forward.
- **Write pointer** (`w`, a plain int): marks *the next box where a
  "kept" element should go*. It only advances when you keep something.

Because `w` never runs ahead of the reader, you only overwrite boxes
the reader already passed. Nothing you still need gets destroyed.

Real-life version: **packing a suitcase from a messy closet**. You scan
every shelf (read), and each keeper goes into the next free suitcase
slot (write). The closet is one container — you're reorganizing inside
it.

## The pattern: move all zeros to the end

```python
def move_zeros(nums):            # mutates nums, returns None
    w = 0                        # next slot for a non-zero
    for x in nums:               # read pointer: sees everything
        if x != 0:
            nums[w] = x
            w += 1
    while w < len(nums):         # fill the leftover tail with zeros
        nums[w] = 0
        w += 1
```

## Trace it by hand — `[0, 1, 0, 3, 12]`

```
read x=0 :  zero, skip                    nums=[0,1,0,3,12]  w=0
read x=1 :  keep -> nums[0]=1, w=1        nums=[1,1,0,3,12]
read x=0 :  zero, skip                    w stays 1
read x=3 :  keep -> nums[1]=3, w=2        nums=[1,3,0,3,12]
read x=12:  keep -> nums[2]=12, w=3       nums=[1,3,12,3,12]
loop ends. w=3, so fill indices 3,4:      nums=[1,3,12,0,0]
```

```python
a = [0, 1, 0, 3, 12]
move_zeros(a)
print(a)    # -> [1, 3, 12, 0, 0]   order kept, in place, O(n) time
```

Notice the moment of trust: when `x=1` wrote `nums[0]`, box 0 held `0`
— already read, safe to overwrite. `w` is always at or behind the
reader's position. That invariant is the whole trick.

## Why it exists

Chapter 07 promised O(1)-space edits; this is *how* you actually do
them without corrupting data mid-scan. One pass, O(n) time, O(1) space,
original order preserved — the checklist interviews ask for.

## Where it's used

- `medium/p02` — move zeros (exactly this code).
- Remove-duplicates from a sorted list, "keep only evens," partitioning
  around a pivot — all are "scan with reader, place with writer."
- You'll meet the sibling pattern — pointers moving from *both ends* —
  in the two-pointers lesson later.

## Common mistake

- **Forgetting the tail-fill.** The `while` loop after the `for` is not
  optional — without it `[0,1,0,3,12]` ends as `[1,3,12,3,12]`.
- **Returning a new list.** `-> None` means mutate; a fresh list fails
  the O(1)-space contract.
- **Advancing `w` unconditionally.** `w += 1` goes *inside* the `if` —
  it moves only when something was kept.

## Your turn

Run the trace mentally on `[0, 0, 7]`. What does `nums` look like
after the `for` loop ends but *before* the tail-fill?

<details><summary>Answer</summary>
`[7, 0, 7]` with `w=1`. Reads: x=0 skip, x=0 skip, x=7 → nums[0]=7,
w=1. The leftover slots (indices 1, 2) still hold stale values — the
tail-fill then writes zeros → `[7, 0, 0]`.
</details>

---

**← Prev** [07 — Change the list, or build a new one?](07-in-place-vs-new-list.md) ·
**Next →** [09 — Scan twice: count first, build second](09-two-passes.md)
