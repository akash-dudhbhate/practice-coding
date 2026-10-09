# 11 — Python's sorted() and .sort(): Timsort, keys, lambdas

> 6-minute read. The one you'll actually type every day.

## The idea, plain words

You will (almost) never hand-write a sort in Python. `sorted()` runs
**Timsort** — a hybrid merge + insertion sort engineered for real-world,
partially-ordered data: O(n log n) worst case, **O(n) on nearly-sorted
input**, and **stable** (chapter 02's superpower, built in).

Two functions, then the `key=` trick:

- `sorted(iterable)` → returns a **new** list, works on anything
- `list.sort()` → sorts **in place**, returns `None`, lists only
- `key=f` → sort by `f(x)` instead of `x`; `reverse=True` → descending

## Watch it happen — multi-field sort, traced

```python
records = [("bob", 75), ("amy", 90), ("cal", 90)]
print(sorted(records, key=lambda r: (-r[1], r[0])))
```

Output:

```
[('amy', 90), ('cal', 90), ('bob', 75)]
```

How the key works: each record becomes a tuple `(-score, name)`. Tuples
compare **element by element** — first by `-score` (so 90s beat 75 — the
minus flips to descending), ties then fall through to `name` ascending:
`amy` < `cal`. Two sort rules, one line.

More everyday keys — try it:

```python
words = ["pear", "kiwi", "banana", "fig"]
print(sorted(words, key=len))                    # by length
print(sorted(words, key=lambda w: (len(w), w)))  # length, then alpha

pairs = [("a", 2), ("b", 1)]
pairs.sort(key=lambda p: p[1])                   # in place
print(pairs)
```

Output:

```
['fig', 'pear', 'kiwi', 'banana']
['fig', 'kiwi', 'pear', 'banana']
[('b', 1), ('a', 2)]
```

## Why it exists

`key=` tuples turn "sort by A, then B, then C" into a declarative one-
liner — the single most common interview sub-task. And because Timsort
exploits natural runs, `sorted()` on almost-sorted real data is nearly
free.

## Where it's used

Everywhere in Python. Sorting dict items by value
(`sorted(d.items(), key=lambda kv: kv[1])`), ranking, `heapq`'s cousins,
any "top-k by field" problem.

## Common mistake

- `arr = arr.sort()` → `sort()` returns `None` — you just deleted your
  data. Call `arr.sort()` as a statement, or use `sorted(arr)`.
- Mixed directions: `(score, name)` can't do score-desc + name-asc with
  `reverse=True` (it flips BOTH). Negate the number: `(-score, name)`.
- Sorting a dict directly gives you sorted *keys* — use `d.items()` and a
  key on `item[1]` for value ordering.
- Reaching for an old-style comparator — Python removed `cmp=`; write a
  `key` function instead (`functools.cmp_to_key` only as a last resort).

## Your turn

`[("a", 2), ("b", 1), ("c", 2)]` sorted by `lambda r: (-r[1], r[0])` —
what's the output?

<details><summary>Answer</summary>
`[('a', 2), ('c', 2), ('b', 1)]` — keys become (−2,'a'), (−1,'b'),
(−2,'c'). −2 sorts first (descending score), and a < c breaks the tie.
</details>

---

**← Prev** [10 — Counting sort](10-counting-sort.md) ·
**Next →** [12 — Picking the right sort](12-picking-the-right-sort.md)
