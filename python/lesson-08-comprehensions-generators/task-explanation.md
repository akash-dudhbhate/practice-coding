# Lesson 08 — List Comprehensions & Generators

## What you'll learn
- Building lists/dicts/sets with comprehensions.
- Lazy evaluation with generator expressions.
- Writing generator functions with `yield`.
- Chaining generators into pipelines.
- `itertools` basics.

## Lesson

Comprehensions build collections concisely; generators do it lazily to save memory.

### Comprehensions
```python
squares = [x*x for x in range(5)]          # list
word_len = {w: len(w) for w in words}      # dict
uniq = {len(w) for w in words}             # set
```

### Generators
```python
gen = (x*x for x in range(5))   # lazy, one at a time
total = sum(x*x for x in range(1000000))  # no big list

def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1
```

### Key rules
- `[...]` builds a list now; `(...)` is lazy.
- Generators are single-use — exhausted after one pass.
- `yield` pauses and resumes; a generator function returns a generator object.
- Keep comprehensions simple; use a loop for complex logic.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete solution from scratch below** (function signature + body) to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.py` — `squares(n)`: return a list of squares from 0 to n-1 using a list comprehension. `squares(4)` → `[0, 1, 4, 9]`.
2. `easy/p02-solve.py` — `evens(nums)`: return a list of even numbers from `nums` using a list comprehension with `if`.
3. `easy/p03-solve.py` — `lengths(words)`: return a dict mapping each word to its length using a dict comprehension.

### Medium
4. `medium/p01-solve.py` — `flatten(matrix)`: flatten a 2D list into 1D using a nested comprehension. `flatten([[1,2],[3,4]])` → `[1,2,3,4]`.
5. `medium/p02-solve.py` — `sum_squares(n)`: return the sum of squares from 0 to n-1 using a generator expression (no list in memory).
6. `medium/p03-solve.py` — `even_squares(n)`: return a list of squares that are even, for x in 0..n-1, using a comprehension with a filter.

### Hard
7. `hard/p01-solve.py` — `fibonacci_gen(n)`: a generator function that yields the first `n` Fibonacci numbers. `list(fibonacci_gen(6))` → `[0, 1, 1, 2, 3, 5]`.
8. `hard/p02-solve.py` — `chunked(iterable, size)`: a generator that yields chunks of `size` items from `iterable`. `list(chunked([1,2,3,4,5], 2))` → `[[1,2],[3,4],[5]]`.
9. `hard/p03-solve.py` — `pipeline(data)`: chain three generator functions — `filter_positive`, `double`, `to_strings` — and return the final list. `pipeline([-1, 2, -3, 4])` → `["4", "8"]`.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python <filename>` to test with your own inputs.
- When done, tell me and I'll review. Say **"give me next task"** to advance to the next lesson.
