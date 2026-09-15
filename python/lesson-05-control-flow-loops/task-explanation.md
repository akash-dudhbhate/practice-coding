# Lesson 05 — Control Flow & Loops

## What you'll learn
- Making decisions with `if`/`elif`/`else`.
- Repeating work with `for` and `while` loops.
- Controlling loops with `break` and `continue`.
- Generating sequences with `range()` and `enumerate()`.
- The accumulator pattern and nested loops.

## Lesson

Control flow decides what runs; loops repeat work.

### Conditionals
```python
if score >= 90: grade = "A"
elif score >= 80: grade = "B"
else: grade = "C"
```

### Loops
```python
for i in range(5): print(i)        # 0..4
while count < 5: count += 1
for i, x in enumerate(items): ...  # index + value
```

### break / continue
```python
for n in nums:
    if n < 0: continue   # skip negatives
    if n == 0: break     # stop at first zero
```

### Key rules
- `range(5)` is 0–4 (stop is exclusive).
- `while` must update its condition or it loops forever.
- `break` exits only the innermost loop.
- Initialize accumulators BEFORE the loop.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete solution from scratch below** (function signature + body) to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.py` — `classify_number(n)`: return `"positive"`, `"negative"`, or `"zero"` based on `n`.
2. `easy/p02-solve.py` — `sum_range(start, stop)`: return the sum of all integers from `start` to `stop` inclusive, using a `for` loop with `range`.
3. `easy/p03-solve.py` — `count_down(n)`: return a list counting down from `n` to `1` using a `while` loop. `count_down(3)` → `[3, 2, 1]`.

### Medium
4. `medium/p01-solve.py` — `first_even(nums)`: return the first even number in the list using `break`; return `None` if there are none.
5. `medium/p02-solve.py` — `skip_negatives(nums)`: return a new list of only the non-negative numbers, using `continue` to skip negatives.
6. `medium/p03-solve.py` — `multiplication_table(n)`: return a list of lists representing an n×n multiplication table. `multiplication_table(3)` → `[[1,2,3],[2,4,6],[3,6,9]]`.

### Hard
7. `hard/p01-solve.py` — `is_palindrome(s)`: return `True` if `s` reads the same forwards and backwards (case-insensitive), using a loop with two pointers (no slicing).
8. `hard/p02-solve.py` — `find_pair(nums, target)`: return the indices of the first pair of numbers that sum to `target`, as a tuple `(i, j)`. Return `None` if no pair exists. Use nested loops.
9. `hard/p03-solve.py` — `collatz_steps(n)`: return the number of steps to reach 1 in the Collatz sequence (even → n/2, odd → 3n+1). `collatz_steps(6)` → `8` (6→3→10→5→16→8→4→2→1).

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python <filename>` to test with your own inputs.
- When done, tell me and I'll review. Say **"give me next task"** to advance to the next lesson.
