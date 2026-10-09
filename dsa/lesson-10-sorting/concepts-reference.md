# Lesson 10 — Concepts Explained (Sorting)

> Read this before solving the problems. Each concept explains:
> **What it is** · **Why it exists** · **Where it's used** · **What goes wrong** without it.
> Then a worked example with real numbers, code, and expected output.

---

## Why Sorting Matters — and the n·log n Floor

**What it is:** Sorting puts elements in a defined order (usually ascending).
It's the most-studied algorithm problem ever, and here's the deep fact: any
sort that works by comparing pairs of elements needs at least **O(n log n)**
comparisons in the worst case. Intuition: n elements have n! possible
orders; each comparison yields at most 1 bit of information (yes/no), and
distinguishing n! outcomes needs log2(n!) ≈ n log n comparisons.

**Why it exists:** Sorted data is a *force multiplier* — binary search needs
it (lesson 09), dedup is trivial on it, "k-th smallest" becomes indexing,
merging datasets becomes a linear walk. Pay O(n log n) once, unlock O(log n)
queries forever.

**Where it's used:** Databases (indexes, ORDER BY, merge joins), search
engines, scheduling, ranking, and as the hidden preprocessing step inside
two-pointer and greedy solutions.

**What goes wrong without it:**
- Searching unsorted → O(n) every query instead of O(log n).
- Trying to "sort" by hand in problem code → you re-derive O(n²) or a buggy
  comparison loop when `sorted()` exists.
- Assuming sorting is free — it isn't: don't sort inside a hot loop, and
  don't sort if the input is already (nearly) sorted.

---

## The O(n²) Trio: Bubble, Selection, Insertion

**What it is:** Three simple sorts, all quadratic worst-case, different
personalities:

- **Bubble:** repeatedly swap adjacent out-of-order pairs; big elements
  "bubble" to the end. After pass k, the last k elements are final.
- **Selection:** find the minimum of the unsorted region, swap it into
  position. Always ~n²/2 comparisons; at most n−1 swaps (minimum writes).
- **Insertion:** grow a sorted prefix — take arr[i], shift bigger elements
  right, insert into the gap.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:   # shift right while bigger
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

**Why it exists:** They're not just bad sorts — insertion sort has a
superpower: on nearly-sorted input the inner loop exits immediately, making
it ~O(n). Tiny arrays also have no recursion/cache overhead. That's why
real-world hybrid sorts (Python's Timsort, Java's dual-pivot quicksort)
switch to insertion sort on small runs.

**Where it's used:** Insertion — small subarrays inside hybrid sorts,
nearly-sorted streams. Selection — when writes are expensive (EEPROM,
flash memory): O(n) swaps vs O(n²) for insertion/bubble.

**What goes wrong without it:**
- Using an O(n²) sort on n = 10⁵+ → 10¹⁰ ops → timeout.
- Choosing insertion sort for REVERSED input — every element shifts past
  every other → maximum O(n²).
- Bubble-sort early-exit forgotten: if a pass makes zero swaps the array is
  sorted — without the flag you always pay full O(n²).

**Worked example (real numbers):** insertion sort on `[5, 2, 4, 1]`

```
i=1 key=2: shift 5 -> [5,5,4,1] insert -> [2,5,4,1]
i=2 key=4: shift 5 -> [2,5,5,1] insert -> [2,4,5,1]
i=3 key=1: shift 5,4,2 -> [2,4,5,5]... insert -> [1,2,4,5]
```

Expected output: `[1, 2, 4, 5]`

---

## Merge Sort — Guaranteed O(n log n) via Divide & Conquer

**What it is:** Split the array in half. Recursively sort each half. Merge
the two sorted halves with the two-pointer walk (take the smaller front
element each step). Recurrence: T(n) = 2T(n/2) + O(n) → O(n log n), ALWAYS
— no bad-pivot surprise.

```
[5, 2, 4, 1]
  split -> [5,2] [4,1]
  sort  -> [2,5] [1,4]
  merge -> 1 (from right), 2 (left), 4 (right), 5 -> [1,2,4,5]
```

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)   # two-pointer merge, O(n)
```

**Why it exists:** It's the sort you reach for when a guaranteed bound
matters (linked lists — where it needs only O(1) extra space — external
sorting of files too big for RAM, stable ordering). Every merge level does
exactly n work, and there are log n levels.

**Where it's used:** `git`'s internal sort, Java's `Arrays.sort` for
objects, linked-list sorting, counting inversions, external merge sort on
data exceeding memory.

**What goes wrong without it:**
- Forgetting it's O(n) EXTRA space — merging needs an output buffer.
  In-place merge sort exists but is rarely worth the complexity.
- Base case `len(arr) <= 1` missing → infinite recursion.
- Taking `right` on ties in merge breaks STABILITY — take `left[i] <=
  right[j]` so equal elements keep their input order (crucial for
  multi-pass key sorting).

**Worked example (real numbers):** merge `[2,5]` and `[1,4]`

```
i=0 j=0: 2>1  -> take right 1   out=[1]
i=0 j=1: 2<4  -> take left 2    out=[1,2]
i=1 j=1: 5>4  -> take right 4   out=[1,2,4]
j done; extend left tail        out=[1,2,4,5]
```

Expected output: `[1, 2, 4, 5]`

---

## Quick Sort — Partition Around a Pivot

**What it is:** Pick a pivot, partition so smaller elements go left and
bigger go right (pivot lands in its FINAL position), recurse on both sides.
Lomuto's partition: pivot = arr[hi]; keep boundary i = last index holding
a ≤-pivot value; scan j, extend the boundary on each small element; swap
the pivot into i+1.

```python
def quicksort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)   # pivot now at final index p
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)
```

**Why it exists:** Average O(n log n) with TINY constants — the inner loop
is a cache-friendly linear scan, and it sorts in place (O(log n) stack
space). Worst case is O(n²) — when every pivot is the min or max (sorted
input + last-element pivot is the classic killer). Random pivot or
median-of-three makes that essentially impossible.

**Where it's used:** C's `qsort`, most languages' primitive-type sorts,
quickselect (k-th smallest in average O(n)). Python's `sorted()` is NOT
quicksort — it's **Timsort** (merge sort + insertion sort hybrid,
engineered for real-world partially-ordered data, O(n) best case).

**What goes wrong without it:**
- Worst-case input: sorting an already-sorted array with `pivot = arr[hi]`
  → partitions are 0 vs n−1 → O(n²) and a stack overflow on big inputs.
- Partition bug: boundary `i` starts at `lo - 1`, not `lo` — starting at
  `lo` treats arr[lo] as already-placed-small without checking it.
- Recursing on `[lo, p]` and `[p+1, hi]` — including p twice → infinite
  recursion. The pivot at p is DONE; recurse `[lo, p−1]` and `[p+1, hi]`.

**Worked example (real numbers):** Lomuto on `[4, 1, 3, 9, 7]`, pivot=7

```
i=-1
j=0: 4<=7 -> i=0 swap a[0]<->a[0]   [4,1,3,9,7]
j=1: 1<=7 -> i=1 swap               [4,1,3,9,7]
j=2: 3<=7 -> i=2 swap               [4,1,3,9,7]
j=3: 9>7  -> skip
final: swap a[3]<->a[4]             [4,1,3,7,9]  pivot at index 3
```

Expected output: `3` (pivot index), array `[4, 1, 3, 7, 9]`

---

## Counting Sort — Beating the n·log n Floor (When Keys Are Small Ints)

**What it is:** The n log n bound applies ONLY to comparison sorts. If keys
are integers in a small range [min, max], skip comparisons entirely: count
how many times each value occurs, then emit each value count[v] times in
order. O(n + k) where k = max − min + 1.

```python
def counting_sort(arr):
    lo, hi = min(arr), max(arr)
    counts = [0] * (hi - lo + 1)     # index = value - lo  <- the OFFSET
    for v in arr:
        counts[v - lo] += 1
    out = []
    for offset, c in enumerate(counts):
        out.extend([offset + lo] * c)
    return out
```

**Why it exists:** Linear time! When k ≈ n (scores 0–100, ages, byte values,
small enum ranges) it crushes every comparison sort. Radix sort extends
the idea digit-by-digit to large keys; bucket sort handles floats.

**Where it's used:** Radix sort's inner pass, histogram problems, sorting
by small integer keys (exam scores, ages, ASCII characters).

**What goes wrong without it:**
- NEGATIVE values: `counts[-3]` isn't index -3 — you need the `value - min`
  offset. Indexing raw values crashes or wraps silently (Python negative
  indexing!) producing wrong output with no error.
- Huge range: k = 10⁹ for three elements → the counts array eats gigabytes.
  O(n + k) is only good when k is small.
- Non-integer keys can't be indices — need comparison sorts or buckets.

**Worked example (real numbers):** `[−3, 1, −1, 2]`, min=−3, max=2

```
counts index:  0   1   2   3   4   5    (value -3..2)
counts      : [1,  0,  1,  0,  1,  1]   <- -3,-1,1,2 each once
emit: -3(×1) -1(×1) 1(×1) 2(×1) -> [-3,-1,1,2]
```

Expected output: `[-3, -1, 1, 2]`

---

## Python's sorted() / list.sort() — Keys, Stability, Timsort

**What it is:** Python sorts with **Timsort** — adaptive merge sort that
detects natural runs (already-ordered stretches) and uses insertion sort on
small pieces. O(n log n) worst, O(n) on nearly-sorted input, and STABLE:
equal elements keep their original order.

- `sorted(iterable)` → NEW list (works on any iterable)
- `list.sort()` → in place, returns None (lists only)
- `key=f` → sort by f(x); tuples compare element-wise
- `reverse=True` → descending

```python
sorted(words, key=len)                    # by length
sorted(words, key=lambda w: (len(w), w))  # length, then alpha
sorted(records, key=lambda r: -r.score)   # numeric desc via negation
students.sort(key=lambda s: s.grade)      # in place
```

**Why it exists:** Two killer features. (1) `key` tuples handle multi-key
sorts declaratively. (2) STABILITY enables multi-pass sorting — sort by
secondary key first, then primary; ties in the primary keep the secondary
order. That's how SQL `ORDER BY a, b` works conceptually.

**Where it's used:** Literally everywhere in Python — and "sort by multiple
fields" is a guaranteed interview sub-problem.

**What goes wrong without it:**
- `list.sort()` returns None — `arr = arr.sort()` destroys your data. Use
  `sorted(arr)` for a value, or call `arr.sort()` as a statement.
- Mixed directions: `(score, name)` can't do score-desc + name-asc with one
  ascending tuple — negate the number: `(-score, name)`, or two stable
  passes. `reverse=True` flips BOTH keys.
- Sorting dicts/sets directly gives keys — use `d.items()` and a key on
  `item[1]` for value ordering.
- Decorating keys inside a comparator — Python removed `cmp=`; use key
  functions (functools.cmp_to_key only as a last resort).

**Worked example (real numbers):**

```python
records = [("bob", 75), ("amy", 90), ("cal", 90)]
print(sorted(records, key=lambda r: (-r[1], r[0])))
```

Expected output:
```
[('amy', 90), ('cal', 90), ('bob', 75)]
```

---

## Picking the Right Sort

| Situation | Winner | Why |
|---|---|---|
| general purpose, Python | `sorted()` / `.sort()` | Timsort: stable, adaptive, tuned |
| guaranteed O(n log n), no memory | heapsort (rare in Python) | merge needs O(n) space |
| linked list | merge sort | nodes reorder by pointers, O(1) extra |
| small int keys, small range | counting/radix | O(n + k) beats the n log n floor |
| nearly sorted / tiny arrays | insertion sort | ~O(n) adaptive, zero overhead |
| k-th smallest, not full sort | quickselect / heap | average O(n) beats O(n log n) sort |
| elements within k of sorted spot | heap of size k+1 | O(n log k) |
| writes expensive (flash) | selection sort | ≤ n−1 swaps |

---

## Quick Reference

| Sort | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| bubble | O(n)* | O(n²) | O(n²) | O(1) | yes |
| selection | O(n²) | O(n²) | O(n²) | O(1) | no |
| insertion | O(n) | O(n²) | O(n²) | O(1) | yes |
| merge | O(n log n) | O(n log n) | O(n log n) | O(n) | yes |
| quick (random pivot) | O(n log n) | O(n log n) | O(n²) | O(log n) | no |
| counting | O(n + k) | O(n + k) | O(n + k) | O(k) | (output rebuild) |
| Timsort (Python) | O(n) | O(n log n) | O(n log n) | O(n) | yes |

*bubble's O(n) best case needs the swapped-flag early exit.
