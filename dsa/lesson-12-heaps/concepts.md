# Lesson 12 — Heaps & Priority Queues

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **12 tiny files, ~5 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [The problem](chapters/01-the-problem-grab-the-extreme-fast.md) | why "grab the extreme fast" is its own problem (ER triage) |
| 02 | [Why simple ideas are too slow](chapters/02-why-simple-ideas-are-too-slow.md) | why sorted/unsorted lists both fail at O(n) |
| 03 | [What a heap is](chapters/03-what-a-heap-is.md) | complete tree + the parent-vs-children rule |
| 04 | [The array trick](chapters/04-the-array-trick.md) | the index math: `(i-1)//2`, `2i+1`, `2i+2` |
| 05 | [Push: bubble up](chapters/05-push-append-and-bubble-up.md) | what `heappush` does inside |
| 06 | [Pop: bubble down](chapters/06-pop-swap-and-bubble-down.md) | what `heappop` does inside |
| 07 | [Why O(log n)](chapters/07-why-push-and-pop-are-ologn.md) | where the speed guarantee comes from |
| 08 | [heapq + negation](chapters/08-heapq-min-heap-and-the-negation-trick.md) | min-heap only — the max-heap trick |
| 09 | [heapify vs n pushes](chapters/09-heapify-faster-than-n-pushes.md) | why heapify is O(n), not O(n log n) |
| 10 | [The top-k pattern](chapters/10-the-top-k-pattern.md) | **the #1 interview pattern — explained from zero** |
| 11 | [Tuples & priority queues](chapters/11-tuples-priorities-and-the-priority-queue.md) | `(priority, counter, item)` + Dijkstra preview |
| 12 | [Two heaps + the recipe](chapters/12-two-heaps-and-the-recipe.md) | streaming medians + recognize it in 10 seconds |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> A heap is a **complete binary tree** (stored as a plain array:
> parent `(i-1)//2`, children `2i+1`/`2i+2`) where every parent is ≤ its
> children → the min is always at index 0. Push = append + bubble-up;
> pop = move-last-to-root + bubble-down; both **O(log n)**. `heapq` is
> min-heap only — negate for max, use `(priority, counter, item)` tuples
> for payloads. Top-k → heap of size k; stream median → two heaps.

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
