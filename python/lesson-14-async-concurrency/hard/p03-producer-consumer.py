"""
LESSON 14 — Async & Concurrency
HARD P03 — Producer-Consumer with Queue
============================================

CONCEPT:
  `asyncio.Queue` decouples producers from consumers: producers put
  items, consumers get them as they arrive. A sentinel value (None)
  tells each consumer to stop.

PROBLEM:
  Write an async `producer(queue)` that puts "item-0" .. "item-9"
  then one None sentinel per consumer, an async `consumer(queue,
  cid)` that collects "C{cid}: {item}" strings until the sentinel,
  and an async `main()` that runs the producer plus 2 consumers and
  returns the total number of items processed.

TRY THIS INPUT:
  ```python
  import asyncio
  print(asyncio.run(main()))
  ```

EXPECTED OUTPUT:
  ```
  10
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
