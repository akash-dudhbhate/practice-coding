# 04 — What is a Queue? (FIFO)

> 3-minute read. The polite cousin of the stack.

## The idea, plain words

A **queue** is a line where you join at the **back** and get served at
the **front**.

Real-life version: **the line at a coffee shop.** First person in line
gets served first. Nobody cuts — the rule is **First In, First Out —
FIFO.** Fair order of arrival.

```
enqueue "Asha"  →   back → [Asha] → front
enqueue "Ravi"  →   back → [Ravi][Asha] → front
enqueue "Meera" →   back → [Meera][Ravi][Asha] → front
dequeue         →   serves Asha     back → [Meera][Ravi] → front
dequeue         →   serves Ravi     back → [Meera] → front
```

Asha arrived FIRST and leaves FIRST. If the coffee shop were a stack,
Meera (who just walked in) would get served first — rude, and exactly
what stacks do.

## Try it — deque is Python's queue

```python
from collections import deque

line = deque()
line.append("Asha")      # enqueue: join the back
line.append("Ravi")
line.append("Meera")
print(line.popleft())    # dequeue: serve the front → Asha
print(line.popleft())    # → Ravi
print(line)              # who's left
```

```
Asha
Ravi
deque(['Meera'])
```

The four queue commands, mirroring the stack's:

| command | Python | what it does |
|---------|--------|--------------|
| **enqueue** | `q.append(x)` | join the back |
| **dequeue** | `q.popleft()` | serve + return the front |
| **peek front** | `q[0]` | look at who's next |
| **is empty?** | `if q:` | False means nobody waiting |

## Why it exists

"Fair order of arrival" is as natural as "most recent first" — and
often what you actually want: print jobs, customer tickets, tasks
waiting for a worker. BFS (chapter 09) *requires* FIFO — process
things in the order you discovered them, layer by layer.

## Where it's used

- Task/job queues (Celery, RQ), message brokers (Kafka, RabbitMQ)
- BFS shortest paths in unweighted graphs (preview ch. 09, full
  treatment in lesson 13)
- Buffering: keyboards, networks — "process in arrival order" anywhere

## Common mistake

Picturing "one working end" again. A stack has ONE working end (the
top). A queue has TWO — back for arrivals, front for service. `deque`
= "**d**ouble-**e**nded **que**ue" — now the name makes sense.

## Your turn

```python
from collections import deque
q = deque([1, 2, 3])
q.append(4)
q.popleft()
print(q[0])
```

What prints?

<details><summary>Answer</summary>
`2` — start `[1,2,3]`; enqueue 4 → `[1,2,3,4]`; dequeue removes the
front 1 → `[2,3,4]`; the front `q[0]` is 2.
</details>

---

**← Prev** [03 — A stack is a plain list](03-stack-as-a-plain-list.md) ·
**Next →** [05 — deque: why list.pop(0) is a trap](05-deque-why-pop0-is-slow.md)
