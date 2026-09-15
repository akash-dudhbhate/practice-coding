# Lesson 05 — Concepts Explained (Control Flow & Loops)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## if / elif / else

**What:** Conditionals that run different code based on whether a condition is true.

```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
# grade -> "B"
```

`if` checks the first condition. `elif` (else-if) checks more conditions only if the previous ones were false. `else` runs when nothing else matched. Only ONE branch runs.

**Why it exists:** Programs must make decisions — different inputs need different handling. Without conditionals, every run does exactly the same thing.

**Where it's used:** Validation, grading, menu selection, error handling, game logic, business rules.

**What goes wrong without it:**
- Using many `if`s instead of `elif`: every `if` is checked independently, so multiple branches can run when you meant only one.
- Forgetting `else` when you need a default → variable never gets assigned → `NameError` later.
- `=` vs `==`: `if x = 5` is a syntax error in Python (lucky), but in logic `if x == 5` is the comparison. Mixing assignment and comparison is a classic bug.

---

## for Loops

**What:** A `for` loop iterates over a sequence (list, string, range, dict, etc.), running the block once per item.

```python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for char in "hello":
    print(char)

for key, value in {"a": 1, "b": 2}.items():
    print(key, value)
```

**Why it exists:** Processing every item in a collection is one of the most common tasks. `for` lets you write 3 lines that handle any number of items instead of copy-pasting.

**Where it's used:** Processing records, transforming data, aggregating totals, searching, generating output.

**What goes wrong without it:**
- Modifying a list while iterating (`for x in lst: lst.remove(x)`) skips items unpredictably. Iterate over a copy or build a new list.
- Using `range(len(lst))` when you don't need the index — works but is less readable than iterating directly.
- Infinite loop if you accidentally iterate over something that keeps growing.

---

## while Loops

**What:** A `while` loop repeats as long as a condition stays true. You control when the condition becomes false.

```python
count = 0
while count < 5:
    print(count)
    count += 1          # MUST update, or infinite loop

# Reading input until valid
password = ""
while password != "secret":
    password = input("Password: ")
```

**Why it exists:** You don't always know in advance how many iterations you need — "keep asking until the user enters valid input," "keep processing until the queue is empty." `while` handles unknown iteration counts.

**Where it's used:** Input validation, game loops, polling, processing until a sentinel value, retry logic.

**What goes wrong without it:**
- **Infinite loop**: forgetting to update the condition variable (`count += 1`). The loop runs forever, freezing the program.
- Off-by-one: `while count <= 5` runs 6 times (0–5) when you wanted 5. Check boundaries carefully.
- Condition that's never true → loop body never runs (sometimes intended, sometimes a bug).

---

## break and continue

**What:** `break` exits the loop immediately. `continue` skips the rest of the current iteration and jumps to the next.

```python
# break: find first even number, then stop
for n in [1, 3, 5, 4, 7]:
    if n % 2 == 0:
        print(f"Found even: {n}")
        break

# continue: skip odd numbers
for n in range(6):
    if n % 2 != 0:
        continue        # skip rest, go to next n
    print(n)            # prints 0, 2, 4
```

**Why it exists:** Sometimes you want to stop early (found what you needed) or skip items (filtering). Without these, you'd need extra flags and nested conditionals.

**Where it's used:** Search (stop when found), validation (skip invalid entries), early exit on error, filtering during iteration.

**What goes wrong without it:**
- Using `break` in the wrong place exits the loop too early, missing later items.
- `continue` inside a `while` loop placed BEFORE the increment → infinite loop (the increment never runs).
- Overusing `break`/`continue` makes loop logic hard to follow — sometimes a cleaner condition or a separate function is better.

---

## range()

**What:** `range()` generates a sequence of numbers without storing them all in memory.

```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5   (start inclusive, stop exclusive)
range(0, 10, 2) # 0, 2, 4, 6, 8   (step of 2)
range(10, 0, -1)# 10, 9, 8, ..., 1 (counting down)
list(range(3))  # [0, 1, 2]  (materialize it)
```

**Why it exists:** You often need a sequence of indices or counted repetitions. `range` produces them lazily (memory-efficient) instead of building a full list.

**Where it's used:** Counted loops, generating indices, repeating an action N times, stepping through ranges.

**What goes wrong without it:**
- `range(5)` gives 0–4, NOT 0–5. Off-by-one is the most common `range` bug.
- `range(5, 0)` is empty (default step is +1, can't go from 5 to 0). Use `range(5, 0, -1)`.
- Iterating `range(1000000)` is fine (lazy); converting to `list(range(1000000))` wastes memory.

---

## enumerate()

**What:** `enumerate()` gives you both the index and the value while looping.

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# 0 apple / 1 banana / 2 cherry

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)   # starts counting at 1
```

**Why it exists:** When you need both the position and the item, `enumerate` is cleaner and less error-prone than `range(len(lst))` + indexing.

**Where it's used:** Numbered output, tracking position while processing, building indexed data.

**What goes wrong without it:**
- `for i in range(len(lst)): item = lst[i]` — works but is verbose and easy to get the index wrong.
- Forgetting `enumerate` returns tuples — `for i, x in enumerate(...)` unpacks correctly; `for pair in enumerate(...)` gives `(0, item)` tuples.

---

## Nested Loops

**What:** A loop inside another loop. The inner loop runs fully for each iteration of the outer loop.

```python
for i in range(3):          # outer
    for j in range(3):      # inner — runs 3 times per outer iteration
        print(i, j)
# 0 0 / 0 1 / 0 2 / 1 0 / 1 1 / 1 2 / 2 0 / 2 1 / 2 2  (9 total)
```

**Why it exists:** Some problems are inherently 2D — grids, matrices, comparing every pair, combinations. Nested loops express that naturally.

**Where it's used:** Grid/matrix processing, pairwise comparison, generating combinations, nested data structures.

**What goes wrong without it:**
- O(n²) performance: a nested loop over 10,000 items = 100 million operations. Works on small data, freezes on large data.
- `break` only exits the INNER loop, not the outer. To break out of both, use a flag variable or `return` from a function.
- Confusing inner/outer loop variables — using `i` for both inner and outer shadows one and causes wrong results.

---

## Loop Else & Early Patterns

**What:** Python's `for`/`while` can have an `else` that runs only if the loop completed WITHOUT hitting `break`.

```python
for n in [2, 4, 6, 8]:
    if n % 2 != 0:
        print("Found odd")
        break
else:
    print("All even")   # runs because no break occurred
```

**Why it exists:** It's a clean way to express "search and if-not-found" logic without a separate flag variable.

**Where it's used:** Search loops (found vs not found), validation (all items valid?).

**What goes wrong without it:**
- The `else` runs on normal loop completion AND when the loop body never runs (empty iterable). This surprises people.
- Many find `for/else` confusing — using a flag variable or returning from a function is often clearer. Know it exists but use judiciously.

---

## Accumulator Pattern

**What:** Keep a running total/result and update it each iteration.

```python
total = 0
for n in [10, 20, 30]:
    total += n          # total goes 0 -> 10 -> 30 -> 60
print(total)            # 60

# Building a string
result = ""
for char in "abc":
    result += char.upper()
# result -> "ABC"

# Building a list
squares = []
for n in range(4):
    squares.append(n * n)
# squares -> [0, 1, 4, 9]
```

**Why it exists:** Most loops that compute something use this pattern — sum, product, concatenation, filtered collection. It's the foundation of aggregation.

**Where it's used:** Summing prices, building output strings, collecting filtered results, counting.

**What goes wrong without it:**
- Forgetting to initialize the accumulator (`total = 0`) before the loop → `NameError`.
- Initializing inside the loop → resets every iteration, you only get the last value.
- `total = total + n` vs `total += n` — same thing, but the latter is clearer and faster for mutable types.
