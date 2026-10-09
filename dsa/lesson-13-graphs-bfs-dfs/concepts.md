# Lesson 13 — Graphs: BFS & DFS

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **14 tiny files, ~5 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [What is a graph?](chapters/01-what-is-a-graph.md) | why we need a new shape at all |
| 02 | [Graph words, made friendly](chapters/02-graph-words-made-friendly.md) | vertex, edge, cycle, component — no fear |
| 03 | [The adjacency list](chapters/03-adjacency-list.md) | **the one data structure to master** |
| 04 | [The adjacency matrix](chapters/04-adjacency-matrix.md) | when the V×V table wins (rarely) |
| 05 | [The grid is secretly a graph](chapters/05-grid-as-graph.md) | each cell = a node — the big unlock |
| 06 | [BFS: ripples on a pond](chapters/06-bfs-ripples.md) | how the queue visits layer by layer |
| 07 | [Why BFS = shortest path](chapters/07-bfs-shortest-path.md) | ring number IS the distance |
| 08 | [The visited set](chapters/08-the-visited-set.md) | the one line that prevents infinite loops |
| 09 | [DFS: follow the corridor](chapters/09-dfs-corridor.md) | recursion + backtracking, traced |
| 10 | [Iterative DFS](chapters/10-iterative-dfs.md) | your own stack, no recursion limit |
| 11 | [BFS or DFS? Decision table](chapters/11-bfs-vs-dfs.md) | which tool answers which question |
| 12 | [Counting islands](chapters/12-counting-islands.md) | the components pattern on grids |
| 13 | [The 10-second recipe](chapters/13-the-recipe.md) | recognize a graph problem instantly |
| 14 | [The pitfall gallery](chapters/14-pitfall-gallery.md) | five ways graph code goes wrong |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> A **graph** = nodes + edges; store it as an **adjacency list**
> (`dict: node → [neighbors]`). **BFS** ripples outward with a queue —
> ring number = distance → shortest path on unweighted graphs. **DFS**
> dives deep then backtracks, recursively or with an explicit stack —
> reachability, cycles, counting, enumerating. Both need a **`seen` set**
> marked at push/enqueue time; both run **O(V + E)**. A **grid is a graph**
> whose edges are computed (`r±1, c±1`), and **islands = connected
> components** found by scan + flood.

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
