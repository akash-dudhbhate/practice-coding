# 07 — Pattern 2: Same Direction — Read & Write Pointers

> 5-minute read.

## The idea, plain words

Both pointers walk **left → right**, but with different jobs:

- **`fast`** (the reader) looks at every element, one by one.
- **`slow`** (the writer) marks where the next *keeper* gets written.

When `fast` sees something worth keeping, copy it to `nums[slow]` and
advance `slow`. At the end, **everything left of `slow` is your compacted
answer** — done in place, O(1) extra space.

Real-life version: **packing a suitcase from a pile.** Your scanning hand
(`fast`) picks up every item; your packing hand (`slow`) only moves when
an item earns a spot. The packed region grows behind `slow`; the junk
stays in the unscanned pile.

## In code — dedup a sorted array

```python
def remove_duplicates(nums):       # nums sorted → equals sit adjacent
    if not nums:
        return 0
    slow = 1                       # index 0 is always a keeper
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:   # different from last keeper?
            nums[slow] = nums[fast]        # yes → write it
            slow += 1
    return slow                    # new length; answer = nums[:slow]

arr = [0, 0, 1, 1, 2]
k = remove_duplicates(arr)
print(k, arr[:k])
```

Output:

```
3 [0, 1, 2]
```

## Hand trace — `[0, 0, 1, 1, 2]`

`F` scans, `W` is the write slot. The packed region is left of `W`:

```
W=1   F → [0, 0, 1, 1, 2]      F=1: 0 == last keeper 0 → skip
W=1      F → [0, 0, 1, 1, 2]   F=2: 1 != keeper 0 → write@1 → W=2
W=2         F → [0, 1, 1, 1, 2]  F=3: 1 == keeper(nums[1]=1) → skip
W=2            F → [0, 1, 1, 1, 2]  F=4: 2 != keeper 1 → write@2 → W=3
done: W=3 → answer = nums[:3] = [0, 1, 2]   (tail [1, 2] is garbage)
```

## Why it exists

"Remove/compact" problems push you toward two bad options:

- Build a new list → O(n) extra space, and "in place" says no.
- Call `.remove(x)` → each call shifts the whole tail left, O(n) per
  removal → **O(n²)** total.

The write pointer does one pass, in place, and hands back the new length.

## Where it's used

`medium/p01` (dedup), move-zeros (ch. 08), remove-a-value in place —
the whole "return new length k, first k elements valid" interview format.

## Common mistake

Reading the **tail**. After the run, positions `slow` and beyond hold
stale garbage (`[0, 1, 2, 1, 2]` above — the trailing `1, 2` are
leftovers). The answer is `nums[:slow]`, never `nums`. Also: this dedup
works **only because sorted order puts equals side by side** — on
unsorted data you need a seen-set instead (chapter 10).

## Your turn

Trace `remove_duplicates([1, 1, 2, 2, 2, 3])`. What `k` and what prefix?

<details><summary>Answer</summary>
F=1: 1==keeper → skip. F=2: 2≠1 → write@1, W=2. F=3,4: 2s → skip.
F=5: 3≠2 → write@2, W=3. **k=3**, prefix `[1, 2, 3]` — array is now
`[1, 2, 3, 2, 2, 3]` with garbage tail.
</details>

---

**← Prev** [06 — Sorted pair-sum](06-sorted-pair-sum.md) ·
**Next →** [08 — Partition: move-zeros](08-partition-move-zeros.md)
