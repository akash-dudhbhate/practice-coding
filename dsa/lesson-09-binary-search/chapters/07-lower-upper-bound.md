# 07 — Lower Bound & Upper Bound — Searching a Boundary, Not a Value

> 6-minute read. The variant that answers "where does it belong?" — even when it's not there.

## The idea, plain words

Sometimes you don't want "is 7 in the list?" — you want "**where would 7
go?**" Two boundary searches always return a position, found or not:

- **Lower bound** = first index `i` where `nums[i] >= target`.
  (If target exists → first occurrence. If not → the slot it would occupy.)
- **Upper bound** = first index `i` where `nums[i] > target`.
  (One past the LAST occurrence.)

With duplicates this is a superpower: `upper − lower` = how many copies.

```python
def lower_bound(nums, target):           # first i: nums[i] >= target
    lo, hi = 0, len(nums)                # hi CAN be len(nums) — legal answer
    while lo < hi:                       # note: < , not <=
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1                 # too small → go right
        else:
            hi = mid                     # mid MIGHT be the answer — keep it
    return lo

print(lower_bound([1, 2, 2, 2, 4], 2))   # first index holding 2
print(lower_bound([1, 2, 2, 2, 4], 3))   # where 3 would insert
print(lower_bound([1, 2, 2, 2, 4], 9))   # past the end!
```

```
1
4
5
```

Hand trace, `lower_bound([1, 2, 2, 2, 4], 2)`:

```
lo=0 hi=5  mid=2  nums[2]=2 >= 2 → hi=2     keep mid (maybe THE first 2)
lo=0 hi=2  mid=1  nums[1]=2 >= 2 → hi=1     keep going left
lo=0 hi=1  mid=0  nums[0]=1 < 2  → lo=1     too small, dead
lo=1 hi=1 → return 1                      first index holding 2
```

## Why it exists

"Does it exist?" loses information. "Where's the boundary?" answers
existence, first occurrence, insertion point, and frequency — all in one
probe count. Notice the DIFFERENT contract: `lo < hi` + `hi = mid` is safe
here because mid rounds toward `lo`, and when `lo+1 == hi` we get
`mid == lo`, which makes `lo` move. The pieces compensate — again.

## Where it's used

First/last occurrence, search-insert-position (LeetCode 35), counting
duplicates, "smallest element ≥ x", and it's the engine inside
"binary search the answer" (chapter 09 — the answer IS a lower bound).

## Common mistake

- Mixing templates: `lo <= hi` together with `hi = mid` → infinite loop
  when `lo == hi` (mid = lo = hi, and `hi = mid` moves nothing).
- Returning `nums[lo]` blindly — lower bound can legally return
  `len(nums)` ("past the end"); check `lo < len(nums)` first.

## Your turn

`lower_bound([2, 4, 4, 4, 6, 8], 5)`?

<details><summary>Answer</summary>
4 — index of the 6, the first element ≥ 5. The 5 isn't there; the bound
tells you exactly where it would slot in.
</details>

---

**← Prev** [06 — The infinite-loop bug](06-infinite-loop-bug.md) ·
**Next →** [08 — The bisect module](08-bisect-module.md)
