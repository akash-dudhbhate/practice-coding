# 06 — The Superpower: Stacks Reverse, Queues Preserve

> 3-minute read. One fact that solves easy problems instantly.

## The idea, plain words

Feed the same sequence into a stack and a queue, then drain them:

- **Stack gives it back REVERSED** — last in is first out.
- **Queue gives it back UNCHANGED** — first in is first out.

## Try it — same input, opposite orders

```python
from collections import deque

stack = []
for x in [10, 20, 30]:
    stack.append(x)
print(stack.pop(), stack.pop(), stack.pop())          # reversed!

queue = deque()
for x in [10, 20, 30]:
    queue.append(x)
print(queue.popleft(), queue.popleft(), queue.popleft())  # same order
```

```
30 20 10
10 20 30
```

Hand-trace the stack version:

```
push 10 → top → [10]
push 20 → top → [20] [10]
push 30 → top → [30] [20] [10]
pop → 30     pop → 20     pop → 10      (mirror image of what went in)
```

## Why it exists

"Reverse something" is a whole family of problems — reverse a string,
undo a sequence of moves, evaluate expressions written backwards
(postfix, `medium/p03`). A stack reverses **for free**: push
everything, pop everything, done. That's the entire `easy/p02`
solution.

A queue's superpower is the opposite: **keeping order**. When arrival
order IS the answer — serve customers, explore a graph's nearest layer
first — a queue preserves it for free.

## Where it's used

- Stack: reverse a string/list, undo history, backtracking (undo the
  last choice), postfix evaluation
- Queue: anything "in order of arrival" — scheduling, BFS layers,
  streaming buffers

## Common mistake

Mixing up which end is which mid-code:

- `list.pop()` → pops the **end** → stack behavior
- `deque.popleft()` → pops the **front** → queue behavior
- `deque.pop()` → pops the **back** → stack behavior on the same object!

Yes, a `deque` can do both — it's double-ended. The discipline lives in
YOUR head: pick stack *or* queue per problem, then use only its two
commands.

## Your turn

```python
s = []
for ch in "abc":
    s.append(ch)
print("".join(s.pop() for _ in range(3)))
```

What prints?

<details><summary>Answer</summary>
`cba` — the stack pops c, then b, then a: the string reversed. That's
`easy/p02` in three lines.
</details>

---

**← Prev** [05 — deque: why list.pop(0) is a trap](05-deque-why-pop0-is-slow.md) ·
**Next →** [07 — Balanced brackets](07-balanced-brackets.md)
