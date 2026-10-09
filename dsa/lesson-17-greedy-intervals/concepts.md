# Lesson 17 — Greedy & Intervals

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **11 tiny files, ~5 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [What "greedy" means](chapters/01-what-greedy-means.md) | what taking the locally-best option is |
| 02 | [When greedy FAILS](chapters/02-when-greedy-fails.md) | the [1,3,4] coin trap — greedy's famous loss |
| 03 | [Greedy or DP?](chapters/03-greedy-or-dp.md) | "does a local choice ever need revising?" |
| 04 | [Interval words](chapters/04-interval-words.md) | start/end, overlap, touching, contained |
| 05 | [Sort by start or by end?](chapters/05-sort-by-key.md) | why the sort key IS the algorithm |
| 06 | [Activity selection](chapters/06-activity-selection.md) | keep max non-overlapping — sort by END |
| 07 | [Merge intervals](chapters/07-merge-intervals.md) | sort by START, grow one blob — traced |
| 08 | [Insert & meeting rooms](chapters/08-insert-and-meeting-rooms.md) | 3-phase insert, room counting |
| 09 | [The exchange argument](chapters/09-exchange-argument.md) | why greedy is provable — "swapping never hurts" |
| 10 | [Reach-tracking greedy](chapters/10-reach-tracking.md) | Jump Game & Gas Station — no sort, one variable |
| 11 | [Greedy or not?](chapters/11-greedy-or-not.md) | the checklist, the recipe, six pitfalls |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> Greedy = take the locally-best choice and never look back — a bet that
> your problem has the "greedy choice property" (coins `[1,3,4]` fail it;
> US coins and interval scheduling pass it — when in doubt, use DP).
> Interval problems: **sort by the right key** (end → keep max
> non-overlapping; start → merge/insert/meeting-rooms), **sweep once**,
> track one `current`/`last_end` variable. Reach problems (jump, gas):
> no sort — one variable tracks how far your decisions can take you.
> Prove it with the exchange argument: swapping never makes it worse.

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
