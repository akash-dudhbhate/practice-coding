# 06 — When Calls Branch: Call Trees

> 6-minute read. Recursion gets a new shape — and a scary new cost.

## The idea, plain words

So far every function called itself **once** — the stack was a straight
line. But a function can call itself *twice* (or more), and then the stack
isn't a line anymore: it's a **tree**.

The classic: Fibonacci, where each number is the sum of the previous two —
`fib(n) = fib(n-1) + fib(n-2)`.

```python
def fib(n):
    if n < 2:                          # base cases: fib(0)=0, fib(1)=1
        return n
    return fib(n - 1) + fib(n - 2)     # TWO recursive calls
```

## Draw the tree for fib(5)

Each call pauses and spawns two children before it can add:

```
                    fib(5)
              ┌──────┴──────┐
           fib(4)          fib(3)
          ┌──┴──┐         ┌──┴──┐
       fib(3)  fib(2)  fib(2)  fib(1)
       ┌─┴─┐   ┌─┴─┐    ┌─┴─┐
    fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
    ┌─┴─┐
 fib(1) fib(0)
```

Count the nodes: **15 calls** just for `fib(5)`. And look — `fib(3)` is
computed TWICE, `fib(2)` three times. The tree keeps re-solving identical
subproblems.

## Watch the cost explode

```python
calls = 0
def fib(n):
    global calls
    calls += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

```
fib(5)  → 15 calls
fib(10) → 177 calls
fib(20) → 21,891 calls
fib(30) → ~2.7 million calls
fib(50) → ~1 trillion calls — do NOT run and wait
```

Every level roughly doubles — that's **O(2ⁿ)**, the "brick wall" from
lesson 01, chapter 10. Each extra input doubles the total work.

## Why it exists

Branching recursion isn't a bug in the function — `fib` is correct. The
explosion comes from **overlapping subproblems**: the same `fib(k)` reached
by many paths, recomputed every time. That diagnosis is the whole game —
and lesson 15 (dynamic programming) is literally the fix: cache each answer
once, and the tree collapses to a line. Preview in chapter 11.

## Where it's used

Call trees are how you *analyze* any branching recursion: nodes = total
calls, depth = stack height. Backtracking (next chapter onward) is entirely
about walking trees like this — except there, each leaf is an answer you
actually want.

## Common mistake

Reading "recursion is exponential" as "recursion is slow." Recursion ≠
slow — *overlapping subproblems* are slow. `fact(n)` recurses n times,
fine. `fib(n)` recurses 2ⁿ times because it forgets. Same syntax, wildly
different work.

## Your turn

In the `fib(5)` tree above, how many times does `fib(1)` appear as a node?

<details><summary>Answer</summary>
5 times — count the leaves labeled `fib(1)`. Every one of them is a
separate call that recomputes "return 1". That's the overlap: the tree
does 15 nodes of work for a problem with only 6 distinct subproblems
(`fib(0)` through `fib(5)`).
</details>

---

**← Prev** [05 — When it never stops](05-when-it-never-stops.md) ·
**Next →** [07 — The three questions](07-the-three-questions.md)
