# lesson-13-iterators-generators — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Iterator Protocol
```python
class Range3:
    def __iter__(self):
        yield 0; yield 1; yield 2

for x in Range3():
    print(x)
```
<details><summary>Answer</summary>
```
0
1
2
```
`__iter__` can be a generator — each `yield` produces a value.
</details>

## Check 02: namedtuple vs tuple
```python
from collections import namedtuple
P = namedtuple("P", "x y")
p = P(1, 2)
print(p[0], p.x)
```
<details><summary>Answer</summary>
`1 1` — namedtuples support BOTH index access (like tuples) AND attribute access.
</details>

## Check 03: deque vs list
```python
from collections import deque
d = deque([1, 2, 3])
d.appendleft(0)
print(d)
```
<details><summary>Answer</summary>
`deque([0, 1, 2, 3])` — deque supports O(1) append/pop at both ends. List is O(n) at the front.
</details>

## Check 04: Chain
```python
from itertools import chain
for x in chain([1, 2], [3, 4]):
    print(x)
```
<details><summary>Answer</summary>
```
1
2
3
4
```
`chain` combines iterables without creating a new list.
</details>

## Check 05: zip_longest
```python
from itertools import zip_longest
for a, b in zip_longest([1, 2], [3, 4, 5]):
    print(a, b)
```
<details><summary>Answer</summary>
```
1 3
2 4
None 5
```
`zip_longest` fills missing values with None (or a specified fillvalue). Regular `zip` stops at the shortest.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Iterator Missing __iter__
```python
class Counter:
    def __init__(self, n): self.n = n
    def __next__(self):
        if self.n <= 0: raise StopIteration
        self.n -= 1
        return self.n + 1
```
<details><summary>Answer</summary>
**Bug:** No `__iter__` method — can't be used in for loops.
**Fix:** Add `def __iter__(self): return self`.
</details>

## Debug 02 (Medium): Generator Not Resumable
```python
def counter():
    n = 0
    while True:
        yield n
        n += 1

gen = counter()
list(gen)  # [0, 1, 2, ...] infinite!
```
<details><summary>Answer</summary>
**Bug:** Infinite generator — `list()` tries to collect all values, hangs forever.
**Fix:** Add a limit parameter or use `itertools.islice(gen, 10)`.
</details>

## Debug 03 (Hard): namedtuple Immutability
```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
p.x = 10
```
<details><summary>Answer</summary>
**Bug:** namedtuples are immutable — can't assign to fields.
**Fix:** Use `p._replace(x=10)` which returns a NEW namedtuple.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Not implementing __iter__
```python
# WRONG — only __next__, can't use in for loop
class MyIter:
    def __next__(self): ...

# CORRECT
class MyIter:
    def __iter__(self): return self
    def __next__(self): ...
```

## Mistake 02: Infinite generator without exit
```python
# DANGEROUS — hangs
def gen():
    while True:
        yield 1
list(gen())  # infinite!

# FIX — add a limit
def gen(n):
    for _ in range(n):
        yield 1
```

## Mistake 03: Using list when deque is needed
```python
# SLOW — O(n) for front operations
queue = [1, 2, 3]
queue.insert(0, 0)  # O(n)

# FAST — O(1)
from collections import deque
queue = deque([1, 2, 3])
queue.appendleft(0)  # O(1)
```

## Mistake 04: Modifying namedtuple
```python
# WRONG
p.x = 10  # AttributeError

# CORRECT
p = p._replace(x=10)
```

## Mistake 05: Not using Counter
```python
# VERBOSE
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1

# BETTER
from collections import Counter
counts = Counter(items)
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Iterator Class for Simple Sequence
### Before
```python
class Range:
    def __init__(self, n): self.n = n; self.i = 0
    def __iter__(self): return self
    def __next__(self):
        if self.i >= self.n: raise StopIteration
        v = self.i; self.i += 1; return v
```
### After
```python
def range_gen(n):
    for i in range(n):
        yield i
```

## Refactor 02 (Medium): Building List for Sum
### Before
```python
total = sum([x * 2 for x in data])
```
### After
```python
total = sum(x * 2 for x in data)
```

## Refactor 03 (Hard): Manual Counter
### Before
```python
class Counter:
    def __init__(self): self.n = 0
    def __next__(self):
        self.n += 1
        return self.n
    def __iter__(self): return self
```
### After
```python
from itertools import count
# count() is infinite counter
```

---

## Approach Comparison — different ways to solve it

## Problem: Custom Iterator

### Approach 1: Iterator protocol
```python
class Range:
    def __init__(self, n): self.n = n; self.i = 0
    def __iter__(self): return self
    def __next__(self):
        if self.i >= self.n: raise StopIteration
        val = self.i; self.i += 1; return val
```

### Approach 2: Generator
```python
def range_gen(n):
    for i in range(n):
        yield i
```

**Winner:** Approach 2 — generators are simpler for most iterators.

---

## Problem: Queue

### Approach 1: list
```python
q = []
q.append(1); q.append(2)
q.pop(0)  # O(n) — shifts all elements
```

### Approach 2: deque
```python
from collections import deque
q = deque()
q.append(1); q.append(2)
q.popleft()  # O(1)
```

**Winner:** Approach 2 — deque is O(1) for both ends.
