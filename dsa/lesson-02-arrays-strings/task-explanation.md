# Lesson 02 — Arrays & Strings

## What you'll learn
- Why indexing is O(1) (contiguous memory)
- Prefix sums: build once O(n), answer range-sums in O(1)
- In-place modification vs new lists (write-pointer pattern)
- Two-pass patterns (count first, build second)
- String scanning: frequency dicts, `join` instead of `+=`
- Kadane's running-total intuition (your first DP)

## Lesson

Arrays store elements in contiguous memory, so `nums[i]` is a single
address calculation — O(1). Strings are arrays you can't mutate.

### Prefix sums

```python
nums = [1, 2, 3, 4, 5]
P = [0]
for x in nums:
    P.append(P[-1] + x)
# P = [0, 1, 3, 6, 10, 15]
# sum of indices i..j inclusive = P[j+1] - P[i]
P[4] - P[1]   # 10 - 1 = 9  (2+3+4)
```

### In-place with a write pointer

```python
def move_zeros(nums):       # mutates nums, O(1) space
    w = 0
    for x in nums:
        if x != 0:
            nums[w] = x
            w += 1
    while w < len(nums):
        nums[w] = 0
        w += 1
```

### String scanning

```python
freq = {}
for c in text:
    freq[c] = freq.get(c, 0) + 1   # O(n) tally

result = "".join(pieces)           # O(n) build, never += in a loop
```

### Kadane's one-liner

```python
cur = best = nums[0]
for x in nums[1:]:
    cur = max(x, cur + x)          # extend or restart
    best = max(best, cur)
```

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here)
1. `easy/p01-running-sum.py` — Write `running_sum(nums)` returning prefix sums in one pass: `[1,2,3,4]` → `[1,3,6,10]`.
2. `easy/p02-max-min-one-pass.py` — Write `max_min(nums)` returning `(max, min)` from a single scan: `[3,1,4,1,5]` → `(5,1)`.
3. `easy/p03-char-frequency.py` — Write `char_freq(text)` returning a `{char: count}` dict: `"aab"` → `{'a': 2, 'b': 1}`.

### Medium
4. `medium/p01-range-sum-queries.py` — Write `answer_queries(nums, queries)` that builds a prefix-sum array once and answers each inclusive `(i, j)` range-sum in O(1): `([1,2,3,4,5], [(0,2),(1,4),(2,2)])` → `[6, 14, 3]`.
5. `medium/p02-move-zeros-inplace.py` — Write `move_zeros(nums)` that pushes all zeros to the end **in place**, keeping order: `[0,1,0,3,12]` → `[1,3,12,0,0]`.
6. `medium/p03-product-except-self.py` — Write `product_except_self(nums)` (two passes, no division): `[1,2,3,4]` → `[24,12,8,6]`.

### Hard
7. `hard/p01-subarray-sum-k.py` — Write `count_subarray_sum(nums, k)` counting contiguous subarrays that sum to `k`, via prefix sums + dict: `([1,1,1], 2)` → `2`.
8. `hard/p02-max-subarray-kadane.py` — Write `max_subarray(nums)` returning the maximum subarray sum (Kadane's): `[-2,1,-3,4,-1,2,1,-5,4]` → `6`. Must handle all-negative input.
9. `hard/p03-two-pass-encode.py` — Write `encode_with_freq(text)` that labels each distinct char (in first-appearance order) with its total count: `"aabca"` → `"a3b1c1"`. Pass 1 counts, pass 2 builds — and build with `join`, not `+=`.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python3 check.py <level>/<pNN>` to test one problem, `python3 check.py all` for everything.
- `coding-check.md` is your manual checklist; `EXTRA-PRACTICE.md` has drills.
- Solutions live in `<level>/solutions/` — look only AFTER trying.
