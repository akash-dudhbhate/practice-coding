# 12 — Picking the right tool: the decision table

> 4-minute read. The meta-skill of the whole lesson.

## The idea, plain words

Every graph problem is secretly asking one of a handful of *kinds* of
questions. Name the kind, and the algorithm chooses itself:

```
"Fewest hops / steps, every edge the same cost?"
        → BFS (lesson 13). Level = distance. O(V + E).

"Cheapest path, edges have weights ≥ 0?"
        → Dijkstra. Heap order = cost order. O((V+E) log V).

"Negative weights possible?"
        → Bellman-Ford. Relax all edges V−1 times. O(V·E).

"Are a and b in the same group? Repeatedly? While edges keep arriving?"
        → Union-Find. ~O(1) per query/union. O(V) space.

"Order me a list where every dependency comes first?"
        → Topological sort. Kahn's or DFS postorder. O(V + E).
        Bonus: can't fully order it → there's a cycle.

"Connect everything, minimum total edge cost?"
        → Kruskal's MST. Sort + Union-Find. O(E log E).
```

## Why it exists

Picking the *wrong* tool is the classic failure mode:

- BFS on a weighted graph → wrong distances (hop count ≠ cost).
- Dijkstra on an unweighted graph → works, but a heap where a deque
  sufficed.
- Union-Find asked for a *path* → can't — it only tracks membership.
  (Reconstruct paths with BFS/Dijkstra parent pointers.)
- Topo sort on an undirected graph → meaningless; every edge is a
  2-cycle.

The skill isn't memorizing six algorithms — it's hearing "what KIND of
question is this?" Distance-in-hops vs cost. Ordering vs membership.
Static graph vs streaming edges.

## Quick drill — name the tool before peeking

1. "Minimum number of flights between two cities, any airline"
2. "Cheapest airfare between two cities"
3. "Friendships arrive one at a time; report group count after each"
4. "Schedule 20 tasks with prerequisites"
5. "Lay cable to connect all offices for minimum cost"

<details><summary>Answers</summary>
1. **BFS** — unweighted hops. 2. **Dijkstra** — weights.
3. **Union-Find** — incremental connectivity. 4. **Topological sort.**
5. **Kruskal's MST** — and notice it *uses* Union-Find.
</details>

## Where it's used

This exact decision — matching problem-shape to algorithm — is what
interviews actually test once you're past "can you code BFS."

## Common mistake

Reaching for the fanciest tool you know. Dijkstra on an unweighted graph
isn't wrong, just wasteful — but Union-Find where you needed an actual
path, or topo-sort where you needed distances, is *structurally* wrong.
Match the question first.

## Your turn

"Detect whether package A's install requirements eventually require
package A itself" — which tool?

<details><summary>Answer</summary>
Cycle detection on a directed graph: three-color DFS (ch.05) or Kahn's
leftover check (ch.03). Requirements = edges, "eventually requires
itself" = cycle.
</details>

---

**← Prev** [11 — Kruskal's MST](11-kruskal-mst.md) ·
**Next →** [13 — The pitfall gallery](13-pitfall-gallery.md)
