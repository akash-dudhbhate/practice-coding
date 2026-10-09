# 01 — The Last 10% Toolkit

> 3-minute read. What this lesson is even for.

## The idea, plain words

Lessons 01–17 gave you the everyday tools — arrays, hashing, two
pointers, sliding window, stacks, trees, heaps, graphs, DP, greedy.
Those cover roughly 90% of interview problems.

This lesson is the **last 10%**: three tools that show up less often —
but when a problem needs one, *nothing else really substitutes*:

- **Tries** — for "words that start with…" and dictionary-driven search
- **Bit manipulation** — for "find the odd one out, in O(1) space"
- **Monotonic stack** — for "the next bigger thing to my right"

Plus a union-find refresher and — most valuable of all — a **clue
table**: how to look at a problem statement and *know* which tool it
wants (chapter 13).

## A tiny taste of all three

```python
words = ["apple", "app", "apricot"]

# Tool 1: a set answers "is this word present"...
print("app" in set(words))                          # True
# ...but "every word starting with 'app'" scans everything:
print([w for w in words if w.startswith("app")])    # ['apple', 'app']

# Tool 2: XOR — pairs cancel, the loner survives, zero extra memory
print(4 ^ 1 ^ 2 ^ 1 ^ 2)                            # 4

# Tool 3: "next warmer day" — you'll build this in chapter 10
temps = [70, 75, 71]       # answer will be [75, -1, -1]  (wait for it)
```

The first tool needs a new data structure (the trie). The second needs a
new *way of seeing numbers* (bits). The third needs a new *way of using
an old tool* (a stack kept sorted).

## Why it exists

Interviewers love these because they're **unfakeable**. "Can you do it
in O(1) space?" forces XOR. "Is this path a prefix of *any* word, in
O(1)?" forces a trie. You can't brute-force your way to the intended
answer — so having these in your pocket is a real edge.

## Where it's used

Autocomplete on your phone, routers matching IP prefixes, file
permissions and compression (bits), stock-price and weather apps (next
greater), and every hard-tier interview question that combines two of
them — like "maximum XOR of a pair," which is secretly a *bitwise trie*.

## Common mistake

Skipping this lesson because "it's rare." Rare ≠ never — and these are
exactly the problems that separate "can code" from "really knows their
tools." One chapter at a time, it'll be painless.

## Your turn

Without running it — what does `3 ^ 3 ^ 7` print? Say it out loud.

<details><summary>Answer</summary>
**7.** `3 ^ 3 = 0` (a pair cancels), and `0 ^ 7 = 7`. You just used the
most important trick in this lesson — chapter 06 explains why.
</details>

---

**Next →** [02 — A trie: a tree made of letters](02-trie-a-tree-of-letters.md)
