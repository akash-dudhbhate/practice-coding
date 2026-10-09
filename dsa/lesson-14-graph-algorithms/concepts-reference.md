# Lesson 14 — Concepts Explained (Graph Algorithms)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.
> This lesson assumes lesson 13 (adjacency lists, BFS, DFS).

---

## Topological Sort — ordering a DAG

**What:** A **DAG** is a Directed Acyclic Graph — arrows, no cycles. Topological sort answers "give me an order of the vertices where every edge points forward" — i.e., every dependency comes before the thing that depends on it.

```
DAG:  A → B → D        One valid topo order: A B C E D
      A → C → D        (also valid: A E C B D — order isn't unique)
      E → D
     "D needs B, C, and E all emitted first"

NOT a DAG:  A → B → C → A   ← a cycle; no valid order exists
```

**Two ways to produce the order:**

**Kahn's algorithm (BFS on indegree).** A vertex with **indegree 0** has no unmet dependencies — it's safe to emit. Emit it, delete its outgoing edges (decrement neighbors' indegrees), and repeat. Newly-freed vertices join the queue.

```python
from collections import deque

def kahn_order(n, edges):
    adj = {v: [] for v in range(n)}
    indeg = [0] * n
    for a, b in edges:                    # edge a -> b
        adj[a].append(b)
        indeg[b] += 1
    q = deque(v for v in range(n) if indeg[v] == 0)
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for nxt in adj[v]:
            indeg[nxt] -= 1               # "delete" the edge v->nxt
            if indeg[nxt] == 0:
                q.append(nxt)             # nxt's deps are all emitted
    return order if len(order) == n else []   # leftovers = cycle!
```

**DFS postorder.** Run DFS; a vertex is emitted when it *finishes* (all descendants done). The order, reversed, is topological — because a vertex only finishes after everything it points to has finished.

```python
def topo_dfs(adj):
    order, state = [], {}                 # state: 0=unseen 1=visiting 2=done
    def dfs(v):
        state[v] = 1
        for nxt in adj[v]:
            if state.get(nxt, 0) == 1:
                return False              # back edge -> cycle
            if state.get(nxt, 0) == 0 and not dfs(nxt):
                return False
        state[v] = 2
        order.append(v)                   # postorder
        return True
    for v in adj:
        if state.get(v, 0) == 0 and not dfs(v):
            return []
    return order[::-1]
```

**Why it exists:** Real work has prerequisites — you can't compile a module before its imports, can't take the lab course before the lecture, can't run a pipeline step before its inputs. Topo sort turns "a web of constraints" into "a legal schedule."

**Where it's used:** Build systems (Make, Bazel), course scheduling, package managers resolving install order, spreadsheet recalculation, task pipelines, `git`'s commit ordering.

**What goes wrong without it:**
- Emitting vertices in arbitrary order → you "build" a target before its dependency exists.
- Forgetting the **cycle check**: on a cyclic graph Kahn's queue empties early and `len(order) < n`. Returning the partial order as if it were valid is the classic silent bug — the leftover vertices are exactly the ones stuck in cycles.
- DFS version: forgetting the three-color `state` (white/gray/black) means you can't distinguish "edge to an ancestor" (cycle!) from "edge to a finished subtree" (fine).

**Worked example — Kahn's on `A→B, A→C, B→D, C→D` (as 0→1, 0→2, 1→3, 2→3):**

```
indeg:    0:0  1:1  2:1  3:2
q=[0]  pop 0 → order=[0]; 1:0, 2:0 → q=[1,2]
pop 1  → order=[0,1];    3:2→1
pop 2  → order=[0,1,2];  3:1→0 → q=[3]
pop 3  → order=[0,1,2,3]
```

Expected output: **`[0, 1, 2, 3]`** (or `[0, 2, 1, 3]` — both legal).

**Worked example — DFS postorder on the same DAG** (`0:[1,2] 1:[3] 2:[3] 3:[]`):

```
dfs(0): visiting; try 1
  dfs(1): visiting; try 3
    dfs(3): no outgoing → emit 3          postorder: [3]
  back at 1: emit 1                        postorder: [3, 1]
  try 2
    dfs(2): try 3 — already done → emit 2  postorder: [3, 1, 2]
  back at 0: emit 0                        postorder: [3, 1, 2, 0]
reversed → [0, 2, 1, 3]                    valid topo order
```

Every vertex emits only after its successors emitted — reversing puts
dependencies first. That's the whole proof in one sentence.

---

## Union-Find (Disjoint Set) — incremental connectivity

**What:** A data structure tracking "which vertices are in the same blob" under repeated merging. Two operations:

- `find(v)` → the **root** (a representative id) of v's set. Two vertices share a set iff their roots match.
- `union(a, b)` → merge a's set and b's set.

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))      # everyone is their own parent
        self.rank = [0] * n               # tree height estimate
        self.count = n                    # number of sets

    def find(self, v):
        while self.parent[v] != v:
            self.parent[v] = self.parent[self.parent[v]]  # PATH COMPRESSION:
            v = self.parent[v]                            #   hop 2 levels
        return v                                          #   per step

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False                  # already same set — edge is redundant
        if self.rank[ra] < self.rank[rb]: # UNION BY RANK: shorter tree
            ra, rb = rb, ra               #   attaches under taller one
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True
```

Mental picture — each set is a tree pointing at its root:

```
union(0,1):  0        union(2,3):  0     2       union(1,3):    0
             ^                       ^    ^                      / \
             1                       1    3                     1   2
                                                                  ^
                                              find(3) hops: 3→2→0  3
```

**Why it exists:** The alternative — "to answer 'are a and b connected?', run BFS" — costs O(V + E) **per query**. Union-Find preprocesses connectivity as you add edges, then answers in nearly O(1). The two optimizations are what make it nearly O(1):

- **Path compression:** every `find` re-points nodes toward the root, flattening the tree. Future finds get shorter.
- **Union by rank:** attach the shallower tree under the deeper one, so height grows slowly (without it, `union` chains can degenerate into linked lists → O(n) finds).

Together they give amortized **O(α(n))** per operation — α is the inverse Ackermann function, effectively a small constant for any n you'll ever see.

**Where it's used:** "Are these already connected?" (cycle detection on undirected graphs, redundant edges), Kruskal's MST, counting components as edges stream in, image processing (connected regions), friend-circle queries, percolation problems.

**What goes wrong without it:**
- Re-running BFS for each connectivity query: Q queries × O(V+E) = quadratic-ish blowup where union-find is ~O(Q).
- Skipping path compression *and* union by rank: the parent pointers degenerate into a chain and `find` becomes O(n) — you built a linked list with extra steps.
- Skipping `if ra == rb` in `union`: merging a set into itself creates a self-loop at the root and corrupts `count`.

**Worked example — trace `n=5`, unions `[(0,1),(2,3),(1,3)]`:**

```
start:          {0} {1} {2} {3} {4}     count=5
union(0,1):     {0,1} {2} {3} {4}       count=4
union(2,3):     {0,1} {2,3} {4}         count=3
union(1,3):     {0,1,2,3} {4}           count=2
same(0, 2)?     find(0)=0, find(2)=0 → True
same(0, 4)?     find(4)=4         → False
```

Expected output for `components_after_unions(5, [(0,1),(2,3),(1,3)])`: **2**

---

## Dijkstra — shortest path on weighted graphs

**What:** BFS answers "fewest hops." Dijkstra answers "**cheapest total**" when edges have non-negative weights. Instead of a plain queue, it uses a **min-heap**: always expand the *currently cheapest* known vertex, and relax its edges (offer each neighbor `dist[v] + w` — keep it if it beats what we have).

```python
import heapq

def dijkstra(n, edges, src):
    adj = {v: [] for v in range(n)}
    for a, b, w in edges:                 # directed edge a -w-> b
        adj[a].append((b, w))
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    heap = [(0, src)]                     # (best-known dist, vertex)
    while heap:
        d, v = heapq.heappop(heap)
        if d > dist[v]:
            continue                      # stale heap entry — skip
        for nxt, w in adj[v]:
            nd = d + w
            if nd < dist[nxt]:            # RELAX: found a cheaper route
                dist[nxt] = nd
                heapq.heappush(heap, (nd, nxt))
    return dist
```

**Why the greedy choice works:** when the heap pops `(d, v)`, `d` is *final* — every other route to v that's still in the heap costs ≥ d already, and any route not yet discovered would have to go through one of those (nonnegative weights mean detours only add cost). That's why BFS fails here but a heap succeeds: the queue order must be by **total cost**, not by hop count.

```
    0 --5--> 1        BFS hops:  0→1 (1 hop) beats 0→2→1 (2 hops) —
    |        ^        it reports the cost-5 route as "shortest".
  1 |        | 1
    v        |        Dijkstra:  dist[1] = min(5, 1+1) = 2
    2 -------+        pops (0,0) → (1,2) → (2,1)
```

**Where it's used:** GPS routing, network latency (network-delay-time — signal propagates at edge-weight speed), flight itineraries, game pathfinding (A* is Dijkstra + heuristic), resource planning.

**What goes wrong without it:**
- **BFS on weighted edges** treats a 1-hop/weight-100 edge as "closer" than a 3-hop/weight-3 path. Hop count ≠ cost.
- **Negative edges break it.** Dijkstra's proof needs "finalized stays final." With a weight of -5, a vertex popped at cost 10 can later be improved to 10-5 — the greedy invariant dies. Negative weights → Bellman-Ford, not Dijkstra.
- **Forgetting the stale-entry guard.** Vertices get pushed multiple times as better distances are found; the heap holds outdated `(old_d, v)` entries. Without `if d > dist[v]: continue` you relax edges from a stale distance — wrong answers and wasted work.
- Pushing `(vertex, dist)` instead of `(dist, vertex)` — heapq orders by the FIRST tuple element, so the distance must come first.

**Worked example — `n=4`, edges `(0,1,5) (0,2,1) (2,1,2) (1,3,1) (2,3,5)`, src=0:**

```
heap=[(0,0)]          pop (0,0): relax → 1:5, 2:1     heap=[(1,2),(5,1)]
pop (1,2): 2's dist final=1 → relax 1: min(5,1+2)=3, 3:6   heap=[(3,1),(5,1),(6,3)]
pop (3,1): 1's dist final=3 → relax 3: min(6,3+1)=4        heap=[(4,3),(5,1),(6,3)]
pop (4,3): 3's dist final=4 → heap=[(5,1),(6,3)]
pop (5,1): STALE (dist[1]=3) → skip
pop (6,3): STALE (dist[3]=4) → skip
dist = [0, 3, 1, 4]
```

Expected output for `dijkstra(4, [(0,1,5),(0,2,1),(2,1,2),(1,3,1),(2,3,5)], 0)`: **`[0, 3, 1, 4]`** — note dist[1]=3 via 0→2→1 beats the direct 5, and that's the whole point.

Complexity: **O((V + E) log V)** time — every push is log-heap-size; **O(V + E)** space.

---

## When to Pick Which — the decision table

**What:** Three tools, three questions:

```
"Fewest hops / steps, every edge the same cost?"
        → BFS (lesson 13). Level = distance. O(V + E).

"Cheapest path, edges have weights ≥ 0?"
        → Dijkstra. Heap order = cost order. O((V+E) log V).

"Are a and b in the same group? Repeatedly? While edges keep arriving?"
        → Union-Find. ~O(1) per query/union. O(V) space.

"Order me a list where every dependency comes first?"
        → Topological sort. Kahn's or DFS postorder. O(V + E).
        Bonus: a DAG that can't be fully ordered has a cycle.
```

**Why it exists:** Picking the wrong tool is the classic interview failure: BFS on a weighted graph gives wrong distances; Dijkstra on an unweighted one works but wastes a heap where a deque sufficed; union-find can't produce a path or an ordering at all — it only answers membership.

**Where it's used:** This exact decision — "what KIND of question is being asked?" — is the skill. Distance-in-hops vs cost, ordering vs membership, static graph vs streaming edges.

**What goes wrong without it:**
- Union-Find asked to return a PATH → it can't; it only tracks set membership. (Reconstruct paths with BFS/Dijkstra parent pointers.)
- Topological sort attempted on an undirected graph → meaningless; every undirected edge is "a before b AND b before a," instantly a cycle.
- Dijkstra on a graph with a negative edge → silently wrong answers, no crash, no warning.

**Quick drill — name the tool:**
1. "Minimum number of flights between two cities, any airline" → **BFS** (unweighted hops).
2. "Cheapest airfare between two cities" → **Dijkstra** (weights).
3. "Given a list of friendships arriving one at a time, report group count after each" → **Union-Find** (incremental connectivity).
4. "Schedule 20 tasks with prerequisites" → **Topological sort**.

---

## The Pitfall Gallery — five ways these algorithms go wrong

**1. Kahn's: returning a partial order on a cyclic graph.**
```python
# WRONG — silently returns an incomplete "order"
return order
# CORRECT — leftover vertices mean a cycle; there IS no valid order
return order if len(order) == n else []
```

**2. DFS cycle check without three colors.**
A single `visited` set can't distinguish a back edge (cycle) from a cross edge to a finished vertex (legal). Use `state[v] in {unseen, visiting, done}`; only `visiting` means cycle.

**3. Union-Find: skipping `ra == rb`.**
Merging a root into itself creates a self-cycle and decrements `count` spuriously. The early return is load-bearing — it's also how you detect redundant edges.

**4. Dijkstra: no stale-entry guard.**
```python
# WRONG — processes outdated (dist, v) pairs; may relax with stale d
d, v = heapq.heappop(heap)
for nxt, w in adj[v]: ...
# CORRECT
d, v = heapq.heappop(heap)
if d > dist[v]:
    continue
for nxt, w in adj[v]: ...
```

**5. Dijkstra on negative edges.**
Greedy finalization assumes costs only grow. A `-5` edge invalidates already-popped distances. If the problem allows negatives, the right answer is Bellman-Ford — or call out the assumption.

**Edge cases to always test:** empty edge list (topo = any order; union-find = n sets), self-loop `(a,a)` (instant cycle), unreachable vertices in Dijkstra (`inf`), single vertex, and "already connected" unions (`same` must stay True, `count` must not drop).
