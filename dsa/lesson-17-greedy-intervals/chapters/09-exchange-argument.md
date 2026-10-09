# 09 — The Exchange Argument: why greedy is *provable*

> 5-minute read. The proof shape behind every correct greedy.

## The idea, plain words

How do you *prove* a greedy rule is optimal — not just "it seems right"?
One trick covers almost all of them: the **exchange argument**.

> Take any optimal solution. **Swap** its first choice for the greedy
> choice. If the swap never makes things worse, greedy's first move is
> safe — and you repeat the argument for every move after.

Picture it for activity selection (chapter 6). Some optimal schedule picks
first meeting `X`. Greedy picks `G`, the earliest-ending of ALL meetings:

```
OPT's first pick:  X  ████████       ends at 8
Greedy's pick:     G  ███            ends at 3
                          ────────────→ time
Swap X → G:  G ends EARLIER → strictly more room for whatever OPT picked
             next. The swap can only help, never hurt. → greedy safe ✓
```

Now compare with the coin trap: swap OPT's `3+3` for greedy's `4` →
remainder 2 needs two pennies → **the swap made it worse** → exchange
fails → greedy illegal. Same test, different verdicts.

## Watch the proof survive 300 random attacks

Can't run a formal proof? Do the next best thing — pit greedy against
brute force on hundreds of tiny inputs:

```python
import itertools, random

def greedy_kept(intervals):                     # sort-by-end greedy
    kept, last_end = 0, float("-inf")
    for s, e in sorted(intervals, key=lambda iv: iv[1]):
        if s >= last_end:
            kept += 1; last_end = e
    return kept

def brute_kept(intervals):                      # try EVERY subset
    best = 0
    for r in range(len(intervals) + 1):
        for combo in itertools.combinations(intervals, r):
            ok = all(combo[i][1] <= combo[j][0] or combo[j][1] <= combo[i][0]
                     for i in range(len(combo)) for j in range(i + 1, len(combo)))
            if ok:
                best = max(best, len(combo))
    return best

random.seed(0)
bad = 0
for _ in range(300):                            # 300 random tiny inputs
    ivs = [(a := random.randint(0, 15), a + random.randint(1, 8))
           for _ in range(random.randint(1, 6))]
    bad += greedy_kept(ivs) != brute_kept(ivs)
print(bad)      # → 0  — greedy matched brute force EVERY time
```

Output: `0` mismatches. That's the exchange argument made visible — the
swap never hurt, so greedy never lost, on any of 300 inputs.

## Why it exists

In an interview, "sort by end and sweep" is worth little alone. "Greedy
works because swapping any optimal first pick for the earliest-ending
meeting only frees more room — exchange argument" is the answer that
lands. Same test kills wrong greedies: if you can find ONE input where
the swap hurts, the rule is dead.

## Where it's used

- Activity selection ✓ (swap frees time)
- Huffman encoding, Kruskal/Prim (lesson 14) — same swap shape
- Coin change `[1,3,4]` ✗ (swap strands the remainder → fails → DP)

## Common mistake

Proving a different, easier statement. "Earliest end is a good heuristic"
≠ "swapping never hurts." The claim is about the *optimal* solution's
choice, not about what's intuitive.

## Your turn

Rule candidate: "keep the SHORTEST meeting first." Does the exchange
argument save it or kill it?

<details><summary>Answer</summary>
**Kills it.** `[[1,5],[4,6],[5,9]]` — shortest is `[4,6]` (len 2), but it
straddles the boundary: keep it and BOTH `[1,5]` and `[5,9]` clash →
kept 1. Optimal keeps `[1,5]` + `[5,9]` = 2. The swap fails — `[4,6]`
ends LATER than `[1,5]`, so exchanging the optimal's first pick blocks
its second. One 3-interval input killed the rule.
</details>

---

**← Prev** [08 — Insert & Meeting Rooms](08-insert-and-meeting-rooms.md) ·
**Next →** [10 — Reach-Tracking Greedy](10-reach-tracking.md)
