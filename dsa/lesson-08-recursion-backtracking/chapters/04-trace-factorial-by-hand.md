# 04 — Tracing Factorial, Frame by Frame

> 6-minute read. THE skill of this lesson — do it with a finger on the screen.

## The idea, plain words

You don't *understand* recursion by thinking about it — you understand it
by **drawing the stack**. Once: the calls pile up, then the answers bubble
back. Do this trace by hand once and recursion stops being magic.

The function:

```python
def fact(n):
    if n <= 1:                 # base case: 1! = 1, 0! = 1
        return 1
    return n * fact(n - 1)     # n! = n × (n-1)!
```

## Phase 1 — calls pile DOWN the stack

`fact(3)` can't finish yet — it needs `fact(2)` first, which needs
`fact(1)`. Each call freezes mid-multiplication:

```
main()
 └─ fact(3)                    ← frozen at "3 * ???"
      └─ fact(2)               ← frozen at "2 * ???"
           └─ fact(1) → returns 1    ← BASE CASE: answers directly
```

Three live frames, each with its own `n`, each waiting on the frame above.

## Phase 2 — answers bubble UP

When `fact(1)` returns `1`, the frame below wakes up and finishes its
frozen line:

```
fact(1) → returns 1           (frame pops)
fact(2) → 2 * 1  → returns 2  (frame pops)
fact(3) → 3 * 2  → returns 6  (frame pops)
main() gets 6
```

Run it to confirm: `print(fact(3))` → `6`. And `print(fact(5))` → `120`.

**Two passes every time:** calls descend (each deeper, each smaller),
answers ascend (each combining with its caller's piece). The deepest call
answers first; the first call answers last. Last-in, first-out — a stack.

## One more trace — `sum_digits(1234)`

Same shape, drawn in one picture (this is `easy/p01`'s function):

```
sum_digits(1234)  ->  10
  └─ 1234 % 10 = 4   +   sum_digits(123)
                        └─ 3  +  sum_digits(12)
                                  └─ 2  +  sum_digits(1)
                                            └─ 1  +  sum_digits(0)
                                                      └─ 0   <- BASE

returns bubble back up:  0 -> 1 -> 3 -> 6 -> 10
```

Each level peels one digit (`n % 10` grabs it, `n // 10` shrinks), adds it
to the answer from below. `print(sum_digits(1234))` → `10`.

## Why it exists

Interviewers literally say "trace it." More importantly, this drawing IS
your debugger — when a recursive function misbehaves, sketch its stack and
the bug (missing base, wrong shrink, wrong combine) shows itself.

## Common mistake

Forgetting phase 2 exists. `fact(3)` does NOT "become" `fact(2)` — it
*contains* it. The `3 *` waits patiently. Beginners often read
`return n * fact(n-1)` as "jump to fact(n-1)" and lose the multiplication.
The frame holds it.

## Your turn

Trace `sum_digits(205)` the same way. What does it return?

<details><summary>Answer</summary>
`205 → 20 → 2 → 0` (base, returns 0). Bubble up: `2 + 0 = 2`,
`0 + 2 = 2` — the middle digit is 0, `5 + 2 = 7`. Returns **7**.
Watch out: `205 % 10 = 5`, `205 // 10 = 20` — the zero digit is handled
normally on the way down.
</details>

---

**← Prev** [03 — The two rules](03-the-two-rules.md) ·
**Next →** [05 — When recursion never stops](05-when-it-never-stops.md)
