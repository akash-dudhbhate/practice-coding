# 05 — Sets: Dicts Without Values

> 4-minute read. Half a dict, twice as useful as it sounds.

## The idea, plain words

A **set** is a dict that stores only keys — no values. It answers exactly
one question: **"is this thing in the club, or not?"**

Real-life version: a **guest list** at a party door. The bouncer doesn't
care *where* anyone lives — just whether your name is on the list.

```python
guests = {"amit", "sara", "john"}
print("sara" in guests)    # O(1) — same hash trick as dicts
guests.add("priya")
print(len(guests))
```

```
True
4
```

Two superpowers come free:

```python
nums = [4, 3, 2, 4, 3, 5]
print(set(nums))      # duplicates auto-deleted
```

```
{2, 3, 4, 5}
```

- **Membership** (`in`) is O(1) average — same hashing as dicts.
- **Deduplication** — a set can't hold repeats, ever.

## Try it by hand — set math

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)    # in both
print(a | b)    # in either
print(a - b)    # in a but not b
```

```
{2, 3}
{1, 2, 3, 4}
{1}
```

## Why it exists

Lots of problems only need a yes/no door-check, not key → value:
"have I seen this?", "any duplicates?", "what's common to both lists?".
A set is a dict stripped down to exactly that.

## Where it's used

Duplicate detection, tracking visited nodes in a graph, intersections/
unions, "does the input contain a repeat", counting *distinct* items
(`len(set(nums))`).

## Common mistakes

- **Sets forget order** — they can't tell you where the *first*
  occurrence was. Need positions? Use a dict (value → index).
- **Sets forget counts** — `len(set([1,1,1]))` is `1`. Need *how many*?
  That's a counting dict — next chapter.
- `{}` is an **empty dict**, not an empty set — the empty set must be
  written `set()`.

## Your turn

```python
s = set()
s.add(5)
s.add(9)
s.add(5)
print(len(s), 5 in s, 7 in s)
```

<details><summary>Answer</summary>
`2 True False` — adding `5` twice changes nothing (no duplicates), and
membership is instant either way.
</details>

---

**← Prev** [04 — Why lookup is almost free](04-why-lookup-is-almost-free.md) ·
**Next →** [06 — Counting things](06-counting-things.md)
