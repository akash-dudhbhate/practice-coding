# Lesson 01 — Time/Space Complexity & Big-O

## What you'll learn
- What time complexity is (counting operations, not seconds)
- Big-O notation: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ)
- Reading complexity off loops (sequential vs nested, hidden inner loops)
- Worst vs average vs best case
- Dropping constants and lower-order terms
- Space complexity and auxiliary space
- Recursion's hidden call-count explosion
- Amortized analysis (why `list.append` is O(1) on average)

## Lesson

Complexity is a count of *operations* as input size `n` grows. Seconds lie
(machines differ), so we count steps. Big-O keeps only the fastest-growing
term and drops constants: `3n² + 12n + 7` → `O(n²)`.

### The growth ladder (ops at n=1000)

```python
O(1)       -> 1           # constant: nums[0]
O(log n)   -> ~10         # halving: binary search
O(n)       -> 1_000       # one loop
O(n log n) -> ~10_000     # good sorting
O(n^2)     -> 1_000_000   # nested loops
O(2^n)     -> astronomical # fib(n) recursion, all subsets
```

### Reading loops

```python
for x in nums:              # O(n) — one pass
    ...

for x in nums:              # O(n) + O(n) = O(n) — sequential
    ...
for x in nums:
    ...

for x in nums:              # O(n²) — nested
    for y in nums:
        ...
```

### Hidden inner loops

`x in list`, `list.count()`, `list.index()` all scan the whole list — each is
O(n). Inside a `for` loop they make your code O(n²). Use `set`/`dict` for
O(1) membership checks.

### Cases

Best / average / worst describe luck. Linear search: best O(1) (target first),
worst O(n) (last or missing). Quote the **worst** unless told otherwise.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here)
1. `easy/p01-count-loop-ops.py` — Write `count_ops(n)` that returns how many times the body of `for i in range(n)` executes. `count_ops(10)` → `10`, `count_ops(0)` → `0`.
2. `easy/p02-identify-bigO.py` — Write `classify_growth(ops_n, ops_2n, ops_4n)`: given operation counts at n, 2n, and 4n, return the growth class — `"O(1)"`, `"O(log n)"`, `"O(n)"`, `"O(n^2)"`, `"O(2^n)"`, or `"unknown"`.
3. `easy/p03-growth-rates.py` — Write `growth_values(n)` returning a dict mapping each Big-O class to its op count at that n (use `math.log2`).

### Medium
4. `medium/p01-nested-pairs-count.py` — Write `count_pair_ops(n)` returning the number of inner-loop executions for `for i in range(n): for j in range(i+1, n)`. `count_pair_ops(5)` → `10`.
5. `medium/p02-find-bottleneck.py` — Write `phase_ops(n)` returning `{"linear": n, "nlogn": n*log2(n), "quadratic": n*n}` and `bottleneck_phase(n)` returning the key of the largest phase.
6. `medium/p03-early-exit-comparisons.py` — Write `count_comparisons(nums, target)` that performs linear search and returns how many comparisons were *actually* made (early exit counts!).

### Hard
7. `hard/p01-measured-dedup.py` — Write `dedup_naive(nums)` and `dedup_set(nums)`. Each returns `(deduped_list, ops_count)`. The naive version counts every element comparison; the set version counts membership checks. Prove O(n²) vs O(n) with real numbers.
8. `hard/p02-fib-call-count.py` — Write `fib_with_count(n)` returning `(fib(n), total_calls)`. `fib_with_count(5)` → `(5, 15)` — count every recursive call to expose the O(2ⁿ) explosion.
9. `hard/p03-optimize-pair-sum.py` — Write `pair_sum_slow(nums, target)` (nested loops) and `pair_sum_fast(nums, target)` (set-based). Each returns `(found, ops_count)` — prove the O(n) version does less work.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python3 check.py <level>/<pNN>` to test one problem, `python3 check.py all` for everything.
- `coding-check.md` is your manual checklist; `EXTRA-PRACTICE.md` has drills.
- Solutions live in `<level>/solutions/` — look only AFTER trying.
