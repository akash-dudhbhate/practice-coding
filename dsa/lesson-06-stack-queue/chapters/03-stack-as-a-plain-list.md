# 03 — A Stack is a Plain List — but ONLY at the End

> 4-minute read. Why the end is cheap and the front is a trap.

## The idea, plain words

In chapter 01 you used `append` and `pop()` without asking why they
work. Here's why: a Python list is a row of numbered slots, and the
**end has free space behind it**. Adding or removing at the end touches
ONE slot.

The **front** is the opposite. There's no free space before slot 0, and
every slot's position is fixed — inserting at the front forces every
element to scoot right; removing from the front forces everyone left.

```
append(9) at the END:   [1][2][3][ ]  →  [1][2][3][9]      1 write
insert(0, 9) at FRONT:  [1][2][3][ ]  →  3,2,1 each slide right
                        [9][1][2][3]                        3 moves + 1 write
pop(0) from FRONT:      [1][2][3]     →  [ ][2][3], then all slide left
                        [2][3][ ]                           2 moves
```

- `append(x)`, `pop()` — **O(1)**. (Occasionally Python grows the list
  and copies it — averaged over many appends it's still O(1). Lesson 01
  ch. 14 called this *amortized*.)
- `insert(0, x)`, `pop(0)` — **O(n)**, EVERY time. No averaging saves
  them.

## Try it — feel which end is which

```python
stack = [1, 2, 3]

stack.append(4)      # cheap: fills the next slot → [1,2,3,4]
stack.pop()          # cheap: chops the last slot → [1,2,3]

# the expensive versions of the same ideas:
# stack.insert(0, 4)   # would slide 1,2,3 right first → [4,1,2,3]
# stack.pop(0)         # would slide everyone left     → [2,3]

print(stack)
```

```
[1, 2, 3]
```

Rule of thumb: **a stack's top is the list's END.** If you find yourself
touching index 0, you're either doing it wrong — or you need a `deque`
(chapter 05).

## Why it exists

Because one tiny choice — "which end is the top?" — is the difference
between O(1) and O(n) per operation. n pushes + pops on the wrong end
= O(n²) total work, for no reason.

## Where it's used

- Every stack you'll ever write: `list.append` / `list.pop`, top = `[-1]`
- The same "ends cheap, middle/front expensive" fact is why `deque`
  exists — it makes BOTH ends cheap (chapter 05).

## Common mistake

Using `insert(0, x)` to "push at the front" — correct answer, wrong
tool: every call pays n slides. Or treating `stack[0]` as the top —
remember, the top lives at `stack[-1]`.

## Your turn

Which of these is O(1) and which is O(n) on a 1,000,000-item list?

```python
a = list(range(10))
a.pop()
a.insert(0, 5)
a.append(5)
```

<details><summary>Answer</summary>
`pop()` → O(1), `insert(0, 5)` → **O(n)** (~a million slides),
`append(5)` → O(1). Only touching the END is cheap.
</details>

---

**← Prev** [02 — push, pop, peek](02-stack-ops-push-pop-peek.md) ·
**Next →** [04 — What is a queue? (FIFO)](04-what-is-a-queue.md)
