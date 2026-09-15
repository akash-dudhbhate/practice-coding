# Lesson 05 — Coding Check

Use this to verify your solutions before asking me to review. Each problem file has its own expected behavior — check against these.

## Easy

### p01-solve.py (classify_number)
- [ ] `classify_number(5)` returns `"positive"`
- [ ] `classify_number(-3)` returns `"negative"`
- [ ] `classify_number(0)` returns `"zero"`

### p02-solve.py (sum_range)
- [ ] `sum_range(1, 5)` returns `15` (1+2+3+4+5)
- [ ] `sum_range(0, 0)` returns `0`
- [ ] `sum_range(5, 5)` returns `5`
- [ ] Uses a `for` loop with `range`

### p03-solve.py (count_down)
- [ ] `count_down(3)` returns `[3, 2, 1]`
- [ ] `count_down(1)` returns `[1]`
- [ ] `count_down(0)` returns `[]`
- [ ] Uses a `while` loop

## Medium

### p01-solve.py (first_even)
- [ ] `first_even([1, 3, 5, 4, 7])` returns `4`
- [ ] `first_even([1, 3, 5])` returns `None`
- [ ] `first_even([])` returns `None`
- [ ] Uses `break`

### p02-solve.py (skip_negatives)
- [ ] `skip_negatives([1, -2, 3, -4, 5])` returns `[1, 3, 5]`
- [ ] `skip_negatives([-1, -2])` returns `[]`
- [ ] `skip_negatives([])` returns `[]`
- [ ] Uses `continue`

### p03-solve.py (multiplication_table)
- [ ] `multiplication_table(3)` returns `[[1,2,3],[2,4,6],[3,6,9]]`
- [ ] `multiplication_table(1)` returns `[[1]]`
- [ ] `multiplication_table(2)` returns `[[1,2],[2,4]]`
- [ ] Uses nested loops

## Hard

### p01-solve.py (is_palindrome)
- [ ] `is_palindrome("racecar")` returns `True`
- [ ] `is_palindrome("RaceCar")` returns `True` (case-insensitive)
- [ ] `is_palindrome("hello")` returns `False`
- [ ] `is_palindrome("")` returns `True`
- [ ] Uses two-pointer loop (no slicing)

### p02-solve.py (find_pair)
- [ ] `find_pair([2, 7, 11, 15], 9)` returns `(0, 1)`
- [ ] `find_pair([1, 2, 3], 7)` returns `None`
- [ ] `find_pair([3, 3], 6)` returns `(0, 1)`
- [ ] Uses nested loops

### p03-solve.py (collatz_steps)
- [ ] `collatz_steps(6)` returns `8`
- [ ] `collatz_steps(1)` returns `0`
- [ ] `collatz_steps(2)` returns `1`
- [ ] Handles large inputs without infinite loop

## How to verify

Run each file with your own test calls:
```bash
python easy/p01-solve.py
```

Or test from a REPL:
```bash
python -c "from easy.p01_solve import classify_number; print(classify_number(5))"
```
