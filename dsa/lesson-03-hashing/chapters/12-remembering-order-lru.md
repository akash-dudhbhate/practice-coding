# 12 — Remembering Order (dict + linked list = LRU cache)

> 5-minute read. The capstone: what a dict can't do alone.

## The idea, plain words

A dict answers "is this key stored?" in O(1) — but it has **no notion of
oldest or newest**. A cache needs a second question answered fast:
*"which entry do I throw away when full?"*

The fix: **two structures covering each other's weakness.**

- A **dict**: key → node. O(1) lookup.
- A **doubly-linked list**: usage order — most-recent at the head,
  evict-candidate at the tail. O(1) to move/remove a node.

```
dict: {1 -> node(1), 2 -> node(2), 3 -> node(3)}
list: head <-> [3] <-> [1] <-> [2] <-> tail
                most recent          evicted next
```

Every `get`/`put` moves that node to the head. Full? Evict the tail.
Both steps O(1). That's an **LRU cache** (Least Recently Used).

## Watch it run — capacity 2

```
put(1,1)  put(2,2)   cache {1,2}    order: 2,1     (1 is oldest)
get(1)               returns 1      order: 1,2     (1 just got used!)
put(3,3)             evicts 2       cache {1,3}    (2 was the tail)
get(2)               -1, a miss
```

Output: `1`, then `-1`. The `get(1)` *rescued* 1 from eviction by
making it most-recent — that's the whole point of LRU.

## Why it exists

Either structure alone fails: dict alone → finding the oldest means
scanning everything, O(n) per eviction. List alone → `get` scans, O(n).
Married, both stay O(1). The general lesson: *combine a hash map with
whatever structure owns the thing hashing can't do.*

## Where it's used

CPU and page caches, browser history, `functools.lru_cache`, database
buffers, memoization with bounded memory — and it's a classic
"design question" in interviews (implement an LRU cache yourself).

## Common mistakes

- Forgetting `get` counts as a **use** — it must refresh order, or
  frequently-read items get evicted by mistake.
- `put` on an existing key must update the value **and** move the node
  to the head — updating value only is a classic bug.

## Your turn

Capacity 2: `put(1,1)`, `put(2,2)`, `get(1)`, `put(3,3)`, `get(2)` —
replay it. What does the last `get(2)` return, and why?

<details><summary>Answer</summary>
`-1`. After `get(1)` the order is 1,2 — so 2 is oldest — and `put(3,3)`
evicts 2. When 3 was inserted, 2 went out the tail.
</details>

---

**← Prev** [11 — Running totals in a map](11-running-totals-in-a-map.md) ·
**Next →** [13 — The hash toolbox](13-the-hash-toolbox.md)
