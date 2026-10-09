# 07 — Grouping Lookalikes (the anagram pattern)

> 5-minute read. One dict, whole families of items.

## The idea, plain words

Sometimes the value isn't a count — it's a **list of everything that
belongs together**. Map a **computed key → list of items** that share it.

Real-life version: **laundry sorting.** You don't compare every sock to
every other sock — you glance at the color (the *key*) and toss each
sock into the right pile.

For anagrams, the key that captures "same letters" is the **sorted
letters**: `"eat"`, `"tea"`, `"ate"` all sort to `"aet"`.

```python
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}
for w in words:
    key = "".join(sorted(w))                # "eat" -> "aet", "tea" -> "aet"
    groups.setdefault(key, []).append(w)    # missing key? make empty list first
print(list(groups.values()))
```

```
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

## Walk it by hand

```
"eat" -> key "aet" -> groups: {"aet": ["eat"]}
"tea" -> key "aet" -> groups: {"aet": ["eat", "tea"]}
"tan" -> key "ant" -> groups: {..., "ant": ["tan"]}
"ate" -> key "aet" -> "aet" pile grows to 3
"nat" -> key "ant" -> "ant" pile grows to 2
"bat" -> key "abt" -> new pile of 1
```

Six words, one pass, three piles — you never compared word-to-word.

## Why it exists

Grouping by comparing *every pair* is O(n²). Grouping by computing a key
is one pass — the dict hands each item its pile in O(1). The art is
**choosing the key**: it must be whatever equal items share (sorted
letters, lowercase email, `value % k`, …).

## Where it's used

Group anagrams, transactions grouped by user, index maps
(value → list of positions), bucketing by date or category, dedup by a
normalized form.

## Common mistakes

- `groups[key].append(w)` on a missing key → **KeyError**. Use
  `groups.setdefault(key, []).append(w)` or `defaultdict(list)`.
- Picking the wrong key: `key = w` gives every word its own pile. The
  key must capture the *sameness* you want.
- Needing sorted output but trusting dict order — dicts keep *insertion*
  order; run `sorted(...)` explicitly if the problem asks.

## Your turn

`words = ["abc", "bca", "xyz"]` — what keys does `groups` end up with,
and how many piles?

<details><summary>Answer</summary>
Keys: `"abc"` (shared by "abc" and "bca" — same letters) and `"xyz"`.
Two piles: `[["abc", "bca"], ["xyz"]]`.
</details>

---

**← Prev** [06 — Counting things](06-counting-things.md) ·
**Next →** [08 — The seen set: O(n²) → O(n)](08-the-seen-set-trick.md)
