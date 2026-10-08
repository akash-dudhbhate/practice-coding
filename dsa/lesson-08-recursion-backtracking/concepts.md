# Lesson 08 — Concepts Explained (Recursion & Backtracking)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What Recursion Is: Base Case + Shrinking Input + Trust

**What:** A recursive function calls itself on a *smaller* version of the same
problem, until it hits a case so small it can answer directly — the **base
case**. Every recursion needs all three ingredients:

1. **Base case** — the input where you return without calling yourself.
2. **Shrinking input** — each call must get strictly closer to the base case.
3. **Trust (the leap of faith)** — assume `f(smaller)` already works; just
   combine its answer with your piece.

**Why it exists:** Some problems are self-similar — a list is "an element plus
a smaller list", a folder is "files plus smaller folders", a tree is "a node
plus subtrees". Recursion lets you describe the structure once and let the
language's call stack do the bookkeeping a loop would need manual state for.

**Where it's used:** Trees (lesson 11!), divide & conquer (merge sort, binary
search), backtracking (this lesson's second half), parsing, filesystem walks,
anything nested. Roughly half of interview problems have a recursive skeleton.

**The call stack — `sum_digits(1234)` unwinding:**

```
sum_digits(1234)  ->  10
  └─ 1234 % 10 = 4   +   sum_digits(123)
                        └─ 3  +  sum_digits(12)
                                  └─ 2  +  sum_digits(1)
                                            └─ 1  +  sum_digits(0)
                                                      └─ 0   <- BASE

returns bubble back up:  0 -> 1 -> 3 -> 6 -> 10
```

Each level is a *stack frame*: it freezes its own variables, waits for the
deeper call, then resumes. Python pushes one frame per call — that's real
memory, which is why depth matters (next concept).

```python
def sum_digits(n):
    if n == 0:                    # base case: nothing left to add
        return 0
    return n % 10 + sum_digits(n // 10)   # last digit + digits' sum
```

**What goes wrong without it:**
- **No base case** → `RecursionError: maximum recursion depth exceeded` —
  the function never stops calling itself.
- **Input doesn't shrink** → `f(n) = f(n)` forever; same crash, slower.
- **No trust** → beginners re-derive the subproblem inside the call ("what
  does sum_digits(123) do?" and mentally simulate it). Don't. Write what the
  function promises to return, then use that promise.

---

## The Three Questions Every Recursive Function Answers

**What:** Before writing a line of recursion, answer out loud:

1. **What does this function return?** (a number? a list? nothing — just
   fills a collector?) The contract must be IDENTICAL at every depth.
2. **What's the base case?** The smallest input with a trivial answer.
3. **How does the input shrink?** `n // 10`? `nums[1:]`? `i + 1`? If it
   doesn't shrink toward the base, it can't terminate.

**Why it exists:** Recursion bugs are all violations of one of the three —
wrong contract (returns a list sometimes, an int others), missing base
(crashes), no shrink (infinite). Answering them first converts "mysterious
recursion" into a checklist.

**Where it's used:** Literally every recursive function you write.

**Worked example — `power(2, 10)` the three questions:**

```python
def power(base, exp):
    # 1. returns a number: base^exp
    # 2. base case: exp == 0 -> 1  (anything^0)
    # 3. shrinks: exp - 1 each call
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
```

```
power(2, 3) -> 2 * power(2,2) -> 2*(2*power(2,1)) -> 2*(2*(2*power(2,0)))
                              base: power(2,0) = 1
unwind: 2*(2*(2*1)) = 8
```

**What goes wrong without it:**
- Contract wobble: `countdown` that appends to a list on some calls and
  returns it on others → `None` propagates and crashes callers.
- Base case below the shrink: `power` recursing on `exp - 1` when `exp` can
  be called with a negative → never hits 0. Guard `exp <= 0` or document
  the precondition.

---

## Recursion vs Iteration — and the Depth Limit

**What:** Anything recursive can be written iteratively with an explicit
stack — recursion just borrows the *call* stack instead. Python caps that
stack at ~1000 frames (`sys.getrecursionlimit()`); exceeding it raises
`RecursionError`.

**Why it exists:** The cap protects you from true infinite recursion eating
all memory — but it also means recursion is a poor fit for "linear" problems
where n can be huge. `sum_digits(10**500)` needs 500+ frames; a loop needs 1
variable.

```python
import sys
sys.getrecursionlimit()          # ~1000 by default
sys.setrecursionlimit(100000)    # you CAN raise it...
# ...but CPython can then segfault on a real stack overflow. Loops are safer
# for deep linear work; save recursion for log-depth or branching problems.
```

**Where it's used:** Recursion wins when the SHAPE is recursive — trees,
backtracking, divide & conquer — each with depth ~log n or problem-bounded.
Iteration wins for long linear scans.

**What goes wrong without it:**
- Recursive `fib` on n=40 → ~330 MILLION calls (exponential; lesson 15's
  memoization fixes exactly this). Recursion ≠ slow — *overlapping
  subproblems* are slow.
- Recursion on a 100k-length list → RecursionError where a `while` loop is
  one line. Match the tool to the depth.
- Hidden O(n) per level: `nums[1:]` COPIES the list — recursion that slices
  is O(n²) total. Pass an index instead of slicing.

---

## Backtracking = Recursion + Undo (choose → explore → unchoose)

**What:** Backtracking is recursion where each level makes a CHOICE,
recurses, then UNDOES the choice to try the next one. The pattern:

```python
def backtrack(state):
    if done(state):
        results.append(copy(state))   # found a full solution
        return
    for choice in available_choices:
        state.append(choice)          # CHOOSE
        backtrack(state)              # EXPLORE deeper
        state.pop()                   # UNCHOOSE — restore for next sibling
```

**Why it exists:** "Generate all X" problems (all subsets, all permutations,
all valid boards) have exponential answer sets — there's no clever closed
form. The only way is systematic enumeration, and the call stack is the
perfect "undo journal": when a call returns, its frame dies and you're back
in the parent with the parent's state — IF you cleaned up after yourself.

**Where it's used:** Subsets/permutations/combinations, N-Queens, sudoku,
word search, constraint puzzles, compilers' instruction selection.

**Subsets — the include/exclude decision tree for `[1, 2]`:**

```
                      []
              include 1 /      \ skip 1
                    [1]          []
                i2/      \s2   i2/    \s2
               [1,2]    [1]   [2]    []
```

Every leaf is one subset: `{1,2}, {1}, {2}, {}`. Depth = position in the
input; choice = include or skip.

```python
def subsets(nums):
    out = []
    def dfs(i, path):
        if i == len(nums):
            out.append(path.copy())   # copy! path gets reused
            return
        dfs(i + 1, path + [nums[i]])  # include nums[i]
        dfs(i + 1, path)              # skip nums[i]
    dfs(0, [])
    return out
```

(The `path + [x]` version passes a fresh list so no undo is needed; the
mutating version `path.append(x) / dfs / path.pop()` is the classic form.)

**Permutations — the other shape:** choices are "any unused element", not
"include/skip". Track `used[i]` or recurse on the remaining pool:

```python
def permutations(nums):
    out = []
    def dfs(path, used):
        if len(path) == len(nums):
            out.append(path.copy()); return
        for i in range(len(nums)):
            if used[i]: continue
            used[i] = True;  path.append(nums[i])   # choose
            dfs(path, used)                          # explore
            path.pop();      used[i] = False         # unchoose
    dfs([], [False] * len(nums))
    return out
```

**What goes wrong without it:**
- **No undo** → state leaks between branches: subsets comes back with
  `[1,2]` junked inside what should be `[]`. If you mutate, you must pop.
- **Appending `path` not `path.copy()`** → every entry in `out` is the SAME
  list object — they all read as whatever `path` ends as. THE #1
  backtracking bug.
- Pruning correctly but forgetting the return: after `done`, `return` — or
  the loop keeps exploring past the solution.

---

## Backtracking vs DP: Choices vs Overlapping Subproblems

**What:** Both decompose problems recursively — the difference is what the
decomposition LOOKS like:

- **Backtracking:** "enumerate all ways to satisfy constraints." The
  subproblems are *different states*, each visited once; you want every
  leaf (or the first valid one). Exponential by nature — the answer set IS
  exponential.
- **DP (lesson 15):** "compute the best count/value." The SAME subproblem
  (`fib(20)`) is reached many ways — so cache it, or the tree explodes.

**Why it exists:** Picking wrong is catastrophic: memoizing subsets gives
you an exponentially-sized cache for an exponential answer (no win); brute
recomputing fib gives exponential time for a scalar answer (disaster).

**The smell test:** If the question asks "all ways / enumerate / any valid
X" → backtracking. If it asks "count / max / min / is it possible" AND you
notice identical subcalls → memoize toward DP.

```
"all subsets of [1,2,3]"   -> backtracking, answer has 8 entries (2^n)
"count ways to climb n stairs" -> fib-shaped; subcalls overlap -> DP/memo
"n-queens: all boards"     -> backtracking, answer IS a list of boards
```

**What goes wrong without it:**
- Using backtracking where DP fits: "how many subsets sum to k?" via
  enumerate-and-count re-visits identical (i, remaining) states — it works
  but wastes exponential time that memoization collapses.
- Using DP thinking on enumeration: there's nothing to cache — every subset
  is a distinct answer. Just generate them all.

Foreshadowing: lesson 15 turns overlapping-subproblem recursion into
memoized DP. If you can write the recursion cleanly here, the memoization
step is a 2-line decoration on top.

---

## The Big Picture

Three questions, one pattern, one fork:

1. **Contract, base, shrink** — every recursive function is these three
   sentences turned into code.
2. **choose → explore → unchoose** — backtracking is just recursion where
   you restore shared state between sibling branches.
3. **Enumerate or optimize?** — "all solutions" = backtracking; "best or
   count with repeated subcalls" = memoization/DP (lesson 15).

If a recursion explodes, ask: *is the answer set itself exponential*
(fine — it's backtracking), *or am I re-solving the same subproblem*
(cache it — that's DP).
