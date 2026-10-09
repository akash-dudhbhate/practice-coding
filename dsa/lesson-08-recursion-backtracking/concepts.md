# Lesson 08 — Recursion & Backtracking

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **11 tiny files, ~5 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.

Recursion is the hardest mental leap so far, so the chapters go SLOW:
what a self-call even means → the stack underneath it → tracing by hand →
then backtracking as "recursion + undo".

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [A function that calls itself](chapters/01-a-function-that-calls-itself.md) | what recursion even IS |
| 02 | [The call stack](chapters/02-the-call-stack.md) | where paused calls wait (lesson 06, again) |
| 03 | [The two rules](chapters/03-the-two-rules.md) | base case + shrinking input |
| 04 | [Tracing factorial by hand](chapters/04-trace-factorial-by-hand.md) | draw the stack, watch answers bubble up |
| 05 | [When it never stops](chapters/05-when-it-never-stops.md) | RecursionError and the ~1000-frame cap |
| 06 | [Trees of calls](chapters/06-trees-of-calls.md) | why `fib` explodes — O(2ⁿ) in the wild |
| 07 | [The three questions](chapters/07-the-three-questions.md) | contract · base · shrink — and TRUST |
| 08 | [Backtracking = recursion + undo](chapters/08-backtracking-choose-explore-unchoose.md) | choose → explore → unchoose |
| 09 | [Subsets: the decision tree](chapters/09-subsets-decision-tree.md) | include/skip — every leaf is an answer |
| 10 | [Permutations: the decision tree](chapters/10-permutations-decision-tree.md) | "any unused" choices and the `used` marks |
| 11 | [Enumerate or optimize?](chapters/11-enumerate-or-optimize.md) | backtracking vs DP — the lesson-15 fork |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> Recursion = a function that calls itself on a **smaller** input until a
> **base case** answers directly; each call is a frozen *frame* on the call
> stack (push on the way down, pop on the way up — capped near ~1000 deep).
> Before coding, answer: **what does it return · what's the base · how does
> it shrink** — then trust the recursive call instead of simulating it.
> Backtracking adds one move: **choose → explore → unchoose**, walking a
> decision tree whose leaves are your answers (`copy()` any path you
> record!). "Enumerate all" → backtracking; "count/best with repeated
> subcalls" → memoize → lesson 15.

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
