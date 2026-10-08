"""
LESSON 06 — Stacks & Queues
HARD P03 — Implement a Queue Using Two Stacks
============================================

CONCEPT:
  inbox stack for enqueues, outbox stack for dequeues. When outbox is
  EMPTY, pour inbox into it — the pour reverses order, canceling the
  LIFO so the oldest element lands on top. Each element is pushed and
  popped per stack at most once → O(1) AMORTIZED per operation.
  Key rule: pour ONLY when outbox is empty, never on every dequeue.

PROBLEM:
  Write a class `TwoStackQueue` with methods:
    enqueue(x)  — add x (O(1))
    dequeue()   — remove/return oldest; None if empty
    peek()      — return oldest without removing; None if empty
    empty()     — True if the queue is empty
  Internal storage: two lists used as stacks (append/pop only).

TRY THIS INPUT:
  ```python
  q = TwoStackQueue()
  q.enqueue(1); q.enqueue(2); q.enqueue(3)
  print(q.peek())
  print(q.dequeue())
  q.enqueue(4)
  print(q.dequeue(), q.dequeue(), q.dequeue())
  print(q.empty())
  print(q.dequeue())
  ```

EXPECTED OUTPUT:
  ```
  1
  1
  2 3 4
  True
  None
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
