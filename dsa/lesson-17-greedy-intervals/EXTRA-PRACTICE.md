# lesson-17-greedy-intervals — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: Greedy or not?

For each problem, say whether a simple greedy works or you need DP/exhaustive:

1. Making 41 cents with coins `[1, 5, 10, 25]`.
2. Making 6 with coins `[1, 3, 4]`.
3. Maximum non-overlapping meetings in one room.
4. Minimum interval deletions to remove all overlap.
5. Minimum coins `[2, 5, 7]` to make an arbitrary amount.

<details><summary>Answer</summary>

1. GREEDY works (canonical US coins): 25+10+5+1 = 41.
2. FAILS — greedy gives 4+1+1 = 3 coins, optimal is 3+3 = 2 → DP.
3. GREEDY — sort by end (activity selection).
4. GREEDY — same problem as 3 in disguise (keep max non-overlapping).
5. FAILS in general — e.g. amount 4 is fine (2+2) but amounts exist where biggest-first strands you; there's no greedy-choice property → DP.
</details>

---

## Check 02: Which sort key?

For "minimum removals so no two intervals overlap" on `[[1,4],[3,5],[0,6],[5,7],[8,9],[5,9]]` — which sort key, and what answer?

<details><summary>Answer</summary>

Sort by **end**. Sorted: `[1,4] [3,5] [0,6] [5,7] [8,9] [5,9]`.
Keep `[1,4]` (last_end=4) → `[3,5]` starts 3 < 4 drop → `[0,6]` drop → `[5,7]` keep (last_end=7) → `[8,9]` keep (last_end=9) → `[5,9]` drop.
Kept 3 → removals = **3**.

Sanity-check the wrong key: sort by start and keep-first would keep `[0,6]` — a giant blocker — then `[8,9]` only → kept 2, removals 4. Wrong sort key = wrong answer.
</details>

---

## Check 03: Trace the boundary

`nums = [2,3,0,1,4]` — for Jump Game II, how many times does the `i == boundary` line fire, and at which `i`?

<details><summary>Answer</summary>

**Twice — at i=0 and i=1.**

- i=0: `farthest = max(0, 0+2) = 2`; `i == boundary(0)` → `jumps = 1`, `boundary = 2`.
- i=1: `farthest = max(2, 1+3) = 4`; not at boundary yet (1 < 2).
- i=2: `i == boundary(2)` → `jumps = 2`, `boundary = 4`.

Wait — recount: boundary after first fire is 2, so the second fire is at **i=2**, not i=1. Fires at **i=0 and i=2** → `jumps = 2`. The loop only runs to `n-2 = 3`, and index 4 is already inside jump #2's reach.
</details>

---

## Check 04: Does greedy break here?

Your rule for gas station: "when `tank < 0`, restart the candidate at `i+1`." On `gas=[6,1,1,1,2], cost=[1,6,1,1,1]` — trace it: what does the algorithm return, and is it right?

<details><summary>Answer</summary>

Diffs: `[+5,-5,0,0,+1]`. i=0: tank=5. i=1: tank=0. i=2: tank=0. i=3: tank=0. i=4: tank=1. `tank` never went negative → `start` stays **0**. Total = 1 ≥ 0 → answer `0`.

Verify manually: start at 0, tank: 6-1=5 → +1-6=0 → +1-1=0 → +1-1=0 → +2-1=1 ✓ completes. Correct.
The rule only moves `start` on an actual deficit — a near-zero tank is still a valid start.
</details>

---

## Check 05: What does this print?

```python
intervals = [[1,2],[2,3],[1,3],[3,4]]
intervals.sort(key=lambda iv: iv[0])       # sort by START — wrong key on purpose
kept, last_end = 0, float("-inf")
for s, e in intervals:
    if s >= last_end:
        kept += 1
        last_end = e
print(len(intervals) - kept)
```

<details><summary>Answer</summary>

Sorted by start: `[1,2] [1,3] [2,3] [3,4]`. Keep `[1,2]` (end=2) → `[1,3]` s=1<2 drop → `[2,3]` keep (end=3) → `[3,4]` keep (end=4). Kept 3 → prints **1**.

Coincidentally correct here (sort-by-end gives the same 1: `[1,2] [2,3] [1,3] [3,4]` → keep `[1,2]`, drop `[1,3]`... wait sort-by-end order: `[1,2] [2,3] [1,3] [3,4]` — ends 2,3,3,4; keep `[1,2]`, `[2,3]`, drop `[1,3]`, keep `[3,4]` → also 1). Small inputs can HIDE a wrong sort key — try `[[1,10],[2,3],[4,5]]`: sort-by-start keeps `[1,10]` only (removals 2, wrong); sort-by-end keeps `[2,3],[4,5]` (removals 1, right). This is why you hunt counterexamples on inputs where a *long early* interval exists.
</details>

---

## Debug Exercises — find and fix the bug

> Fix the broken code. Find bugs mentally before running.

---

## Debug 01 (Easy): Merge — not sorting, wrong overlap test

```python
def merge(intervals):
    merged = []
    for s, e in intervals:                 # BUG: never sorted
        if merged and s < merged[-1][1]:   # BUG: < excludes touching
            merged[-1][1] = e              # BUG: doesn't take max
        else:
            merged.append([s, e])
    return merged
```

**Hint:** Three bugs. Try `[[1,4],[4,5]]`, `[[1,4],[2,3]]`, and `[[2,6],[1,3]]`.

<details><summary>Answer</summary>

**Bug 1:** no `intervals.sort()` — `[[2,6],[1,3]]` emits `[[2,6],[1,3]]` unmerged.
**Bug 2:** `s < merged[-1][1]` misses touching intervals — `[[1,4],[4,5]]` stays two instead of `[[1,5]]`; needs `s <= merged[-1][1]`.
**Bug 3:** `merged[-1][1] = e` can SHRINK — `[[1,4],[2,3]]` becomes `[[1,3]]`; needs `max(merged[-1][1], e)`.

Fixed:
```python
intervals = sorted(intervals)
...
if merged and s <= merged[-1][1]:
    merged[-1][1] = max(merged[-1][1], e)
```
</details>

---

## Debug 02 (Medium): Erase-overlaps — sorted by start

```python
def erase_overlap_intervals(intervals):
    intervals.sort()                       # BUG: sorts by (start, end)
    kept, last_end = 0, float("-inf")
    for s, e in intervals:
        if s >= last_end:
            kept += 1
            last_end = e
    return len(intervals) - kept
```

**Hint:** Try `[[1,10],[2,3],[4,5]]`.

<details><summary>Answer</summary>

**Bug:** sorting by start keeps `[1,10]` first — it blocks everything. Result: kept 1, removals 2. Optimal: keep `[2,3],[4,5]`, removals **1**.
**Fix:** `intervals.sort(key=lambda iv: iv[1])` — earliest-ending first frees the most room. The sort key IS the algorithm here.
</details>

---

## Debug 03 (Medium): Jump game — off-by-one direction

```python
def can_jump(nums):
    reach = 0
    for i, x in enumerate(nums):
        reach = max(reach, i + x)          # BUG: updates before checking
        if i > reach:
            return False
    return True
```

**Hint:** What does it return for `[0, 1]`? Is that right?

<details><summary>Answer</summary>

**Bug:** reach is updated from an index we may not even be able to stand on. `[0,1]`: i=0 reach=0; i=1: `reach = max(0, 1+1) = 2` BEFORE the check → `i=1 > reach=2`? No → returns True. But you can't reach index 1 — `nums[0]=0` means you can't move!
**Fix:** check FIRST, then extend:
```python
if i > reach:
    return False
reach = max(reach, i + x)
```
</details>

---

## Debug 04 (Hard): Jump II — counting jumps every index

```python
def jump(nums):
    jumps, reach = 0, 0
    for i in range(len(nums) - 1):
        if i + nums[i] > reach:
            jumps += 1                     # BUG: counts reach-improvements
            reach = i + nums[i]
    return jumps
```

**Hint:** Try `[3,1,1,1,4]` — you reach the end in ONE jump, but what does this count?

<details><summary>Answer</summary>

**Bug:** it counts "indices that improve reach," not "jumps." `[3,1,1,1,4]`: i=0 improves reach to 3 (jumps=1); i=1,2 don't improve; i=3 improves to 4 (jumps=2) — returns 2, but ONE jump from index 0 reaches index 3, and... wait, nums[0]=3 reaches index 3, not 4. From index 3, nums[3]=1 reaches 4. So true answer IS 2. Bad example — try `[2,3,1,1,4]`: i=0 → reach 2 (jumps 1); i=1 → reach 4 (jumps 2); i=2 → no improvement; → returns 2 = correct answer by luck. Now `[1,3,1,1,4]`: i=0 → reach 1 (jumps 1); i=1 → reach 4 (jumps 2); i=2,3 no improvement → returns 2. True answer: 0→1→4 = 2. Still lucky! The real break: `[1,1,3,1,4]` → i=0 reach1 (jumps1), i=1 reach2 (jumps2), i=2 reach5 (jumps3) → returns 3. True: 0→1→2→4? nums[2]=3 from index 2 reaches 5 → 0→2 needs 2 jumps (0→1→2) then 2→4 = 3. Hmm also 3!
Try `[5,1,1,1,1,4]`: i=0 → reach 5 (jumps1). i=1..4: 1+1=2, 2+1=3, 3+1=4, 4+1=5 — index 4 gives reach 5, not >5 → only counted at i=0... i=4: 4+1=5 not > 5. So returns **1**. True: jump 0→anything→... from index 0 (5) can reach index 5 directly! Wait nums[0]=5, n=6, index 0 reaches index 5 = last. So true answer IS 1. Argh.
Decisive case — `[4,1,1,1,1,1]`: i=0 reach 4 (jumps 1); i=1..4 never beat it → returns 1. True answer: 0→4 (index 4), then 4→5 = **2** jumps. The buggy code undercounts because reaching the max reach in one bound still required an intermediate jump. THIS is the break.
**Fix:** track `boundary` (end of current jump's range) and `farthest`; increment `jumps` when `i == boundary`:
```python
jumps = boundary = farthest = 0
for i in range(len(nums) - 1):
    farthest = max(farthest, i + nums[i])
    if i == boundary:
        jumps += 1
        boundary = farthest
```
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: Sorting by start for activity selection
```python
# WRONG — keeps the long early meeting
intervals.sort(key=lambda iv: iv[0])

# CORRECT — earliest end frees the most room
intervals.sort(key=lambda iv: iv[1])
```

## Mistake 02: `<` vs `<=` on touching intervals
```python
# Merge: touching intervals DO merge
if s <= merged[-1][1]:        # [1,4]+[4,5] → [1,5]

# Scheduling: touching intervals do NOT clash
if s >= last_end:             # [1,2],[2,3] → both kept
```

## Mistake 03: Extending with `e` instead of `max(..., e)`
```python
# WRONG — nested interval shrinks the merge: [[1,4],[2,3]] → [[1,3]]
merged[-1][1] = e

# CORRECT
merged[-1][1] = max(merged[-1][1], e)
```

## Mistake 04: Simulating paths instead of tracking reach
```python
# WRONG — trying every jump sequence → exponential/DP
def explore(i): ...

# CORRECT — one variable summarizes all paths
reach = max(reach, i + nums[i])
```

## Mistake 05: Forgetting the feasibility check in gas station
```python
# WRONG — returns a start index even when impossible
return start

# CORRECT — sum(gas) < sum(cost) means NO start works
return start if total >= 0 else -1
```

## Mistake 06: Greedy where it isn't valid
```python
# WRONG — "biggest coin first" fails on [1,3,4] for amount 6
count += amount // c

# CORRECT — no greedy-choice property → DP (lesson 15)
dp[a] = min(dp[a - c] + 1 for c in coins if a >= c)
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Merge with manual index bookkeeping
### Before
```python
def merge(intervals):
    intervals.sort()
    merged = [intervals[0]]
    i = 1
    while i < len(intervals):
        if intervals[i][0] <= merged[-1][1]:
            if intervals[i][1] > merged[-1][1]:
                merged[-1][1] = intervals[i][1]
        else:
            merged.append(intervals[i])
        i += 1
    return merged
```
### Problems
1. `while` + manual `i` where `for s, e in intervals` reads directly.
2. Nested `if` for the extension hides `max`; crashes on `[]` (`intervals[0]`).
3. Appending the original `[s,e]` list object — mutating `merged[-1]` later can mutate the caller's input.

### After
```python
def merge(intervals):
    merged = []
    for s, e in sorted(intervals):         # sorted() leaves caller's list alone
        if merged and s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])          # fresh list, not an alias
    return merged
```

---

## Refactor 02 (Medium): Insert interval with flag-soup
### Before
```python
def insert(intervals, newInterval):
    result = []
    inserted = False
    for s, e in intervals:
        if e < newInterval[0]:
            result.append([s, e])
        elif s > newInterval[1]:
            if not inserted:
                result.append(newInterval)
                inserted = True
            result.append([s, e])
        else:
            newInterval = [min(s, newInterval[0]), max(e, newInterval[1])]
    if not inserted:
        result.append(newInterval)
    return result
```
### Problems
1. Works, but the `inserted` flag is a smell — the interval belongs in exactly one place.
2. Three logical phases (before/overlap/after) hidden inside one flag-driven loop.

### After — the three phases made explicit
```python
def insert(intervals, newInterval):
    result, i, n = [], 0, len(intervals)
    while i < n and intervals[i][1] < newInterval[0]:      # phase 1: before
        result.append(intervals[i]); i += 1
    while i < n and intervals[i][0] <= newInterval[1]:     # phase 2: absorb
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)
    result.extend(intervals[i:])                            # phase 3: after
    return result
```

---

## Refactor 03 (Hard): Gas station — O(n²) simulation to O(n)
### Before
```python
def can_complete_circuit(gas, cost):
    n = len(gas)
    for start in range(n):                   # try every start
        tank = 0
        for step in range(n):
            i = (start + step) % n
            tank += gas[i] - cost[i]
            if tank < 0:
                break
        else:
            return start
    return -1
```
### Problems
1. O(n²) — n starts × n steps; n = 10⁵ is 10¹⁰.
2. Relearns nothing between attempts — the failed stretch `start..i` is re-simulated inside the next candidate.

### After
```python
def can_complete_circuit(gas, cost):
    total = tank = start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:                    # failed stretch start..i
            start = i + 1               # nothing in it can be the answer
            tank = 0
    return start if total >= 0 else -1
```
Why the skip is safe: if you failed reaching `i` from `start`, then starting at any `j` in `(start, i]` arrives with ≤ 0 extra fuel — the same deficit. O(n).

---

## Approach Comparison — different ways to solve it

## Problem: Erase minimum overlapping intervals

### Approach 1: Sort by END, keep earliest-ending (correct greedy)
```python
def f(intervals):
    intervals.sort(key=lambda iv: iv[1])
    kept, last_end = 0, float("-inf")
    for s, e in intervals:
        if s >= last_end:
            kept += 1; last_end = e
    return len(intervals) - kept
```
**Pros:** O(n log n), provably optimal via the exchange argument. **Cons:** you must know the end-sort trick — nothing about the code screams "why."

### Approach 2: Sort by START, drop the longer of each clash
```python
# When intervals clash, keep the one ending sooner:
# if s < last_end: kept_end = min(last_end, e)  → i.e. drop the later-ending one
```
**Pros:** Also correct (equivalent greedy stated differently) — dropping the interval with the larger end is optimal. **Cons:** trickier to reason about; easy to mis-implement.

### Approach 3: DP — longest non-overlapping subsequence
```python
# sort by end; dp[i] = best using first i intervals
# dp[i] = max(dp[i-1], 1 + dp[last compatible index])   — needs binary search
```
**Pros:** Bulletproof; generalizes to weighted intervals (max-profit scheduling). **Cons:** O(n log n) with much more code; overkill when the unweighted greedy suffices.

**Winner:** Approach 1 — one-line sort key, three-line sweep. Mention Approach 3 as "what I'd do if intervals had profits."

---

## Problem: Jump Game (reachability)

### Approach 1: Greedy reach tracking (this lesson)
```python
def f(nums):
    reach = 0
    for i, x in enumerate(nums):
        if i > reach: return False
        reach = max(reach, i + x)
    return True
```
**O(n) time, O(1) space.** Optimal.

### Approach 2: DP — `can[i] = any(can[j] and j + nums[j] >= i)`
```python
def f(nums):
    can = [False] * len(nums)
    can[0] = True
    for i in range(1, len(nums)):
        can[i] = any(can[j] and j + nums[j] >= i for j in range(i))
    return can[-1]
```
**Pros:** Mirrors the "reachable" definition directly; extends to variants (e.g., min-cost jumps). **Cons:** O(n²) — n = 10⁴ is borderline, n = 10⁵ dead.

### Approach 3: Backward greedy — work from the goal
```python
goal = len(nums) - 1
for i in range(len(nums) - 2, -1, -1):
    if i + nums[i] >= goal:
        goal = i                  # i becomes the new target
return goal == 0
```
**Pros:** Same O(n), sometimes easier to explain ("can anything reach the goal? then the goal moves left"). **Cons:** doesn't extend to Jump-II as naturally.

**Winner:** Approach 1 for clarity; Approach 3 is a neat alternative worth mentioning in interviews.
