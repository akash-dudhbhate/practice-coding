# 02 — Stack Operations: push, pop, peek — all O(1)

> 3-minute read. Four commands to memorize.

## The idea, plain words

A stack only understands four commands:

| command | Python | what it does |
|---------|--------|--------------|
| **push** | `stack.append(x)` | put x on top |
| **pop** | `stack.pop()` | remove + return the top |
| **peek** | `stack[-1]` | look at the top, keep it |
| **is empty?** | `if stack:` | False means nothing inside |

Every one is **O(1)** — one fixed action, no matter how tall the pile.
Taking the top plate costs the same with 3 plates or 3 million.

## Try it

```python
stack = []
stack.append(10)          # push
stack.append(20)          # push
print(stack[-1])          # peek → 20  (still inside!)
print(stack.pop())        # pop  → 20  (now it's gone)
print(stack[-1])          # peek → 10
print(stack)
```

```
20
20
10
[10]
```

Peek vs pop is the difference between *looking at* the top plate and
*taking* it.

## Why it exists

O(1) per operation is the whole selling point. Everything in this
lesson — bracket matching, next-greater-element — is built from
millions of these tiny constant-time pushes and pops adding up to a
single O(n) pass.

## Where it's used

- **Peek** when you need to decide based on the top before committing —
  "does this `)` match the bracket on top? Look first, then pop."
- `while stack:` = "keep working until the pile is empty" — the most
  common stack loop in existence.

## Common mistake — popping an empty stack

```python
empty = []
# empty.pop()        # IndexError: pop from empty list
# empty[-1]          # IndexError: list index out of range
```

Always guard:

```python
stack = []
if stack:              # or:  while stack:
    top = stack.pop()
```

In bracket problems, a closer arriving at an empty stack isn't a crash
— it's an *answer*: "unmatched." Return False, don't explode.

## Your turn

```python
stack = [1, 2]
print(stack[-1] + stack.pop())
```

What prints, and what's left in the stack?

<details><summary>Answer</summary>
`4` — peek sees 2, then pop removes 2, so 2 + 2 = 4. Stack is `[1]`.
(Peek doesn't remove — but the pop runs right after, inside the same
expression.)
</details>

---

**← Prev** [01 — What is a stack?](01-what-is-a-stack.md) ·
**Next →** [03 — A stack is a plain list](03-stack-as-a-plain-list.md)
