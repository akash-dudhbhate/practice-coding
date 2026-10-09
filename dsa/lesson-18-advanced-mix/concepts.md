# Lesson 18 — Advanced Mix (Tries, Bits, Monotonic Stack)

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **13 tiny files, ~4 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.

This is the **last lesson** — the "last 10%" toolkit. These tools are
rarer in interviews than lessons 02–15, but each is *the* answer for its
niche, and no general-purpose technique covers that niche well.

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [The last 10%](chapters/01-the-last-10-percent.md) | why this lesson exists at all |
| 02 | [A trie: a tree made of letters](chapters/02-trie-a-tree-of-letters.md) | how autocomplete is a data structure |
| 03 | [Coding a trie: the `is_end` flag](chapters/03-trie-code-is-end.md) | `search` vs `startsWith` — the whole point |
| 04 | [What a bit actually is](chapters/04-what-is-a-bit.md) | binary from zero — no fear |
| 05 | [The six bit operators](chapters/05-six-bit-operators.md) | read `& \| ^ ~ << >>` column by column |
| 06 | [XOR cancels pairs](chapters/06-xor-cancels-pairs.md) | find the loner in O(1) space |
| 07 | [The lowest-bit tricks](chapters/07-lowest-bit-tricks.md) | `x & (x-1)`, `x & -x`, power-of-2 |
| 08 | [Two loners + Python's quirks](chapters/08-two-singles-and-python-quirks.md) | the XOR partition; why `~5 = -6` |
| 09 | [The bitwise trie: max XOR](chapters/09-bitwise-trie-max-xor.md) | two tools fused — `hard/p02` unlocked |
| 10 | [Monotonic stack: next greater](chapters/10-monotonic-stack-next-greater.md) | the O(n) "next bigger thing" trick |
| 11 | [Largest rectangle + circular](chapters/11-rectangle-and-circular.md) | the sentinel + wrap-around moves |
| 12 | [Union-find: when it beats DFS](chapters/12-union-find-when-it-wins.md) | dynamic vs static connectivity |
| 13 | [The clue table + what's next](chapters/13-the-clue-table.md) | which tool a problem wants — all 18 lessons |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> Three niche tools: a **trie** stores words as shared letter-paths so
> prefix questions ("starts with 'app'") cost one hop per character; one
> `is_end` flag separates "path exists" from "word ends here." **Bit
> manipulation** treats numbers as rows of switches — XOR cancels pairs
> (`a^a=0`) to find loners in O(1) space, `x & (x-1)` erases the lowest
> 1-bit (power-of-2 test, bit counting), `x & -x` isolates it. A
> **monotonic stack** keeps indices sorted so a new element pops
> everything it dominates — answering "next greater" for every element
> in one O(n) pass. Union-find still owns *streaming* connectivity.

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
