# 04 — Topo sort via DFS: finish last, print first

> 5-minute read. The clever one-liner version.

## The idea, plain words

Kahn's emitted vertices when their *prerequisites* were done. DFS does
the mirror image: **emit a vertex when it *finishes*** — after everything
it points to is already emitted.

A vertex that finishes last must be a thing nothing depended on — so it
belongs **first**. Hence: **postorder, reversed.**

```
"D only finishes after B, C, E finish. So D is emitted last
 in postorder — and last-emitted means first in the schedule."
```

## The code

```python
def topo_dfs(adj):
    order, state = [], {}          # state: 0=unseen  1=visiting  2=done
    def dfs(v):
        state[v] = 1
        for nxt in adj[v]:
            if state.get(nxt, 0) == 1:
                return False       # edge to a vertex on my stack = cycle!
            if state.get(nxt, 0) == 0 and not dfs(nxt):
                return False
        state[v] = 2
        order.append(v)            # postorder: emitted on the way OUT
        return True
    for v in adj:
        if state.get(v, 0) == 0 and not dfs(v):
            return []
    return order[::-1]             # reverse postorder = topo order
```

## Hand trace — `0:[1,2]  1:[3]  2:[3]  3:[]`

```
dfs(0): visiting
  dfs(1): visiting
    dfs(3): nothing to visit → emit 3     postorder: [3]
  back at 1 → emit 1                      postorder: [3, 1]
  dfs(2): tries 3 — already done → emit 2 postorder: [3, 1, 2]
  back at 0 → emit 0                      postorder: [3, 1, 2, 0]

reversed → [0, 2, 1, 3]   ✓ valid topo order
```

Every vertex emits only **after** its successors emitted — so reversing
puts dependencies first. That's the whole proof in one sentence.

## Why it exists

Sometimes you can't count indegrees — the graph arrives as "here's a
node, explore it" (implicit graphs, trees of calls). DFS postorder needs
no preprocessing pass: the ordering falls out of the recursion for free.
Same O(V + E) as Kahn's.

## Where it's used

Dependency resolution inside compilers/interpreters, `git`'s commit walk,
anywhere the graph is discovered by traversal rather than listed upfront.

## Common mistake

Forgetting to **reverse**. Plain postorder gives you "most-dependent
first" — the exact backwards schedule. `order[::-1]` is the whole trick.
(Also: don't reuse a plain `visited` set — see next chapter for why the
three states matter.)

## Your turn

Same DAG, Kahn's gave `[0,1,2,3]` and DFS gave `[0,2,1,3]`. Which is
right?

<details><summary>Answer</summary>
Both. Topological order is not unique — any order where every edge
points forward is valid. Two correct algorithms may return different
ones.
</details>

---

**← Prev** [03 — Kahn's algorithm](03-kahns-algorithm.md) ·
**Next →** [05 — Detecting cycles](05-cycle-detection.md)
