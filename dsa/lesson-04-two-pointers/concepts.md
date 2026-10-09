# Lesson 04 — Two Pointers

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **11 tiny files, ~4 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [A "pointer" is just an index](chapters/01-a-pointer-is-just-an-index.md) | what a pointer even is (a finger, not a type) |
| 02 | [The two-pointer idea](chapters/02-the-two-pointer-idea.md) | why two indices beat nested loops |
| 03 | [Opposite ends — meet in the middle](chapters/03-opposite-ends.md) | the converging skeleton + its move-rules |
| 04 | [Reverse in place](chapters/04-reverse-in-place.md) | swap ends, walk inward, O(1) space |
| 05 | [Palindrome check](chapters/05-palindrome-check.md) | ends must match; skip-the-junk variant |
| 06 | [Sorted pair-sum — the blame rule](chapters/06-sorted-pair-sum.md) | **why sorted input unlocks O(n) — the core chapter** |
| 07 | [Read & write pointers](chapters/07-read-write-pointers.md) | fast scans, slow writes — in-place dedup |
| 08 | [Partition: keepers left](chapters/08-partition-move-zeros.md) | move-zeros; the road to Dutch-flag |
| 09 | [Two pointers vs hashing](chapters/09-vs-hashing.md) | the O(1)-space tradeoff interviews love |
| 10 | [When two pointers FAILS](chapters/10-when-it-fails.md) | unsorted input → silent wrong answers |
| 11 | [Leveling up](chapters/11-leveling-up.md) | 3-sum, containers, merge, rain water |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> Two pointers = **two index variables moved by rules, never restarting.**
> Opposite ends (`L`/`R` walk inward) solve symmetric and pair problems;
> same direction (`fast` reads, `slow` writes keepers) solve in-place
> compaction. The magic is the move-rule: sorted input makes "too small →
> move L" a guaranteed discard, collapsing O(n²) pair-search to O(n) with
> O(1) space. No sorted structure → no blame rule → use hashing instead.

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
