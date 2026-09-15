# Lesson 08 — Concepts Explained (List Comprehensions & Generators)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## List Comprehension

**What:** A concise way to build a list by transforming/filtering items in one expression.

```python
# Transform
squares = [x*x for x in range(5)]        # [0, 1, 4, 9, 16]

# Filter
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Transform + filter
upper_vowels = [c.upper() for c in "hello" if c in "aeiou"]  # ['E', 'O']

# Equivalent loop:
squares = []
for x in range(5):
    squares.append(x*x)
```

**Why it exists:** Building lists from other iterables is extremely common. The comprehension expresses "map + filter" in one readable line instead of a 4-line loop.

**Where it's used:** Data transformation, filtering records, parsing, building derived collections.

**What goes wrong without it:**
- Over-nesting: `[x for row in matrix for x in row]` is valid but hard to read. More than two `for` clauses → use a regular loop.
- Putting side effects inside (e.g., `print`) → comprehension is for building a list, not for actions. Use a loop.
- Modifying the source while comprehending → unpredictable. Build from a stable iterable.

---

## Dict & Set Comprehensions

**What:** Same idea, producing a dict or set.

```python
# Dict comprehension
squares = {n: n*n for n in range(4)}       # {0:0, 1:1, 2:4, 3:9}
word_len = {w: len(w) for w in ["hi", "hello"]}  # {"hi":2, "hello":5}

# Set comprehension
unique_lens = {len(w) for w in ["a", "bb", "a", "ccc"]}  # {1, 2, 3}
```

**Why it exists:** Dicts and sets are built from data just as often as lists. These comprehensions keep that concise and consistent.

**Where it's used:** Building lookup maps, deduping with a property, inverting dicts, frequency tables.

**What goes wrong without it:**
- Dict comprehension with duplicate keys → later values overwrite earlier silently. Make sure keys are unique if that matters.
- Set comprehension drops order and duplicates — fine if that's intended, surprising if you expected a list.

---

## Generator Expression

**What:** Like a list comprehension but lazy — it produces items one at a time, on demand, using `()` instead of `[]`.

```python
squares_list = [x*x for x in range(5)]    # builds full list in memory
squares_gen  = (x*x for x in range(5))    # lazy generator

next(squares_gen)  # 0
next(squares_gen)  # 1
list(squares_gen)  # [4, 9, 16]  (remaining)

# Memory-efficient: sum without building a list
total = sum(x*x for x in range(1000000))  # no giant list created
```

**Why it exists:** A list comprehension on 1 million items builds a 1-million-item list in memory. A generator expression produces items one at a time, using almost no memory. For pipelines that feed into `sum`/`max`/`any`, this is a big win.

**Where it's used:** Feeding aggregators (`sum`, `max`, `any`, `sorted`), lazy pipelines, large data, memory-constrained environments.

**What goes wrong without it:**
- Generators are single-use: after you iterate once, it's exhausted. `list(gen)` twice → second is empty. Convert to a list if you need reuse.
- `next()` on an exhausted generator raises `StopIteration`. Use `next(gen, default)`.
- Can't index or get `len()` of a generator — it's lazy, size unknown until consumed.

---

## The `yield` Keyword (Generator Functions)

**What:** A function with `yield` is a generator. Each `yield` produces a value and pauses; calling resumes after the `yield`.

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i        # produce i, pause here
        i += 1         # resume here on next call

gen = count_up_to(3)
next(gen)   # 1
next(gen)   # 2
next(gen)   # 3
next(gen)   # StopIteration

for x in count_up_to(5):
    print(x)   # 1 2 3 4 5
```

**Why it exists:** Some sequences are huge or infinite (Fibonacci, reading a file line by line). `yield` lets you produce values lazily without building the whole collection in memory.

**Where it's used:** Streaming large files, infinite sequences, custom iteration, pipelines, lazy data processing.

**What goes wrong without it:**
- Returning a list of 10 million items → memory blowup. `yield` produces them one at a time.
- Using `return value` in a generator stops it (raises `StopIteration`); `return` with no value just ends it. Confusing `return` and `yield` breaks the sequence.
- Generator state is local and paused — debugging can be tricky because code doesn't run until you iterate.

---

## Generator Pipelines

**What:** Chain generators so each transforms a stream lazily, one item at a time.

```python
def numbers():
    yield from range(1000)

def squared(seq):
    for x in seq:
        yield x * x

def evens(seq):
    for x in seq:
        if x % 2 == 0:
            yield x

# Pipeline: only even squares, computed lazily
result = list(evens(squared(numbers())))
# At no point is the full 1000-item list held in memory twice
```

**Why it exists:** Processing large data in stages (read → parse → filter → transform) without holding every intermediate stage in memory. Each stage pulls one item through.

**Where it's used:** ETL, log processing, streaming analytics, data transformation pipelines.

**What goes wrong without it:**
- Building each stage as a full list → multiple copies in memory, slow for big data.
- Forgetting that a generator is exhausted after one pass → second pipeline use is empty.
- Order matters: `evens(squared(...))` vs `squared(evens(...))` give different results.

---

## itertools Basics

**What:** `itertools` provides fast, memory-efficient iterator-building functions.

```python
from itertools import chain, islice, count, takewhile, product

# chain: combine iterables
list(chain([1,2], [3,4]))           # [1, 2, 3, 4]

# islice: slice a generator (lazy)
list(islice(count(), 5))            # [0, 1, 2, 3, 4]  (count() is infinite)

# takewhile: take until condition fails
list(takewhile(lambda x: x < 5, count()))  # [0, 1, 2, 3, 4]

# product: cartesian product
list(product([1,2], ['a','b']))     # [(1,'a'),(1,'b'),(2,'a'),(2,'b')]
```

**Why it exists:** Common iteration patterns (chaining, slicing lazily, combinations, infinite counters) are tedious to write by hand and easy to get wrong. `itertools` gives correct, fast, memory-efficient implementations.

**Where it's used:** Combinatorics, streaming, pagination of generators, grouping, advanced data processing.

**What goes wrong without it:**
- `list(count())` on an infinite generator → hangs forever / memory blowup. Always bound it with `islice` or `takewhile`.
- Reimplementing `chain`/`product` by hand → slower and buggy.
- `islice` doesn't support negative indices like list slicing does.

---

## When to Use Comprehension vs Loop vs Generator

**What:** A decision guide.

```python
# List comprehension: simple transform/filter, you need the whole list
squares = [x*x for x in range(10)]

# Generator expression: feeding an aggregator, or huge data
total = sum(x*x for x in range(1000000))

# Regular loop: complex logic, multiple statements, side effects
result = []
for x in data:
    if validate(x):
        transformed = complex_logic(x)
        result.append(transformed)
```

**Why it exists:** Choosing the right tool keeps code readable and efficient. Comprehensions for simple builds, generators for memory efficiency, loops for complexity.

**Where it's used:** Every data-processing decision.

**What goes wrong without it:**
- Forcing complex logic into a comprehension → unreadable one-liner. Use a loop.
- Building a huge list when you only need `sum`/`max` → wasted memory. Use a generator expression.
- Using a generator where you need random access / multiple passes → convert to a list.
