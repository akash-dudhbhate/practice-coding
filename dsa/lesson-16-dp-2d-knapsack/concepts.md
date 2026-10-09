# Lesson 16 — 2D DP & Knapsack

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **12 tiny files, ~5 minutes each**. This is the hardest
lesson in the course: read one chapter, try the mini-practice at the
bottom, take a breath, come back. That's the design.

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [When one index isn't enough](chapters/01-when-one-index-isnt-enough.md) | why `dp[i]` sometimes fails |
| 02 | [Unique paths: your first 2D table](chapters/02-unique-paths-your-first-grid.md) | fill a 3×3 grid by hand |
| 03 | [Reading a 2D table](chapters/03-reading-a-2d-table.md) | say what `dp[i][j]` means in a sentence |
| 04 | [Costs & walls](chapters/04-min-path-sum-and-walls.md) | same grid, min-cost + obstacles |
| 05 | [0/1 knapsack: take or skip](chapters/05-knapsack-take-or-skip.md) | **the canonical 2D DP, traced cell by cell** |
| 06 | [The backwards loop trick](chapters/06-the-backwards-loop-trick.md) | why `w` descends in 1-row knapsack |
| 07 | [LCS: two strings](chapters/07-lcs-two-strings.md) | prefix × prefix states |
| 08 | [Edit distance](chapters/08-edit-distance.md) | min-problems need real borders |
| 09 | [Wildcard matching](chapters/09-wildcard-matching.md) | same skeleton, boolean cells |
| 10 | [Interval DP](chapters/10-interval-dp-burst-balloons.md) | pick the LAST move, fill by length |
| 11 | [The pitfall gallery](chapters/11-the-pitfall-gallery.md) | the 5 bugs that get everyone |
| 12 | [The "is it 2D?" checklist](chapters/12-the-2d-checklist.md) | recognize the shape in 15 seconds |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> 2D DP is for subproblems that need TWO variables — items×capacity,
> row×col, prefix×prefix, wall×wall. Write `dp[i][j]` as a sentence
> ("best answer using first `i` of X and first `j` of Y"), seed row 0 /
> col 0 with real base values (zeros for counts, costs for min-problems),
> fill in dependency order (row-major for prefixes, by-length for
> intervals), and read the answer usually at `dp[m][n]`. The recurrence is
> always a choice: take-or-skip, top+left, match-or-skip, last-pick.

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
