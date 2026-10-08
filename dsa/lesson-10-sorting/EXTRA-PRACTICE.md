# lesson-10-sorting — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: Insertion sort on nearly-sorted input
```python
arr = [1, 2, 3, 5, 4]   # ONE element out of place
```
Roughly how much work does insertion sort do — O(n) or O(n²)?

<details><summary>Answer</summary>
**~O(n).** For i=0..3 the inner `while arr[j] > key` fails immediately (1
comparison each). Only i=4 (key=4) shifts once past 5. Nearly-sorted input
is insertion sort's best case — the inner loop is essentially free.
</details>

---

## Check 02: Why can't comparisons beat n log n?
Sorting 4 elements by pairwise comparison — in the worst case, what's the
minimum number of comparisons needed to guarantee the right answer?

<details><summary>Answer</summary>
4 elements → 4! = 24 possible orders. Each comparison gives ≤ 1 bit;
distinguishing 24 cases needs ⌈log2 24⌉ = 5 comparisons. In general
log2(n!) ≈ n log n — that's the comparison-sort floor.
</details>

---

## Check 03: Merge order
```python
left  = [2, 5]
right = [1, 4]
```
Walk the merge. Which element is taken third?

<details><summary>Answer</summary>
**4.** 2>1 take right `1`; 2<4 take left `2`; 5>4 take right `4`; left tail
`5` appends. Output `[1,2,4,5]` — third taken is 4.
</details>

---

## Check 04: Quicksort worst case
```python
arr = [1, 2, 3, 4, 5]   # already sorted
# quicksort with pivot = arr[hi] (last element)
```
What do the partitions look like, and what's the time?

<details><summary>Answer</summary>
Every partition puts ALL n−1 elements on one side (pivot is already the
max): sizes n, n−1, n−2, ... → O(n²) comparisons and O(n) recursion depth —
the classic last-element-pivot killer. Fixed by random or median-of-three
pivot selection.
</details>

---

## Check 05: Counting sort index
```python
arr = [-3, 1, -1, 2]
counts = [0] * 6        # range -3..2 -> size 6
```
What's the index of value −3, and why is the offset needed?

<details><summary>Answer</summary>
Index = `value − min = −3 − (−3) = 0`. Without `− min` offset, `counts[-3]`
either wraps (Python's negative indexing — silently corrupting counts[3])
or is just wrong. The offset maps the value range onto indices 0..k−1.
</details>

---

## Check 06: Mixed-direction key sort
```python
records = [("bob", 75), ("amy", 90), ("cal", 90)]
print(sorted(records, key=lambda r: (r[0], -r[1])))
```
What prints — and is it what "score desc, name asc" wants?

<details><summary>Answer</summary>
`[('amy', 90), ('bob', 75), ('cal', 90)]` — sorted by NAME first, then
score. That's NOT the goal. For score-desc-primary + name-asc-tiebreak use
`key=lambda r: (-r[1], r[0])` — negate the numeric key inside one ascending
tuple.
</details>

---

## Debug Exercises — find and fix the bug

---

## Debug 01 (Easy): Insertion sort loses an element

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[i]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = arr[i]
    return arr
```

**Hint:** trace `insertion_sort([2, 1])` — the 1 overwrites the 2 before
it's saved.

<details><summary>Answer</summary>

**Bug:** `arr[i]` is read AFTER its slot was already overwritten by the
shift. `arr[1]=1`: while arr[0]=2 > arr[1]=1 → arr[1] = arr[0] = 2 →
`arr[j+1] = arr[i]` writes arr[1]... which is now 2. Result `[2,2]`.
**Fix:** save `key = arr[i]` FIRST, compare and write `key`:
```python
key = arr[i]
j = i - 1
while j >= 0 and arr[j] > key:
    arr[j + 1] = arr[j]; j -= 1
arr[j + 1] = key
```
</details>

---

## Debug 02 (Easy): Merge drops the tail

```python
def merge_two_sorted(a, b):
    merged = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i]); i += 1
        else:
            merged.append(b[j]); j += 1
    return merged
```

**Hint:** `merge_two_sorted([5, 9], [1])` — where do 5 and 9 go?

<details><summary>Answer</summary>

**Bug:** when the `while` exits, one list still has unconsumed elements —
they're silently dropped: `[5,9]` + `[1]` returns `[1]`.
**Fix:** append both tails after the loop (one is empty):
```python
merged.extend(a[i:])
merged.extend(b[j:])
```
</details>

---

## Debug 03 (Medium): Quicksort recurses on the pivot

```python
def quicksort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p)      # ???
        quicksort(arr, p + 1, hi)
```

**Hint:** the pivot at index p is already final — what does including it do?

<details><summary>Answer</summary>

**Bug:** `quicksort(lo, p)` re-partitions a range containing the pivot.
Since arr[p] is the max of that range and (with last-element pivot) lands
at p again — same call, forever: infinite recursion.
**Fix:** exclude the settled pivot: `quicksort(arr, lo, p - 1)`.
</details>

---

## Debug 04 (Medium): Merge sort — unstable merge

```python
def merge(left, right):
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:     # ???
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    ...
```

**Hint:** sorting `(name, score)` records in two passes relies on merge
being stable. What does `<` instead of `<=` break?

<details><summary>Answer</summary>

**Bug:** on `left[i] == right[j]` the `<` branch takes RIGHT first, so
equal elements swap their original order — stability broken. Two-pass
multi-key sorting (name pass, then score pass) then produces wrong order
inside score ties.
**Fix:** `if left[i] <= right[j]` — prefer the left element on ties.
</details>

---

## Debug 05 (Hard): Counting sort on negatives

```python
def counting_sort(arr):
    counts = [0] * (max(arr) + 1)
    for v in arr:
        counts[v] += 1
    ...
```

**Hint:** `counting_sort([-3, 1, -1, 2])` — does it crash, or worse?

<details><summary>Answer</summary>

**Bug:** `counts[-3]` is legal Python — it indexes the THIRD slot from the
end — so negatives silently corrupt the output instead of crashing:
-3 lands in counts[3], -1 in counts[5]... garbage, no error.
**Fix:** offset by the minimum:
```python
lo, hi = min(arr), max(arr)
counts = [0] * (hi - lo + 1)
for v in arr: counts[v - lo] += 1
# emit offset + lo
```
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: `arr = arr.sort()` throws away the list
```python
# WRONG — .sort() returns None; arr becomes None
arr = arr.sort()

# CORRECT — statement form for in-place, or sorted() for a new list
arr.sort()
arr = sorted(arr)
```

## Mistake 02: reverse=True on multi-key sorts
```python
# WRONG — flips EVERY key, not just the numeric one
sorted(records, key=lambda r: (r[1], r[0]), reverse=True)

# CORRECT — negate the numeric key inside an ascending tuple
sorted(records, key=lambda r: (-r[1], r[0]))
```

## Mistake 03: Insertion sort comparing to a moving target
```python
# WRONG — arr[i] mutates during the shift; save it first
while arr[j] > arr[i]:

# CORRECT
key = arr[i]
while j >= 0 and arr[j] > key:
```

## Mistake 04: Quicksort on sorted input with last-element pivot
```python
# DANGER — sorted/reversed input + arr[hi] pivot = O(n²) + deep recursion

# CORRECT — random pivot, or pivot = arr[(lo+hi)//2]
import random
pivot_idx = random.randint(lo, hi)
arr[pivot_idx], arr[hi] = arr[hi], arr[pivot_idx]
```

## Mistake 05: Merge sort base case / slicing bugs
```python
# WRONG — len(arr) == 1 falls through to infinite recursion
def merge_sort(arr):
    mid = len(arr) // 2   # 0 for len 1 -> left=[], right=[x] -> same call?

# CORRECT
if len(arr) <= 1:
    return arr[:]
```

## Mistake 06: Counting sort on a huge range
```python
# WRONG — k = max-min+1 = ~10^9 -> memory blows up for tiny n
counting_sort([1, 10**9, 5])

# CORRECT — counting sort only when the value RANGE is small;
# otherwise use a comparison sort
```

## Mistake 07: Stability forgotten in inversion counting
```python
# WRONG — counting (left[i] - i) on left[i] > right[j] but taking
# right first on EQUALITY over-counts (equal is NOT an inversion)
if left[i] < right[j]: take left   # takes right on ties -> counts ties!

# CORRECT — take left on ties; count only when left[i] > right[j]
if left[i] <= right[j]: take left
else: take right; inv += len(left) - i
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Bubble sort → insertion sort
### Before
```python
def sort_it(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```
### Problems
1. No early exit — runs full O(n²) even on sorted input
2. Swaps churn: each element can swap ~n times (3 assignments per swap)

### After
```python
def sort_it(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]; j -= 1
        arr[j + 1] = key
    return arr
```
One write per shift instead of a swap; ~O(n) on nearly-sorted data.
(Or at minimum add a `swapped` flag to bubble for early exit.)

---

## Refactor 02 (Medium): Double-loop sort → sorted() with a key
### Before
```python
def sort_words(words):
    # sort by length, ties alphabetical — hand-rolled bubble
    for i in range(len(words)):
        for j in range(len(words) - 1):
            if (len(words[j]), words[j]) > (len(words[j + 1]), words[j + 1]):
                words[j], words[j + 1] = words[j + 1], words[j]
    return words
```
### Problems
1. O(n²) where O(n log n) exists in one call
2. Recomputes len() ~n² times; reinvents tuple comparison

### After
```python
def sort_words(words):
    return sorted(words, key=lambda w: (len(w), w))
```
Real-world sorting is `sorted()` + the right key. Hand-rolled sorts are
for learning; production code should never contain them.

---

## Refactor 03 (Hard): O(n²) inversion count → merge-sort count
### Before
```python
def count_inversions(arr):
    inv = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv
```
### Problems
1. O(n²) — n = 10⁵ → 5·10⁹ pair checks → timeout

### After
```python
def count_inversions(arr):
    def rec(a):
        if len(a) <= 1: return a, 0
        m = len(a) // 2
        l, il = rec(a[:m]); r, ir = rec(a[m:])
        out, i, j, inv = [], 0, 0, 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]: out.append(l[i]); i += 1
            else:
                out.append(r[j]); j += 1
                inv += len(l) - i
        out += l[i:] + r[j:]
        return out, il + ir + inv
    return rec(arr)[1]
```
O(n log n) — the merge step counts every cross-half inversion in bulk.

---

## Approach Comparison — different ways to solve it

## Problem: Sort n records

### Approach 1: O(n²) simple sort
Bubble/selection/insertion. **Pros:** trivial code, no extra space, and
insertion is ~O(n) on nearly-sorted input. **Cons:** dies past ~10⁴.

### Approach 2: Merge sort
**Pros:** guaranteed O(n log n), stable, the only good linked-list sort.
**Cons:** O(n) extra space, cache-unfriendly vs quicksort.

### Approach 3: Quicksort
**Pros:** fastest in practice (in-place, cache-friendly, small constants).
**Cons:** O(n²) worst case without pivot care; not stable.

### Approach 4: Timsort / sorted()
**Winner in Python** — adaptive to existing order, stable, tuned for real
data. Reach for a hand-rolled sort only when the problem demands it.

---

## Problem: Sort with integer keys in a small range

### Approach 1: Comparison sort
O(n log n) — fine, but ignores that keys are tiny ints.

### Approach 2: Counting sort
O(n + k) — **winner when k ≈ n** (scores, ages, bytes). Loses when k is
huge (counts array too big) or keys aren't ints.

---

## Problem: Sort a nearly-sorted stream (each element within k)

### Approach 1: Insertion sort
O(n·k) worst — good for small k, simple, in place.

### Approach 2: Full sort
O(n log n) — correct but ignores the k-bound.

### Approach 3: Min-heap of size k+1
O(n log k) — **winner** for large n and small k; the next output element
is always inside the current k+1 window.
