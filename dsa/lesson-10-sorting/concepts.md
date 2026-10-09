# Lesson 10 — Sorting

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **12 tiny files, ~5 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [Why sorting matters](chapters/01-why-sorting-matters.md) | what sorted order unlocks (search, dedup, ranking) |
| 02 | [What "sorted" means + stability](chapters/02-sorted-and-stability.md) | why equal-key order survives a stable sort |
| 03 | [Bubble sort](chapters/03-bubble-sort.md) | how the biggest element floats to the end |
| 04 | [Selection sort](chapters/04-selection-sort.md) | find the smallest, swap it into place |
| 05 | [Insertion sort](chapters/05-insertion-sort.md) | the card-hand sort — and its secret superpower |
| 06 | [Why all three are O(n²)](chapters/06-why-all-n2.md) | count the comparisons, see the cliff |
| 07 | [Merge sort](chapters/07-merge-sort.md) | divide & conquer — guaranteed O(n log n) |
| 08 | [Quicksort](chapters/08-quicksort.md) | pivot, partition — fast average, scary worst case |
| 09 | [The O(n log n) floor](chapters/09-the-nlogn-floor.md) | why no comparison sort can go faster |
| 10 | [Counting sort](chapters/10-counting-sort.md) | the legal loophole that beats the floor |
| 11 | [Python's sorted() / .sort()](chapters/11-python-sorted-sort.md) | Timsort, key=, lambda multi-field sorts |
| 12 | [Picking the right sort](chapters/12-picking-the-right-sort.md) | sort vs heap vs hash — and the full cheat sheet |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> Sorting puts items in a defined order — and sorted data makes search,
> dedup, and ranking cheap. The simple sorts (bubble, selection, insertion)
> each fix one element per pass → O(n²). The fast ones divide the problem:
> merge sort guarantees O(n log n), quicksort averages it. No *comparison*
> sort can beat n log n — but counting sort dodges the rule by never
> comparing. In Python just use `sorted()` / `.sort()` (Timsort: stable,
> adaptive, `key=` for multi-field) — and don't sort at all when a heap or
> hash answers your real question cheaper.

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
