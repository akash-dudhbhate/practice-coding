# 10 — Two Stacks Make a Queue (and other design tricks)

> 4-minute read. A classic interview puzzle with a beautiful trick.

## The idea, plain words

Simulate FIFO using **two LIFO stacks**: `inbox` for enqueues,
`outbox` for dequeues. When `outbox` runs dry, **pour** `inbox` into
it.

The pour is the trick: popping everything from `inbox` into `outbox`
REVERSES the order — which undoes the LIFO. The oldest element lands
on top of `outbox`, exactly where a queue wants it.

```
enqueue 1,2,3:   inbox → [1,2,3]        outbox → []
dequeue:         pour → inbox []        outbox top → [1] [2] [3]
                 pop → 1  ✓ oldest first!
dequeue:         outbox top = 2 → pop → 2 ✓
enqueue 4:       inbox → [4]   (outbox still holds 3 — no pour needed)
dequeue:         serves 3, then next pour brings 4. Order preserved!
```

Two wrongs make a right: LIFO + LIFO = FIFO.

## Try it

```python
class TwoStackQueue:
    def __init__(self):
        self.inbox, self.outbox = [], []
    def enqueue(self, x):
        self.inbox.append(x)
    def dequeue(self):
        if not self.outbox:                    # pour ONLY when needed
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop() if self.outbox else None
```

```python
q = TwoStackQueue()
q.enqueue(1); q.enqueue(2); q.enqueue(3)
print(q.dequeue(), q.dequeue())   # FIFO check
q.enqueue(4)
print(q.dequeue(), q.dequeue())
```

```
1 2
3 4
```

Order out = order in. A queue, built from two piles of plates.

## Why it exists — amortized O(1)

A single pour can move n elements — that one dequeue is expensive. But
each element is pushed and popped from each stack **at most once** in
its whole life. Spread over all operations → O(1) *amortized* per
dequeue (same averaging argument as `list.append`, lesson 01 ch. 14).
In interviews say "amortized O(1)" — not "O(1) worst case."

## Where it's used — the pattern generalizes

- **Min-stack:** a second stack tracking "minimum so far" → O(1) min
- **Browser history:** two stacks — one for back, one for forward
- Languages/libraries that give you a stack but no deque

## Common mistake

Pouring `inbox → outbox` on **every** dequeue:

```python
# WRONG place for the pour — this is the buggy version:
# while self.inbox:
#     self.outbox.append(self.inbox.pop())   # runs unconditionally
```

Unconditional pouring costs O(n) per dequeue AND breaks FIFO — freshly
enqueued items leapfrog over un-served ones waiting in `outbox`. Pour
**only when `outbox` is empty.** That's the entire trick.

## Your turn

After `enqueue(1); enqueue(2); dequeue(); enqueue(3); dequeue()` —
what do the two dequeues return, and what's inside each stack?

<details><summary>Answer</summary>
Dequeues return `1` then `2`. Timeline: inbox=[1,2] → pour →
outbox=[2,1] (top=1), pop→1 (outbox=[2]) → enqueue 3 (inbox=[3],
outbox=[2]) → pop→2. Left: inbox=[3], outbox=[]. A third dequeue would
pour [3] and serve it.
</details>

---

**← Prev** [09 — Sliding-window max & BFS](09-sliding-window-max-and-bfs.md) ·
**Next →** [11 — Stack vs queue: how to choose](11-choosing-stack-vs-queue.md)
