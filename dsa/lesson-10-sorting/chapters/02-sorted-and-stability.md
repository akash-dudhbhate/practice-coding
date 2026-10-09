# 02 — What "Sorted" Means + Stability

> 4-minute read.

## The idea, plain words

"Sorted" always means **sorted BY something** — a *key*. Numbers sort by
value, names by alphabet, people by... age? name? height? You pick the key.

Now the subtle part: when two items have the SAME key, what order do they
end up in? A **stable** sort promises: equal items keep their original
order. An **unstable** sort makes no such promise — ties can come out
scrambled.

Real-life version: a class list sorted by grade. Two students both scored
90 — a stable sort keeps them in whatever order they were listed before.
Why care? Because of the trick below.

## Watch it happen — why stability is a feature

```python
people = [("cal", 30), ("amy", 30), ("bob", 25)]

by_name = sorted(people, key=lambda p: p[0])   # first pass: by name
print(by_name)
# [('amy', 30), ('bob', 25), ('cal', 30)]

by_age = sorted(by_name, key=lambda p: p[1])   # second pass: by age
print(by_age)
# [('bob', 25), ('amy', 30), ('cal', 30)]
```

Hand-trace the second sort: bob (25) moves first — fine. But amy and cal
BOTH have age 30. Python's sort is stable, so they keep the order they had
in `by_name`: amy before cal → alphabetical. **Two sorts = "sort by age,
ties broken by name."** That only works because stability preserves the
first pass.

## Why it exists

Stability enables **multi-pass sorting**: sort by the least important key
first, the most important key last — each earlier sort survives inside
ties. That's exactly how SQL's `ORDER BY age, name` works conceptually.
(Chapter 11 shows Python's one-line tuple-key equivalent.)

## Where it's used

Multi-field sorting everywhere — spreadsheets ("sort by date, then by
amount"), databases, merge sort's `<=` comparison exists specifically to
stay stable.

## Common mistake

Assuming every sort is stable — it ISN'T. Selection sort and plain
quicksort can reorder equal elements. Merge sort and Python's `sorted()`
are stable. If tie-order matters, check your algorithm or add the
tiebreaker to the key explicitly.

## Your turn

`people = [("amy", 30), ("bob", 25), ("cal", 30)]` — sorted stably by age,
is amy or cal first?

<details><summary>Answer</summary>
amy — both have age 30, and amy came before cal in the original list.
Stability preserves that. With an unstable sort, either order is legal.
</details>

---

**← Prev** [01 — Why sorting matters](01-why-sorting-matters.md) ·
**Next →** [03 — Bubble sort](03-bubble-sort.md)
