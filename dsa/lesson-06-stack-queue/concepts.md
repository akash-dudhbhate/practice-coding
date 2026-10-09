# Lesson 06 — Stacks & Queues

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **12 tiny files, ~4 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [What is a stack? (LIFO)](chapters/01-what-is-a-stack.md) | the one rule a stack enforces |
| 02 | [Stack ops: push, pop, peek](chapters/02-stack-ops-push-pop-peek.md) | the 4 commands + their cost |
| 03 | [A stack is a plain list](chapters/03-stack-as-a-plain-list.md) | why append/pop are O(1) but insert(0) isn't |
| 04 | [What is a queue? (FIFO)](chapters/04-what-is-a-queue.md) | the fair counterpart to LIFO |
| 05 | [deque: why list.pop(0) is a trap](chapters/05-deque-why-pop0-is-slow.md) | O(n) vs O(1) at the front |
| 06 | [Stacks reverse, queues preserve](chapters/06-stack-reverses-queue-preserves.md) | the superpower behind easy problems |
| 07 | [Balanced brackets](chapters/07-balanced-brackets.md) | **THE canonical stack problem — traced step by step** |
| 08 | [Monotonic stack: next greater](chapters/08-monotonic-stack-next-greater.md) | the pop moment = the answer |
| 09 | [Sliding-window max & BFS](chapters/09-sliding-window-max-and-bfs.md) | monotonic deque + FIFO preview |
| 10 | [Two stacks make a queue](chapters/10-two-stacks-make-a-queue.md) | the pour trick + amortized O(1) |
| 11 | [Stack vs queue: how to choose](chapters/11-choosing-stack-vs-queue.md) | the decision cheat sheet |
| 12 | [The pitfall gallery](chapters/12-pitfall-gallery.md) | six ways it goes wrong |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> A **stack** is Last-In-First-Out — a pile of plates; in Python it's a
> list with `append`/`pop()` (O(1) at the end). A **queue** is
> First-In-First-Out — a line at a shop; in Python it's
> `collections.deque` with `append`/`popleft` (O(1) at both ends —
> `list.pop(0)` is O(n), a trap). Stacks match nested things (balanced
> brackets) and reverse sequences; a *monotonic* stack turns "next
> greater element" from O(n²) into O(n); a monotonic deque gives
> sliding-window max; two stacks poured into each other make a queue.
> Everything here is "each element enters and leaves once" → O(n).

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
