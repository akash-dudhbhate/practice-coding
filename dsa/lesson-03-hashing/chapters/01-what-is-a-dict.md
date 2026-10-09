# 01 — What is a Dict? (the key → value idea)

> 4-minute read. One idea only.

## The idea, plain words

A **dict** (short for *dictionary*) stores **pairs**: a **key** and the
**value** attached to it. Other languages call it a **map** or **hash
map** — same thing, different name.

Real-life version: **your phone's contacts app.** The key is a name
("Mum"), the value is what you want back (her phone number). You never
scroll contacts position-by-position — you look up *by name*.

```python
d = {}                 # an empty dict — think "empty contacts list"
d["apple"] = 3         # key "apple" -> value 3
d["banana"] = 7
print(d["apple"])      # look up BY NAME, not by position
```

```
3
```

A list answers *"what's at position 2?"* A dict answers *"what's stored
under 'apple'?"* Different question, different tool.

## Try it by hand

```python
scores = {"amit": 90, "sara": 85}
scores["john"] = 78        # add a new pair
scores["amit"] = 95        # same key -> replaces the old value
print(scores)
```

```
{'amit': 95, 'sara': 85, 'john': 78}
```

One key holds **one** value — assigning again overwrites, never
duplicates.

## Why it exists

Lists force you to remember *positions*. Real data has *names*: words and
their counts, users and their emails, items and their prices. A dict lets
data carry its own label — and (next chapter) finds it instantly.

## Where it's used

Everywhere: counting, caches, indexes, config settings, JSON data.
The `dict` is the most-used data structure in all of Python.

## Common mistake

```python
print(scores["riya"])        # KeyError — she's not in the dict
print(scores.get("riya"))    # None — .get returns a default instead
print(scores.get("riya", 0)) # 0 — you pick the default
```

## Your turn

```python
d = {"a": 1}
d["a"] = 5
d["b"] = 2
```

What is `d["a"]`, and how many pairs are in `d`?

<details><summary>Answer</summary>
`d["a"]` is `5` — the second assignment overwrote the 1. Two pairs:
`a -> 5` and `b -> 2`. Keys are unique; same key just replaces.
</details>

---

**Next →** [02 — How a key becomes a slot](02-how-a-key-becomes-a-slot.md)
