# Lesson 03 — Coding Check

Use this to verify your solutions before asking me to review. Each problem file has its own expected behavior — check against these.

## Easy

### p01-solve.py (sum_list)
- [ ] `sum_list([1, 2, 3, 4, 5])` returns `15`
- [ ] `sum_list([])` returns `0`
- [ ] `sum_list([-1, 1])` returns `0`
- [ ] No use of built-in `sum()`

### p02-solve.py (reverse_list)
- [ ] `reverse_list([1, 2, 3])` returns `[3, 2, 1]`
- [ ] `reverse_list([])` returns `[]`
- [ ] Original list is NOT mutated (check after the call)
- [ ] `reverse_list(["a", "b"])` returns `["b", "a"]`

### p03-solve.py (contains)
- [ ] `contains([1, 2, 3], 2)` returns `True`
- [ ] `contains([1, 2, 3], 5)` returns `False`
- [ ] `contains([], 1)` returns `False`
- [ ] No use of `in` operator

## Medium

### p01-solve.py (remove_duplicates)
- [ ] `remove_duplicates([1, 2, 2, 3, 3, 3])` returns `[1, 2, 3]`
- [ ] `remove_duplicates([1, 2, 3])` returns `[1, 2, 3]` (no dupes, unchanged)
- [ ] `remove_duplicates([])` returns `[]`
- [ ] Order is preserved (first occurrence kept)

### p02-solve.py (sort_by_length)
- [ ] `sort_by_length(["cat", "elephant", "dog"])` returns `["cat", "dog", "elephant"]`
- [ ] `sort_by_length(["a", "bb", "ccc"])` returns `["a", "bb", "ccc"]`
- [ ] Returns a NEW list (uses `sorted()`)
- [ ] `sort_by_length([])` returns `[]`

### p03-solve.py (swap_pairs)
- [ ] `swap_pairs([1, 2, 3, 4, 5])` returns `[2, 1, 4, 3, 5]`
- [ ] `swap_pairs([1, 2, 3, 4])` returns `[2, 1, 4, 3]`
- [ ] `swap_pairs([])` returns `[]`
- [ ] `swap_pairs([1])` returns `[1]`

## Hard

### p01-solve.py (flatten)
- [ ] `flatten([[1, 2], [3], [4, 5]])` returns `[1, 2, 3, 4, 5]`
- [ ] `flatten([[1], [], [2, 3]])` returns `[1, 2, 3]`
- [ ] `flatten([])` returns `[]`
- [ ] `flatten([[1, 2, 3]])` returns `[1, 2, 3]`

### p02-solve.py (second_largest)
- [ ] `second_largest([5, 1, 4, 4, 3])` returns `4`
- [ ] `second_largest([10, 10, 10])` returns `None` (only one unique value)
- [ ] `second_largest([1])` returns `None`
- [ ] `second_largest([3, 1, 2])` returns `2`

### p03-solve.py (tuple_stats)
- [ ] `tuple_stats((3, 1, 4, 1, 5))` returns `(1, 5, 2.8)`
- [ ] `tuple_stats(())` returns `(None, None, 0.0)`
- [ ] `tuple_stats((7,))` returns `(7, 7, 7.0)`
- [ ] Average is a float (not int)

## How to verify

Run each file with your own test calls:
```bash
python easy/p01-solve.py
```

Or test from a REPL:
```bash
python -c "from easy.p01_solve import sum_list; print(sum_list([1,2,3]))"
```
