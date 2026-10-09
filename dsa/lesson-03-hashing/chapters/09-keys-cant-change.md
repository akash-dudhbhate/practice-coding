# 09 — Keys Can't Change (why lists fail + the tuple trick)

> 4-minute read. One rule, one workaround.

## The idea, plain words

A dict key's hash is its **permanent address** — it picks the slot the
moment you store the pair. If the key could *change* afterwards, its
address would be stale: the pair would sit in the wrong slot and lookups
would randomly miss forever.

So Python enforces: **keys must be immutable** — things that can't
change after creation.

| Can be a key? | Examples |
|---|---|
| ✅ Yes | numbers, strings, tuples of immutables |
| ❌ No | lists, dicts, sets — anything mutable |

```python
d = {}
d[(1, 2)] = "grid cell"     # OK — a tuple can't change
d[[1, 2]] = "grid cell"     # TypeError: unhashable type: 'list'
```

## The freezing trick

When your natural key IS a list — freeze it into a tuple (or a string):

```python
key1 = tuple(sorted("tea"))         # sorted() gives a LIST -> freeze to tuple
key2 = "".join(sorted("tea"))       # or glue into a string: "aet"
print(key1, key2)
```

```
('a', 'e', 't') aet
```

That's the chapter-07 anagram key explained: `sorted("tea")` returns a
*list* — illegal as a key — so we either `tuple(...)` it or
`"".join(...)` it into a string. Both are immutable "signatures".

## Why it exists

Same reason an envelope's address can't rewrite itself mid-delivery:
the table *already filed* your pair by the old address. Immutability is
what makes the hash a trustworthy fingerprint.

## Where it's used

Grid coordinates `d[(row, col)]`, memoized results keyed by
`d[(arg1, arg2)]`, sorted-tuple signatures for anagrams, "distinct
configurations" kept in a set.

## Common mistakes

- `seen.add([1, 2])` → TypeError — convert first:
  `seen.add(tuple([1, 2]))`.
- `(1, [2])` still fails — a tuple containing a mutable is unhashable.
  **Every level** must be immutable.
- Forgetting `sorted()` returns a list — it's the `tuple()`/`join()`
  around it that makes the key legal.

## Your turn

Which of these are legal dict keys?
`(3, 4)` · `[3, 4]` · `"34"` · `(3, [4])` · `tuple(sorted("ab"))`

<details><summary>Answer</summary>
Legal: `(3, 4)`, `"34"`, `tuple(sorted("ab"))` — all fully immutable.
Illegal: `[3, 4]` (a list) and `(3, [4])` — a tuple holding a list;
the list inside can still change, so the whole thing is unhashable.
</details>

---

**← Prev** [08 — The seen set: O(n²) → O(n)](08-the-seen-set-trick.md) ·
**Next →** [10 — The complement trick](10-the-complement-trick.md)
