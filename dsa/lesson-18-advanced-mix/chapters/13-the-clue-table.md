# 13 — The Clue Table + What's Next

> 5-minute read. The capstone: naming the tool from the problem.

## The idea, plain words

The hardest interview skill isn't using a tool — it's **recognizing
which one a problem wants.** Problems never say "use a trie." They say
"autocomplete," or "appears twice except," or "next warmer day." Here's
the decoder — memorize the smells, not the tools:

| The problem smells like… | Reach for | Lesson |
|--------------------------|-----------|--------|
| "prefix", "autocomplete", "words starting with", dictionary-driven search | **Trie** | 18 |
| "every element appears twice except…", O(1) space required, parity | **XOR tricks** | 18 |
| count/isolate bits, power of two, bitmask over ≤ 20 items | **Bit manipulation** | 18 |
| "next greater/smaller", "days until", span, largest rectangle | **Monotonic stack** | 18 |
| "are a and b connected" as edges stream in, "does this edge make a cycle" | **Union-find** | 14 |
| top-K, streaming median, "k-th largest" | **Heap** | 12 |
| longest/shortest contiguous window | **Sliding window** | 05 |
| sorted input, "find the target/threshold" | **Binary search** | 09 |
| pairs with a sum, dedup, "seen before" | **Hashing** | 03 |
| "try all options, undo the choice" | **Backtracking** | 08 |
| overlapping subproblems, "count ways", "min cost" | **DP** | 15–16 |
| "best local choice", intervals, scheduling | **Greedy** | 17 |

Two heuristics are nearly deterministic:
**"pairs cancel / find the odd one out" → XOR.** And
**"for each element, the next/first position where…" → monotonic stack.**
And when a hard problem mixes grid DFS with a word list — the trie is
the accelerant; plain DFS×words is the TLE.

## Common mistake

Memorizing the *tools* instead of the *smells*. Nobody is asked "code a
trie" — they're asked "return all dictionary words findable on this
grid," and the people who practiced pattern-recognition spot the trie
in 10 seconds while everyone else writes a TLE brute force. When a
problem resists every tool you try, ask the table's question: **what
does the problem smell like?**

## Edge cases to always test (all 18 lessons)

Empty input · single element · all-same-values · negatives in bit
problems · words that are prefixes of other words (`"app"`/`"apple"`) ·
single-row histograms · grid words longer than the board can spell.

## Your turn — name the tool before peeking

1. "Find any word in the grid, given a dictionary of 100k words."
2. "Every number appears 3 times except one."
3. "How many days until a warmer temperature, per day?"
4. "Edges arrive one at a time — report the first that forms a cycle."

<details><summary>Answers</summary>
1. **Trie** on the dictionary + grid DFS that dies on non-prefixes
   (`hard/p01`). 2. **Bit counting per bit-position** — count 1s in
   each column mod 3 (XOR works only for "twice"). 3. **Monotonic
   stack** of indices; answer = `i - popped_index`. 4. **Union-find** —
   the first edge where `find(a) == find(b)`.
</details>

## You finished the whole course — really

Eighteen lessons: from "what is an algorithm" to bitwise tries. You now
own every core interview tool **and** the map that picks between them.

What's next:

1. `task-explanation.md` → solve `easy/` → `medium/` → `hard/` in
   order; run `check.py` after each. Peek at `solutions/` only after a
   real attempt — then close it and redo from memory.
2. `coding-check.md` — the oral drills; say the answers out loud.
3. `EXTRA-PRACTICE.md` — real interview questions on these topics.
4. After this course: **re-solve old problems cold** in a week, then a
   month — spaced repetition is how "I once knew this" becomes "I just
   know this." Then mock interviews: say the clue-table reasoning out
   loud before you write a line. That narration IS the interview.

Go build the nine problems. You've earned this lesson.

---

**← Prev** [12 — Union-find: when it beats DFS](12-union-find-when-it-wins.md) ·
Done with concepts? → Open `task-explanation.md` and solve `easy/p01` next.
