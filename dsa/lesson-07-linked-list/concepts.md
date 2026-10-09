# Lesson 07 — Linked Lists

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **11 tiny files, ~5 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [What is a node?](chapters/01-what-is-a-node.md) | what the two halves of a node are |
| 02 | [Array vs linked list](chapters/02-array-vs-linked-list.md) | the trade: O(1) index vs O(1) rewiring |
| 03 | [Building a list](chapters/03-building-a-list.md) | Node class, `head`, `build_list`/`to_list` |
| 04 | [Walking the list](chapters/04-walking-the-list.md) | the `curr = curr.next` loop — learn it cold |
| 05 | [No index: lookup is O(n)](chapters/05-no-index-lookup-on.md) | why "get item k" costs a walk |
| 06 | [Insert & delete](chapters/06-insert-and-delete.md) | rewiring arrows — skip a node, don't move it |
| 07 | [The dummy node trick](chapters/07-the-dummy-node.md) | how one fake node deletes your edge cases |
| 08 | [Fast & slow: the middle](chapters/08-fast-and-slow-middle.md) | finding halfway by speed ratio, no counting |
| 09 | [Cycle detection: Floyd's](chapters/09-cycle-detection-floyds.md) | why two runners must meet inside a loop |
| 10 | [Reversing a list](chapters/10-reversing-a-list.md) | prev/curr/nxt — **the interview classic** |
| 11 | [Merge & big picture](chapters/11-merge-and-big-picture.md) | merge sorted lists + the 3 muscles recap |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> A linked list is a chain of **nodes** — each holds a value plus an arrow
> to the next node; you only hold `head` and walk `.next` by `.next`.
> No index → lookup is O(n), but insert/delete at a known spot is O(1) —
> the arrow trade. Three tools solve nearly every problem: **rescue
> pointers** (save `next` before overwriting), **dummy nodes** (fake head
> kills edge cases), **fast/slow walkers** (middle, cycles, nth-from-end —
> position by ratio, never by counting).

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
