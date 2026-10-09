# 05 — When Recursion Never Stops: RecursionError

> 5-minute read. The crash you'll see most, and why Python causes it
> on purpose.

## The idea, plain words

Frames cost real memory (chapter 02). A function that never hits its base
case would pile up frames until your computer ran out of memory entirely —
so Python **cuts it off** at a fixed ceiling:

```python
import sys
sys.getrecursionlimit()        # 1000 — about a thousand frames deep
```

Call deeper than that and Python raises:

```
RecursionError: maximum recursion depth exceeded
```

Watch it happen, safely:

```python
def forever(n):
    return forever(n + 1)      # no base case, n only grows

try:
    forever(0)
except RecursionError as e:
    print("RecursionError caught:", e)
```

```
RecursionError caught: maximum recursion depth exceeded
```

The function called itself ~1000 times, Python said "enough", and threw
the error. That's a *rescue*, not a malfunction — an unbounded stack would
be far worse.

## Recursion vs a plain loop

Anything recursive CAN be written with a loop plus an explicit stack (or
just a variable, for linear shapes). So when do you pick which?

```python
# same job, two shapes
def sum_digits_rec(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits_rec(n // 10)

def sum_digits_loop(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
```

- **The loop** uses O(1) memory — one variable, no matter how huge `n` is.
- **The recursion** spends one frame per digit — fine for a 10-digit number,
  dead at ~1000 digits.

**Rule of thumb:** recursion for *branching or log-depth* shapes (trees,
backtracking, divide & conquer — depth ~log n or small). Loops for *long
linear* walks where depth ≈ n.

You CAN raise the ceiling — `sys.setrecursionlimit(100000)` — but CPython
can then actually crash (segfault) on a real stack overflow. Don't treat
that as a fix; treat it as a sign the problem wanted a loop.

## Why it exists

Two reasons: the cap protects you from true infinite recursion eating all
memory — AND it quietly teaches you to match tool to shape. `RecursionError`
is Python saying "this problem was linear; recursion was the wrong tool."

## Where it's used

You'll hit this error constantly while learning — every forgotten base case,
every wrong shrink direction. Read it as "rule 1 or rule 2 from chapter 03
was violated" and go find which.

## Common mistake

`nums[1:]` looks like it shrinks (and it does) — but it *copies* the list
each call: O(n) work per frame → O(n²) total on top of the depth cost.
Pass an index `i` instead of slicing. (The problems in `medium/` do exactly
that.)

## Your turn

```python
def down(n):
    if n == 0:
        return "done"
    return down(n - 1)
```

Does `down(500)` work? `down(5000)`? What changes between them?

<details><summary>Answer</summary>
`down(500)` → "done" — about 501 frames, under the 1000 ceiling.
`down(5000)` → RecursionError — it would need ~5001 frames. Same code,
same rules, only the depth differs. The fix is a `while n > 0` loop —
one variable, zero frames.
</details>

---

**← Prev** [04 — Tracing factorial](04-trace-factorial-by-hand.md) ·
**Next →** [06 — When calls branch: call trees](06-trees-of-calls.md)
