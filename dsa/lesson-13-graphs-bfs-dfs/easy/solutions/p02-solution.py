"""
SOLUTION: BFS Traversal Order — (Easy)
==============================
deque + popleft = FIFO = level order. Mark `seen` at ENQUEUE time so
each vertex enters the queue exactly once. O(V + E) time, O(V) space.
"""
from collections import deque

def bfs_order(adj, start):
    seen = {start}
    q = deque([start])
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for nxt in adj[v]:
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return order

if __name__ == "__main__":
    adj = {0:[1,2], 1:[0,3], 2:[0,4,5], 3:[1], 4:[2], 5:[2]}
    assert bfs_order(adj, 0) == [0, 1, 2, 3, 4, 5]
    assert bfs_order({0:[]}, 0) == [0]
    assert bfs_order({0:[1], 1:[0], 2:[]}, 0) == [0, 1]   # disconnected
    assert bfs_order({0:[1], 1:[0,2], 2:[1]}, 0) == [0, 1, 2]
    print("All tests passed!")
