# 10 — Iterative DFS: Your Own Stack

> 5-minute read. Same dive, no recursion limit.

## The idea, plain words

Recursive DFS borrows Python's call stack — and that stack has a ~1000-frame
limit. **Iterative DFS builds its own stack in a plain list** — which can
grow to millions. Swap `popleft()` for `pop()` (right end) and the queue
from ch.06 becomes a stack: last in, first out. Most recent discovery gets
explored first → that's the dive.

```python
def dfs_iter(adj, start):
    seen = {start}
    stack = [start]
    out = []
    while stack:
        v = stack.pop()          # RIGHT end = newest = dive deeper
        out.append(v)
        for nxt in adj[v]:
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return out

adj = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"],
       "D": ["B", "C", "E"], "E": ["D"]}
print(dfs_iter(adj, "A"))        # ['A', 'C', 'D', 'E', 'B']
```

## Hand-trace the stack

```
stack=[A]      pop A → out=[A]          push B,C      stack=[B,C]
stack=[B,C]    pop C → out=[A,C]        C: A✗, push D stack=[B,D]
stack=[B,D]    pop D → out=[A,C,D]      D: B✗C✗,push E stack=[B,E]
stack=[B,E]    pop E → out=[A,C,D,E]    E: D✗         stack=[B]
stack=[B]      pop B → out=[...,B]      B: A✗,D✗      stack=[]

out = [A, C, D, E, B]
```

## Two honest warnings

1. **The order differs from recursive DFS.** Recursive visited
   `[A, B, D, C, E]`; the stack version visits `[A, C, D, E, B]` — a stack
   pops the LAST pushed neighbor first, so it tries C before B. Both are
   valid DFS; don't expect identical orderings between the two versions.
2. **Nodes can sit "seen but not yet popped"** — B was pushed early, then
   waited at the bottom while C, D, E were explored. That's normal. `seen`
   is still marked at push time, exactly like BFS enqueue-time marking.

## Why it exists

- **Recursion limits:** chains and deep graphs crash recursive DFS;
  a list on the heap has no such ceiling.
- **Control:** interviewers sometimes want to see that you understand what
  recursion *does* — the explicit stack is the answer.

## Where it's used

Same places as recursive DFS (reachability, components, flood fill) — plus
anywhere inputs can be big: million-row grids, deep dependency chains.

## Common mistake

Treating `stack.pop()` vs `queue.popleft()` as interchangeable. It's the
SAME code skeleton — one word decides whether it dives (DFS) or ripples
(BFS). Mixing them up is the classic "my shortest path is wrong" bug.

## Your turn

In the trace, why does B come out LAST even though it was pushed first?

<details><summary>Answer</summary>
Because the stack is last-in-first-out: B was pushed under C, then sat at
the bottom while everything pushed after it (D, E) was popped and explored.
It's still marked seen at push time — it just waits its turn at the bottom
of the pile.
</details>

---

**← Prev** [09 — DFS corridor](09-dfs-corridor.md) ·
**Next →** [11 — BFS or DFS? The decision table](11-bfs-vs-dfs.md)
