# 08 — The Visited Set (the one line that prevents infinite loops)

> 5-minute read. THE bug of this lesson lives here.

## The idea, plain words

Graphs have **cycles** — paths that loop back to where you started:

```
    A — B          walk without memory:
    |   |          A → B → D → C → A → B → D → C → A → ...
    C — D — E      forever. A's neighbors include C, C's include A...
```

A traversal with no memory re-enters nodes it's already done — and on a
cyclic graph it NEVER finishes. The fix is a **`seen` set**: a checklist.
Before touching a node, ask "been here?" If yes, skip.

```python
from collections import deque

def bfs(adj, start):
    seen = {start}               # the checklist — starts with the seed
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for nxt in adj[v]:
            if nxt not in seen:  # "been here?" → skip
                seen.add(nxt)    # check it off
                queue.append(nxt)
```

Each node enters `seen` exactly once → each node is processed exactly once
→ the loop MUST end. Total work: O(V + E) — every node, every edge, once.

## The subtle rule: mark at ENQUEUE time

There's a right moment and a lazy moment to check the box:

```python
from collections import deque

adj = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"],
       "D": ["B", "C", "E"], "E": ["D"]}

def pushes_at_enqueue(adj, start):     # RIGHT — mark when it JOINS
    seen = {start}
    q, pushes = deque([start]), 0
    while q:
        v = q.popleft()
        for nxt in adj[v]:
            if nxt not in seen:
                seen.add(nxt)          # ← inside the discovery if
                q.append(nxt)
                pushes += 1
    return pushes

def pushes_at_pop(adj, start):         # LAZY — mark when it's POPPED
    seen, q, pushes = set(), deque([start]), 0
    while q:
        v = q.popleft()
        if v in seen:
            continue                   # ← works, but wasteful
        seen.add(v)
        for nxt in adj[v]:
            q.append(nxt)              # pushes even queued/seen nodes!
            pushes += 1
    return pushes

print(pushes_at_enqueue(adj, "A"))     # 4  — each node pushed once
print(pushes_at_pop(adj, "A"))         # 10 — duplicates pile in
```

Lazy marking lets the same node get pushed many times before it's popped —
on our tiny 5-node map it pushes 10 times instead of 4. Still correct, but
wasteful; on dense or cyclic graphs it can explode. Enqueue-time marking
guarantees: **in the queue at most once.**

## Watch it fail — the trace without `seen`

Remove the `if nxt not in seen` guard on our map:

```
queue=[A]     pop A:  enqueue B, C          queue=[B,C]
              pop B:  enqueue A(!), D       queue=[C,A,D]
              pop C:  enqueue A(!), D(!)    queue=[A,D,A,D]
              pop A:  enqueue B, C          queue=[D,A,D,B,C]
              ...the queue refills faster than it drains...
```

A "walk" that was 5 nodes becomes an infinite loop. `RecursionError` in
DFS, a silent hang in BFS. This is **the most common graph bug** — every
interviewer watches for it.

## Why it exists

"Process each vertex exactly once" is the invariant under every traversal
in this lesson. `seen` is how you enforce it. In grids, we even mutate the
cell to `0` as a free visited set (ch.12) — same idea, cheaper memory.

## Common mistake

Two flavors: (1) forgetting `seen` entirely → infinite loop; (2) marking at
pop time → correct but the queue grows V×E-ish worst case. Do both halves
right: mark, and mark early.

## Your turn

`adj = {"X": ["Y"], "Y": ["X"]}` — a 2-node cycle. How many times is `Y`
enqueued in BFS from `X` with correct enqueue-time marking?

<details><summary>Answer</summary>
Once. Pop X → push Y, mark seen. Pop Y → its only neighbor is X, already in
`seen` → skip. Queue empties. Without `seen`, X and Y would enqueue each
other forever.
</details>

---

**← Prev** [07 — BFS shortest path](07-bfs-shortest-path.md) ·
**Next →** [09 — DFS: follow the corridor](09-dfs-corridor.md)
