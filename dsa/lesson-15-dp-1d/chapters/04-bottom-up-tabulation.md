# 04 — Bottom-Up: skip the recursion, fill a table

> 6-minute read. The second way to "remember" — and the one interviews love.

## The idea, plain words

Top-down (ch.02) starts at the big question and digs down. **Bottom-up**
flips it: start with the answers you already know (`fib(0)`, `fib(1)`),
then build up one small step at a time until you reach the target.

Real-life version: instead of "to answer fib(7) I need fib(6), for which
I need fib(5)…" you just write the sequence on a line, left to right:
0, 1, then each next number = sum of the previous two. You did this as a
kid. **That left-to-right writing IS bottom-up DP.** The notebook becomes
a row of boxes — the `dp` array.

```python
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)          # the row of boxes, dp[i] = fib(i)
    dp[1] = 1                   # base cases
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]   # same rule as the recursion!
    return dp[n]
```

## Watch the table fill — fib(7), cell by cell

```
i:      0   1   2   3   4   5   6   7
        ─────────────────────────────
init:   0   1   _   _   _   _   _   _      base cases
i=2:    0   1   1   _   _   _   _   _      dp[2] = dp[1]+dp[0] = 1+0
i=3:    0   1   1   2   _   _   _   _      dp[3] = dp[2]+dp[1] = 1+1
i=4:    0   1   1   2   3   _   _   _      dp[4] = dp[3]+dp[2] = 2+1
i=5:    0   1   1   2   3   5   _   _      dp[5] = 3+2
i=6:    0   1   1   2   3   5   8   _      dp[6] = 5+3
i=7:    0   1   1   2   3   5   8   13     dp[7] = 8+5  ← answer at dp[n]
```

Read the trace slowly. Each cell **only ever reads cells to its left** —
that's why one forward `for` loop is a legal fill order. Verified output:
`fib(7)` → 13, `fib(10)` → 55.

## Top-down vs bottom-up — same answer, two directions

| | Top-down (memo) | Bottom-up (table) |
|---|---|---|
| Start at | the answer, recurse down | base cases, loop up |
| Storage | dict / `@lru_cache` | list `dp` |
| Stack | recursion depth n (limit risk!) | none — just a loop |
| Computes | only states it reaches | every state, always |
| Feels like | "write recursion, add 2 lines" | "fill a spreadsheet row" |

## Why it exists

Three practical wins: **no recursion-limit crash** (try top-down
`fib(10000)` — Python's stack dies around depth ~1000), a hair less
overhead per answer, and — this matters later — the explicit table is
what lets you **shrink the memory** (ch.12).

## Where it's used

Everywhere DP appears in production code. In interviews, top-down is
acceptable; bottom-up signals mastery. Most "real" DP solutions you see
online are bottom-up tables.

## Common mistake

**Wrong fill order.** If `dp[i]` reads `dp[i-1]` but your loop runs `i`
from high→low, every cell reads a not-yet-filled `0`. Rule: loop in the
direction the arrows point away from — dependencies first, dependents
after. For 1D recurrences reading earlier cells: loop `i` ascending.

## Your turn

In the table code above, what would go wrong if you wrote
`for i in range(n, 1, -1)` (counting down)?

<details><summary>Answer</summary>
`dp[i]` reads `dp[i-1]` and `dp[i-2]`, which haven't been filled yet —
they're still 0. Every cell computes `0+0=0`, and `fib(7)` returns 0.
Fill order must match the dependency direction.
</details>

---

**← Prev** [03 — When does DP apply?](03-when-does-dp-apply.md) ·
**Next →** [05 — Climbing stairs](05-climbing-stairs.md)
