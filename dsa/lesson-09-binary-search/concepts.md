# Lesson 09 — Binary Search

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **11 tiny files, ~5 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [The guessing game](chapters/01-the-guessing-game.md) | what "halving the search space" means |
| 02 | [Why sorted is required](chapters/02-why-sorted.md) | why unsorted data silently breaks it |
| 03 | [The template, line by line](chapters/03-the-template.md) | lo, hi, mid — and why `<=` + `mid ± 1` |
| 04 | [Hand trace, start to finish](chapters/04-hand-trace.md) | draw lo/mid/hi shrinking on `[1,3,5,7,9,11]` |
| 05 | [Why O(log n)](chapters/05-why-log-n.md) | why a billion items cost ~30 probes |
| 06 | [The infinite-loop bug](chapters/06-infinite-loop-bug.md) | the `lo = mid` trap + the overflow note |
| 07 | [Lower bound & upper bound](chapters/07-lower-upper-bound.md) | "where does it belong?" not "is it there?" |
| 08 | [The bisect module](chapters/08-bisect-module.md) | bisect_left vs bisect_right without guessing |
| 09 | [Search the answer space](chapters/09-search-the-answer.md) | **the interview pattern** — min capacity, Koko's bananas |
| 10 | [Rotated sorted array](chapters/10-rotated-array.md) | binary search when sortedness has a scar |
| 11 | [Peaks: without sortedness](chapters/11-peak-without-sorted.md) | the real rule — kill half each step |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> Binary search probes the **middle** of a live range `[lo, hi]` and uses
> the result to kill half the candidates — every step. It needs a
> **monotone elimination rule** (usually: sorted order). Keep the range
> inclusive (`while lo <= hi`), keep `mid` OUT of the surviving half
> (`mid ± 1`), and it's `O(log n)` — a billion elements in ~30 probes.
> Same skeleton everywhere: bounds, answer spaces, rotated arrays, peaks —
> only the "which half dies" rule changes.

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
