# 10 — Interval DP: Pick the LAST Move, Not the First

> 7-minute read. The hardest shape in the lesson — the trick is one word.

## The idea, plain words

Balloons in a row: `[3, 1, 5, 8]`. Bursting balloon `k` pays
`left_neighbor × k × right_neighbor` coins — but its neighbors are whatever
is still alive, which changes as you burst. Maximize total coins.

Try "**burst the best one first**" and the problem fights back: after
bursting `k`, the two sides *merge* — your first choice changes every later
payment. The halves aren't independent.

The trick, in one word: **LAST.** Pick which balloon between two *walls*
`i` and `j` is burst **last**. By then, everything between is gone — its
neighbors are the walls, fixed. And the two halves (`i..k` and `k..j`) were
already fully solved. Independent. That's a valid DP.

The sentence: **`dp[i][j]` = max coins bursting all balloons strictly
between walls `i` and `j`.** Pad the array with `1`s on both ends — they
are the outer walls.

```
dp[i][j] = max over k in (i, j):
               nums[i] * nums[k] * nums[j]   ← k pops LAST, walls i and j
             + dp[i][k] + dp[k][j]           ← the two halves, already solved
```

## Mini trace — `nums = [3, 1, 5]`, padded `[1, 3, 1, 5, 1]`

Fill by **interval length** — small gaps before big ones (a cell reads
*smaller* intervals on both sides).

```
length 2 (one balloon inside):
  dp[0][2]: k=1 → 1·3·1 = 3        dp[1][3]: k=2 → 3·1·5 = 15
  dp[2][4]: k=3 → 1·5·1 = 5
length 3 (two inside):
  dp[0][3]: k=1 → 1·3·5 + dp[1][3]=15 → 30     '3' pops last → wins
            k=2 → 1·1·5 + dp[0][2]=3  → 8      '1' pops last → worse
  dp[1][4]: k=3 → 3·5·1 + dp[1][3]=15 → 30     '5' pops last → wins
length 4 (all three inside):
  dp[0][4]: k=1 → 1·3·1 + dp[1][4]=30 → 33
            k=2 → 1·1·1 + dp[0][2]+dp[2][4]=3+5 → 9
            k=3 → 1·5·1 + dp[0][3]=30 → 35       ← WINNER: '5' pops last
```

Answer: `dp[0][4] = 35`. Sanity check — burst order `1, 3, 5`:
`3·1·5=15` → `[3,5]` → `1·3·5=15` → `[5]` → `1·5·1=5`. Total `35`. ✓
The DP found it by asking "what pops *last*" at each level.

## Why "last" and not "first" — the whole point

Choosing `k` first entangles the halves: who bursts next changes `k`'s
neighbors retroactively. Choosing `k` last *decouples* them — the walls
`i,j` are guaranteed present when `k` finally pops. Any problem where
"the cost of a move depends on what's left" wants this reversed thinking:
**palindrome partitioning, matrix-chain multiplication, optimal BSTs.**

## Fill order — by length, not by row

```
for length in 2..n:              # gap size grows
    for i in 0..n-length:
        j = i + length
        dp[i][j] = best over k in (i,j)
```

Row-major order would read unwritten cells — interval cells need *smaller*
intervals, which live diagonally, not above-left. Different arrows,
different order. Check your arrows before choosing the loops.

## The code

```python
def max_coins(nums):
    arr = [1] + nums + [1]              # outer walls
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):          # interval size: small → big
        for i in range(n - length):
            j = i + length
            for k in range(i + 1, j):   # k = balloon burst LAST
                dp[i][j] = max(dp[i][j],
                               arr[i] * arr[k] * arr[j]
                               + dp[i][k] + dp[k][j])
    return dp[0][n - 1]
```

Verified: `max_coins([3,1,5])` → `35` · `max_coins([3,1,5,8])` → `167`.

## Where it's used

Burst balloons (`hard/p03`), palindrome partitioning / longest palindromic
subsequence (interval `[i][j]` = "inside this range"), matrix-chain
multiplication, optimal BST — any "best order of operations" problem.

## Common mistake

Forgetting the padding `1`s — or writing the recurrence as "first pick" and
wondering why the halves overlap. If your subproblems share elements, your
pick is in the wrong direction.

## Your turn

Why does the answer live at `dp[0][n-1]` and not bottom-right `dp[n-1][n-1]`?

<details><summary>Answer</summary>
The two indices mean *wall positions*, not "first i" / "first j". The whole
problem is "burst everything between the outer walls" — wall `0` (the left
padding `1`) and wall `n-1` (the right padding `1`). The answer is the
biggest interval's cell, which happens to be a corner, not the diagonal.
</details>

---

**← Prev** [09 — Wildcard matching](09-wildcard-matching.md) ·
**Next →** [11 — The pitfall gallery](11-the-pitfall-gallery.md)
