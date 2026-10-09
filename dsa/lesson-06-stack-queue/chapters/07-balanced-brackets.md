# 07 — Balanced Brackets: THE canonical stack problem

> 6-minute read. Take this one slowly — it's the reason stacks exist.

## The idea, plain words

Given a string of brackets `()[]{}`, check that every opener has a
matching closer **in the right order**.

- `"({[]})"` → balanced ✓
- `"([)]"` → **not** balanced — `)` tries to close `[` before `]` does.

Real-life version: **nested boxes.** When you close a box lid, it can
only be the box you opened *most recently*. That's LIFO — which means
the tool is a stack.

## The algorithm in one breath

**Push every opener. On every closer, the top must match — pop it.
At the end, the stack must be empty.**

## Hand-trace `"({[]})"` — watch the stack every step

```
'(' → opener: push              top → [ ( ]
'{' → opener: push              top → [ { ] [ ( ]
'[' → opener: push              top → [ [ ] [ { ] [ ( ]
']' → closer: top is '[' ✓ pop  top → [ { ] [ ( ]
'}' → closer: top is '{' ✓ pop  top → [ ( ]
')' → closer: top is '(' ✓ pop  stack → [ ]
end → stack empty → BALANCED ✓
```

Counter-trace `"([)]"`: `(` then `[` push; `)` arrives but the top is
`[` → mismatch → **invalid**. The `)` wanted to close `(` — but `[` is
more recent. LIFO enforces "most recent first" automatically.

## Try it

```python
def is_balanced(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in s:
        if c in '([{':                 # opener → push
            stack.append(c)
        elif c in ')]}':               # closer → must match the top
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack                   # nothing left unmatched?
```

```python
print(is_balanced("({[]})"))     # trace above said True
print(is_balanced("([)]"))       # wrong order
print(is_balanced("((("))        # openers never closed
```

```
True
False
False
```

O(n) time — one pass. O(n) worst-case space — all openers, e.g.
`"((((("`.

## Why it exists

Nesting is everywhere: code blocks, HTML tags, JSON, math with
parentheses. "Is this properly nested?" is the minimal version of "is
this parseable?" The thing you must match next is ALWAYS the most
recently opened one — and a stack hands you exactly that, every time,
in O(1).

## Where it's used

- Python itself — unbalanced parens → `SyntaxError`
- Editor bracket matching (rainbow parens!), JSON/XML validators
- Evaluating expressions like `(3 + (4 × 2))`

## Common mistake — four traps in one problem

1. **Counting** `"("` vs `")"` — `")("` has equal counts but is
   invalid. Order matters, not totals.
2. **Popping on empty** — a closer with nothing to match → guard with
   `not stack` before popping (exactly what the code above does).
3. **Forgetting the empty check** — `"((("` pushes three, pops zero.
   `return not stack` catches it.
4. **Matching any earlier opener** instead of the most recent — the
   stack exists to force "most recent." Don't dig through it.

## Your turn

```python
print(is_balanced("()[]"))
print(is_balanced(")("))
print(is_balanced(""))
```

Predict all three.

<details><summary>Answer</summary>
`True`, `False`, `True`. `"()[]"` — two separate pairs, the stack
empties twice. `")("` — a closer arrives on an empty stack → False
immediately. `""` — the loop never runs and the stack is empty →
balanced (an empty string IS trivially balanced).
</details>

---

**← Prev** [06 — Stacks reverse, queues preserve](06-stack-reverses-queue-preserves.md) ·
**Next →** [08 — Monotonic stack: next greater](08-monotonic-stack-next-greater.md)
