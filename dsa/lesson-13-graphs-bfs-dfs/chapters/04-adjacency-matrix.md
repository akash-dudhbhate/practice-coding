# 04 — The Adjacency Matrix (quick look — know it, rarely use it)

> 4-minute read. The alternative you'll meet in old textbooks.

## The idea, plain words

An **adjacency matrix** is a V×V grid of 0s and 1s:
`matrix[a][b] == 1` means "edge a→b exists." It's a giant lookup table —
row = from, column = to.

Our same map (A=0, B=1, C=2, D=3, E=4):

```
    A — B                     to: 0  1  2  3  4
    |   |                  0  [ 0, 1, 1, 0, 0 ]
    C — D — E    ──►       1  [ 1, 0, 0, 1, 0 ]
                           2  [ 1, 0, 0, 1, 0 ]
                           3  [ 0, 1, 1, 0, 1 ]
                           4  [ 0, 0, 0, 1, 0 ]
```

```python
matrix = [
#    to: 0  1  2  3  4
    [0, 1, 1, 0, 0],   # from 0 (A): reaches B, C
    [1, 0, 0, 1, 0],   # from 1 (B): reaches A, D
    [1, 0, 0, 1, 0],   # from 2 (C): reaches A, D
    [0, 1, 1, 0, 1],   # from 3 (D): reaches B, C, E
    [0, 0, 0, 1, 0],   # from 4 (E): reaches D
]
print(matrix[3][4])   # 1 — is D connected to E? instant answer
```

Notice the matrix is a mirror image across the diagonal — that's what
undirected looks like: `matrix[a][b]` always equals `matrix[b][a]`.

## List vs matrix — the honest comparison

| Question | Adjacency list | Adjacency matrix |
|----------|---------------|------------------|
| Space | O(V + E) — pays for real edges | O(V²) — pays for every possible edge |
| "Is u a neighbor of v?" | O(degree) scan of `adj[v]` | O(1) lookup `matrix[u][v]` |
| "List ALL neighbors of v" | O(degree) — just read the list | O(V) — scan a whole row |
| V = 100,000 nodes, sparse | fine | 10 billion cells — dead |

## Why it exists (and when it wins)

The matrix wins on exactly one thing: **instant edge lookup**. If an
algorithm asks "is there an edge between x and y?" millions of times, the
O(1) check beats scanning a list. It also shows up when the input *already
is* a matrix — grids (ch.05), or dense graphs where most edges exist anyway.

For everything else — especially the sparse graphs real problems give you —
the list wins on memory and on "list all neighbors," which traversals need
constantly.

## Common mistake

Reaching for a matrix because it "feels simpler," then blowing up memory.
100k nodes × 100k nodes = 10¹⁰ cells — your program dies before the
algorithm starts. Default to the adjacency list; switch to a matrix only
for small or dense graphs.

## Your turn

In `matrix` above, how do you check whether A (node 0) and E (node 4) are
neighbors — and what's the answer?

<details><summary>Answer</summary>
`matrix[0][4]` → `0`, so no — A and E are not neighbors (they're connected
by a path through D, but no direct edge). One lookup, O(1). In an adjacency
list you'd instead check `4 in adj[0]` — a small scan.
</details>

---

**← Prev** [03 — Adjacency list](03-adjacency-list.md) ·
**Next →** [05 — The grid is secretly a graph](05-grid-as-graph.md)
