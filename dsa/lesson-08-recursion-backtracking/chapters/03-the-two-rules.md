# 03 — The Two Rules Every Recursion Obeys

> 4-minute read. The whole safety manual in two sentences.

## The idea, plain words

Every working recursive function has two ingredients — miss either one and
it breaks:

1. **A base case** — an input so small you can answer it directly, with NO
   recursive call. This is the "last person in line" from chapter 01.
2. **A shrinking input** — each recursive call must get strictly *closer*
   to that base case. `n - 1`, `n // 10`, `nums[1:]` — something that runs
   out eventually.

Think of **walking down stairs**: the base case is the floor, and each step
must actually go *down*. A staircase where a step leads sideways or back up
is a staircase you never leave.

## Watch the two rules work

```python
def sum_digits(n):
    if n == 0:                            # RULE 1: base case — nothing to add
        return 0
    return n % 10 + sum_digits(n // 10)   # RULE 2: n // 10 removes a digit
```

`sum_digits(1234)`: `1234 → 123 → 12 → 1 → 0`. Four digits, so the input
shrinks four times and then *must* hit the base case. It can't miss.

## Watch each rule break

**Break rule 1 — no base case:**

```python
def bad(n):
    return n + bad(n - 1)     # never stops — no floor
```

**Break rule 2 — input doesn't shrink:**

```python
def also_bad(n):
    if n == 0:
        return 0
    return n + also_bad(n)    # same n forever — a sideways step
```

Both end the same way: `RecursionError`. One falls forever, one treads
water forever. (Chapter 05 shows the actual crash.)

A subtler break — shrinking toward the WRONG base:

```python
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

power(2, -1)   # exp goes -1, -2, -3 ... it STEPS OVER the base case
```

Shrinking isn't enough — you must shrink *toward* your base case. Guard
with `exp <= 0` if negatives are possible.

## Why it exists

These two rules turn "does my recursion work?" into a checklist instead of
a leap of faith. Termination is automatic: a strictly shrinking input over
finite data *must* reach the base case. You don't trace every call to prove
it — you check the two rules.

## Where it's used

Literally every recursive function in this lesson — and every recursive
function anyone writes. `easy/` problems are all "name the base, name the
shrink."

## Common mistake

Writing the recursive call first and bolting on a base case at the end.
Write the base case FIRST — it's the answer you build everything on.

## Your turn

```python
def mystery(n):
    if n == 1:
        return 1
    return n + mystery(n - 2)
```

Does `mystery(10)` finish? Why or why not?

<details><summary>Answer</summary>
No — it crashes. `n` shrinks by 2: 10 → 8 → 6 → 4 → 2 → **0**, stepping
right over the base case `n == 1`. Rule 2 fails the "toward the base" test.
(For odd inputs like 7 it would finish fine — the bug hides until you feed
it an even number.)
</details>

---

**← Prev** [02 — The call stack](02-the-call-stack.md) ·
**Next →** [04 — Tracing factorial, frame by frame](04-trace-factorial-by-hand.md)
