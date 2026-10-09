# 07 — The Three Questions (and the Leap of Faith)

> 5-minute read. This converts "mysterious recursion" into a checklist.

## The idea, plain words

Before writing any recursive function, answer three questions out loud:

1. **What does this function return?** The *contract* — a number? a list?
   nothing, just fills a collector? It must be IDENTICAL at every depth.
2. **What's the base case?** The smallest input with a trivial answer.
3. **How does the input shrink toward it?** `n - 1`? `n // 10`? `i + 1`?

Then — the hard part — **trust the recursive call.** Assume `f(smaller)`
already works and just combine its answer with your piece. Programmers call
this the *leap of faith*: you drive the car; you don't re-invent the engine
at every wheel.

## Worked example — `power(base, exp)`

`power(2, 10)` = 2¹⁰ without `**`. Answer the questions:

```python
def power(base, exp):
    # 1. CONTRACT: returns a number — base^exp
    # 2. BASE: exp == 0 -> 1   (anything^0 is 1)
    # 3. SHRINK: exp - 1 each call, walking toward 0
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
```

`print(power(2, 10))` → `1024`.

Now the faith part. Writing `return base * power(base, exp - 1)`, a
beginner's brain screams *"but what does power(2, 9) DO?"* — and tries to
simulate it. Don't. The contract already answered that: it returns 2⁹.
Your line just multiplies it by one more 2. That's the whole thought.

```
power(2,3) → 2 * power(2,2) → 2*(2*power(2,1)) → 2*(2*(2*power(2,0)))
                                       base: power(2,0) = 1
unwind:    2 * (2 * (2 * 1)) = 8
```

## Why it exists

Every recursion bug is a violation of exactly one of the three:

- **Contract wobble** — returns a list on some paths, `None` on others →
  callers crash on the `None`.
- **Missing base** → RecursionError (chapter 05).
- **No shrink toward base** → same crash, slower.

Answer the questions first and most bugs can't even be written.

## Where it's used

`easy/p02` (`countdown`) and `easy/p03` (`power`) are literally this
checklist with different numbers. And `hard/p03` (word search) uses the
same three questions — the "input" there is just a grid position instead
of a number.

## Common mistake

The un-faith: re-deriving the subproblem *inside* the call. You see
`power(2, 9)` in your own code and mentally start unrolling it — 30 seconds
later you're lost in frames. Write the contract in a comment, believe it,
and use it. Tracing (chapter 04) is for *after* it works, or when it's
broken — not as your mental model while writing.

## Your turn

Write — on paper or in your head — the three answers for:
`reverse_string(s)` → returns `s` backwards, `"abc"` → `"cba"`.
(Hint: the shrink is `s[1:]`, the combine is "rest reversed + first char.")

<details><summary>Answer</summary>
1. Contract: returns a string — `s` reversed.
2. Base: `s == ""` (or length ≤ 1) → return `s`.
3. Shrink: `s[1:]` — one char shorter toward empty.
Code: `return reverse_string(s[1:]) + s[0]`. Then trust it:
`reverse("bc")` promises `"cb"`, you tack `"a"` on the end → `"cba"`.
</details>

---

**← Prev** [06 — Call trees](06-trees-of-calls.md) ·
**Next →** [08 — Backtracking: choose, explore, unchoose](08-backtracking-choose-explore-unchoose.md)
