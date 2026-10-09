# 02 — Why Sorted Is Required

> 4-minute read. The one rule you can't break.

## The idea, plain words

The guessing game works because "higher/lower" is **trustworthy** — the hint
genuinely rules out half the numbers. A sorted list gives you the same
guarantee: if `nums[mid]` is too small, EVERYTHING to its left is also too
small (sorted means they only get smaller going left).

Unsorted data breaks the promise. The middle element tells you nothing
about its neighbors.

## Watch it fail — same code, unsorted data

```python
def binary_search(nums, target):       # this function needs SORTED nums
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1               # trust: left half is all smaller
        else:
            hi = mid - 1               # trust: right half is all bigger
    return -1

print(binary_search([5, 1, 9, 3, 7], 3))   # 3 IS in there — unsorted!
print(binary_search([1, 3, 5, 7, 9], 3))   # same numbers, sorted
```

```
-1
1
```

Hand trace on the unsorted `[5, 1, 9, 3, 7]`, target `3`:

```
mid=2 → nums[2]=9 > 3 → "go left", hi=1
mid=0 → nums[0]=5 > 3 → "go left", hi=-1 → give up, return -1
```

The `3` was sitting at index 3 the whole time — thrown away by a hint that
was meaningless. And notice: **no error, no crash — just a wrong answer.**
That's the dangerous part.

## Why it exists

Binary search isn't magic — it's a bet. You bet that "mid is too small"
proves the whole left half is dead. Sorted order is what makes that bet
safe. No order → no proof → you're just guessing randomly.

## Where it's used

Everywhere binary search appears, sortedness (or something that *acts*
like it — see chapter 11) is the entry fee. Sorting first, then searching,
is often still faster than scanning unsorted data many times.

## Common mistake

Calling binary search on data you *assume* is sorted. Check the problem
statement — "given a sorted array" is a gift; silence means sort it
yourself or don't use binary search.

## Your turn

`binary_search([10, 20, 5, 30], 20)` — will it find the 20?

<details><summary>Answer</summary>
Yes — by luck. mid=1 → nums[1]=20 → found immediately. Unsorted data
doesn't always fail; it fails *unpredictably*, which is worse — it works
in testing and lies in production.
</details>

---

**← Prev** [01 — The guessing game](01-the-guessing-game.md) ·
**Next →** [03 — The template, line by line](03-the-template.md)
