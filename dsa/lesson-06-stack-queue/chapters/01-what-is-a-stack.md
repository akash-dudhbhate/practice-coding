# 01 — What is a Stack? (LIFO)

> 3-minute read. One idea only.

## The idea, plain words

A **stack** is a pile where you can only touch the **top**.

Real-life version: **a stack of plates** in a cafeteria. You put a clean
plate on top; the next person takes one off the top. Nobody slides a
plate out of the middle — the pile would collapse.

That gives one rule: **Last In, First Out — LIFO.** The last thing you
put on is the first thing that comes off.

```
push "A" →   top → [A]
push "B" →   top → [B] [A]
push "C" →   top → [C] [B] [A]
pop      →   returns C        top → [B] [A]
pop      →   returns B        top → [A]
```

C was added LAST but leaves FIRST. A waits at the bottom until
everything above it is gone.

## Try it — a stack is just a list used one way

```python
plates = []                # an empty stack
plates.append("A")         # push: put on top
plates.append("B")
plates.append("C")
print(plates.pop())        # pop: take the top → C
print(plates.pop())        # → B
print(plates)              # what's left
```

```
C
B
['A']
```

Nothing special about `plates` — it's an ordinary Python `list`.
"Stack" is a *way of using* a list, not a new type.

## Why it exists

Most structures let you grab any element. A stack *deliberately*
restricts you to the top — and the restriction is the feature. "Deal
with the most recent thing first" is exactly LIFO: undo in a text
editor (undo the last keystroke), browser back (revisit the last page),
nested brackets (close the innermost first — chapter 07).

## Where it's used

- The **call stack** — Python itself uses one: every function call
  pushes, every `return` pops. A `RecursionError` is a stack overflow.
- Undo/redo in editors, back/forward in browsers
- Checking nested structures: brackets, HTML tags, JSON
- Depth-first search (DFS) — dives deep first, like a stack

## Common mistake

Reaching for the wrong end. For a Python list, **the END is the top** —
`stack[-1]`, not `stack[0]`. Peek `stack[0]` and you grab the *oldest*
item, not the newest.

## Your turn

```python
stack = []
for x in [5, 6, 7]:
    stack.append(x)
stack.pop()
stack.append(8)
print(stack[-1])
```

What prints?

<details><summary>Answer</summary>
`8` — trace it: push 5,6,7 → `[5,6,7]`; pop removes 7 → `[5,6]`;
push 8 → `[5,6,8]`; the top (`stack[-1]`) is 8.
</details>

---

**Next →** [02 — Stack operations: push, pop, peek](02-stack-ops-push-pop-peek.md)
