# 14 — Amortized: why `append` is "O(1) with an asterisk"

> 4-minute read. The last concept — then the recipe.

## The idea, plain words

**Amortized** = "average over many operations, even though a few are pricey."

Real-life version: **buying a monthly transit pass.** Most days you just tap
(1 step). One day a month you pay for the whole month (expensive day).
Spread the cost over all days → each day is cheap *on average*.

## Python's list.append — the famous example

A list keeps a block of memory with some empty slots. When it runs out,
Python grabs a bigger block (roughly double) and **copies everything over**:

```
append 1 2 3 4 → slots [_,_,_,_] fill up → all cheap
append 5       → FULL! allocate 8 slots, copy 4 old items → EXPENSIVE append
append 6 7 8   → cheap again
append 9       → FULL! allocate 16, copy 8 → expensive
```

```
Capacity:   4   4   4   4 | 8   8   8   8 | 16 ...
Append #:   1   2   3   4 | 5   6   7   8 | 9  ...
Copy cost:  0   0   0   4 | 0   0   0   8 | 0  ...
```

8 appends → total copy work = 4 + 8 = 12 moves. Per append: 12/8 = 1.5
extra ops. The expensive copies are rare and their cost shrinks relative to
the count — so we call it **O(1) amortized**.

## Why it exists

Without amortized thinking you'd either avoid `append` (over-fearing) or be
confused by timing spikes (under-understanding). Knowing the pattern lets
you use lists confidently — and spot the same pattern elsewhere (dict/set
rehashing on growth, dynamic arrays in every language).

## Where it's used

- `list.append`, `list.pop()` — O(1) amortized
- dict/set inserts — O(1) amortized (occasional resize + rehash)
- The counterexample: `list.insert(0, x)` or `pop(0)` — O(n) EVERY time
  (shifts everything left). No amortization saves those — that's why
  `deque` exists for front work.

## Your turn

Why is "insert at position 0" NOT O(1) amortized like append is?

<details><summary>Answer</summary>
Because it's expensive EVERY time, not occasionally — every single
insert(0) shifts all n elements right. No "usually cheap" → nothing to
average down. It's plain O(n) per call.
</details>

---

**← Prev** [13 — Space complexity](13-space-complexity.md) ·
**Next →** [15 — The analysis recipe](15-the-recipe.md)
