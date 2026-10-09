# 11 — Enumerate or Optimize? (Backtracking vs DP)

> 5-minute read. The fork in the road — and the bridge to lesson 15.

## The idea, plain words

Both backtracking and DP decompose problems recursively. The difference is
what the tree of calls *looks like* — and what the question asks for:

- **Backtracking:** "enumerate ALL ways to satisfy constraints." Each node
  is a *different state*, visited once; you want every leaf. Exponential —
  because the answer set itself is exponential.
- **DP (lesson 15):** "compute the best count/value." The SAME subproblem
  is reached many ways (remember `fib` from chapter 06, computed 5× over) —
  so cache it, or the tree explodes.

## The smell test — read the question

```
"all subsets of [1,2,3]"        → backtracking — the answer HAS 8 entries
"n-queens: all boards"          → backtracking — the answer IS a list
"how many ways to climb stairs" → fib-shaped — subcalls overlap → memo/DP
"count subsets that sum to k"   → DP — identical (i, remaining) states recur
```

**"all / enumerate / every valid X" → backtracking.**
**"count / max / min / is it possible" + repeated identical subcalls → DP.**

Picking wrong is catastrophic in both directions: memoizing subsets buys
you a huge cache for an inherently exponential answer (no win). Recomputing
`fib` gives exponential time for a single number (disaster — chapter 06's
1-trillion-call `fib(50)`).

## The preview — a 2-line fix

Chapter 06's `fib` made 21,891 calls for `fib(20)`. Add one dict and it
collapses:

```python
def fib(n, memo={}):
    if n < 2:
        return n
    if n in memo:                       # seen this subproblem? reuse it
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

`fib(20)` now needs ~40 calls, not 21,891 — the repeated subtrees get
answered from the cache instead of recomputed. That's **memoization**:
recursion + remembering. Lesson 15 makes it the main event; if you can
write the recursion cleanly (three questions, chapter 07), the memoization
step is a small decoration on top.

## Why it exists

Interviewers watch whether you NOTICE which world you're in before coding.
Backtracking written for a count problem "works" but times out; DP written
for an enumeration problem has nothing to cache. Two seconds of smell-test
saves you from building the wrong machine.

## Where it's used

- `medium/` + `hard/` here: pure backtracking — enumerate, prune invalid
  choices early (that's all N-Queens is: the same tree, plus "skip columns
  and diagonals already under attack").
- Lesson 15 `dp-1d` and lesson 16 `dp-2d-knapsack`: the cache-first world.

## Common mistake

Reading "count the ways" and reaching for a queue of partial answers —
enumerating millions of paths just to count them. If only the NUMBER
matters, never build the paths; recurse on `(state)` → `int`, and memoize.

## Your turn

Classify each: (a) "list every valid sudoku completion", (b) "minimum coins
to make $1.00", (c) "all palindrome partitions of a string".

<details><summary>Answer</summary>
(a) backtracking — "every" + constraints. (b) DP — "minimum" + the same
remaining-amount subproblems recur. (c) backtracking — "all" again. The
word "all" is the loudest signal in the whole lesson.
</details>

## What you now know

You can: explain the call stack, state the two rules, trace a recursion
frame by frame, predict RecursionError, read a call tree, write the three
questions before coding, and tell enumerate-all from optimize-with-cache.
**That's the whole lesson.** `easy/` → `medium/` → `hard/` now drills it.

---

**← Prev** [10 — Permutations](10-permutations-decision-tree.md) ·
Done with concepts? → Open `task-explanation.md` and solve `easy/p01` next.
