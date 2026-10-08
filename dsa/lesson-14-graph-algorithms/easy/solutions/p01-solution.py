"""
SOLUTION: Detect a Cycle in a Directed Graph — (Easy)
==============================
Kahn's leftover trick: peel every indegree-0 vertex (nothing depends on
it). A DAG emits all n; a cyclic graph leaves vertices whose indegree
never reaches 0 — they're waiting on each other forever.
"""
from collections import deque

def has_directed_cycle(n, edges):
    adj = {v: [] for v in range(n)}
    indeg = [0] * n
    for a, b in edges:
        adj[a].append(b)
        indeg[b] += 1
    q = deque(v for v in range(n) if indeg[v] == 0)
    emitted = 0
    while q:
        emitted += 1
        for nxt in adj[q.popleft()]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return emitted < n

if __name__ == "__main__":
    assert has_directed_cycle(3, [(0,1),(1,2),(2,0)]) is True
    assert has_directed_cycle(3, [(0,1),(1,2)]) is False
    assert has_directed_cycle(4, [(0,1),(1,2),(2,3)]) is False
    assert has_directed_cycle(2, [(0,1),(1,0)]) is True
    assert has_directed_cycle(1, [(0,0)]) is True
    assert has_directed_cycle(4, [(0,1),(0,2),(1,3),(2,3)]) is False
    assert has_directed_cycle(0, []) is False
    print("All tests passed!")
