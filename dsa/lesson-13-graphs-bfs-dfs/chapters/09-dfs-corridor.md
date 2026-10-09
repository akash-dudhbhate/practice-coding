# 09 — DFS: Follow the Corridor to the End

> 6-minute read. The other traversal — depth before breadth.

## The idea, plain words

**DFS (Depth-First Search) is maze logic:** pick a corridor and follow it
as far as it goes. Dead end? Backtrack to the last junction and try the
next corridor. Never check "how far from the start" — just keep diving.

Same map:

```
    A — B              DFS from A (neighbors alphabetical):
    |   |
    C — D — E          A → B → D → C   (dead end — C's neighbors all seen)
                            ↓ backtrack to D, try its next neighbor
                            E          (dead end — done)
```

BFS would visit A, B, C, D, E by distance. DFS dives `A→B→D→C` first —
a completely different order, equally valid.

## Code: 5 lines of recursion

The function calls itself on each unvisited neighbor. Python's **call
stack** remembers where to backtrack to — you get "retrace my steps"
for free.

```python
def dfs(adj, v, seen, out):
    seen.add(v)            # 1. check the box FIRST (ch.08!)
    out.append(v)          # 2. record the visit
    for nxt in adj[v]:     # 3. dive into each unvisited neighbor
        if nxt not in seen:
            dfs(adj, nxt, seen, out)

adj = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"],
       "D": ["B", "C", "E"], "E": ["D"]}
seen, out = set(), []
dfs(adj, "A", seen, out)
print(out)                 # ['A', 'B', 'D', 'C', 'E']
```

## Hand-trace the recursion

```
dfs(A): seen={A}        out=[A]        neighbors: B, C
  dfs(B): seen+={B}     out+=[B]       B's neighbors: A✗, D
    dfs(D): seen+={D}   out+=[D]       D's neighbors: B✗, C, E
      dfs(C): seen+={C} out+=[C]       C's neighbors: A✗, D✗ → return
      dfs(E): seen+={E} out+=[E]       E's neighbor:   D✗   → return
    (D done) → return
  (B done) → return
  back in A: next neighbor C — already in seen → skip
final: [A, B, D, C, E]
```

Watch how deep it goes before ever looking at A's second neighbor C —
that's "depth-first" in action. C got reached from D, not from A.

## Why it exists

DFS answers different questions than BFS: "is there ANY path?", "what's
reachable?", "does a cycle exist?", "enumerate every possibility."
It's the natural shape when the answer lives at the *deepest* point —
backtracking, puzzle solving, tree walks. And at 5 lines it's the shortest
correct graph code you'll ever write.

## Where it's used

Reachability, component counting, cycle detection, topological sort
(lesson 14), backtracking (every "try all combinations" problem is DFS on
an implicit graph), flood fill.

## Common mistake

**Recursion depth.** Python bails at ~1000 nested calls. A chain-shaped
graph of 2000 nodes crashes recursive DFS with `RecursionError` — even
though the logic is perfect. The fix is the next chapter: same algorithm,
explicit stack.

## Your turn

Run the same recursive DFS starting at **E**. What's the visit order?
(D's neighbor list is `["B", "C", "E"]` — B first.)

<details><summary>Answer</summary>
`[E, D, B, A, C]` — dive E→D→B→A, then A's second neighbor C is unvisited
→ dfs(C). Compare with BFS from E (E,D,B,C,A): DFS reaches A *before* C
because it dives instead of rippling.
</details>

---

**← Prev** [08 — Visited set](08-the-visited-set.md) ·
**Next →** [10 — Iterative DFS](10-iterative-dfs.md)
