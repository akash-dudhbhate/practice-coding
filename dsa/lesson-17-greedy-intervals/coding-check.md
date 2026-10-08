# Lesson 17 — Coding Check

Use this to verify your solutions before asking for review.

## Easy

### p01 — Merge overlapping intervals
- [ ] `merge([[1,3],[2,6],[8,10],[15,18]])` returns `[[1,6],[8,10],[15,18]]`
- [ ] `merge([[1,4],[4,5]])` returns `[[1,5]]` (touching intervals merge — use `s <= prev_end`)
- [ ] `merge([[1,4],[2,3]])` returns `[[1,4]]` (nested interval swallowed — take `max` of ends)
- [ ] `merge([[5,7]])` returns `[[5,7]]` (single interval)
- [ ] `merge([[2,6],[1,3]])` returns `[[1,6]]` — you sorted FIRST, right?

### p02 — Meeting rooms: can attend all?
- [ ] `can_attend_all([[0,30],[5,10],[15,20]])` returns `False`
- [ ] `can_attend_all([[7,10],[2,4]])` returns `True` (unsorted input — sort first)
- [ ] `can_attend_all([[1,5],[5,8],[8,10]])` returns `True` (touching endpoints do NOT clash)
- [ ] `can_attend_all([])` returns `True` and `can_attend_all([[1,2]])` returns `True`

### p03 — Assign cookies
- [ ] `find_content_children([1,2,3], [1,1])` returns `1`
- [ ] `find_content_children([1,2], [1,2,3])` returns `2`
- [ ] `find_content_children([10,9,8,7], [5,6,7,8])` returns `2` (cookies 7 and 8 satisfy greed 7 and 8)
- [ ] `find_content_children([], [1,2])` and `find_content_children([1,2,3], [])` return `0`
- [ ] You sort BOTH lists and pair least-greedy child with smallest sufficient cookie

## Medium

### p01 — Erase minimum overlapping intervals
- [ ] `erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]])` returns `1`
- [ ] `erase_overlap_intervals([[1,2],[1,2],[1,2]])` returns `2`
- [ ] `erase_overlap_intervals([[1,2],[2,3]])` returns `0` (touching = not overlapping)
- [ ] `erase_overlap_intervals([[0,2],[1,3],[2,4],[3,5],[4,6]])` returns `2`
- [ ] You sorted by **end** (`iv[1]`), not start — sort-by-start is THE bug here

### p02 — Insert interval
- [ ] `insert([[1,3],[6,9]], [2,5])` returns `[[1,5],[6,9]]`
- [ ] `insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])` returns `[[1,2],[3,10],[12,16]]`
- [ ] `insert([], [5,7])` returns `[[5,7]]`
- [ ] `insert([[1,5]], [2,7])` returns `[[1,7]]` (new interval grows by absorbing)
- [ ] `insert([[5,8]], [1,3])` returns `[[1,3],[5,8]]` (insert entirely BEFORE — output order stays sorted)

### p03 — Jump game: reachable?
- [ ] `can_jump([2,3,1,1,4])` returns `True`
- [ ] `can_jump([3,2,1,0,4])` returns `False` (the `0` at index 3 is a wall)
- [ ] `can_jump([0])` returns `True` (already at the end)
- [ ] `can_jump([2,0,0])` returns `True` (can jump OVER zeros)
- [ ] `can_jump([1,1,0,1])` returns `False`
- [ ] You track `reach` and bail when `i > reach` — NOT simulating actual jump paths

## Hard

### p01 — Jump game II: minimum jumps
- [ ] `jump([2,3,1,1,4])` returns `2`
- [ ] `jump([2,3,0,1,4])` returns `2`
- [ ] `jump([1,1,1,1])` returns `3`
- [ ] `jump([0])` returns `0`
- [ ] `jump([1,2,3])` returns `2`
- [ ] You increment `jumps` only when `i` hits `boundary` — not on every index (that's the overcount bug)

### p02 — Gas station
- [ ] `can_complete_circuit([1,2,3,4,5], [3,4,5,1,2])` returns `3`
- [ ] `can_complete_circuit([2,3,4], [3,4,3])` returns `-1` (total gas < total cost)
- [ ] `can_complete_circuit([5,1,2,3,4], [4,4,1,5,1])` returns `4`
- [ ] `can_complete_circuit([3,1,1], [1,2,2])` returns `0`
- [ ] When `tank < 0` you restart the candidate at `i + 1` and reset `tank = 0`

### p03 — Partition labels
- [ ] `partition_labels("ababcbacadefegdehijhklij")` returns `[9,7,8]`
- [ ] `partition_labels("eccbbbbdec")` returns `[10]` (one char reaches the last index → single part)
- [ ] `partition_labels("a")` returns `[1]`
- [ ] `partition_labels("abac")` returns `[3,1]`
- [ ] You precomputed `last[c]` for every char and cut when `i == farthest_last_seen`

## How to verify

```bash
python3 check.py all            # all nine of your files
python3 check.py medium/p02     # just one
python3 check.py solutions      # sanity-check the reference solutions
```
