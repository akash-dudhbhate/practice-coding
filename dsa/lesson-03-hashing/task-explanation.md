# Lesson 03 — Hashing (Dict & Set Patterns)

## What you'll learn
- Why dict/set lookups are O(1) — hash → bucket → jump straight to it
- Counting with a dict / Counter (frequency tables)
- Set membership for "seen before" and dedup
- The complement-lookup pattern (two-sum): O(n²) → O(n)
- Grouping by a computed key (anagrams, index maps)
- Why hash keys must be immutable — and the sorted-key trick
- Prefix-sum hashing for subarray-sum problems
- Combining a hash map with ordering for LRU-style designs

## Lesson

Almost every "find / count / pair" problem whose brute force is a nested loop
gets faster the same way: **store the past in a dict or set so each new element
can query it in O(1).** You trade O(n) extra memory for a massive speed win.

```python
seen = {}                    # value -> index
for i, x in enumerate(nums):
    if target - x in seen:   # the complement trick
        return [seen[target - x], i]
    seen[x] = i
```

The other three moves you'll use constantly:

```python
counts[x] = counts.get(x, 0) + 1          # frequency table
groups.setdefault(key, []).append(item)   # grouping by a key
set(a) & set(b)                           # O(n) intersection
```

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here)
1. `easy/p01-count-frequencies.py` — Build an item→count dict for a list.
   `count_frequencies(["a","b","a"])` → `{"a": 2, "b": 1}`
2. `easy/p02-find-duplicates.py` — Return a sorted list of values that repeat.
   `find_duplicates([4,3,2,4,3,5])` → `[3,4]`
3. `easy/p03-first-unique-char.py` — Index of the first char appearing once.
   `first_unique_char("leetcode")` → `0`

### Medium
4. `medium/p01-two-sum.py` — Indices of two numbers summing to target, O(n).
   `two_sum([2,7,11,15], 9)` → `[0,1]`
5. `medium/p02-group-anagrams.py` — Group words by sorted-letter signature.
   `group_anagrams(["eat","tea","bat"])` → `[["eat","tea"],["bat"]]`
6. `medium/p03-array-intersection.py` — Sorted unique values in both lists.
   `intersection([1,2,2,1],[2,2])` → `[2]`

### Hard
7. `hard/p01-longest-consecutive.py` — Longest consecutive run, O(n).
   `longest_consecutive([100,4,200,1,3,2])` → `4`
8. `hard/p02-subarray-sum-k.py` — Count subarrays summing to k via prefix hash.
   `subarray_sum([1,1,1], 2)` → `2`
9. `hard/p03-lru-cache.py` — O(1) LRU cache: dict + doubly-linked list.
   `get`/`put` with capacity-2 eviction as described in the file.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python3 check.py easy/p01` to verify; `python3 check.py all` for all.
- `coding-check.md` has the manual checklist; `EXTRA-PRACTICE.md` has drills.
