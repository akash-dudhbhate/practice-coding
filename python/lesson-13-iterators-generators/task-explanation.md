# Lesson 13 — Iterators & Generators

## What you'll learn
- Iterator protocol (__iter__, __next__, StopIteration)
- Iterable vs iterator
- Generator functions with yield
- Generator expressions
- yield from
- Infinite generators
- itertools module
- Generator pipelines
- Memory efficiency

## Lesson

### Custom iterator
```python
class Range2:
    def __init__(self, n): self.n = n; self.i = 0
    def __iter__(self): return self
    def __next__(self):
        if self.i >= self.n: raise StopIteration
        self.i += 1
        return self.i - 1
```

### Generator function
```python
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

### Generator expression
```python
sum(x**2 for x in range(1000000))  # memory efficient
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Write a generator function `count_up_to(n)` that yields numbers from 1 to n.
2. `easy/p02-solve.py` — Write a generator expression that produces squares of even numbers from 0 to 20. Convert to list and print.
3. `easy/p03-solve.py` — Write a custom iterator class `CountDown(n)` that counts from n down to 1. Implement `__iter__` and `__next__`.

### Medium
4. `medium/p01-solve.py` — Write an infinite generator `fibonacci()` that yields Fibonacci numbers. Use `itertools.islice` to print the first 10.
5. `medium/p02-solve.py` — Write a generator `flatten(nested_list)` that flattens a nested list of arbitrary depth using `yield from`.
6. `medium/p03-solve.py` — Build a generator pipeline: generate numbers 1-100 → filter multiples of 3 → square them → take first 5. Chain generators.

### Hard
7. `hard/p01-solve.py` — Write a generator `read_lines(filename)` that yields lines from a file one at a time (without loading the whole file into memory). Handle file not found.
8. `hard/p02-solve.py` — Write a generator `chunked(iterable, size)` that yields chunks of `size` items from any iterable. Example: `chunked([1,2,3,4,5], 2)` → `[1,2], [3,4], [5]`.
9. `hard/p03-solve.py` — Write a generator `cycle_forever(iterable)` that cycles through an iterable infinitely (like itertools.cycle). Then use it to assign round-robin to 3 workers.

### How to work
- Write your complete solution from scratch below the TODO marker.
- Remove the TODO line when done.
