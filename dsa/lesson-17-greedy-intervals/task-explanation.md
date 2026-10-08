# Lesson 17 — Greedy & Intervals

## What you'll learn
- What "greedy" actually means: locally-best choices that are *provably* globally optimal — and the coin-change case where greedy FAILS
- THE interval pattern: sort (by start or end — the key IS the algorithm), sweep once, track `current`
- Activity selection: sort by END to keep the most non-overlapping intervals
- Reach-tracking greedy: jump game, min jumps, gas station
- How to sanity-check a greedy rule with a 30-second counterexample hunt

## Lesson

**Greedy** = take the locally-best option and never reconsider. It only works
when the problem has the *greedy choice property* — coin change `[1,3,4]`
making 6 is the famous counterexample (greedy gives 4+1+1=3 coins, optimal is
3+3=2). When you can't justify greedy, use DP.

### Interval skeleton — sort, sweep, track current
```python
intervals.sort(key=lambda iv: iv[0])       # or iv[1] — by END for activity selection
merged = []
for s, e in intervals:
    if merged and s <= merged[-1][1]:      # overlaps current
        merged[-1][1] = max(merged[-1][1], e)
    else:
        merged.append([s, e])
```

### Activity-selection skeleton — sort by END
```python
intervals.sort(key=lambda iv: iv[1])
kept, last_end = 0, float("-inf")
for s, e in intervals:
    if s >= last_end:                      # doesn't clash → keep it
        kept += 1
        last_end = e
```

### Reach-tracking skeleton — jump game
```python
reach = 0
for i, x in enumerate(nums):
    if i > reach: return False             # stranded
    reach = max(reach, i + x)
```

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here) — the interval pattern + a pure greedy
1. `easy/p01-merge-overlapping-intervals.py` — `merge(intervals)` → merge all overlapping intervals.
   `[[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]`. Sort by start, extend the top of `merged`.
2. `easy/p02-meeting-rooms-can-attend-all.py` — `can_attend_all(intervals)` → `True` if no two meetings overlap.
   `[[0,30],[5,10],[15,20]] → False`; `[[7,10],[2,4]] → True`. Touching endpoints (`[1,5],[5,8]`) are OK.
3. `easy/p03-assign-cookies.py` — `find_content_children(g, s)` → max children contented; child `i` needs a cookie of size `>= g[i]`, each cookie feeds at most one child.
   `g=[1,2,3], s=[1,1] → 1`; `g=[1,2], s=[1,2,3] → 2`. Greedy: smallest cookie that satisfies the least-greedy remaining child.

### Medium — the two sort keys + reach tracking
4. `medium/p01-erase-minimum-overlaps.py` — `erase_overlap_intervals(intervals)` → minimum removals to make the rest non-overlapping.
   `[[1,2],[2,3],[3,4],[1,3]] → 1`. Sort by END (activity selection); touching ends don't overlap.
5. `medium/p02-insert-interval.py` — `insert(intervals, newInterval)` → insert into a sorted, disjoint list and merge.
   `([[1,3],[6,9]], [2,5]) → [[1,5],[6,9]]`; `([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) → [[1,2],[3,10],[12,16]]`.
   Three phases: intervals ending before it / overlapping it (absorb) / after it.
6. `medium/p03-jump-game-reachable.py` — `can_jump(nums)` → can you reach the last index? `nums[i]` = max jump length from `i`.
   `[2,3,1,1,4] → True`; `[3,2,1,0,4] → False`. Track `reach`; if `i > reach` you're stranded.

### Hard — reach tracking with richer state
7. `hard/p01-jump-game-min-jumps.py` — `jump(nums)` → FEWEST jumps to reach the last index (always reachable).
   `[2,3,1,1,4] → 2`; `[1,1,1,1] → 3`. Track `boundary` (farthest your current jump count reaches) and `farthest`; spend a jump when `i` crosses the boundary.
8. `hard/p02-gas-station.py` — `can_complete_circuit(gas, cost)` → starting station index to complete the loop, or `-1`.
   `gas=[1,2,3,4,5], cost=[3,4,5,1,2] → 3`. If `tank` goes negative at `i`, no station in the failed stretch can start — restart at `i+1`. Feasibility: `sum(gas) >= sum(cost)`.
9. `hard/p03-partition-labels.py` — `partition_labels(s)` → sizes of the max number of parts so each letter appears in at most one part.
   `"ababcbacadefegdehijhklij" → [9,7,8]`; `"eccbbbbdec" → [10]`. Record each char's last index; a part ends when `i` reaches the max-last of chars seen so far. (Intervals in disguise: each letter owns `[first, last]`.)

### How to work
- Read `concepts.md` first — especially "sort by start vs end" and the counterexample hunt.
- Open a problem file, read the header, write your code under the TODO marker.
- Run `python3 check.py easy/p01` for one problem, `python3 check.py all` for all nine.
- `coding-check.md` is your manual checklist; `EXTRA-PRACTICE.md` has debug drills after you finish.
- Peek at `solutions/` only after a real attempt — then close it and redo from memory.
