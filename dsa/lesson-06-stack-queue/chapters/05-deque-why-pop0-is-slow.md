# 05 — Why `list.pop(0)` is a Trap — and `deque` Fixes It

> 4-minute read. The single most-asked "why deque?" question.

## The idea, plain words

Chapter 03 showed it: removing from the front of a list slides *every*
element left one slot. That's O(n) — do it n times and you've built
O(n²) by accident.

`collections.deque` is built so **both ends are cheap**: `append`/`pop`
on the right, `appendleft`/`popleft` on the left — all O(1), every
time, no sliding.

```
list:   [1][2][3][4][5]
pop(0)  →  2,3,4,5 EACH slide left → 4 moves  (grows with n!)

deque:  (blocks linked from both ends)
popleft →  unhook the front block → 1 move, always
```

## Try it — same job, two costs

```python
from collections import deque

# the slow way — correct answer, wrong tool
slow = [1, 2, 3, 4]
slow.pop(0)                # 2,3,4 each slide left → 3 moves
print(slow)

# the fast way — one move no matter the size
fast = deque([1, 2, 3, 4])
fast.popleft()             # front unhooks → 1 move
print(fast)
```

```
[2, 3, 4]
deque([2, 3, 4])
```

Same result! The difference only shows at scale: n = 100,000 dequeues
→ ~10 BILLION element slides for the list vs ~100,000 moves for the
deque. That's the O(n²) vs O(n) gap — minutes vs milliseconds.

## Why it exists

`deque` exists precisely because lists are cheap at one end only.
Whenever you remove from the front **more than a handful of times** —
queue, BFS, sliding window — reach for `deque`.

## Where it's used

- Every queue in this lesson and in real code: `q.append` + `q.popleft`
- Sliding-window problems (ch. 09) — it removes from BOTH ends
- Bonus extras lists lack: `q.rotate()`, `deque(maxlen=k)` bounded queue

## Common mistake

```python
queue = []
for x in [1, 2, 3]:
    queue.append(x)
while queue:
    item = queue.pop(0)     # works! ... and O(n) each time
print("done")
```

This *runs* — small tests even pass. Then the interviewer says
"n = 100,000" and it times out. `list.pop(0)` is pitfall #1 in the
pitfall gallery (ch. 12) for a reason.

## Your turn

You need "serve the oldest request first." Which two lines do you
write?

```python
from collections import deque
q = deque()
# enqueue:  ?
# dequeue:  ?
```

<details><summary>Answer</summary>
`q.append(x)` to enqueue (joins the back), `q.popleft()` to dequeue
(serves the front). Both O(1). If you wrote `q.appendleft`/`q.pop`,
that's *also* a valid queue — just flipped which end is which.
</details>

---

**← Prev** [04 — What is a queue?](04-what-is-a-queue.md) ·
**Next →** [06 — Stacks reverse, queues preserve](06-stack-reverses-queue-preserves.md)
