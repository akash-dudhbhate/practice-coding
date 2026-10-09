# 14 — The big picture: three moves

> 4-minute read. Zoom out — the whole lesson was three ideas wearing costumes.

## The idea, plain words

Strip the names off every chapter and you're left with three moves.
Learn to smell them and most array/string problems collapse into one.

### Move 1 — Precompute once, query cheaply

Pay O(n) *once* to build a summary; answer every later question in O(1).

- Prefix sums (ch 05–06): O(n) build → every range-sum is one
  subtraction.
- Smell: *"the same kind of question, asked many times."*

### Move 2 — Trade space for time

Spend O(n) memory on a dict to avoid rescanning.

- Frequency tally (ch 10): one dict replaces `count()` rescans.
- Seen-prefixes dict (ch 12): `P - k` lookups replace inner loops.
- Smell: *"for each X, check all other Ys"* — the nested loop that a
  hashmap dissolves.

### Move 3 — One pass + running state

Carry exactly the summary you need; don't look back.

- Write pointer (ch 08): `w` remembers where keepers go.
- Kadane (ch 13): `cur` remembers "best ending here."
- Even `max` in a loop: `biggest` remembers the champion so far.
- Smell: *"the answer at position i only depends on a summary of
  positions < i."*

## One glance back

```
idea                    | chapter | buys you
------------------------+---------+--------------------------
index = address math    |  01-02  | O(1) reads anywhere
contiguity's cost       |   03    | front ops are O(n) — know it
immutability            |  04, 11 | read free, edit = copy, join once
prefix sums             |  05-06  | range queries in O(1)
in-place / write ptr    |  07-08  | O(1) space edits, safely
two passes              |   09    | gather facts, then spend them
freq dict               |   10    | O(n) tallies
prefix + hashmap        |   12    | subarray-sum-k in one pass
running state           |   13    | Kadane: extend or restart
```

## Why it exists (the meta-lesson)

"For each X, check all other Ys" is the O(n²) instinct everyone starts
with. The whole lesson trains the counter-question:

> *Can I precompute it, hash it, or carry it in a variable instead?*

Interviewers aren't testing whether you memorized Kadane — they're
watching whether you ask that question.

## Where it's used

Right now: `easy/` → `medium/` → `hard/` in this folder. Every problem
maps onto the table — `easy/p01` is ch 05, `medium/p01` is ch 06,
`medium/p02` is ch 08, `medium/p03` is ch 09, `hard/p01` is ch 12,
`hard/p02` is ch 13, `hard/p03` is ch 09+10+11 together.

## Your turn (the real exercise)

For each problem smell, name the move:

1. "Answer 500 different range-sum questions on one array."
2. "Check if two strings are anagrams."
3. "Find the longest run of consecutive wins."

<details><summary>Answer</summary>
1. Precompute — build `P` once, subtract per query (ch 05–06).
2. Trade space — tally each string's chars, compare dicts (ch 10).
3. Running state — carry `cur` streak and `best`, one pass (ch 13's
   shape, even simpler).
</details>

---

**← Prev** [13 — Kadane's: extend or restart](13-kadane-extend-or-restart.md) ·
**Up** → [Lesson index](../concepts.md) ·
**Then** → `task-explanation.md` and the `easy/` folder
