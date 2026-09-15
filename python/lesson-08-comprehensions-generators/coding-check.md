# Lesson 08 — Coding Check

Use this to verify your solutions before asking me to review. Each problem file has its own expected behavior — check against these.

## Easy

### p01-solve.py (squares)
- [ ] `squares(4)` returns `[0, 1, 4, 9]`
- [ ] `squares(0)` returns `[]`
- [ ] `squares(1)` returns `[0]`
- [ ] Uses a list comprehension

### p02-solve.py (evens)
- [ ] `evens([1, 2, 3, 4, 5, 6])` returns `[2, 4, 6]`
- [ ] `evens([1, 3, 5])` returns `[]`
- [ ] `evens([])` returns `[]`
- [ ] Uses a comprehension with `if`

### p03-solve.py (lengths)
- [ ] `lengths(["hi", "hello"])` returns `{"hi": 2, "hello": 5}`
- [ ] `lengths([])` returns `{}`
- [ ] Uses a dict comprehension

## Medium

### p01-solve.py (flatten)
- [ ] `flatten([[1, 2], [3, 4]])` returns `[1, 2, 3, 4]`
- [ ] `flatten([[], [1], [2, 3]])` returns `[1, 2, 3]`
- [ ] `flatten([])` returns `[]`
- [ ] Uses a nested comprehension

### p02-solve.py (sum_squares)
- [ ] `sum_squares(4)` returns `14` (0+1+4+9)
- [ ] `sum_squares(0)` returns `0`
- [ ] Uses a generator expression (not a list)

### p03-solve.py (even_squares)
- [ ] `even_squares(5)` returns `[0, 4, 16]` (0,2,4 squared, even results)
- [ ] `even_squares(0)` returns `[]`
- [ ] Filter is on the square being even (or x being even — clarify in your code)

## Hard

### p01-solve.py (fibonacci_gen)
- [ ] `list(fibonacci_gen(6))` returns `[0, 1, 1, 2, 3, 5]`
- [ ] `list(fibonacci_gen(0))` returns `[]`
- [ ] `list(fibonacci_gen(1))` returns `[0]`
- [ ] Uses `yield` (generator function)

### p02-solve.py (chunked)
- [ ] `list(chunked([1,2,3,4,5], 2))` returns `[[1,2],[3,4],[5]]`
- [ ] `list(chunked([1,2,3,4], 2))` returns `[[1,2],[3,4]]`
- [ ] `list(chunked([], 2))` returns `[]`
- [ ] Last chunk may be smaller than `size`

### p03-solve.py (pipeline)
- [ ] `pipeline([-1, 2, -3, 4])` returns `["4", "8"]`
- [ ] `pipeline([1, 2, 3])` returns `["2", "4", "6"]`
- [ ] `pipeline([])` returns `[]`
- [ ] Uses three chained generator functions

## How to verify

Run each file with your own test calls:
```bash
python easy/p01-solve.py
```

Or test from a REPL:
```bash
python -c "from hard.p01_solve import fibonacci_gen; print(list(fibonacci_gen(6)))"
```
