# Lesson 01 — Coding Check

Use this to verify your solutions before asking for a review.

## Easy

### p01-count-loop-ops.py — Count loop operations
- [ ] `count_ops(10)` returns `10`
- [ ] `count_ops(0)` returns `0`
- [ ] `count_ops(1)` returns `1`
- [ ] `count_ops(1000)` returns `1000`
- [ ] Return is `n` — the loop runs exactly n times → O(n)

### p02-identify-bigO.py — Classify growth from measurements
- [ ] `classify_growth(7, 7, 7)` returns `"O(1)"` (constant)
- [ ] `classify_growth(10, 11, 12)` returns `"O(log n)"` (+1 per doubling)
- [ ] `classify_growth(50, 100, 200)` returns `"O(n)"` (×2 per doubling)
- [ ] `classify_growth(25, 100, 400)` returns `"O(n^2)"` (×4 per doubling)
- [ ] `classify_growth(8, 64, 4096)` returns `"O(2^n)"` (squared per doubling)

### p03-growth-rates.py — Compare growth rates numerically
- [ ] `growth_values(8)["O(1)"]` returns `1`
- [ ] `growth_values(8)["O(log n)"]` returns `3`
- [ ] `growth_values(8)["O(n)"]` returns `8`
- [ ] `growth_values(8)["O(n log n)"]` returns `24`
- [ ] `growth_values(8)["O(n^2)"]` returns `64`
- [ ] `growth_values(8)["O(2^n)"]` returns `256`

## Medium

### p01-nested-pairs-count.py — Nested loop analysis
- [ ] `count_pair_ops(5)` returns `10` (4+3+2+1)
- [ ] `count_pair_ops(4)` returns `6`
- [ ] `count_pair_ops(1)` returns `0`
- [ ] `count_pair_ops(10)` returns `45`
- [ ] Formula is `n*(n-1)//2` → still O(n²)

### p02-find-bottleneck.py — Find the dominant phase
- [ ] `phase_ops(8)` returns `{"linear": 8, "nlogn": 24, "quadratic": 64}`
- [ ] `bottleneck_phase(8)` returns `"quadratic"`
- [ ] `bottleneck_phase(2)` returns `"quadratic"`
- [ ] Total work = sum of phases, but Big-O = largest phase only

### p03-early-exit-comparisons.py — Best vs worst case
- [ ] `count_comparisons([5,9,2,7], 5)` returns `1` (best case)
- [ ] `count_comparisons([5,9,2,7], 7)` returns `4` (last element)
- [ ] `count_comparisons([5,9,2,7], 99)` returns `4` (worst case — not found)
- [ ] `count_comparisons([], 1)` returns `0`

## Hard

### p01-measured-dedup.py — Naive vs set dedup with measured counts
- [ ] `dedup_naive([1,2,2,3])` returns `([1,2,3], 5)`
- [ ] `dedup_set([1,2,2,3])` returns `([1,2,3], 4)`
- [ ] `dedup_naive([1,2,3,4,5])` returns `([1,2,3,4,5], 10)`
- [ ] Both return the same deduped list — only the op count differs
- [ ] Naive ops grow quadratically; set ops grow linearly

### p02-fib-call-count.py — Recursive fib call explosion
- [ ] `fib_with_count(0)` returns `(0, 1)`
- [ ] `fib_with_count(1)` returns `(1, 1)`
- [ ] `fib_with_count(5)` returns `(5, 15)`
- [ ] `fib_with_count(10)` returns `(55, 177)`
- [ ] Call count grows ~exponentially → O(2ⁿ)

### p03-optimize-pair-sum.py — O(n²) → O(n) proof
- [ ] `pair_sum_slow([1,4,7,2,9], 11)` returns `(True, 5)`
- [ ] `pair_sum_fast([1,4,7,2,9], 11)` returns `(True, 3)`
- [ ] `pair_sum_slow([1,2,3], 10)` returns `(False, 3)`
- [ ] `pair_sum_fast([1,2,3], 10)` returns `(False, 3)`
- [ ] Same answers, fewer ops — on big inputs the gap explodes

## How to verify

```bash
python3 check.py easy/p01     # one problem
python3 check.py all          # everything
```
