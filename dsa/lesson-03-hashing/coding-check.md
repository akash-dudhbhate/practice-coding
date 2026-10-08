# Lesson 03 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01 — Count frequencies
- [ ] `count_frequencies(["a","b","a","c","b","a"])` returns `{"a":3,"b":2,"c":1}`
- [ ] `count_frequencies([7,7,7])` returns `{7:3}`
- [ ] `count_frequencies([])` returns `{}`
- [ ] No `counts[x] += 1` KeyError on a missing key (use `.get` or defaultdict)

### p02 — Find duplicates
- [ ] `find_duplicates([4,3,2,4,3,5])` returns `[3,4]` (sorted, each once)
- [ ] `find_duplicates([1,2,3])` returns `[]`
- [ ] `find_duplicates([5,5,5,5])` returns `[5]` — not `[5,5,5]`
- [ ] `find_duplicates([])` returns `[]`

### p03 — First unique char
- [ ] `first_unique_char("leetcode")` returns `0`
- [ ] `first_unique_char("loveleetcode")` returns `2`
- [ ] `first_unique_char("aabb")` returns `-1`
- [ ] `first_unique_char("")` returns `-1`
- [ ] Two passes: count first, then scan for first count==1 (order matters!)

## Medium

### p01 — Two sum
- [ ] `two_sum([2,7,11,15], 9)` returns `[0,1]`
- [ ] `two_sum([3,2,4], 6)` returns `[1,2]`
- [ ] `two_sum([3,3], 6)` returns `[0,1]` (same value at different indices is fine)
- [ ] `two_sum([3], 6)` returns `[]` — an element must NOT pair with itself
- [ ] `two_sum([1,5,9], 20)` returns `[]`
- [ ] Check complement BEFORE storing current element

### p02 — Group anagrams
- [ ] `group_anagrams(["eat","tea","tan","ate","nat","bat"])` gives groups `{ate,eat,tea}`, `{nat,tan}`, `{bat}`
- [ ] `group_anagrams([])` returns `[]`
- [ ] `group_anagrams(["a"])` returns `[["a"]]`
- [ ] Key is the sorted letters: `"".join(sorted(w))`

### p03 — Array intersection
- [ ] `intersection([1,2,2,1],[2,2])` returns `[2]`
- [ ] `intersection([4,9,5],[9,4,9,8,4])` returns `[4,9]` (unique + sorted)
- [ ] `intersection([1,2],[3,4])` returns `[]`

## Hard

### p01 — Longest consecutive sequence (O(n))
- [ ] `longest_consecutive([100,4,200,1,3,2])` returns `4`
- [ ] `longest_consecutive([0,3,7,2,5,8,4,6,0,1])` returns `9`
- [ ] `longest_consecutive([])` returns `0`
- [ ] `longest_consecutive([1,2,0,1])` returns `3` (duplicates ok)
- [ ] No sorting — run starts detected via `x-1 not in set`

### p02 — Subarray sum k
- [ ] `subarray_sum([1,1,1], 2)` returns `2`
- [ ] `subarray_sum([1,2,3], 3)` returns `2`
- [ ] `subarray_sum([1,-1,0], 0)` returns `3`
- [ ] `subarray_sum([0,0,0], 0)` returns `6`
- [ ] Frequency map seeded with `{0: 1}`; query before recording prefix

### p03 — LRU cache
- [ ] `get` returns value or `-1`, and marks the key most-recent
- [ ] `put` past capacity evicts the LEAST recently used key
- [ ] `put` on an existing key updates value + refreshes recency
- [ ] Both `get` and `put` run in O(1)

## How to verify

```bash
python3 check.py all          # your files
python3 check.py solutions    # reference solutions (should be 9/9)
```
