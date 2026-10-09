# 02 — When Greedy FAILS (the famous coin trap)

> 5-minute read. The most important chapter in this lesson.

## The idea, plain words

Same vending machine, but the country minted weird coins: **`[1, 3, 4]`**.
Make change for **6**.

```
Greedy:  take the biggest coin first
         4  → remainder 2
         1  → remainder 1
         1  → remainder 0
         = 3 coins (4 + 1 + 1)

Optimal: 3 + 3 = 2 coins        ← greedy LOST
```

Greedy's very first move — grabbing the 4 — was locally best and globally
fatal. Taking it stranded the remainder 2, which only pennies can fill.

Same code, different coins, different verdict:

```python
def coin_change_greedy(coins, amount):
    coins = sorted(coins, reverse=True)
    count = 0
    for c in coins:
        count += amount // c    # take as many of c as possible
        amount %= c             # NEVER reconsider smaller splits
    return count if amount == 0 else -1
```

Run both and stare at the results:

| Amount | `[1,5,10,25]` greedy | Optimal | `[1,3,4]` greedy | Optimal |
|--------|----------------------|---------|------------------|---------|
| 6      | 5+1 = **2**          | 2 ✓     | 4+1+1 = **3**    | **2** ✗ |
| 12     | 10+1+1 = **3**       | 3 ✓     | 4+4+4 = **3**    | 3 ✓     |
| 8      | 5+1+1+1 = **4**      | 4 ✓     | 4+4 = **2**      | 2 ✓     |

`coin_change_greedy([1,5,10,25], 6)` → **2** ·
`coin_change_greedy([1,3,4], 6)` → **3** (wrong! optimal is 2).

Row 1 is the whole lesson. US coins happen to have a magic structure
(each coin ≥ ~2× the previous) that makes greedy safe. `[1,3,4]` doesn't.
**Greedy correctness lives in the problem, not the code.**

## Why it exists (as a warning)

Greedy code is short, which makes *wrong* greedy seductive — it compiles,
passes the two examples in the prompt, and dies on hidden test #47.
The interview question behind every greedy problem is really:
*"prove your local rule can't strand you."*

## Where it's used

This counterexample is the standard answer to "when is greedy wrong?":
coin change with weird denominations is THE textbook failure, and the fix
is DP — lesson 15's `coin_change` problem verbatim.

## Common mistake

Testing greedy only on the *canonical* input (US coins, sorted meetings)
and shipping. One weird denomination breaks the silent assumption.

## Your turn

`coin_change_greedy([1,3,4], 12)` returned 3 — was greedy wrong there too?

<details><summary>Answer</summary>
No — optimal IS 3 (4+4+4). Greedy isn't always wrong on `[1,3,4]`, just
*sometimes* — and "sometimes wrong" is exactly what makes it unusable.
You'd have to check every amount to trust it.
</details>

---

**← Prev** [01 — What "Greedy" Means](01-what-greedy-means.md) ·
**Next →** [03 — Greedy or DP?](03-greedy-or-dp.md)
