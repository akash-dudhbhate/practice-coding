# Lesson 05 — Sliding Window

## What you'll learn
- The two window shapes: fixed-size vs variable-size
- The expand/shrink loop: `right` grows, `left` shrinks when invalid
- Window bookkeeping: running sum, count dict, `formed` counters
- Why sliding window is O(n): each element enters and leaves exactly once

## Lesson

A **window** is a contiguous chunk `nums[left..right]`. Sliding means each
element enters the window once and leaves once — so a "nested-looking" loop
runs in O(n).

### Fixed-size window (k is given)
```python
window_sum = sum(nums[:k])               # build once
for right in range(k, len(nums)):
    window_sum += nums[right]            # enter
    window_sum -= nums[right - k]        # leave
```

### Variable-size window (longest/shortest satisfying a rule)
```python
left = 0
for right in range(n):
    add nums[right] to state             # EXPAND
    while window_invalid:
        remove nums[left]; left += 1     # SHRINK until valid
    record answer                        # longest: after shrink
```

For **shortest-valid** problems the loop inverts: `while valid: record; shrink`.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here) — fixed windows
1. `easy/p01-max-sum-fixed-window.py` — `max_sum_k(nums, k)` → max sum of any contiguous subarray of length `k`.
   `[2,1,5,1,3,2], k=3 → 9` (window `[5,1,3]`).
2. `easy/p02-window-averages.py` — `window_averages(nums, k)` → list of averages for every size-`k` window.
   `[1,2,3,4], k=2 → [1.5, 2.5, 3.5]`. Return `[]` if `k > len(nums)`.
3. `easy/p03-count-windows-meeting-target.py` — `count_windows_at_least(nums, k, target)` → how many size-`k` windows sum to `>= target`.
   `[1,4,2,10,2,3,1,0,20], k=4, target=15 → 5` (sums 17, 18, 17, 16, 6, 24 — five of six qualify).

### Medium — variable windows
4. `medium/p01-longest-substring-no-repeat.py` — `length_of_longest_substring(s)` → length of longest substring with all unique chars.
   `"abcabcbb" → 3`, `"bbbbb" → 1`, `"pwwkew" → 3`, `"dvdf" → 3` (stale-index trap: `left` must only move *forward*).
5. `medium/p02-max-consecutive-ones-flips.py` — `longest_ones(nums, k)` → longest run of 1s possible after flipping at most `k` zeros.
   Trick: it's "longest window containing `<= k` zeros".
   `[1,1,1,0,0,0,1,1,1,1,0], k=2 → 6` (flip the two zeros at index 4–5, take indices 3–8).
6. `medium/p03-min-size-subarray-sum.py` — `min_subarray_len(target, nums)` → length of smallest subarray with sum `>= target`; `0` if none.
   `target=7, [2,3,1,2,4,3] → 2` (the `[4,3]`). Positive numbers only — that's what makes shrinking safe.

### Hard — variable windows with richer state
7. `hard/p01-minimum-window-substring.py` — `min_window(s, t)` → smallest substring of `s` containing every char of `t` (duplicates count).
   `("ADOBECODEBANC", "ABC") → "BANC"`. Track `need` counts + `formed` counter; shrink while `formed == len(need)`.
8. `hard/p02-longest-substring-k-distinct.py` — `length_of_longest_k_distinct(s, k)` → longest substring with `<= k` distinct chars.
   `"eceba", k=2 → 3`, `"abcadcacacaca", k=3 → 11`. Delete zero-count keys or `len(count)` lies.
9. `hard/p03-fruit-into-baskets.py` — `total_fruit(fruits)` → longest subarray with `<= 2` distinct values (the P02 skeleton with `k=2`).
   `[3,3,3,1,2,1,1,2,3,3,4] → 5` (subarray `[1,2,1,1,2]`).

### How to work
- Read `concepts.md` first — the recipe section maps each problem to a shape.
- Open a problem file, read the header, write your code under the TODO marker.
- Run `python3 check.py easy/p01` for one problem, `python3 check.py all` for all nine.
- `coding-check.md` is your manual checklist; `EXTRA-PRACTICE.md` has debug drills after you finish.
- Peek at `solutions/` only after a real attempt — then close it and redo from memory.
