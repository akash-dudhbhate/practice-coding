# 03 — The Template, Line by Line

> 6-minute read. Take this one slowly — it's the code everything else copies.

## The idea, plain words

Binary search has three moving parts: **`lo`** (lowest index still alive),
**`hi`** (highest index still alive), **`mid`** (where we probe). The
unbreakable rule — the *invariant*: **if the answer exists, it's inside
`[lo, hi]`**. Every update must keep that true while shrinking the range.

```python
def binary_search(nums, target):        # nums must be SORTED
    lo, hi = 0, len(nums) - 1           # line 1: every index is alive
    while lo <= hi:                     # line 2: while anyone's still alive
        mid = (lo + hi) // 2            # line 3: probe the middle
        if nums[mid] == target:
            return mid                  # found it
        elif nums[mid] < target:
            lo = mid + 1                # mid too small → kill mid and left
        else:
            hi = mid - 1                # mid too big → kill mid and right
    return -1                           # range empty → not there
```

## Every line, explained

- **Line 1** — `hi = len(nums) - 1`, not `len(nums)`. The range is
  *inclusive*: index `len(nums)` doesn't exist, so it can't start alive.
- **Line 2** — `lo <= hi`, not `lo < hi`. When `lo == hi` there's still
  ONE element left to check. `lo < hi` would quit early and skip it.
- **Line 3** — `(lo + hi) // 2` is the midpoint, rounded **down** (toward
  `lo`). You'll see `lo + (hi - lo) // 2` in other languages — same math,
  avoids integer overflow; Python ints can't overflow so both work.
- **`lo = mid + 1` / `hi = mid - 1`** — the `± 1` matters. `mid` was just
  checked and failed, so it's dead too. Leaving it in invites an infinite
  loop (chapter 06 shows the horror).

```python
print(binary_search([1, 3, 5, 7, 9], 3))
print(binary_search([1, 3, 5, 7, 9], 4))
```

```
1
-1
```

## Why it exists

This exact shape is the answer to "how do I never get an off-by-one bug?"
Pick inclusive `[lo, hi]` + `lo <= hi` + `mid ± 1` and the three pieces
are *consistent* — each one compensates for the others. Mix and match
(`lo < hi` with `hi = mid - 1`, say) and you get silent skipped elements.

## Where it's used

Every binary-search variant in this lesson is this template with a
different "which half is dead" rule. Memorize the shape; derive the rule.

## Common mistake

`hi = len(nums)` in this template — then the first probe can read
`nums[len(nums)]` → `IndexError`. Inclusive template wants
`len(nums) - 1`. (Boundary searches in chapter 07 use `len(nums)`
deliberately — different contract.)

## Your turn

In `binary_search([1, 3, 5, 7, 9], 9)`, what's `mid` on the first probe,
and what does it do next?

<details><summary>Answer</summary>
lo=0, hi=4 → mid=(0+4)//2=2. nums[2]=5 < 9 → kill left half: lo=3.
Next probe: mid=(3+4)//2=3, nums[3]=7 < 9 → lo=4, then mid=4 → found.
</details>

---

**← Prev** [02 — Why sorted is required](02-why-sorted.md) ·
**Next →** [04 — Hand trace, start to finish](04-hand-trace.md)
