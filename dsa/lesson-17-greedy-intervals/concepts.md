# Lesson 17 — Concepts Explained (Greedy & Intervals)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What "Greedy" Means — and When It FAILS

**What:** A greedy algorithm makes the **locally-best choice at each step** — take the biggest cookie, the earliest-ending meeting, the farthest reachable index — and never looks back, never reconsiders. If a chain of locally-best choices provably lands on the globally-best answer, greedy works. That "provably" is the load-bearing word: greedy is not a technique, it's a *bet that your problem has a special property*.

**Why it exists:** The alternatives — trying every combination (exponential) or dynamic programming (correct but heavier) — cost a lot. When greedy is valid, you get the optimal answer in one sorted pass, usually O(n log n) from the sort alone. Interviews love greedy because the code is 10 lines but the *justification* is the real test.

**Where it's used:** Interval scheduling (which meetings to keep), resource allocation (cookies to children, machines to jobs), minimum coins/jumps/refuels, Huffman encoding, Kruskal's/Prim's spanning-tree algorithms (lesson 14 territory), job sequencing with deadlines.

**What goes wrong without it — the coin-change counterexample:**

Greedy is **not always optimal**, and believing it is will sink you. Making change for 6 with denominations `[1, 3, 4]`:

```
Greedy:  take the biggest coin first
         4  → remainder 2
         1  → remainder 1
         1  → remainder 0
         = 3 coins (4 + 1 + 1)

Optimal: 3 + 3 = 2 coins        ← greedy lost
```

Yet with US coins `[1, 5, 10, 25]`, greedy *is* optimal — the denominations happen to have the "greedy choice property" (each coin is at least double the previous, roughly). Same algorithm shape, different data, different verdict. **Greedy correctness lives in the problem, not the code.** When in doubt, the safe fallback is DP (lesson 15/16): slower, but always correct.

**Worked example — the difference in one table:**

| Amount | Coins `[1,5,10,25]` greedy | Optimal | Coins `[1,3,4]` greedy | Optimal |
|--------|--------------------------|---------|------------------------|---------|
| 6      | 5+1 = 2                  | 2 ✓     | 4+1+1 = 3              | **2** ✗ |
| 12     | 10+1+1 = 3               | 3 ✓     | 4+4+4 = 3              | 3 ✓     |
| 8      | 5+1+1+1 = 4              | 4 ✓     | 4+4 = 2                | 2 ✓     |

Row 1 is the whole lesson: greedy failed on `[1,3,4]` for amount 6.

```python
def coin_change_greedy(coins, amount):
    coins = sorted(coins, reverse=True)
    count = 0
    for c in coins:
        count += amount // c          # take as many of c as possible
        amount %= c                   # NEVER reconsider smaller splits
    return count if amount == 0 else -1
```

Expected outputs: `coin_change_greedy([1,5,10,25], 6)` → **2** · `coin_change_greedy([1,3,4], 6)` → **3** (wrong! optimal is 2) — same code, different coins, one failure.

---

## The Interval Pattern — sort, sweep, track "current"

**What:** Almost every interval problem collapses to three moves:

```python
intervals.sort(key=lambda iv: iv[KEY])   # KEY = 0 (start) or 1 (end)
current = <first interval / sentinel>
for iv in intervals[1:]:
    if iv overlaps/current-relates:
        update current
    else:
        commit current; current = iv
```

You **sort** to impose order on chaos, **sweep** left to right once, and carry a single `current` variable — the merged-so-far interval, the last-kept end time, the current reach — that summarizes everything you've decided so far.

**Why it exists:** Unsorted intervals are a tangle: `[8,10]` might overlap `[1,3]` through a chain of intermediates. Sorting makes overlap a *local* question — after sorting by start, if interval `i` doesn't overlap `i-1`, it can't overlap anything earlier either. That converts O(n²) pairwise comparisons into one linear pass.

**Where it's used:** Calendar applications (merging busy times), meeting-room allocation, CPU scheduling, genomics (merging overlapping gene ranges), network firewall rules, "can the person attend all meetings".

**What goes wrong without it:**
- Checking every pair of intervals for overlap → O(n²); times out at n = 10⁵.
- Sorting by **start** when the problem wants **end** (or vice versa) — see the next sections; the sort key IS the algorithm.
- Merging eagerly without finishing the current interval: `[1,10],[2,3],[4,5]` — after merging into `[1,10]`, intervals 2 and 3 are swallowed *inside* it; if you advance `current` per input interval instead of extending it, you double-count.

**The two sort orders, and what each buys you:**

| Sort by | Question it answers | Used in |
|---------|--------------------|---------|
| `iv[0]` start | "what comes next in time order?" | merge intervals, insert interval, meeting rooms |
| `iv[1]` end | "what frees up soonest?" | erase-min-overlaps, activity selection |

**Worked example — why sorting by start makes overlap local:**

```
Input:  [[8,10],[1,3],[2,6],[15,18]]
Sorted: [[1,3],[2,6],[8,10],[15,18]]

Sweep:  current=[1,3]
        [2,6]: 2 <= 3 overlaps → current=[1,6]
        [8,10]: 8 > 6 disjoint → commit [1,6]; current=[8,10]
        [15,18]: disjoint → commit [8,10]; current=[15,18]
Answer: [[1,6],[8,10],[15,18]]    — 3 comparisons, not 6 pairwise
```

---

## Merge & Insert — the "current interval" family

**What:** Merge takes a list of possibly-overlapping intervals and returns the minimal non-overlapping cover. Insert is merge's cousin: intervals arrive *already sorted and disjoint*, plus one new interval that must be slotted in — merging whatever it touches.

**Why it exists:** These are the canonical "sort + sweep + one running variable" problems. If you internalize this skeleton, half of all interval questions in interviews become transcription.

**Where it's used:** Calendar "free/busy" computation, collapsing version ranges, union of IP ranges, the insert variant appears when your calendar is maintained sorted and a new meeting arrives.

**What goes wrong without it:**
- Merge without sorting first: `[[2,6],[1,3]]` — you'd emit `[2,6]` then fail to merge `[1,3]` backward.
- Insert by "merge everything anyway" — works but wasteful; the clean version walks three phases: (1) intervals entirely **before** the new one, (2) intervals **overlapping** it (absorb and grow), (3) intervals entirely **after**.
- The classic insert bug: comparing `iv.end < new.start` when you meant `<=` — decide whether touching endpoints `[1,3]+[3,5]` merge (they do: overlap means `iv.start <= new.end`, not `<`).

**Worked example — merge:**

```
intervals = [[1,3],[2,6],[8,10],[15,18]]   sorted by start
merged = []
[1,3] → merged=[[1,3]]
[2,6] → 2 <= 3 overlap → extend top: [[1,6]]
[8,10] → 8 > 6 new → [[1,6],[8,10]]
[15,18] → new → [[1,6],[8,10],[15,18]]
```

**Worked example — insert `newInterval=[4,8]` into `[[1,2],[3,5],[6,7],[8,10],[12,16]]`:**

```
Phase 1 (before):  [1,2] ends 2 < 4 → output it
Phase 2 (overlap): [3,5],[6,7],[8,10] all start <= 8 → absorb → new=[3,10]
                   [12,16] starts 12 > 10 → stop
Phase 3 (after):   [12,16] → output it
Result: [[1,2],[3,10],[12,16]]
```

```python
def merge(intervals):
    intervals = sorted(intervals)          # by start
    merged = []
    for s, e in intervals:
        if merged and s <= merged[-1][1]:  # overlaps the top interval
            merged[-1][1] = max(merged[-1][1], e)   # extend, don't append
        else:
            merged.append([s, e])
    return merged
```

Expected output for `merge([[1,3],[2,6],[8,10],[15,18]])`: **[[1,6],[8,10],[15,18]]**

---

## Activity Selection — sort by END, keep what fits

**What:** "Remove the fewest intervals so nothing overlaps" is the same question as "keep the *most* non-overlapping intervals." And the greedy that solves it is famous: **sort by end time; repeatedly take the interval that ends earliest and doesn't clash with what you kept.** Earliest-ending first leaves the most room for everything after — that's the provable part.

**Why it exists:** Sorting by *start* doesn't work here — a long early-starting meeting blocks the whole afternoon. Sorting by *end* is optimal: any optimal schedule's first meeting can be swapped for the earliest-ending one without making things worse (it only frees time). This "exchange argument" is THE standard greedy proof shape.

**Where it's used:** Booking maximum meetings in one room, minimum deletions, choosing max non-overlapping jobs, "how many intervals can I attend" variants.

**What goes wrong without it:**
- Sorting by start: `[[1,10],[2,3],[3,4]]` keeps the 9-hour meeting and loses the other two → keeps 1, optimal is 2.
- Sorting by length: shortest-first can straddle two compatible ones.
- Comparing `s < prev_end` vs `s <= prev_end`: touching endpoints `[1,2],[2,3]` do NOT overlap — a meeting can start when another ends.

**Worked example — `[[0,2],[1,3],[2,4],[3,5],[4,6]]`, minimize removals:**

```
Sort by end:  [0,2] [1,3] [2,4] [3,5] [4,6]
Keep [0,2]  (last_end = 2)
[1,3]: starts 1 < 2  → DROP (overlaps kept interval)
[2,4]: starts 2 >= 2 → KEEP (last_end = 4)
[3,5]: starts 3 < 4  → DROP
[4,6]: starts 4 >= 4 → KEEP (last_end = 6)
Kept: 3 → answer = 5 - 3 = 2 removals
```

```python
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda iv: iv[1])   # earliest END first — the trick
    kept, last_end = 0, float("-inf")
    for s, e in intervals:
        if s >= last_end:                  # no overlap with last kept
            kept += 1
            last_end = e
    return len(intervals) - kept
```

Expected output for `erase_overlap_intervals([[0,2],[1,3],[2,4],[3,5],[4,6]])`: **2**

---

## Reach-Tracking Greedy — Jump Game & Gas Station

**What:** A second greedy family with no sorting at all. You carry one variable — `reach`, `tank`, `boundary` — that summarizes "how far my decisions so far can take me," then scan once, updating it greedily.

- **Jump Game (can I reach the end?):** `reach` = farthest index reachable. For each `i <= reach`, extend `reach = max(reach, i + nums[i])`. If some `i > reach` before the end — you're stranded → `False`.
- **Jump Game II (minimum jumps):** track `end_of_current_jump` — the farthest you can get with the jumps used so far — and `farthest` — the farthest reachable with one more. When `i` hits the boundary, you MUST spend a jump.
- **Gas Station:** if total gas < total cost, impossible (`-1`). Otherwise: drive, and whenever `tank` goes negative, the answer can't be any station in the failed stretch — restart the candidate at `i + 1`. One pass decides both feasibility and the start.

**Why it exists:** The "how far can my current budget stretch" framing turns quadratic simulation (try every start, try every jump sequence) into O(n). The greedy bet: locally extending reach as far as possible never hurts — a shorter reach is dominated by a longer one.

**Where it's used:** Jump/reach problems, refueling/leap scheduling, network hop problems, game-move reachability.

**What goes wrong without it:**
- Jump Game: simulating actual jump paths → exponential/DP territory. The insight is you don't care *which* jumps — only the max reach they afford.
- Jump II: incrementing `jumps` every index instead of only when `i` crosses the current boundary — overcounts.
- Gas Station: trying every start O(n²); or the subtle invariant — if you fail between `start` and `i`, **no station in `[start..i]` can work either** (you'd arrive there with ≤ 0 tank and face the same deficit). Skipping the whole failed block is what makes it O(n).

**Worked example — Jump Game `nums = [3,2,1,0,4]`:**

```
i=0: i<=reach(0) ✓  reach = max(0, 0+3) = 3
i=1: 1<=3 ✓        reach = max(3, 1+2) = 3
i=2: 2<=3 ✓        reach = max(3, 2+1) = 3
i=3: 3<=3 ✓        reach = max(3, 3+0) = 3
i=4: 4 > 3  → STRANDED → False     (the 0 at index 3 is a wall)
```

**Worked example — Jump Game II `nums = [2,3,1,1,4]`:**

```
jumps=0, boundary=0, farthest=0
i=0: farthest=2; i==boundary → jumps=1, boundary=2   (jump #1 committed)
i=1: farthest=max(2,4)=4
i=2: i==boundary → jumps=2, boundary=4               (jump #2 committed)
i=4 is the last index, inside jump 2 → answer 2
```

```python
def can_jump(nums):
    reach = 0
    for i, x in enumerate(nums):
        if i > reach:
            return False          # can't even stand here
        reach = max(reach, i + x)
    return True
```

Expected output for `can_jump([2,3,1,1,4])`: **True** · `can_jump([3,2,1,0,4])`: **False**

---

## Sanity-Checking a Greedy Idea BEFORE You Code It

**What:** Greedy code is short, which makes wrong greedy *seductive*. The skill: spend 2 minutes trying to **break your rule** on tiny inputs before writing anything.

**The checklist:**

1. **State your rule in one sentence.** "Always take the earliest-ending interval." If you can't say it plainly, you don't have a greedy — you have a vibe.
2. **Write the smallest possible counterexample hunt.** n = 2–4 elements, a dozen hand cases. You're looking for *one* input where the local choice diverges from the global optimum.
3. **Try the exchange argument.** Can any optimal solution's first choice be swapped for your greedy choice without making it worse? For activity selection: yes (earlier end frees more room). For coin change `[1,3,4]`: no (swapping `3+3` for `4` makes it worse).
4. **Check structural assumptions.** Greedy on intervals needs sorted input. Reach-greedy on Jump Game needs non-negative jumps. If the input can violate it, handle or reject.
5. **When it breaks, don't force it** — pivot to DP (min-coin-change), binary-search-the-answer (lesson 9), or exhaustive-with-pruning.

**Why it exists:** In an interview, stating the greedy rule + one sentence of justification + admitting you'd switch to DP if the rule breaks is worth more than silently coding a wrong greedy.

**What goes wrong without it:** You code the intuitive greedy, it passes the 2 examples in the prompt, fails hidden test #47, and debugging means re-deriving correctness anyway — the counterexample hunt you skipped.

**Worked counterexample hunt — "is longest-first a valid rule for erase-overlaps?":**

```
Rule candidate: keep longest intervals first.
Try [[1,10],[2,3],[4,5]]:  keep [1,10] → must drop both small ones = 2 removals.
                         optimal: keep [2,3],[4,5] → drop only [1,10] = 1 removal.
Rule broken in ONE 3-interval input → reject, use sort-by-end.
```

That's the whole technique: 30 seconds of small inputs killed a wrong algorithm before it was written.

---

## The Recipe — recognize it in 10 seconds

1. **Intervals involved?** → sort (by start for merge/insert/meeting-check, by end for keep-max-non-overlapping), sweep once, track `current`/`last_end`.
2. **"Minimum/maximum count of choices" on a line?** → reach-tracking greedy (jump, gas, refuel).
3. **"Satisfy as many as possible" (kids/cookies, jobs/machines)?** → sort both lists, pair smallest-need with smallest-sufficient-resource.
4. **Can't prove the greedy?** → coin-change trap: say so, and use DP instead.

Complexity to say out loud: **O(n log n)** for the sort, **O(n)** sweep; **O(1)** extra space (besides output).

---

## The Pitfall Gallery — six ways greedy goes wrong

**1. Wrong sort key.** Sort-by-start on an activity-selection problem is the #1 greedy bug. Ask: does the decision depend on when things *begin* (order processing) or when they *free resources* (earliest end)?

**2. `<=` vs `<` at boundaries.** Intervals `[1,3]` and `[3,5]` — overlapping or adjacent? Merge/overlap problems treat touching as mergeable (`s <= prev_end`); scheduling treats end==start as compatible (`s >= last_end`). Pick deliberately.

**3. Greedy where DP belongs.** Coin change with weird denominations, "minimum cost with carryover constraints." If a locally-best pick can strand you, it's DP.

**4. Mutating while iterating.** `intervals.sort()` then popping from it inside the same loop — build a `merged` output list instead.

**5. Forgetting feasibility.** Gas station with `total < 0` → `-1`, not a wrong index. Jump Game on `[0]` → `True` (already at the end). Always handle the empty/single/impossible case.

**6. Optimizing the wrong objective.** "Min jumps" ≠ "max reach per position." Jump-II's boundary variable is the trick — a plain max-reach pass answers *reachability*, not *count*.

**Edge cases to always test:** empty list, single interval/element, all-disjoint, all-overlapping (`[[1,10],[2,3],[4,5]]` merges to one), touching endpoints, negative coordinates, and guaranteed-unreachable inputs (`[3,2,1,0,4]`).
