# Lesson 13 — Coding Check

## Easy

### p01-solve.py — count_up_to generator
- [ ] `list(count_up_to(5))` returns `[1, 2, 3, 4, 5]`
- [ ] `list(count_up_to(0))` returns `[]`
- [ ] Uses `yield` not `return`

### p02-solve.py — Generator expression
- [ ] Produces squares of even numbers: `[0, 4, 16, 36, 64, 100, 144, 196, 256, 324]`
- [ ] Uses generator expression syntax `(x**2 for x in ...)`
- [ ] Only even numbers are included

### p03-solve.py — CountDown iterator
- [ ] `list(CountDown(3))` returns `[3, 2, 1]`
- [ ] `list(CountDown(0))` returns `[]`
- [ ] Implements `__iter__` and `__next__`
- [ ] Raises `StopIteration` when done

## Medium

### p01-solve.py — Fibonacci generator
- [ ] First 10 Fibonacci numbers: `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`
- [ ] Generator is infinite (no termination condition)
- [ ] Uses `while True` and `yield`

### p02-solve.py — Flatten generator
- [ ] `list(flatten([1, [2, [3, 4]], 5]))` returns `[1, 2, 3, 4, 5]`
- [ ] `list(flatten([]))` returns `[]`
- [ ] `list(flatten([1, 2, 3]))` returns `[1, 2, 3]` (no nesting)
- [ ] Uses `yield from` for recursion

### p03-solve.py — Generator pipeline
- [ ] Pipeline: 1-100 → multiples of 3 → squared → first 5
- [ ] Result: `[9, 36, 81, 144, 225]` (3², 6², 9², 12², 15²)
- [ ] Each stage is a generator function
- [ ] No intermediate lists created

## Hard

### p01-solve.py — read_lines generator
- [ ] Yields lines from a file one at a time
- [ ] Doesn't load entire file into memory (uses `yield` per line)
- [ ] Handles `FileNotFoundError` gracefully (returns empty generator or raises clear error)
- [ ] Strips newline characters from each line

### p02-solve.py — chunked generator
- [ ] `list(chunked([1,2,3,4,5], 2))` returns `[[1,2], [3,4], [5]]`
- [ ] `list(chunked([1,2,3,4], 2))` returns `[[1,2], [3,4]]`
- [ ] `list(chunked([], 3))` returns `[]`
- [ ] Last chunk may be smaller than `size`
- [ ] Works with any iterable (not just lists)

### p03-solve.py — cycle_forever generator
- [ ] `list(islice(cycle_forever([1,2,3]), 7))` returns `[1,2,3,1,2,3,1]`
- [ ] Generator is infinite
- [ ] Round-robin assignment works: 3 workers get tasks in rotation
- [ ] Handles empty iterable (either raises error or yields nothing)
