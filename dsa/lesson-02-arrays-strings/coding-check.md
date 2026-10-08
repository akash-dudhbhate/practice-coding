# Lesson 02 — Coding Check

Use this to verify your solutions before asking for a review.

## Easy

### p01-running-sum.py — Running sum
- [ ] `running_sum([1,2,3,4])` returns `[1,3,6,10]`
- [ ] `running_sum([5])` returns `[5]`
- [ ] `running_sum([])` returns `[]`
- [ ] `running_sum([1,-1,1,-1])` returns `[1,0,1,0]`

### p02-max-min-one-pass.py — Max and min in one pass
- [ ] `max_min([3,1,4,1,5])` returns `(5, 1)`
- [ ] `max_min([7])` returns `(7, 7)`
- [ ] `max_min([-2,-9,-4])` returns `(-2, -9)`
- [ ] Single loop — no `max(nums)` + `min(nums)` two-scan combo (that's 2 passes)

### p03-char-frequency.py — Character frequency
- [ ] `char_freq("aab")` returns `{'a': 2, 'b': 1}`
- [ ] `char_freq("hello")` returns `{'h': 1, 'e': 1, 'l': 2, 'o': 1}`
- [ ] `char_freq("")` returns `{}`
- [ ] Case-sensitive: `char_freq("Aa")` returns `{'A': 1, 'a': 1}`

## Medium

### p01-range-sum-queries.py — Prefix-sum range queries
- [ ] `answer_queries([1,2,3,4,5], [(0,2)])` returns `[6]`
- [ ] `answer_queries([1,2,3,4,5], [(0,2),(1,4),(2,2)])` returns `[6,14,3]`
- [ ] `answer_queries([1,2,3,4,5], [(0,4)])` returns `[15]`
- [ ] Ranges are INCLUSIVE — `sum(i..j) = P[j+1] - P[i]`
- [ ] Prefix array built ONCE — not re-summed per query

### p02-move-zeros-inplace.py — Move zeros in place
- [ ] Input `[0,1,0,3,12]` becomes `[1,3,12,0,0]` (list is mutated!)
- [ ] Input `[0,0,1]` becomes `[1,0,0]`
- [ ] Input `[1,2,3]` stays `[1,2,3]`
- [ ] Input `[]` stays `[]`
- [ ] O(1) extra space — no second list

### p03-product-except-self.py — Product except self
- [ ] `product_except_self([1,2,3,4])` returns `[24,12,8,6]`
- [ ] `product_except_self([2,3,4])` returns `[12,8,6]`
- [ ] `product_except_self([-1,1,0,-3,3])` returns `[0,0,9,0,0]` (zeros work!)
- [ ] No division used

## Hard

### p01-subarray-sum-k.py — Subarray sum equals k
- [ ] `count_subarray_sum([1,1,1], 2)` returns `2`
- [ ] `count_subarray_sum([1,2,3], 3)` returns `2` ([1,2] and [3])
- [ ] `count_subarray_sum([1,-1,0], 0)` returns `3`
- [ ] `count_subarray_sum([1], 1)` returns `1`
- [ ] Seed `{0: 1}` or subarrays starting at index 0 get missed

### p02-max-subarray-kadane.py — Maximum subarray (Kadane)
- [ ] `max_subarray([-2,1,-3,4,-1,2,1,-5,4])` returns `6`
- [ ] `max_subarray([5,4,-1,7,8])` returns `23`
- [ ] `max_subarray([-3,-1,-2])` returns `-1` (all negative — no empty-subarray trick)
- [ ] `max_subarray([7])` returns `7`

### p03-two-pass-encode.py — Two-pass frequency encoding
- [ ] `encode_with_freq("aabca")` returns `"a3b1c1"`
- [ ] `encode_with_freq("zzz")` returns `"z3"`
- [ ] `encode_with_freq("ab")` returns `"a1b1"`
- [ ] `encode_with_freq("")` returns `""`
- [ ] Order = first appearance, and the string is built with `join`

## How to verify

```bash
python3 check.py easy/p01     # one problem
python3 check.py all          # everything
```
