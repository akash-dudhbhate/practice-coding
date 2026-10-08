# lesson-14-graph-algorithms — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: Indegree zero
```
edges: 0→1, 0→2, 1→3, 2→3
indegrees: 0:0  1:1  2:1  3:2
```
Kahn's algorithm starts by enqueuing vertices with indegree 0. Which
vertex MUST be emitted last in every valid topo order?

- (A) 0
- (B) 1 or 2
- (C) 3

<details><summary>Answer</summary>
**(C) 3** — vertex 3 waits on BOTH 1 and 2, which both wait on 0. Only
vertex 3 has incoming edges from two different chains converging, so it
can't be emitted until every predecessor is out. Vertex 0 is forced to be
first; 1 and 2 can swap freely.
</details>

---

## Check 02: The leftover queue
```
edges: 0→1, 1→2, 2→0, 0→3
```
Kahn's runs to the end. What does `order` contain, and what does that
tell you?

<details><summary>Answer</summary>
**`order` = `[3]`... or possibly `[0?]`** — let's trace: indegrees are
0:1, 1:1, 2:1, 3:1. NO vertex has indegree 0 → the queue starts EMPTY →
`order = []`. Either way, `len(order) < n` = cycle detected. On a cyclic
graph Kahn's can't even start: every vertex in the cycle (and everything
downstream of it) has an indegree ≥ 1 forever. That emptiness IS the
cycle signal — don't return the partial list as if it were valid.
</details>

---

## Check 03: Why heap order = cost order
```python
heap = [(5, 'direct'), (3, 'via_detour')]   # (dist, vertex)
```
BFS pops by arrival order. Dijkstra pops the heap's minimum. If we popped
'direct' (cost 5) before 'via_detour' (cost 3), what breaks?

<details><summary>Answer</summary>
**Finality.** Dijkstra's guarantee — "a popped vertex's distance is
final" — only holds because the heap serves cheapest-first. Pop the 5
before the 3, and later the 3-path relaxes the already-"finalized"
neighbors of the 5-path to lower costs. Every downstream distance then
needs repair — the whole greedy invariant collapses into a mess of
re-updates (that's roughly Bellman-Ford, with worse constants).
</details>

---

## Check 04: Union-Find after compressions
```python
uf = UnionFind(6)
uf.union(0,1); uf.union(2,3); uf.union(0,3)
# tree: 3 -> 2 -> 0 roughly, with ranks deciding the exact shape
uf.find(3)
```
After `find(3)` returns, what changed in `parent`?

<details><summary>Answer</summary>
**Every node on 3's root-path got re-pointed closer to the root** — path
compression. `find` isn't just a query; it's a repair operation that pays
for itself: the next `find(3)` (or `find` of anything under it) is one
hop instead of a walk. Skip it and union-by-rank alone keeps heights
logarithmic — still fine — but compression is what makes repeated queries
effectively O(1).
</details>

---

## Check 05: Redundant edge intuition
```
edges (in order): (1,2) (1,3) (2,3)
```
Processing with union-find, which union call returns False — and why is
that exactly the answer?

<details><summary>Answer</summary>
**`(2,3)`.** `(1,2)` merges {1},{2}; `(1,3)` merges {3} into {1,2};
at `(2,3)` both already share root → union returns False → that edge
closes a cycle → it's THE redundant one. Because input order is
respected, the FIRST failed union is automatically the LAST edge in
input order that creates a cycle. The whole problem is one line:
`if not uf.union(a,b): return [a,b]`.
</details>

---

## Debug Exercises — find and fix the bug

> Fix the broken code. Find bugs mentally before running.

---

## Debug 01 (Easy): Topo order that loses vertices

```python
def topo_order(n, edges):
    adj = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b)
    indeg = [0] * n
    for a, b in edges:
        indeg[b] += 1
    q = deque(v for v in range(n) if indeg[v] == 0)
    order = []
    while q:
        v = q.popleft(); order.append(v)
        for nxt in adj[v]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return order if len(order) == n else []
```

**Hint:** `topo_order(3, [(1,2)])` should be a permutation of [0,1,2] —
but it crashes.

<details><summary>Answer</summary>

**Bug:** `adj` is built only from edge STARTS — `adj[2]` never exists,
but vertex 2 (indegree… wait, vertex 0 has indegree 0 and no outgoing
edges; when vertex 2 is enqueued... actually vertex 0 pops and `adj[0]`
→ KeyError since 0 has no outgoing edges.
**Fix:** seed every vertex before adding edges:
```python
adj = {v: [] for v in range(n)}
for a, b in edges:
    adj[a].append(b)
```
Same lesson as lesson 13: vertices exist independently of edges.
</details>

---

## Debug 02 (Medium): Dijkstra without the stale guard

```python
def dijkstra(n, edges, src):
    adj = {v: [] for v in range(n)}
    for a, b, w in edges:
        adj[a].append((b, w))
    dist = [float("inf")] * n
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, v = heapq.heappop(heap)
        for nxt, w in adj[v]:               # <- missing stale check
            if d + w < dist[nxt]:
                dist[nxt] = d + w
                heapq.heappush(heap, (d + w, nxt))
    return dist
```

**Hint:** on `[(0,1,1),(0,2,10),(1,2,1)]`, trace what happens when the
stale `(10,2)` heap entry pops AFTER `dist[2]` already became 2.

<details><summary>Answer</summary>

**Bug:** stale entries reprocess a vertex with an OUTDATED distance.
Here `(10,2)` pops after `dist[2]` is final at 2, then scans all of
2's edges anyway — `10 + w` can't beat `dist[nxt]`, so the output stays
correct on THIS graph, but every stale entry burns a full adjacency
scan and keeps the heap (and runtime) bloated far past O(E log V).
The finality guarantee is also why you want the habit: with negative
edges the same stale pop CAN corrupt answers.
**Fix:**
```python
d, v = heapq.heappop(heap)
if d > dist[v]:
    continue                     # expired entry — discard, don't rescan
for nxt, w in adj[v]:
    ...
```
The relax check `nd < dist[nxt]` writes improvements; the stale guard
prevents the wasted work. You need BOTH — they answer different
questions ("is this a better path?" vs "is this pop even current?").
</details>

---

## Debug 03 (Hard): Union-Find that forgets the root check

```python
def union(self, a, b):
    self.parent[self.find(a)] = self.find(b)   # <- the bug
    self.count -= 1
    return True
```

**Hint:** `union(0,1); union(0,1)` — what happens to `count`, and to
`parent` at the root?

<details><summary>Answer</summary>

**Bug:** no `ra == rb` early return. Unioning an already-merged pair
writes `parent[root] = root` (harmless-looking self-loop) and decrements
`count` anyway — so `count` silently over-reports merges and every
"redundant edge" check breaks.
**Fix:**
```python
ra, rb = self.find(a), self.find(b)
if ra == rb:
    return False
self.parent[rb] = ra
self.count -= 1
return True
```
The `False` return isn't decoration — redundant-connection is answered
BY it.
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: Partial topo order on a cycle
```python
# WRONG — returns a truncated "order" as if it were legal
return order

# CORRECT — leftover vertices ARE the cycle
return order if len(order) == n else []
```

## Mistake 02: One-color DFS cycle check
```python
# WRONG — "visited" can't distinguish back edges from finished subtrees;
# a diamond DAG (0->1, 0->2, 1->3, 2->3) gets flagged as cyclic
if v in visited: return True

# CORRECT — three states: unseen / visiting / done
if state[nxt] == 1: return False   # visiting = back edge = cycle
```

## Mistake 03: Heap tuple in the wrong order
```python
# WRONG — heapq sorts on element 0; this heaps by vertex id!
heapq.heappush(heap, (vertex, dist))

# CORRECT
heapq.heappush(heap, (dist, vertex))
```

## Mistake 04: BFS on weighted edges
```python
# WRONG — counts hops; a 1-hop cost-99 edge "wins" over a 3-hop cost-3 path
queue.popleft()  # level order != cost order

# CORRECT — the heap orders by TOTAL COST
heapq.heappop(heap)
```

## Mistake 05: Union-Find keyed wrong on 1-indexed input
```python
# WRONG — vertices 1..n but parent array sized n → vertex n is out of range
uf = UnionFind(n)

# CORRECT — size n+1 (ignore slot 0) or subtract 1 everywhere
uf = UnionFind(n + 1)
```

## Mistake 06: Forgetting `same`/`find` need ROOTS, not parents
```python
# WRONG — parent[a] is only the NEXT hop, not the root
return self.parent[a] == self.parent[b]

# CORRECT — compare roots
return self.find(a) == self.find(b)
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Cycle detect via "did Kahn emit everything?"
### Before
```python
def has_directed_cycle(n, edges):
    # ... 40 lines of 3-color recursive DFS ...
```
### Problems
1. Correct but heavyweight for a yes/no question
2. Recursion-limit risk on deep graphs

### After
```python
def has_directed_cycle(n, edges):
    adj = {v: [] for v in range(n)}
    indeg = [0] * n
    for a, b in edges:
        adj[a].append(b); indeg[b] += 1
    q = deque(v for v in range(n) if indeg[v] == 0)
    emitted = 0
    while q:
        v = q.popleft()
        emitted += 1
        for nxt in adj[v]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return emitted < n       # leftovers = cycle. One counter, no colors.
```
You don't even need to STORE the order when all you want is the verdict.

---

## Refactor 02 (Medium): Union-Find without rank
### Before
```python
def union(self, a, b):
    ra, rb = self.find(a), self.find(b)
    if ra == rb: return False
    self.parent[rb] = ra     # attach arbitrarily — b's root under a's
    self.count -= 1
    return True
```
### Problems
1. Chained unions `union(0,1), union(1,2), union(2,3), ...` build a
   HEIGHT-n tree — `find` degrades toward O(n)
2. Path compression alone helps but repeated worst-case shapes still hurt

### After
```python
def union(self, a, b):
    ra, rb = self.find(a), self.find(b)
    if ra == rb: return False
    if self.rank[ra] < self.rank[rb]:
        ra, rb = rb, ra           # shorter tree goes under the taller
    self.parent[rb] = ra
    if self.rank[ra] == self.rank[rb]:
        self.rank[ra] += 1        # height grew only on a tie
    self.count -= 1
    return True
```
Rank = "how tall is this tree, roughly." Attach small under tall:
heights stay ≤ log n even before compression does its work.

---

## Refactor 03 (Hard): Dijkstra with decrease-key simulation mess
### Before
```python
# trying to keep the heap "clean" by removing outdated entries manually
if (old_d, v) in heap:
    heap.remove((old_d, v))      # O(heap size) — worse than the problem
```
### Problems
1. `heap.remove` is linear — destroys the log V that made heaps worth it
2. Tracking old entries costs more code than just letting them expire

### After
```python
# the standard trick: NEVER remove. Push the better entry; let stale
# ones die at pop time with one comparison.
heapq.heappush(heap, (nd, nxt))
# later, at pop:
d, v = heapq.heappop(heap)
if d > dist[v]:
    continue                     # expired — cost: one comparison
```
"Lazy deletion" — the heap may hold O(E) stale entries but each costs
O(log V) to discard once, keeping total O(E log V).

---

## Approach Comparison — different ways to solve it

## Problem: Cycle detection in a directed graph

### Approach 1: 3-color DFS — O(V + E)
```python
# state: 0 unseen, 1 visiting (on stack), 2 done; 1->back edge = cycle
```
**Pros:** Finds the actual cycle path; works recursively. **Cons:**
recursion depth limits; 3-state bookkeeping.

### Approach 2: Kahn's leftover — O(V + E)
```python
# emit indegree-0 vertices; emitted < n => cycle
```
**Pros:** Iterative, doubles as topo sort, trivially small. **Cons:**
can't report WHICH vertices form the cycle (leftovers include everything
downstream of one).

**Winner:** Kahn's for a yes/no verdict — you get topo order for free.
3-color DFS when you must identify the cycle itself.

---

## Problem: "Are a and b connected?" — asked q times as edges stream in

### Approach 1: BFS per query — O(q·(V+E))
```python
# rebuild/flood from scratch per question
```
**Pros:** Zero machinery. **Cons:** q floods; for q ≈ E you're quadratic.

### Approach 2: Union-Find — O((E + q)·α(V))
```python
for a, b in edges_so_far: uf.union(a, b)
answer = uf.same(x, y)
```
**Pros:** Near-constant per query; edges can keep arriving for free.
**Cons:** Can't produce the path, can't handle edge DELETION.

**Winner:** Approach 2 — streaming connectivity is union-find's entire
reason to exist. If the question were "WHAT is the path", neither helps:
that's back to BFS/Dijkstra.
