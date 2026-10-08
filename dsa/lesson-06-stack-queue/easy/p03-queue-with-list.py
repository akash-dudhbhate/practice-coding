"""
LESSON 06 — Stacks & Queues
EASY P03 — Implement a Queue With a List
============================================

CONCEPT:
  FIFO: first in, first out. enqueue adds at the back, dequeue removes
  from the front. A plain list works but `pop(0)` is O(n) — every
  remaining element shifts left. That's why collections.deque exists;
  for this exercise build the list version first so you feel the cost.
  (Bonus: can you keep a `head` index instead of pop(0) to skip the
  shifting?)

PROBLEM:
  Write a class `SimpleQueue` with methods:
    enqueue(x)  — add x to the back
    dequeue()   — remove and return the front element; None if empty
    peek()      — return the front element without removing; None if empty
    is_empty()  — True if the queue has no elements

TRY THIS INPUT:
  ```python
  q = SimpleQueue()
  print(q.is_empty())
  q.enqueue(1); q.enqueue(2); q.enqueue(3)
  print(q.peek())
  print(q.dequeue(), q.dequeue())
  print(q.is_empty())
  print(q.dequeue())
  print(q.is_empty())
  print(q.dequeue())
  ```

EXPECTED OUTPUT:
  ```
  True
  1
  1 2
  False
  3
  True
  None
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
