# Lesson 01 — Complexity & Big-O

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **15 tiny files, ~5 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [What is an algorithm?](chapters/01-what-is-an-algorithm.md) | what "algorithm" even means |
| 02 | [What is *n*?](chapters/02-what-is-n.md) | why every formula uses the letter n |
| 03 | [Counting steps by hand](chapters/03-counting-steps-by-hand.md) | count what code actually does |
| 04 | [Why not seconds?](chapters/04-why-not-seconds.md) | why we count steps, not time |
| 05 | [What Big-O means](chapters/05-what-big-o-means.md) | read O(...) without fear |
| 06 | [O(1) — constant](chapters/06-o1-constant.md) | "instant no matter the input" |
| 07 | [O(n) — linear](chapters/07-on-linear.md) | "one look per item" |
| 08 | [O(n²) — quadratic](chapters/08-on2-quadratic.md) | **the one you asked about — explained from zero** |
| 09 | [O(log n) — halving](chapters/09-ologn-halving.md) | why dictionary lookups are magic |
| 10 | [O(n log n) & O(2ⁿ)](chapters/10-onlogn-and-2n.md) | sorting-tier and recursive-explosion-tier |
| 11 | [Nested vs sequential loops](chapters/11-nested-vs-sequential.md) | multiply vs add — the #1 trap |
| 12 | [Best / worst / average](chapters/12-best-worst-average.md) | which case to report |
| 13 | [Space complexity](chapters/13-space-complexity.md) | the "...and space?" follow-up |
| 14 | [Amortized](chapters/14-amortized-append.md) | why append is "O(1) with an asterisk" |
| 15 | [The recipe](chapters/15-the-recipe.md) | analyze any code in 5 steps |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> Big-O counts **how many steps** code takes as input size *n* grows —
> ignoring constants and small terms, reporting the **worst case**.
> O(1) = instant · O(log n) = halving · O(n) = one pass ·
> O(n log n) = good sorting · O(n²) = nested loops · O(2ⁿ) = recursive
> explosion. Nested loops multiply; side-by-side loops add. Same counting
> applied to *memory* is space complexity.

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
