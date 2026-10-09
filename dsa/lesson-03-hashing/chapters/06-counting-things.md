# 06 — Counting Things (the frequency pattern)

> 5-minute read. The single most-used dict pattern.

## The idea, plain words

"How many times does each thing appear?" Use a dict where the **key is
the item** and the **value is the running count**.

Real-life version: a **tally sheet** — every time a pen shows up, add a
mark to pen's row.

```python
items = ["pen", "book", "pen", "pen", "book"]
counts = {}
for x in items:
    counts[x] = counts.get(x, 0) + 1   # .get(key, default): missing key -> 0
print(counts)
print(max(counts, key=counts.get))     # most frequent item
```

```
{'pen': 3, 'book': 2}
pen
```

## Walk it by hand

```
x="pen"   counts.get("pen",0)=0  ->  counts: {"pen": 1}
x="book"                         ->  counts: {"pen": 1, "book": 1}
x="pen"                          ->  counts: {"pen": 2, "book": 1}
x="pen"                          ->  counts: {"pen": 3, "book": 1}
x="book"                         ->  counts: {"pen": 3, "book": 2}
```

One pass over the data — **O(n)** — and the finished table answers every
"how many" question instantly.

## The shortcut: Counter

Python ships this pattern pre-packaged:

```python
from collections import Counter
c = Counter(["a", "b", "a"])
print(c)                                # Counter({'a': 2, 'b': 1})
print(Counter("eat") == Counter("tea")) # same letters -> same counts
```

```
Counter({'a': 2, 'b': 1})
True
```

That last line is gold: **two words are anagrams exactly when their
letter-counts match.** No sorting needed.

## Why it exists

Frequency questions hide inside everything: most-frequent element,
duplicate finding, voting, histograms, anagram checks, inventory tallies.
It's usually step 1 of a bigger problem.

## Where it's used

Word counts, "top k frequent", checking anagrams
(`Counter(a) == Counter(b)`), finding which items appear more than once.

## Common mistakes

- `counts[x] += 1` on a missing key → **KeyError**. Use
  `counts.get(x, 0)`, or `from collections import defaultdict` +
  `counts = defaultdict(int)` which auto-creates `0` for new keys.
- Counting by sort-then-scan runs **O(n log n)** and destroys order.
  The dict count is O(n).

## Your turn

By hand: what's `counts` after this loop over `"aabca"`?

```python
for x in "aabca":
    counts[x] = counts.get(x, 0) + 1
```

<details><summary>Answer</summary>
`{'a': 3, 'b': 1, 'c': 1}` — three a's, one b, one c.
</details>

---

**← Prev** [05 — Sets: dicts without values](05-sets-dicts-without-values.md) ·
**Next →** [07 — Grouping lookalikes](07-grouping-lookalikes.md)
