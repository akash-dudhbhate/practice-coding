# 01 — Fib Revisited: the recursion you already know, and its dirty secret

> 5-minute read. One idea only — and you already know the code.

## The idea, plain words

You wrote this in lesson 08 (recursion). Fibonacci:

`fib(n) = fib(n-1) + fib(n-2)`, with `fib(0) = 0`, `fib(1) = 1`.

```python
def fib(n):
    if n <= 1:
        return n                    # base cases: fib(0)=0, fib(1)=1
    return fib(n - 1) + fib(n - 2)
```

Clean, correct, beautiful. And **horribly slow**. `fib(30)` makes
**2,692,537 function calls** — that's 2.7 million, for a 2-digit answer.

## Watch the waste — the call tree of fib(5)

```
                    fib(5)
                   /      \
              fib(4)        fib(3) ◄──────┐
             /     \        /    \        │ same subtree,
        fib(3)◄─┐ fib(2)  fib(2) fib(1)   │ computed AGAIN
        /   \   │  /  \    /  \
     fib(2) f(1)│f(1) f(0)f(1) f(0)
     /  \       │
   f(1) f(0)    └── fib(3) again!  ...and fib(2) shows up 3 times total
```

Count the repeats for `fib(5)` — only 15 calls, but already:

- `fib(3)` is computed **2 times**
- `fib(2)` is computed **3 times**
- `fib(1)` is computed **5 times**

Every repeated subtree is pure waste — `fib(3)` is **always** 2. The
answer can't change. Computing it twice is like re-solving the same math
homework problem because you forgot you already did it.

And it gets worse fast:

| n | calls (measured) |
|---|------------------|
| 5 | 15 |
| 10 | 177 |
| 20 | 21,891 |
| 30 | **2,692,537** |
| 50 | ~billions (don't wait for it) |

The calls grow like the Fibonacci numbers themselves — exponential.

## Why this matters (the whole lesson in one line)

The repeated subtrees are the bug AND the opportunity. If we could make
`fib(3)` computed **once** and remembered forever, the explosion
disappears. That's literally all dynamic programming is:

> **DP = recursion that remembers.**

Everything else in this lesson is details of *how* to remember.

## Common mistake

"My recursion is slow → recursion is bad." No — the recursion is *fine*;
the *re-solving* is bad. Don't abandon the recursive shape. Add memory.

## Your turn

In the `fib(5)` tree above, how many times does `fib(0)` get computed?

<details><summary>Answer</summary>
3 times — once under the left `fib(2)`, once under the middle `fib(2)`
(inside the second `fib(3)`), and once under the right `fib(2)`.
Every leaf is wasted re-computation.
</details>

---

**Next →** [02 — Memoization: write the answers down](02-memoization-top-down.md)
