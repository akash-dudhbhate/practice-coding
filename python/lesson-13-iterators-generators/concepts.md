# Lesson 13 — Concepts Explained (Iterators & Generators)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Iterator Protocol

**What:** An iterator is any object that implements `__iter__()` and `__next__()`. `__next__()` returns the next value; when there are no more values, it raises `StopIteration`.

```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # the iterator is itself

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for num in CountDown(3):
    print(num)    # 3, 2, 1
```

**Why it exists:** The iterator protocol is how Python makes ANY object work with `for` loops. Lists, strings, files, dicts — they all implement this protocol. Without it, you'd need different loop syntax for every data type.

**Where it's used:** Every `for` loop in Python. `list()`, `sum()`, `max()`, `min()` all accept iterators. File objects are iterators (line by line). `map()`, `filter()`, `zip()` return iterators.

**What goes wrong without it:**
- Forgetting `raise StopIteration` → infinite loop when iterating.
- Forgetting `__iter__` → `TypeError: 'X' object is not iterable`.
- Iterators are EXHAUSTED after one pass: `it = iter([1,2,3]); list(it); list(it)` → second list is empty. You must create a new iterator.

---

## Iterable vs Iterator

**What:**
- **Iterable:** has `__iter__()` → can be looped over (lists, strings, dicts, files).
- **Iterator:** has `__iter__()` AND `__next__()` → produces values one at a time.

```python
my_list = [1, 2, 3]          # iterable (has __iter__)
my_iter = iter(my_list)      # iterator (has __iter__ AND __next__)
next(my_iter)                 # 1
next(my_iter)                 # 2
next(my_iter)                 # 3
next(my_iter)                 # StopIteration!
```

**Why it exists:** Separating iterable from iterator lets you create multiple independent iterators from the same iterable. `iter([1,2,3])` creates a fresh iterator each time — you can have two loops over the same list simultaneously.

**Where it's used:** Every time you use `for`, `iter()`, `next()`, or unpack (`a, b, c = my_list`).

**What goes wrong without it:**
- Confusing the two: calling `next()` on a list → `TypeError: 'list' is not an iterator`. Must call `iter()` first.
- Reusing an exhausted iterator → empty results. Create a new one with `iter()`.
- Lists are iterables, not iterators. `list.__next__()` doesn't exist. `iter(list).__next__()` does.

---

## Generator Function (yield)

**What:** A generator function uses `yield` instead of `return`. It produces values one at a time, pausing between each.

```python
def count_up_to(max_val):
    count = 1
    while count <= max_val:
        yield count          # produce a value, PAUSE here
        count += 1           # resume here on next call

for num in count_up_to(3):
    print(num)    # 1, 2, 3

gen = count_up_to(3)
next(gen)    # 1 — function runs until yield, pauses
next(gen)    # 2 — resumes after yield, runs until next yield
next(gen)    # 3
next(gen)    # StopIteration — function ended
```

**Why it exists:** Without generators, you'd build the entire list in memory then iterate. For 1 million items, that's 1 million items in memory. Generators produce items ONE AT A TIME — near-zero memory, even for infinite sequences.

**Where it's used:** Processing large files (line by line), infinite sequences (Fibonacci, primes), streaming data, pipelines, `range()` is a generator-like object.

**What goes wrong without it:**
- Using `return` instead of `yield` → only produces one value, stops immediately.
- Forgetting that generators are lazy — they don't execute until you iterate. Creating a generator without consuming it → no output, no side effects.
- Generators are single-use: once exhausted, you must create a new one. Can't rewind.

---

## Generator Expression

**What:** A generator expression is like a list comprehension but with parentheses instead of brackets. It produces values lazily.

```python
# List comprehension — creates full list in memory
squares_list = [x**2 for x in range(1000000)]   # ~8MB in memory

# Generator expression — produces values on demand
squares_gen = (x**2 for x in range(1000000))    # ~100 bytes in memory

next(squares_gen)    # 0
next(squares_gen)    # 1
sum(squares_gen)     # sum of remaining — no full list created
```

**Why it exists:** For large data, list comprehensions waste memory. Generator expressions give you the clean syntax of comprehensions with the memory efficiency of generators.

**Where it's used:** `sum(x for x in range(1000000))`, `any(x > 0 for x in data)`, `max(len(line) for line in file)`, passing to functions that accept iterables.

**What goes wrong without it:**
- Using `[]` instead of `()` → creates full list in memory → memory error for large data.
- Generator expressions are single-use: `gen = (x for x in range(5)); list(gen); list(gen)` → second list is empty.
- Can't index: `gen[0]` → `TypeError`. Generators don't support indexing — they're not sequences.

---

## yield from

**What:** `yield from` delegates to another iterable/generator, yielding all its values.

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)    # yield all values from recursive call
        else:
            yield item

list(flatten([1, [2, [3, 4]], 5]))    # [1, 2, 3, 4, 5]
```

**Why it exists:** Without `yield from`, you'd write `for sub_item in sub_gen: yield sub_item` — verbose. `yield from` is cleaner and also handles edge cases (sending values, returning from sub-generators).

**Where it's used:** Flattening nested structures, delegating to sub-generators, recursive generators.

**What goes wrong without it:**
- `yield gen` instead of `yield from gen` → yields the generator OBJECT, not its values. You get a generator inside your generator.
- Forgetting `yield from` in recursive generators → only yields one level deep → nested lists stay nested.

---

## Infinite Generators

**What:** A generator that never stops — it has no termination condition.

```python
def fibonacci():
    a, b = 0, 1
    while True:          # never stops
        yield a
        a, b = b, a + b

fib = fibonacci()
next(fib)    # 0
next(fib)    # 1
next(fib)    # 1
next(fib)    # 2
next(fib)    # 3
# ... infinite — use itertools.islice to take a finite number
```

**Why it exists:** Some sequences are infinite (Fibonacci, primes, natural numbers). You can't store them in a list. Generators let you work with them — take as many as you need, when you need them.

**Where it's used:** Mathematical sequences, streaming data, real-time feeds, ID generators, simulation steps.

**What goes wrong without it:**
- `list(fibonacci())` → infinite loop / memory error — never try to materialize an infinite generator.
- Forgetting to break: `for x in fibonacci(): print(x)` → runs forever. Use `itertools.islice` or `break`.
- No `StopIteration` → the generator never raises it → `next()` always works.

---

## itertools Module

**What:** `itertools` provides fast, memory-efficient tools for working with iterators.

```python
from itertools import count, cycle, chain, islice, combinations, permutations

count(10)              # 10, 11, 12, 13, ... (infinite)
cycle("AB")            # A, B, A, B, A, B, ... (infinite)
chain([1,2], [3,4])    # 1, 2, 3, 4 (combine iterables)
islice(count(), 5)     # 0, 1, 2, 3, 4 (take first N from infinite)
combinations("ABC", 2) # AB, AC, BC
permutations("ABC", 2) # AB, AC, BA, BC, CA, CB
```

**Why it exists:** These patterns (chaining, cycling, taking N, combinations) are common but tedious to implement. `itertools` provides them in C — faster than writing them in Python.

**Where it's used:** Data processing pipelines, combinatorics, cycling through values, merging iterables, pagination.

**What goes wrong without it:**
- Reinventing `chain` with nested loops → slower, more code.
- `list(combinations(range(20), 10))` → 184,756 combinations in memory → could be huge. Use generators to process one at a time.
- Infinite iterators without `islice` → infinite loops.

---

## Generator Pipelines

**What:** Chain generators together — each processes data and passes it to the next. Like a Unix pipe.

```python
def numbers():
    yield from range(100)

def evens(gen):
    for n in gen:
        if n % 2 == 0:
            yield n

def squared(gen):
    for n in gen:
        yield n ** 2

# Pipeline: numbers → filter evens → square
pipeline = squared(evens(numbers()))
list(pipeline)    # [0, 4, 16, 36, 64, ...] (only even squares)
```

**Why it exists:** Without pipelines, you'd build intermediate lists at each step — 100 numbers → filter → 50 evens list → square → 50 squared list. With pipelines, each item flows through all stages without creating intermediate lists. Memory efficient for large data.

**Where it's used:** Data processing, ETL pipelines, log analysis, streaming data transformation.

**What goes wrong without it:**
- Materializing intermediate lists → high memory usage for large data.
- Order matters: `squared(evens(numbers()))` vs `evens(squared(numbers()))` → different results (squares all then filters evens vs filters evens then squares).
- Each stage must accept a generator and yield values — if one stage returns a list, the pipeline breaks the lazy evaluation.

---

## Memory Efficiency Comparison

**What:** The key advantage of generators — they use near-constant memory regardless of data size.

```python
# List approach — all in memory
sum([x**2 for x in range(10000000)])    # ~80MB for the list

# Generator approach — one value at a time
sum(x**2 for x in range(10000000))      # ~100 bytes — same result, 800,000x less memory
```

**Why it exists:** For large datasets (log files, CSV exports, database rows), you can't fit everything in memory. Generators let you process terabytes of data with kilobytes of RAM.

**Where it's used:** Processing large files, database cursors, streaming APIs, big data.

**What goes wrong without it:**
- `MemoryError` when processing large files with lists.
- Slow startup — building a huge list before you can start processing.
- Can't handle files larger than available RAM — generators can (process line by line).
