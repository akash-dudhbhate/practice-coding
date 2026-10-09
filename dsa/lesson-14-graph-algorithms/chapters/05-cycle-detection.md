# 05 — Detecting cycles: three colors, not two

> 5-minute read. Why one `visited` set is a lie.

## The idea, plain words

In a **directed** graph, "I've seen this vertex before" splits into two
very different situations:

- **Edge to a vertex still on my DFS stack** → I can reach my own
  ancestor → **cycle!** (a "back edge")
- **Edge to a vertex fully finished** → just a cross edge. Fine.

One `visited` set can't tell them apart. You need **three states**:

```
0 = unseen   (white)   never touched
1 = visiting (gray)    on the current DFS path — "in my family line"
2 = done     (black)   fully explored, never coming back
```

Only **gray** means cycle.

## The code

```python
def has_cycle(adj):
    state = {}                       # 0=unseen 1=visiting 2=done
    def dfs(v):
        state[v] = 1                 # gray: on my path now
        for nxt in adj[v]:
            if state.get(nxt, 0) == 1:
                return True          # pointing at an ancestor -> CYCLE
            if state.get(nxt, 0) == 0 and dfs(nxt):
                return True
        state[v] = 2                 # black: fully explored
        return False
    return any(state.get(v, 0) == 0 and dfs(v) for v in adj)

print(has_cycle({0:[1], 1:[2], 2:[0]}))         # → True   (0→1→2→0)
print(has_cycle({0:[1,2], 1:[3], 2:[3], 3:[]})) # → False  (diamond)
```

## Watch the trap it's built to catch

```
      0
     / \
    v   v
    1   2
     \ /
      v
      3          A diamond: 0→1→3 and 0→2→3.
                 dfs(2) sees 3 again — but 3 is BLACK (done),
                 not gray. Not a cycle. A 2-color visited set
                 would panic here.
```

Compare with a real cycle `0→1→2→0`:

```
dfs(0) gray → dfs(1) gray → dfs(2) gray → edge 2→0:
0 is still GRAY (it's on the path above us) → CYCLE ✓
```

## Why it exists

Lesson-13 visited sets work for "don't re-explore." Cycle detection asks
a sharper question — "is this edge pointing into my **current** path?"
— and only the gray state encodes "current path."

## Where it's used

Deadlock detection (processes waiting on each other), circular-import
checks, spreadsheet self-reference, course-schedule validation.

## Common mistake

Using a plain `visited` set and reporting every re-seen vertex as a
cycle. The diamond graph above proves it wrong: vertex 3 gets re-seen
legitimately. Three colors or nothing.

## Your turn

Kahn's algorithm (ch. 03) detects cycles too — without any colors. How?

<details><summary>Answer</summary>
Cyclic vertices never reach indegree 0, so they never enter the queue.
If `len(order) < n` at the end, the leftovers are exactly the vertices
stuck in cycles. BFS version of the same detection.
</details>

---

**← Prev** [04 — Topo sort via DFS](04-topo-sort-dfs.md) ·
**Next →** [06 — Union-Find](06-union-find.md)
