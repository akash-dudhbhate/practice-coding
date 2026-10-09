# 01 — What "Greedy" Means

> 4-minute read. One idea only.

## The idea, plain words

A **greedy algorithm** always grabs the **best-looking option right now** —
and never goes back to reconsider.

Real-life version: **a vending machine giving change.** Owe you 41 cents?
It doesn't plan clever coin combos. It just does:

- biggest coin that fits → quarter (16 left)
- biggest that fits → dime (6 left)
- biggest that fits → nickel (1 left)
- biggest that fits → penny (done)

Four coins, no thinking ahead, and — for US coins — it's actually optimal.

```python
def make_change(amount):
    coins = [25, 10, 5, 1]      # biggest first — the greedy order
    used = []
    for c in coins:
        while amount >= c:      # take coin c as many times as it fits
            used.append(c)
            amount -= c         # never reconsider a smaller split
    return used
```

`make_change(41)` → `[25, 10, 5, 1]` · `make_change(30)` → `[25, 5]`.
One pass, top coin down, done. That *is* the whole shape of greedy:
**sort by "best", walk once, commit, never look back.**

## Why it exists

The careful alternatives are expensive. Trying every coin combination is
exponential; dynamic programming (lesson 15/16) is correct but heavier.
When greedy is *legal*, you get the optimal answer in one pass —
usually `O(n log n)`, and that's just the sort. Interviews love greedy
because the code is 10 lines but the **justification** is the real test.

## Where it's used

- Interval scheduling — which meetings to keep (most of this lesson!)
- Resource allocation — cookies to children, machines to jobs
- Minimum coins / jumps / refuels
- Huffman encoding, Kruskal's & Prim's spanning trees (lesson 14)

## Common mistake

Believing "greedy = always right." It's not a technique — it's a **bet
that your problem has a special property**. For US coins the bet wins.
The next chapter shows a tiny case where the exact same code loses.

## Your turn (30 seconds)

`make_change(17)` — what list comes back, and how many coins?

<details><summary>Answer</summary>
`[10, 5, 1, 1]` — 4 coins. Greedy takes the dime, then nickel, then two
pennies. (Optimal too — for US coins it always is.)
</details>

---

**Next →** [02 — When Greedy FAILS](02-when-greedy-fails.md)
