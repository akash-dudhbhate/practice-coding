# Lesson 18 — Coding Check

Use this to verify your solutions before asking for review.

## Easy

### p01 — XOR single number
- [ ] `single_number([2,2,1])` returns `1`
- [ ] `single_number([4,1,2,1,2])` returns `4`
- [ ] `single_number([1])` returns `1`
- [ ] `single_number([-1,-1,-2])` returns `-2` (XOR works on negatives too)
- [ ] `single_number([7,3,5,3,5])` returns `7`
- [ ] O(1) space — a `Counter`/`set` technically passes but misses the point

### p02 — Power of two check
- [ ] `is_power_of_two(1)` returns `True` (2⁰)
- [ ] `is_power_of_two(16)` returns `True`
- [ ] `is_power_of_two(3)` returns `False`
- [ ] `is_power_of_two(0)` returns `False` — the `n > 0` guard is required
- [ ] `is_power_of_two(-8)` returns `False`
- [ ] `is_power_of_two(1024)` returns `True`, `is_power_of_two(6)` returns `False`

### p03 — Count set bits
- [ ] `hamming_weight(11)` returns `3` (binary 1011)
- [ ] `hamming_weight(128)` returns `1`
- [ ] `hamming_weight(0)` returns `0`
- [ ] `hamming_weight(255)` returns `8`
- [ ] `hamming_weight(2147483647)` returns `31`
- [ ] Uses `n &= n - 1` (one iteration per set bit), not `bin(n).count('1')`

## Medium

### p01 — Implement Trie
- [ ] After `insert("apple")`: `search("apple")` → `True`, `search("app")` → `False`, `startsWith("app")` → `True`
- [ ] After also `insert("app")`: `search("app")` → `True`
- [ ] `search("apples")` → `False` and `startsWith("apples")` → `False` (no such path)
- [ ] `insert("app")` then `insert("application")` then `startsWith("appli")` → `True`
- [ ] `is_end` distinguishes "word ends here" from "path merely passes through"

### p02 — XOR two single numbers
- [ ] `single_numbers([1,2,1,3,2,5])` returns `{3, 5}` as a list (order irrelevant)
- [ ] `single_numbers([-1,0])` returns the two elements
- [ ] `single_numbers([0,1])` returns the two elements
- [ ] `single_numbers([1,2,3,4,1,2,3,7])` returns `{4, 7}`
- [ ] You split on `xor & -xor` (lowest differing bit), not trial-and-error

### p03 — Next greater element, circular
- [ ] `next_greater_elements([1,2,1])` returns `[2,-1,2]`
- [ ] `next_greater_elements([1,2,3,4,3])` returns `[2,3,4,-1,4]`
- [ ] `next_greater_elements([5,4,3,2,1])` returns `[-1,5,5,5,5]` (wraparound finds the 5)
- [ ] `next_greater_elements([1,2,3,2,1])` returns `[2,3,-1,3,2]`
- [ ] `next_greater_elements([3])` returns `[-1]`
- [ ] Second pass does NOT push (`if i < n: stack.append(i)`)

## Hard

### p01 — Word search II with trie
- [ ] `find_words(board4x4, ["oath","pea","eat","rain"])` returns `["eat","oath"]` (sorted)
- [ ] `find_words([["a","b"],["c","d"]], ["abcb"])` returns `[]` — cell reuse is banned
- [ ] `find_words([["a"]], ["a"])` returns `["a"]`
- [ ] `find_words([["a","b"],["c","d"]], ["ab","ba","cd","abd"])` returns all four, sorted
- [ ] You mark cells visited and RESTORE them after recursing (other paths need them)
- [ ] The trie prunes DFS — you're not checking each word separately

### p02 — Max XOR of two numbers
- [ ] `find_maximum_xor([3,10,5,25,2,8])` returns `28`
- [ ] `find_maximum_xor([0])` returns `0`, `find_maximum_xor([5,5])` returns `0`
- [ ] `find_maximum_xor([2,4])` returns `6`, `find_maximum_xor([8,10,2])` returns `10`
- [ ] `find_maximum_xor([14,70,53,83,49,91,36,80,92,51,66,70])` returns `127`
- [ ] O(32·n) trie approach — not O(n²) pairwise (n=10⁵ would be 10¹⁰ ops)

### p03 — Largest rectangle in histogram
- [ ] `largest_rectangle_area([2,1,5,6,2,3])` returns `10`
- [ ] `largest_rectangle_area([2,4])` returns `4`
- [ ] `largest_rectangle_area([1])` returns `1`
- [ ] `largest_rectangle_area([4,2,0,3,2,5])` returns `6`
- [ ] `largest_rectangle_area([])` returns `0`
- [ ] You push INDICES (need positions for widths) and flush the stack at the end (sentinel or drain loop)

## How to verify

```bash
python3 check.py all            # all nine of your files
python3 check.py medium/p01     # just one
python3 check.py solutions      # sanity-check the reference solutions
```
