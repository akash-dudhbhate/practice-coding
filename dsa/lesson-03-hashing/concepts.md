# Lesson 03 — Hashing: Dict & Set Patterns

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **13 tiny files, ~5 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [What is a dict?](chapters/01-what-is-a-dict.md) | what a key → value pair even is |
| 02 | [How a key becomes a slot](chapters/02-how-a-key-becomes-a-slot.md) | how hash + % picks a home for your data |
| 03 | [When keys collide](chapters/03-when-keys-collide.md) | why two keys can share a slot (and it's OK) |
| 04 | [Why lookup is almost free](chapters/04-why-lookup-is-almost-free.md) | O(1) average, O(n) worst — honestly |
| 05 | [Sets: dicts without values](chapters/05-sets-dicts-without-values.md) | "in or out" questions, answered instantly |
| 06 | [Counting things](chapters/06-counting-things.md) | the frequency-table pattern |
| 07 | [Grouping lookalikes](chapters/07-grouping-lookalikes.md) | bucket items by a shared signature (anagrams) |
| 08 | [The seen set](chapters/08-the-seen-set-trick.md) | turn O(n²) duplicate hunts into O(n) |
| 09 | [Keys can't change](chapters/09-keys-cant-change.md) | why lists can't be keys + the tuple trick |
| 10 | [The complement trick](chapters/10-the-complement-trick.md) | two-sum — **the #1 interview pattern** |
| 11 | [Running totals in a map](chapters/11-running-totals-in-a-map.md) | count subarrays summing to k |
| 12 | [Remembering order](chapters/12-remembering-order-lru.md) | dict + linked list = LRU cache |
| 13 | [The hash toolbox](chapters/13-the-hash-toolbox.md) | which tool for which task |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> A dict/set is a **hash table**: a hash function turns each key into a
> slot number, so lookup jumps straight there — **O(1) on average**
> (O(n) worst, when everything collides). Sets are dicts without values.
> On top sit four interview superpowers: **count** with a dict, **group**
> by a computed key, **remember the past** in a seen set, and ask for the
> **complement** — each turning O(n²) brute force into O(n). Keys must be
> immutable; prefix-sums and LRU are the same tricks in fancier clothes.
> The price is O(n) extra memory — hashing trades space for time.

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
