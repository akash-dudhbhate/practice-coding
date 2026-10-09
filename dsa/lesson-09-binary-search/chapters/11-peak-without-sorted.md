# 11 — Peaks: Binary Search Without Sortedness

> 5-minute read. The final boss of the mental model.

## The idea, plain words

A **peak** is an element bigger than both neighbors. Arrays pretend to
fall off to `-∞` past the edges, so a peak always exists. Now — the array
is NOT sorted, yet binary search still works:

- If `nums[mid] < nums[mid+1]` you're climbing **uphill** → a peak MUST
  exist to the right (the slope has to come down eventually — `-∞` at
  the edge forces it).
- Otherwise you're on a peak or going downhill → a peak exists at mid
  or left.

Either way: kill a half. THAT'S the true rule of binary search — not
"sorted array" but "a guaranteed way to eliminate half the candidates."

## Watch it work

```python
def find_peak(nums):                        # nums[i] != nums[i+1]
    lo, hi = 0, len(nums) - 1
    while lo < hi:                          # < keeps mid off the last index
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1                    # uphill → peak is to the right
        else:
            hi = mid                        # peak is at mid or left
    return lo                               # lo == hi = a peak index

print(find_peak([1, 3, 5, 4, 2]))
print(find_peak([1, 2, 3, 1]))
```

```
2
2
```

Hand trace on `[1, 3, 5, 4, 2]`:

```
lo=0 hi=4  mid=2  nums[2]=5 > nums[3]=4  → downhill: hi=2
lo=0 hi=2  mid=1  nums[1]=3 < nums[2]=5  → uphill:  lo=2
lo=2 hi=2  → return 2                    (nums[2]=5 is a peak)
```

## Why it exists

This breaks the beginner mental model "binary search = sorted array" and
replaces it with the real one: "**binary search = monotone elimination
rule**." Rotated arrays, answer spaces, peaks — same skeleton, different
rule for which half dies.

## Where it's used

Find-a-peak (LeetCode 162), bitonic-array maximum, valley finding — any
problem where one LOCAL comparison implies a GLOBAL direction.

## Common mistake

- Checking BOTH neighbors of mid. One is enough — `nums[mid+1]` plus the
  `-∞` boundary guarantee the slope argument.
- Using `while lo <= hi` — then `mid` can BE the last index and
  `nums[mid+1]` reads out of bounds. The `lo < hi` contract keeps mid
  safely inside.

## Your turn

Why is a peak guaranteed in `[1, 2, 3, 1]` even though it's not sorted?

<details><summary>Answer</summary>
Walk uphill as long as values rise; the moment they drop — or the array
ends (pretend `-∞` beyond it) — the highest point you passed is a peak.
Here: 1 < 2 < 3, then 3 > 1 → index 2 (value 3) is the peak.
</details>

---

**← Prev** [10 — Rotated sorted array](10-rotated-array.md) ·
**Back to index →** [concepts.md](../concepts.md)
