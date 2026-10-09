# 02 — Memoization: write the answers down (top-down DP)

> 6-minute read. The single most important trick in this lesson.

## The idea, plain words

**Memoization** (not "memorization" — it's from *memo*, a written note):
before computing an answer, **check your notebook**. If it's there, return
it instantly. If not, compute it once and **write it down**.

Real-life version: a classmate asks you "what's 47 × 83?" You work it out:
3901. Ten minutes later someone asks again. You don't redo the
multiplication — you glance at your notebook. Same question → same answer
→ zero new work.

Keep the recursion from chapter 01 *exactly as is*. Add a dict.

```python
def fib(n, memo={}):
    if n in memo:                # notebook check FIRST
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)   # write it down
    return memo[n]
```

Python even ships the notebook for you:

```python
from functools import lru_cache

@lru_cache(maxsize=None)          # "remember every answer forever"
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

## Watch it work — call counter, measured

Same function, a `calls += 1` line at the top:

```
naive:   fib(30) → 832040   after 2,692,537 calls
memo:    fib(30) → 832040   after       59 calls
```

**2.7 million → 59.** The memoized `fib(30)` asks each of `fib(0..30)`
once; every repeat is a dict lookup. That's the whole magic of DP.

Hand-trace `fib(5)` with memo — watch the cache hits:

```
fib(5)
 ├─ fib(4)
 │   ├─ fib(3)
 │   │   ├─ fib(2)
 │   │   │   ├─ fib(1) → compute: 1   memo={1:1}
 │   │   │   └─ fib(0) → compute: 0   memo={0:0, 1:1}
 │   │   │   → memo[2] = 1
 │   │   └─ fib(1) → CACHE HIT → 1
 │   │   → memo[3] = 2
 │   └─ fib(2) → CACHE HIT → 1
 │   → memo[4] = 3
 └─ fib(3) → CACHE HIT → 2
 → memo[5] = 5
```

The entire right half of the old tree — gone. Every `CACHE HIT` was a
whole subtree we didn't climb.

## Why it exists

We proved in ch.01 that naive recursion re-solves identical subproblems
exponentially many times. Memoization is the minimal fix: same code
shape, +2 lines, and each distinct subproblem runs its body **once**.

This style is called **top-down**: you start at the big question
(`fib(30)`) and recurse down to the base cases, filling the notebook on
the way back up.

## Where it's used

Any recursive solution where you spot repeated calls. Interviews accept
top-down + `@lru_cache` as a full DP answer — it's often the fastest path
from "I see the recursion" to working code.

## Common mistake

Forgetting to **store** before returning — `return fib(n-1)+fib(n-2)`
without `memo[n] = ...` means the notebook stays empty and nothing is
saved. Also: the memo key must capture everything the answer depends on.
Here it's just `n`. If your function depends on two things
(`fib(n, k)`), the key must include both.

## Your turn

Memoized `fib(5)` made 9 calls total (count them in the trace: 6 computes
+ 3 cache hits). How many calls does memoized `fib(6)` make?

<details><summary>Answer</summary>
11. `fib(6)` = 1 new compute + the whole `fib(5)` subtree (9 calls) +
1 cache hit for `fib(4)` → 1 + 9 + 1 = 11. The pattern: memoized
`fib(n)` ≈ `2n − 1` calls. Linear, not exponential.
</details>

---

**← Prev** [01 — Fib revisited](01-fib-revisited.md) ·
**Next →** [03 — When does this trick apply?](03-when-does-dp-apply.md)
