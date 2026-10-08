"""
SOLUTION: Kahn's Topological Order — (Medium)
==============================
Indegree table + queue seeded with every indegree-0 vertex. Each pop
emits a vertex and "deletes" its outgoing edges; neighbors hitting
indegree 0 join the queue. len(order) < n => cycle => [].
"""
from collections import deque

def kahn_order(n, edges):
    adj = {v: [] for v in range(n)}
    indeg = [0] * n
    for a, b in edges:
        adj[a].append(b)
        indeg[b] += 1
    q = deque(v for v in range(n) if indeg[v] == 0)
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for nxt in adj[v]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return order if len(order) == n else []

if __name__ == "__main__":
    def valid(order, n, edges):
        if len(order) != n:
            return False
        pos = {v: i for i, v in enumerate(order)}
        return all(pos[a] < pos[b] for a, b in edges)

    e1 = [(0,1),(0,2),(1,3),(2,3)]
    assert valid(kahn_order(4, e1), 4, e1)
    assert kahn_order(2, [(0,1),(1,0)]) == []
    e3 = [(1,0),(2,0),(3,1),(3,2)]
    assert valid(kahn_order(4, e3), 4, e3)
    assert valid(kahn_order(3, []), 3, [])
    assert kahn_order(3, [(0,1),(1,2),(2,0)]) == []
    print("All tests passed!")
