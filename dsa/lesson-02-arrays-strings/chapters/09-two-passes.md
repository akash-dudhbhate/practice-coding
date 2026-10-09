# 09 — Scan twice: count first, build second

> 5-minute read. When the answer needs facts you don't have yet.

## The idea, plain words

Some questions can't be answered for element 0 until you've seen
**all** the elements. "Label each item with how many times it appears
in total" — you can't label the first item until you've counted the
whole list.

So do two passes:

- **Pass 1 — gather.** Scan once, collecting facts: counts, totals,
  running products.
- **Pass 2 — produce.** Scan again, using those facts to build the
  answer.

Real-life version: **a teacher curving a test**. Nobody's grade is
final until *everyone's* score is known — so she grades all papers
first (pass 1), then assigns the curved marks (pass 2).

## The showcase: product of everything except self

Goal: `out[i]` = product of all elements **except** `nums[i]` — and
division is banned (it would crash on zeros anyway).

```python
def product_except_self(nums):
    n = len(nums)
    out = [1] * n
    left = 1
    for i in range(n):              # pass 1: out[i] = product LEFT of i
        out[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):  # pass 2: multiply in product RIGHT of i
        out[i] *= right
        right *= nums[i]
    return out
```

"Everything except i" = (everything left of i) × (everything right of
i). Pass 1 captures all the lefts; pass 2 walks backward capturing the
rights.

## Trace it — `[1, 2, 3, 4]`

```
pass 1 (left -> right), left starts at 1:
  i=0: out[0]=1,  left=1*1=1
  i=1: out[1]=1,  left=1*2=2
  i=2: out[2]=2,  left=2*3=6
  i=3: out[3]=6,  left=6*4=24
  out = [1, 1, 2, 6]          # each = product of everything to its left

pass 2 (right -> left), right starts at 1:
  i=3: out[3]=6*1=6,    right=1*4=4
  i=2: out[2]=2*4=8,    right=4*3=12
  i=1: out[1]=1*12=12,  right=12*2=24
  i=0: out[0]=1*24=24,  right=24*1=24
  out = [24, 12, 8, 6]
```

```python
print(product_except_self([1, 2, 3, 4]))   # -> [24, 12, 8, 6]
```

Check one: `out[2]` should be `1×2×4 = 8`. Yes — `out[2]` got `2`
(product of left side: `1×2`) times `4` (right side). No division, no
nested loop.

## Why it exists

The tempting alternative — "for each i, loop over everything else and
multiply" — is O(n²). Two passes are **O(n) + O(n) = O(n)**: nested
loops *multiply*, sequential loops *add* (lesson-01 chapter 11 — the
same math, applied on purpose).

## Where it's used

- `medium/p03` — this exact problem.
- `hard/p03` — label each character with its total frequency: pass 1
  counts, pass 2 builds the label string.
- Any "each element needs a fact about the whole array" problem.

## Common mistake

Reaching for `total_product // nums[i]` — it crashes on `0` (and the
problem often bans division anyway). The two running products sidestep
it completely. Also: initializing `left`/`right` to `0` instead of `1`
— multiplying by 0 erases everything.

## Your turn

"For each element, output how many elements in the array are larger
than it" — sketch the two passes in words (no code needed).

<details><summary>Answer</summary>
Pass 1: scan once to count each value's frequency (a dict — chapter
10) — or for a simpler version, sort a copy so counts-to-the-right are
known. Pass 2: for each element, look up how many values exceed it and
write the answer. Either way: one scan learns global facts, the second
scan spends them. Never "for each i, rescan all n."
</details>

---

**← Prev** [08 — The write-pointer trick](08-write-pointer.md) ·
**Next →** [10 — Counting characters in one pass](10-counting-characters.md)
