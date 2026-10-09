# 04 — Interval Words: start, end, overlap, contain

> 5-minute read. Learn to *see* intervals before solving them.

## The idea, plain words

An **interval** `[start, end]` is a chunk of a line — a meeting from 1:00
to 4:00, a bus route, a gene range. Everything in this family comes down
to **how two chunks sit next to each other**. Draw them as bars on a
timeline:

```
[1,4]   ████
[2,5]    ████          overlap — share times 2,3,4
[6,8]        ███       disjoint — gap between 5 and 6
        ────────────→ time
        1 2 3 4 5 6 7 8
```

Only three relationships exist:

```
OVERLAP          TOUCHING           CONTAINED
[1,4] ████       [1,3] ███          [1,10] ██████████
[2,5]  ████      [3,5]    ███       [3,5]     ███
      ↑ share          ↑ meet               ↑ one lives inside
        2..4             at 3
```

One tiny predicate captures overlap — **a starts before b ends, AND b
starts before a ends**:

```python
def overlaps(a, b):
    return a[0] <= b[1] and b[0] <= a[1]   # share ANY point?
```

`overlaps([1,4], [2,5])` → `True` · `overlaps([1,4], [5,8])` → `False` ·
`overlaps([1,4], [4,6])` → `True` (they share the single instant 4).

## Why it exists

Half of every interval bug is a *word* bug: you coded "overlap" but the
problem meant "touching", or vice versa. Naming the three cases first
turns vague panic into a checklist.

## Where it's used

- Calendar apps — free/busy computation (merge busy bars)
- CPU scheduling — processes as time intervals
- Genomics — merging overlapping gene ranges
- Firewall rules, IP ranges, booking systems

## Common mistake

**`<=` vs `<` at the boundary.** Is `[1,3]` + `[3,5]` one meeting or two?

- **Merge/busy-time problems:** touching counts as connected → `s <= prev_end`
- **Scheduling problems:** a meeting may start the instant another ends →
  compatible when `s >= last_end`

Pick deliberately per problem — this one character flips answers.

## Your turn

`overlaps([2,6], [6,9])` — True or False? And would a *scheduler* call
these two meetings conflicting?

<details><summary>Answer</summary>
`True` by the predicate (they share instant 6). But a scheduler says **no
conflict** — meeting 2 can start exactly when meeting 1 ends (`s >= last_end`
passes). Same pair, different verdicts, different `<` vs `<=`.
</details>

---

**← Prev** [03 — Greedy or DP?](03-greedy-or-dp.md) ·
**Next →** [05 — Sort by Start or by End?](05-sort-by-key.md)
