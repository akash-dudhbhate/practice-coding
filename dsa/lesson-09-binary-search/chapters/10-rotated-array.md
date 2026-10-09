# 10 — Rotated Sorted Array — Sortedness with a Scar

> 6-minute read. The precondition is broken — and rescued.

## The idea, plain words

Take `[0, 1, 2, 4, 5, 6, 7]`, grab it at index 3, and rotate the tail to
the front: `[4, 5, 6, 7, 0, 1, 2]`. Not sorted globally — but here's the
rescue: **at every probe, at least ONE half of `[lo, hi]` is fully
sorted.** Find the clean half, check if target fits in its value range.
Inside → search it. Outside → the messy half must hold it.

## Watch it work

```python
def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:              # LEFT half is the clean one
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1                   # target inside clean range
            else:
                lo = mid + 1                   # must be in the messy half
        else:                                  # RIGHT half is clean
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 6))
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))
```

```
4
2
-1
```

Hand trace, target `0`:

```
lo=0 hi=6  mid=3  nums[3]=7   left [4,5,6,7] sorted; 0 ∉ [4,7) → lo=4
lo=4 hi=6  mid=5  nums[5]=1   left? nums[4]=0 ≤ nums[5]=1 sorted;
                              0 ∈ [0,1) → hi=4
lo=4 hi=4  mid=4  nums[4]=0   FOUND → return 4
```

## Why it exists

It looks impossible — "binary search needs sorted" (chapter 02), and this
isn't sorted. The deeper lesson: the real requirement isn't global
sortedness, it's **a guaranteed way to kill half each step**. Local
sortedness is enough, because a clean half lets you decide direction with
a range check instead of a bare `nums[mid] < target`.

## Where it's used

Find-target-in-rotated (LeetCode 33), find-the-rotation-point (= index of
the minimum, LeetCode 153), "almost sorted" arrays. Interviewers love it —
it tests whether you adapt the invariant or just recite it.

## Common mistake

Comparing only `nums[mid]` to `target`. Rotation makes "mid < target"
meaningless — you must first ask **which half is clean**, then use the
range check. For the find-minimum cousin: `nums[mid] > nums[hi]` → min is
right (`lo = mid + 1`); else min is at-or-left of mid (`hi = mid` —
not `mid - 1`, or you'd skip the minimum itself).

## Your turn

In `[4, 5, 6, 7, 0, 1, 2]` with `lo=0, hi=6, mid=3` — why is it safe to
jump `lo` to 4 when target is `0`?

<details><summary>Answer</summary>
nums[lo]=4 ≤ nums[mid]=7 proves the left half is the clean sorted run
[4,5,6,7]. The 0 can't live in a range where every value is ≥ 4 — so the
messy right half is the only place left. Range check = the new hint.
</details>

---

**← Prev** [09 — Search the answer space](09-search-the-answer.md) ·
**Next →** [11 — Peaks: binary search without sortedness](11-peak-without-sorted.md)
