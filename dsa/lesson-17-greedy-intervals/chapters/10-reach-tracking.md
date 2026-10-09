# 10 — Reach-Tracking Greedy: Jump Game & Gas Station

> 6-minute read. A second greedy family — no sorting at all.

## The idea, plain words

Some greedy problems have nothing to sort. Instead you carry **one
variable that summarizes "how far my decisions so far can take me"** —
`reach`, `tank`, `boundary` — and update it greedily in a single pass.

Think of a frog on lily pads: you don't care *which* hops it took, only
the farthest pad its hops could possibly reach. **A longer reach always
dominates a shorter one** — that's the bet, and it never strands you.

## Jump Game — `nums = [3,2,1,0,4]` (value = max jump length)

```
i=0: i<=reach(0) ✓   reach = max(0, 0+3) = 3
i=1: 1<=3 ✓          reach = max(3, 1+2) = 3
i=2: 2<=3 ✓          reach = max(3, 2+1) = 3
i=3: 3<=3 ✓          reach = max(3, 3+0) = 3   ← the 0 is a wall
i=4: 4 > 3 → STRANDED → False
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

`can_jump([2,3,1,1,4])` → `True` · `can_jump([3,2,1,0,4])` → `False` ·
`can_jump([0])` → `True` (already at the end — edge case!).

**Jump Game II (minimum jumps):** same idea, two variables — `farthest`
(best reach with one more jump) and `boundary` (farthest the jumps already
spent can reach). When `i` hits `boundary`, you MUST spend a jump:

```python
def jump(nums):
    jumps = boundary = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == boundary:            # forced: spend jump, commit boundary
            jumps += 1
            boundary = farthest
    return jumps
```

`jump([2,3,1,1,4])` → **2** (jump to index 1, then to the end).

**Gas Station:** if `total gas < total cost`, impossible → `-1`. Otherwise
drive; whenever `tank` dips below 0, no station in the failed stretch can
be the start (you'd arrive there with ≤ 0 and hit the same deficit) — so
restart the candidate at `i + 1`. One pass finds feasibility AND start.

## Why it exists

The naive versions are brutal: simulating jump paths is exponential, and
trying every gas-station start is `O(n²)`. The "how far can my budget
stretch" framing collapses both to `O(n)` — you never simulate paths, you
only track the best reachable frontier.

## Where it's used

- Jump/reach and game-move reachability problems
- Refueling & leap scheduling, network hop problems
- Any "minimum/maximum count of choices on a line" prompt

## Common mistake

- **Jump Game:** simulating actual jump sequences → exponential/DP
  territory. Only the max reach matters, never the path.
- **Jump II:** incrementing `jumps` every index instead of only when `i`
  crosses `boundary` → overcounts.
- **Gas Station:** forgetting the feasibility check — `sum(gas) <
  sum(cost)` means return `-1`, not a wrong index.

## Your turn

`can_jump([1,0,1])` — True or False?

<details><summary>Answer</summary>
`False`. `i=0`: reach = max(0, 0+1) = 1. `i=1`: `1 <= 1` ✓, reach =
max(1, 1+0) = 1. `i=2`: `2 > 1` → stranded. The `0` at index 1 is a wall
and index 0's jump only reaches exactly onto it.
</details>

---

**← Prev** [09 — The Exchange Argument](09-exchange-argument.md) ·
**Next →** [11 — Greedy or Not?](11-greedy-or-not.md)
