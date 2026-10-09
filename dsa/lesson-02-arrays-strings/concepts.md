# Lesson 02 — Arrays & Strings

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **14 tiny files, ~5 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.

This lesson assumes lesson 01 (Big-O) is done — terms like O(n) and O(1)
are used freely. Everything else is defined when it first appears.

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [What is an array, really?](chapters/01-what-is-an-array.md) | what an array is in memory, why index starts at 0 |
| 02 | [Why is `nums[5000]` as fast as `nums[0]`?](chapters/02-why-indexing-is-o1.md) | why indexing is a jump but `in` is a search |
| 03 | [Why is adding at the front expensive?](chapters/03-append-vs-insert.md) | why `insert(0)`/`pop(0)` cost O(n) — the loop trap |
| 04 | [Strings: arrays you can't write to](chapters/04-strings-immutable-arrays.md) | immutability, `ord`, and the cost of every string op |
| 05 | [Running totals](chapters/05-running-totals.md) | build a prefix-sum array by hand |
| 06 | [Any range-sum in one subtraction](chapters/06-range-sum-one-subtraction.md) | `P[j+1] - P[i]` — and the off-by-one to avoid |
| 07 | [Change the list, or build a new one?](chapters/07-in-place-vs-new-list.md) | in-place vs O(n) space — and the `sort()` = None trap |
| 08 | [The write-pointer trick](chapters/08-write-pointer.md) | edit in place safely: read pointer + write pointer |
| 09 | [Scan twice: count first, build second](chapters/09-two-passes.md) | why two passes beat a nested loop (product-except-self) |
| 10 | [Counting characters](chapters/10-counting-characters.md) | tally a string in one pass with `dict.get` |
| 11 | [Building strings: `join`, not `+=`](chapters/11-join-not-plus-equals.md) | why `+=` in a loop is secretly O(n²) |
| 12 | [Prefix sums + a dict](chapters/12-subarray-sum-k.md) | count subarrays summing to k in O(n) — seed `{0:1}` |
| 13 | [Kadane's: extend or restart](chapters/13-kadane-extend-or-restart.md) | max subarray in one pass — your first DP |
| 14 | [The big picture: three moves](chapters/14-the-big-picture.md) | precompute / hash / carry — the O(n²)→O(n) instinct |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> Arrays store elements in **contiguous memory**, so `nums[i]` is one
> address calculation — O(1) — but inserting at the front shifts
> everything → O(n). Strings are immutable char arrays: reads are O(1),
> edits are copies, so build with `join`, never `+=`. The techniques:
> **prefix sums** (pay O(n) once, answer range-sums in O(1)),
> **write pointers** (edit in place with O(1) space), **two passes**
> (gather global facts, then spend them), **frequency dicts** (tally in
> one pass), and **Kadane's** (carry `cur = max(x, cur + x)` — the seed
> of dynamic programming). Whenever a problem smells like "for each X,
> check all other Ys" — precompute, hash, or carry a running total.

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
