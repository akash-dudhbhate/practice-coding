# Lesson 14 — Graph Algorithms

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **13 tiny files, ~5 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.
This lesson assumes lesson 13 (adjacency lists, BFS, DFS).

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [When BFS/DFS isn't enough](chapters/01-when-bfs-dfs-isnt-enough.md) | the 4 questions that need new tools |
| 02 | [DAGs and topological order](chapters/02-dags-and-topo-order.md) | what "every dependency first" means |
| 03 | [Kahn's algorithm](chapters/03-kahns-algorithm.md) | topo sort by indegree — traced |
| 04 | [Topo sort via DFS](chapters/04-topo-sort-dfs.md) | postorder, reversed — why it works |
| 05 | [Detecting cycles](chapters/05-cycle-detection.md) | why one `visited` set is a lie |
| 06 | [Union-Find](chapters/06-union-find.md) | "same group?" without re-running BFS |
| 07 | [Why Union-Find is fast](chapters/07-why-union-find-is-fast.md) | rank + compression = ~O(1) |
| 08 | [Dijkstra: the idea](chapters/08-dijkstra-idea.md) | cheapest-first instead of first-come |
| 09 | [Dijkstra: full trace](chapters/09-dijkstra-trace.md) | the distance table + heap, step by step |
| 10 | [Negative edges break Dijkstra](chapters/10-negative-edges.md) | the counterexample; when Bellman-Ford |
| 11 | [Kruskal's MST](chapters/11-kruskal-mst.md) | cheapest edges first — Union-Find callback |
| 12 | [Picking the right tool](chapters/12-picking-the-tool.md) | match the question's shape to an algorithm |
| 13 | [The pitfall gallery](chapters/13-pitfall-gallery.md) | the 5 classic bugs + edge cases |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> Four questions, four tools. **Ordering with dependencies** → topological
> sort (Kahn's: emit indegree-0 vertices; or DFS postorder reversed).
> **Cycle in a directed graph** → three-color DFS; only "still on my
> path" (gray) means cycle. **Repeated "same group?" while edges stream
> in** → Union-Find, ~O(1) per op thanks to union by rank + path
> compression. **Cheapest path, weights ≥ 0** → Dijkstra: a heap ordered
> by distance, relax edges, skip stale entries; negative weights break
> its "popped = final" promise → Bellman-Ford. And **connect everything
> cheapest** → Kruskal's MST, which is just sort + Union-Find.

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
