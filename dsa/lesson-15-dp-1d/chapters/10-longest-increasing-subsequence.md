# 10 — Longest Increasing Subsequence: a different table shape

> 7-minute read. `dp[i]` reads ALL previous cells — and the answer lives at `max(dp)`.

## The idea, plain words

> `nums = [10, 9, 2, 5, 3, 7, 101, 18]`. A **subsequence** = pick some
> elements, in order, skipping freely. Find the length of the longest
> *increasing* one. (Here: `[2, 5, 7, 101]` or `[2, 3, 7, 18]` → 4.)

Real-life version: scanning a bookshelf left to right for the tallest
stack of books with strictly increasing heights — you may skip books,
but never reorder.

New state definition — note the "**ending at**":

```
dp[i] = length of the longest increasing subsequence ENDING at index i
```

Why "ending at" and not "up to i"? Because to extend a chain onto
`nums[i]`, what matters is chains that *end* somewhere before `i` with a
smaller last value. So:

```
dp[i] = 1 + max( dp[j] )   over all j < i where nums[j] < nums[i]
        (or just 1 if no such j — nums[i] starts its own chain)
```

**New shape alert:** `dp[i]` doesn't read `dp[i-1]`/`dp[i-2]` — it reads
**every** earlier cell. Two nested loops → O(n²).

## Watch the table fill

```
nums:    10   9   2   5   3   7   101  18
i:        0   1   2   3   4   5   6    7
          ────────────────────────────────
init:     1   1   1   1   1   1   1    1    every element: a chain of len 1
i=3:      1   1   1   2   .   .   .    .    5 can follow 2 → dp[2]+1 = 2
i=4:      1   1   1   2   2   .   .    .    3 can follow 2 → 2
i=5:      1   1   1   2   2   3   .    .    7 follows 2/5/3 → max(1,2,2)+1 = 3
i=6:      1   1   1   2   2   3   4    .    101 follows ALL → max(...)+1 = 4
i=7:      1   1   1   2   2   3   4    4    18 follows 2/5/3/7 → 3+1 = 4
Answer: max(dp) = 4
```

```python
def length_of_LIS(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)              # each element alone is a chain of 1
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)                    # NOT dp[-1]!
```

Verified: `length_of_LIS([10,9,2,5,3,7,101,18])` → 4,
`length_of_LIS([4,2,1,3])` → 2.

## Why it exists

It's the cleanest example of a state that needs **history, not just
neighbors** — the best chain onto `nums[i]` might end anywhere behind
you. It's also the classic demo that **the answer isn't `dp[n-1]`**: the
longest chain can end at *any* index, so you report `max(dp)`.

## Where it's used

`hard/p02`. LIS itself: patience-sorting tricks, scheduling, version
diffs. The "dp[i] = best chain ENDING at i" idiom reappears in Russian
doll envelopes, max-sum increasing subsequence, longest bitonic, etc.

## Common mistake

Returning `dp[-1]`. Try `nums = [2, 5, 1]` → `dp = [1, 2, 1]`; the LIS
is `[2,5]` ending at index 1, and `dp[-1] = 1` would wrongly answer 1.
The final cell only knows about chains ending at the *last* element —
the winner may have finished early. Always `max(dp)`.

## Your turn

`length_of_LIS([4, 2, 1, 3])` — write the dp row and the answer.

<details><summary>Answer</summary>
`dp = [1, 1, 1, 2]` → answer **2**. Nothing before index 3 is smaller
than 4/2/1... except: 3 can follow 2 (dp[1]) or 1 (dp[2]) → dp[3]=2.
Best chain: `[2,3]` or `[1,3]`.
</details>

---

**← Prev** [09 — Coin change](09-coin-change.md) ·
**Next →** [11 — Word break: can you reach?](11-word-break.md)
