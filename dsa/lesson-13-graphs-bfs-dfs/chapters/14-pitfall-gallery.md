# 14 — The Pitfall Gallery: Five Ways Graph Code Goes Wrong

> 6-minute read. Every bug here has shipped in real interviews.

## 1. No `seen` set → infinite loop

```python
# WRONG — cycles forever on any cyclic graph
def dfs(adj, v, out):
    out.append(v)
    for nxt in adj[v]:
        dfs(adj, nxt, out)

# CORRECT — guard at entry
def dfs(adj, v, seen, out):
    seen.add(v)
    out.append(v)
    for nxt in adj[v]:
        if nxt not in seen:
            dfs(adj, nxt, seen, out)
```

On our map (`A—B—D—C—A` is a cycle), the wrong version walks
`A→B→D→C→A→B→…` until `RecursionError`. Ch.08 is the whole story — this is
THE graph bug.

## 2. Marking `seen` at pop time (BFS)

Enqueue-time marking means each vertex enters the queue ONCE. Pop-time
marking lets duplicates pile in — the queue balloons with the same node
many times over. Correctness survives; complexity doesn't. Mark when the
node **joins** the frontier, not when it leaves.

## 3. One-directional edges on an undirected graph

```python
adj = {0: [], 1: []}
adj[0].append(1)          # undirected edge... but adj[1].append(0) missing!
print(adj)                # {0: [1], 1: []} — can go 0→1, never 1→0
```

Your traversal can walk to a node but never back — half the graph becomes
invisible and component counts come out wrong. Undirected edge = TWO
appends (ch.03).

## 4. Dropping isolated vertices

```python
n, edges = 4, [(0, 1)]
adj = {v: [] for v in range(n)}   # seed EVERY vertex FIRST
for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)
print(adj)   # {0: [1], 1: [0], 2: [], 3: []} — nodes 2 and 3 still exist
```

A vertex with no edges is still a vertex: it counts as a component and can
still be a traversal start. Build the dict from `range(n)` first, then add
edges — or meet `KeyError` mid-traversal.

## 5. Asking BFS for weighted shortest paths

BFS minimizes **hop count**, not **cost**. A 3-hop route of weights
1+1+1 is cheaper than a 1-hop edge of weight 100 — but BFS crowns the
single hop anyway, because it counts rings. Weighted shortest paths =
Dijkstra (lesson 14).

## Edge cases to always test

- empty graph / empty edge list
- single vertex (it's 1 component, distance 0 from itself)
- disconnected graph — does your code count/handle ALL components?
- self-loop `(a, a)` — `seen` handles it, but only if present
- `start == target` in shortest path → answer: **0**
- directed vs undirected — did you append both directions correctly?

## Your turn

Someone writes "BFS" but codes `v = queue.pop()` instead of `popleft()`.
What's broken?

<details><summary>Answer</summary>
It became iterative DFS — `.pop()` takes the NEWEST element (a stack), not
the oldest. It still visits every reachable node, but ring order is gone,
so any distance/shortest-path answer it produces is wrong. One word decides
the whole algorithm (ch.10 vs ch.06).
</details>

---

**← Prev** [13 — The recipe](13-the-recipe.md) ·
Done with concepts? → Open `task-explanation.md` and solve `easy/p01` next.
