# Lesson 05 — Coding Check

Use this to verify your solutions before asking for review.

## Easy

### p01 — Max sum of a fixed window
- [ ] `max_sum_k([2, 1, 5, 1, 3, 2], 3)` returns `9`
- [ ] `max_sum_k([1, 2, 3, 4, 5], 2)` returns `9`
- [ ] `max_sum_k([5], 1)` returns `5` (window = whole array)
- [ ] `max_sum_k([-1, -2, -3], 2)` returns `-3` (works when all values are negative — don't init `best` to 0!)
- [ ] Each slide does O(1) work — no `sum(window)` inside the loop

### p02 — Window averages
- [ ] `window_averages([1, 2, 3, 4], 2)` returns `[1.5, 2.5, 3.5]`
- [ ] `window_averages([5, 5, 5], 3)` returns `[5.0]`
- [ ] `window_averages([1, 2], 3)` returns `[]` (k > n)
- [ ] Result has exactly `len(nums) - k + 1` entries

### p03 — Count windows meeting target
- [ ] `count_windows_at_least([1, 4, 2, 10, 2, 3, 1, 0, 20], 4, 15)` returns `5`
- [ ] `count_windows_at_least([1, 1, 1], 2, 3)` returns `0`
- [ ] `count_windows_at_least([3, 3, 3], 2, 5)` returns `2`
- [ ] `count_windows_at_least([1, 2], 3, 0)` returns `0` (k > n)

## Medium

### p01 — Longest substring without repeats
- [ ] `length_of_longest_substring("abcabcbb")` returns `3`
- [ ] `length_of_longest_substring("bbbbb")` returns `1`
- [ ] `length_of_longest_substring("pwwkew")` returns `3` (answer is `"wke"`, not `"pwke"`)
- [ ] `length_of_longest_substring("")` returns `0`
- [ ] `length_of_longest_substring("dvdf")` returns `3` — the stale-index trap; `left` must never move *backward*
- [ ] `length_of_longest_substring("abba")` returns `2`

### p02 — Max consecutive ones with k flips
- [ ] `longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2)` returns `6`
- [ ] `longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)` returns `10`
- [ ] `longest_ones([1,1,1], 0)` returns `3` (k=0 still counts existing runs)
- [ ] `longest_ones([0,0,0], 1)` returns `1`
- [ ] You count **zeros in the window**, not ones — `while zeros > k: shrink`

### p03 — Min size subarray sum
- [ ] `min_subarray_len(7, [2, 3, 1, 2, 4, 3])` returns `2`
- [ ] `min_subarray_len(4, [1, 4, 4])` returns `1` (single element can satisfy)
- [ ] `min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1])` returns `0` (impossible → 0, not an error)
- [ ] `min_subarray_len(15, [1, 2, 3, 4, 5])` returns `5` (whole array)
- [ ] You record `best` **inside** the `while total >= target` loop, then shrink

## Hard

### p01 — Minimum window substring
- [ ] `min_window("ADOBECODEBANC", "ABC")` returns `"BANC"`
- [ ] `min_window("a", "a")` returns `"a"`
- [ ] `min_window("a", "aa")` returns `""` (impossible → empty string)
- [ ] `min_window("aa", "aa")` returns `"aa"` — duplicates in `t` matter (multiplicity)
- [ ] `min_window("bba", "ab")` returns `"ba"` (smaller valid window exists)
- [ ] `formed` increments only when a char's count *reaches* its required count, not every sighting

### p02 — Longest substring with k distinct
- [ ] `length_of_longest_k_distinct("eceba", 2)` returns `3`
- [ ] `length_of_longest_k_distinct("aa", 1)` returns `2`
- [ ] `length_of_longest_k_distinct("abcadcacacaca", 3)` returns `11`
- [ ] `length_of_longest_k_distinct("aabbcc", 2)` returns `4`
- [ ] `length_of_longest_k_distinct("abc", 0)` returns `0`
- [ ] Zero-count keys are deleted from the dict — `len(count)` must equal *distinct chars currently in window*

### p03 — Fruit into baskets
- [ ] `total_fruit([1, 2, 1])` returns `3`
- [ ] `total_fruit([0, 1, 2, 2])` returns `3`
- [ ] `total_fruit([1, 2, 3, 2, 2])` returns `4`
- [ ] `total_fruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4])` returns `5`
- [ ] `total_fruit([])` returns `0`
- [ ] Recognized the disguise: this is "at most 2 distinct" — P02 with k=2

## How to verify

```bash
python3 check.py all            # all nine of your files
python3 check.py medium/p02     # just one
python3 check.py solutions      # sanity-check the reference solutions
```
