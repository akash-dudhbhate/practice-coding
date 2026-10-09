# Lesson 05 — Sliding Window

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **9 tiny files, ~5 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [What is a "window"?](chapters/01-what-is-a-window.md) | what left/right fingers mark |
| 02 | [The brute-force way](chapters/02-the-brute-force-way.md) | why re-summing costs O(n·k) |
| 03 | [The slide](chapters/03-the-slide.md) | the one-out-one-in trick — **the core of the lesson** |
| 04 | [Fixed-size windows](chapters/04-fixed-size-windows.md) | the build-slide-record template |
| 05 | [Variable-size windows](chapters/05-variable-size-windows.md) | grow right, shrink left until valid |
| 06 | [Window + a count dict](chapters/06-window-with-a-count-dict.md) | the substring-problem pattern |
| 07 | [Why it's O(n)](chapters/07-why-sliding-is-on.md) | why a `while` inside a `for` is still linear |
| 08 | [Windows vs two-pointers](chapters/08-windows-vs-two-pointers.md) | which lesson-04/05 tool to grab |
| 09 | [The recipe & pitfalls](chapters/09-the-recipe-and-pitfalls.md) | recognize it in 10s + the 5 classic bugs |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> A **window** is a contiguous chunk `nums[left..right]` — just two
> indices, not a copy. Sliding means each element enters once and leaves
> once, so "nested-looking" loops run in **O(n)**. Fixed size k given →
> build once, then `+= enterer / −= leaver` per slide. Longest/shortest
> satisfying a rule → `for right` expands, `while` shrinks `left`;
> record after the shrink for *longest*, inside it for *shortest*.
> String problems swap the running sum for a count dict (and `del` keys
> at zero).

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
