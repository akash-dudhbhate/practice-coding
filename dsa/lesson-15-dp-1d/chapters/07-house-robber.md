# 07 — House Robber: the take-it-or-skip-it choice

> 6-minute read. First "min/max" problem — and a constraint that changes everything.

## The idea, plain words

> Houses in a row hold `[2, 7, 9, 3, 1]` dollars. Rob any houses you
> want — but **never two adjacent ones** (the alarm trips). Max loot?

Real-life version: a street of free-sample stands where taking a sample
at one stand means the next stand's vendor recognizes you. Take it or
skip it — but never twice in a row.

At each house you face a **choice of two**. Standing at house `i`:

- **Rob it** → collect `nums[i]`, but then house `i-1` was forbidden →
  your total is `nums[i] + dp[i-2]`
- **Skip it** → collect nothing here → your total is whatever `dp[i-1]` was

Take the better option. That's the recurrence:

```
dp[i] = max( dp[i-1],  nums[i] + dp[i-2] )
            └─ skip ─┘  └──── rob ────┘
```

## Run the recipe (ch.06)

- **State:** `dp[i]` = max loot using houses `0..i`.
- **Recurrence:** `max(dp[i-1], nums[i] + dp[i-2])` as above.
- **Base cases:** `dp[0] = nums[0]` (only choice); `dp[1] = max(nums[0], nums[1])` (can't take both).
- **Fill order:** reads `i-1`, `i-2` → ascending.
- **Answer:** `dp[n-1]`.

## Watch the table fill — nums = [2, 7, 9, 3, 1]

```
house:    2   7   9   3   1
i:        0   1   2   3   4
          ─────────────────
init:     2   7   _   _   _    dp[0]=2, dp[1]=max(2,7)=7
i=2:      2   7   11  _   _    max(7, 9+2)=11    rob houses {0,2}
i=3:      2   7   11  11  _    max(11, 3+7)=11   skip house 3
i=4:      2   7   11  11  12   max(11, 1+11)=12  rob {0,2,4}
Answer: dp[4] = 12
```

```python
def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
    return dp[n - 1]
```

Verified: `rob([2,7,9,3,1])` → 12, `rob([1,2,3,1])` → 4 (houses 0 and 2).

## Why it exists

Stairs had *no forbidden combinations* — every path was legal. The
"no two adjacent" constraint is what forces the **choice**: the
recurrence can't just sum, it must `max` over rob-vs-skip. This
take-or-skip pattern is the backbone of half the DP problems you'll meet.

## Where it's used

`medium/p01` here. In the wild: any "pick items, no two adjacent"
problem — house robber II (circular), delete-and-earn, max-sum
non-adjacent subsequence.

## Common mistake

Writing `dp[i] = nums[i] + dp[i-2]` alone — always robbing. The `max`
with the skip-case `dp[i-1]` is the whole point: sometimes the best move
at house `i` is to leave it alone (like house 3 above, worth only 3 —
skipping kept our 11).

## Your turn

`rob([2, 1, 1, 2])` — trace the table in your head, give the answer.

<details><summary>Answer</summary>
`dp = [2, 2, 3, 4]` → answer **4**. dp[0]=2, dp[1]=max(2,1)=2,
dp[2]=max(2, 1+2)=3, dp[3]=max(3, 2+2)=4 → rob houses 0 and 3.
</details>

---

**← Prev** [06 — The 5-step recipe](06-the-five-step-recipe.md) ·
**Next →** [08 — Min-cost stairs](08-min-cost-climbing-stairs.md)
