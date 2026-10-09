# 06 — The 5-Step Recipe: every 1D DP, same checklist

> 7-minute read. The most important chapter — bookmark it.

## The idea, plain words

Every DP problem in this lesson reduces to answering **five questions, in
order**. Memorize the list, then watch it solve a brand-new problem live.

1. **Define `dp[i]` in one sentence.** If you can't say it in one
   sentence, you don't have a state yet.
2. **Write the recurrence.** How does `dp[i]` come from earlier cells?
   (Usually: think about the last move / the last choice.)
3. **Base cases.** The cells filled by hand, no recurrence needed.
4. **Fill order.** Which loop direction guarantees dependencies are
   ready before dependents?
5. **Answer location.** Which cell holds the final answer? (NOT always
   `dp[n-1]` — this is the most-forgotten step.)

## Apply it live — Tribonacci

> `T(0)=0, T(1)=1, T(2)=1`, and `T(n) = T(n-1)+T(n-2)+T(n-3)`.
> Find `T(n)`.

Walk the recipe out loud:

- **Step 1, state:** "`dp[i]` = the i-th tribonacci number." One
  sentence ✓
- **Step 2, recurrence:** given to us: `dp[i] = dp[i-1]+dp[i-2]+dp[i-3]`.
- **Step 3, base cases:** `dp[0]=0`, `dp[1]=1`, `dp[2]=1` — these don't
  need the formula.
- **Step 4, fill order:** reads `i-1`, `i-2`, `i-3` — all to the left →
  loop `i` ascending from 3.
- **Step 5, answer:** `dp[n]` directly.

## Watch the table fill — T(6)

```
i:      0   1   2   3   4   5   6
        ─────────────────────────
init:   0   1   1   _   _   _   _     base cases
i=3:    0   1   1   2   _   _   _     dp[3] = 1+1+0 = 2
i=4:    0   1   1   2   4   _   _     dp[4] = 2+1+1 = 4
i=5:    0   1   1   2   4   7   _     dp[5] = 4+2+1 = 7
i=6:    0   1   1   2   4   7   13    dp[6] = 7+4+2 = 13
Answer: dp[6] = 13
```

```python
def tribonacci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1                    # T(1) = T(2) = 1
    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1               # dp[0] already 0
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]
```

Verified: `tribonacci(4)` → 4, `tribonacci(6)` → 13,
`tribonacci(25)` → 1389537.

## Why it exists

DP feels like magic until you notice it's **clerical work**: name the
cell, name the rule, name the seeds, name the direction, name the exit.
The recipe turns "I don't know where to start" into "start at step 1."

## Where it's used

All nine problems in this lesson. Print the 5 steps on a sticky note;
for every problem, write all five answers in comments BEFORE coding.

## Common mistake

Skipping to step 2. Beginners hunt for "the formula" before they can say
what `dp[i]` *means*. A recurrence without a state definition is how you
end up with a formula that computes something-but-not-what-you-need.

## Your turn

Next problem (ch.07): a row of houses with money inside; robbing two
*adjacent* houses triggers an alarm. Maximize loot. Do ONLY step 1:
write `dp[i]` in one sentence.

<details><summary>Answer</summary>
"`dp[i]` = the maximum money I can get robbing houses `0..i`." (Or
equivalently, "...considering the first i+1 houses.") If yours said
something like "max money ending at i," that's fine too — just be sure
you could fill it left to right.
</details>

---

**← Prev** [05 — Climbing stairs](05-climbing-stairs.md) ·
**Next →** [07 — House robber](07-house-robber.md)
