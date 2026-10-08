# 10 — Iterators vs Generators

> **Interview question:** "What's the difference between an iterator and a generator? Write a generator and explain what `yield` does."
> **What the interviewer is really testing:** Do you understand lazy evaluation and Python's iteration protocol, or have you just memorized "generators save memory"?

## Theory — what it is

An **iterable** is anything you can loop over — a list, string, dict, file. It has an `__iter__` method that hands back an iterator. An **iterator** is the object that actually does the walking: it has a `__next__` method that returns one item at a time and raises `StopIteration` when it's done. A `for` loop is just sugar for "call `iter()` once, then call `next()` until `StopIteration`."

A **generator** is a shortcut for writing an iterator. You write a normal-looking function but use `yield` instead of `return`. The moment Python sees `yield` in a function body, it turns that function into a generator function — you never write `__iter__`, `__next__`, or `StopIteration` logic yourself.

`yield` means "pause here, hand this value to the caller, and freeze exactly where I was." On the next `next()` call, the function resumes right after the `yield` with all its local variables intact. When the function finally returns (or just ends), Python raises `StopIteration` for you.

This pause/resume behavior is called **laziness**: values are produced one at a time, on demand — not all upfront.

## Why it was needed

Two problems. First, **memory**: if you want to process a billion rows from a file, building a `list` means holding a billion items in RAM. An iterator produces one row at a time, so memory stays flat no matter the input size.

Second, **ergonomics**: writing an iterator class by hand is painful — you need `__iter__`, `__next__`, instance attributes to track position, and `StopIteration` handling. Generators give you the same laziness in three lines: the function's local variables *are* the state, and `yield` is the pause point.

## Where it's used in a real project

- **Streaming large files**: `for line in open("big.log")` — the file object is an iterator; it never loads the whole file.
- **Paginated APIs / DB cursors**: `yield` rows as you fetch each page, so callers consume results without waiting for every page.
- **Data pipelines**: `sum(x * x for x in stream)` — a generator expression feeds `sum` one item at a time.
- **Built-ins**: `range`, `enumerate`, `zip`, `reversed` are all lazy — `range(10**9)` doesn't allocate a billion ints.

## Diagram

```
iterable: [1, 2, 3]                    generator function:
      |                                 def gen():
   iter()  ->  iterator                    yield 1   <- send 1 out, PAUSE
      |           |                        yield 2   <- send 2 out, PAUSE
      |        next() -> 1                 yield 3   <- send 3 out, PAUSE
      |        next() -> 2              (return)  -> StopIteration
      |        next() -> 3
      |        next() -> StopIteration         ^
      v                                        |
 ALL values live in RAM                function suspended between
 at once, from the start               values; locals preserved
```

## Code — explained

```python
def countdown(n):
    while n > 0:
        yield n          # (a) pause here, hand n to the caller
        n -= 1           # (b) next() resumes right here
    # (c) falling off the end -> StopIteration, automatically

c = countdown(3)         # (d) NOTHING in the body runs yet!
print(next(c))           # 3
print(next(c))           # 2
print(next(c))           # 1
# next(c) would now raise StopIteration

for x in countdown(2):   # (e) the for-loop calls iter()/next() for you
    print(x)             # prints 2, then 1
```

Line-by-line:

1. `def countdown(n)` — because the body contains `yield`, calling it does **not** run the body; it returns a generator object.
2. `c = countdown(3)` — `c` is a generator. `n` is stored, but the `while` hasn't executed once.
3. First `next(c)` — runs until the first `yield`, sends `3` out, freezes the frame.
4. Second `next(c)` — resumes at `n -= 1`, loops, `yield`s `2`. Same for `1`.
5. When `n` hits 0 the `while` exits, the function ends, and Python raises `StopIteration` — the `for` loop catches it silently and stops.

The same countdown as a **hand-written iterator class**, for contrast — this is what the generator saves you from:

```python
class Countdown:
    def __init__(self, n):
        self.n = n                     # state lives on the instance

    def __iter__(self):
        return self                    # an iterator returns itself

    def __next__(self):
        if self.n <= 0:
            raise StopIteration        # we must signal the end manually
        self.n -= 1
        return self.n + 1

print(list(Countdown(3)))              # [3, 2, 1] — same result, 5x the code
```

Notice the bookkeeping the generator hid: `self.n` replaces the local variable, `__next__` replaces `yield`, and `raise StopIteration` replaces "function ends."

## Problems

### Easy — Squares on demand
**Problem:** Write a generator `squares(n)` that yields `1², 2², ..., n²`.
**Try this input:** `list(squares(5))`
**Expected output:** `[1, 4, 9, 16, 25]`
**Solution:**
```python
def squares(n):
    for i in range(1, n + 1):
        yield i * i

print(list(squares(5)))   # [1, 4, 9, 16, 25]
```
**Logic explained:**
1. `range(1, n + 1)` walks `i` from 1 to 5.
2. Each iteration hits `yield i * i`, pausing and emitting one square.
3. `list(...)` keeps calling `next()` until `StopIteration`, collecting the yielded values.

### Medium — Infinite Fibonacci
**Problem:** Write `fib()`, a generator that yields Fibonacci numbers `0, 1, 1, 2, 3, 5, ...` forever. (This is only possible because generators are lazy — an infinite list can't exist.)
**Try this input:** take the first 8 values.
**Expected output:** `[0, 1, 1, 2, 3, 5, 8, 13]`
**Solution:**
```python
from itertools import islice

def fib():
    a, b = 0, 1
    while True:          # never ends — fine, because it's lazy
        yield a
        a, b = b, a + b  # slide the window forward

print(list(islice(fib(), 8)))   # [0, 1, 1, 2, 3, 5, 8, 13]
```
**Logic explained:**
1. `a, b` hold the current and next Fibonacci number.
2. `yield a` emits the current one, then `a, b = b, a + b` shifts both forward.
3. `islice` grabs exactly 8 values — without it, `list(fib())` would never finish.

### Hard — Lazy batching
**Problem:** Write `batches(items, size)`, a generator that yields lists of at most `size` items — e.g. chunking records before bulk-inserting into a database. It must work on any iterable, not just lists.
**Try this input:** `list(batches(range(7), 3))`
**Expected output:** `[[0, 1, 2], [3, 4, 5], [6]]`
**Solution:**
```python
def batches(items, size):
    batch = []
    for x in items:            # works on ANY iterable, lazily
        batch.append(x)
        if len(batch) == size:
            yield batch        # hand over a full batch
            batch = []         # start a fresh one
    if batch:                  # flush the leftover partial batch
        yield batch

print(list(batches(range(7), 3)))   # [[0, 1, 2], [3, 4, 5], [6]]
```
**Logic explained:**
1. Accumulate items into `batch` one at a time — never more than `size` in memory.
2. The moment `batch` fills, `yield` it and reset.
3. After the loop, a non-empty leftover `batch` means a partial final chunk — yield it too.
4. If `items` were a 10-GB stream, this still uses ~`size` elements of memory.

## The 30-second interview answer

"An iterator is any object implementing `__next__`, producing values one at a time and raising `StopIteration` at the end; an iterable is anything `iter()` can turn into one. A generator is a function with `yield` — Python auto-builds the iterator machinery: each `yield` pauses the function, emits a value, and `next()` resumes it where it left off. The payoff is laziness — I can stream a billion-row file with constant memory. If I had to write that by hand I'd need a class with `__iter__`, `__next__`, and manual state; a generator does it in three lines."

## Follow-up trap

**"Can you iterate a generator twice?"** — No. A generator is single-use: once exhausted, every `next()` raises `StopIteration` forever. If you need multiple passes, either materialize it (`items = list(gen)`) or call the generator *function* again for a fresh generator.

A second classic: **"How do you push a value INTO a generator?"** — `gen.send(x)`; inside the generator, the `yield` *expression* evaluates to whatever was sent (`received = yield produced`). That's the foundation of coroutines/`asyncio`. Even if you've never used `send`, knowing it exists — and that `yield` can be an expression, not just a statement — signals real depth.
