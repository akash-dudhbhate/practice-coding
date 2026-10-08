"""
SOLUTION: Dijkstra's Shortest Path — (Hard)
==============================
Min-heap keyed by distance. Pop = cheapest-known = FINAL distance
(non-negative weights make that provable). Relax each edge; stale
pops die on `d > dist[v]`. O((V+E) log V) time.
"""
import heapq

def dijkstra(n, edges, src):
    adj = {v: [] for v in range(n)}
    for a, b, w in edges:
        adj[a].append((b, w))            # directed
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, v = heapq.heappop(heap)
        if d > dist[v]:
            continue                     # stale entry
        for nxt, w in adj[v]:
            nd = d + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(heap, (nd, nxt))
    return dist

if __name__ == "__main__":
    edges = [(0,1,5),(0,2,1),(2,1,2),(1,3,1),(2,3,5)]
    assert dijkstra(4, edges, 0) == [0, 3, 1, 4]
    assert dijkstra(3, [(0,1,2)], 0) == [0, 2, float("inf")]
    assert dijkstra(3, [(0,1,2),(0,2,5)], 1) == [float("inf"), 0, float("inf")]
    assert dijkstra(1, [], 0) == [0]
    assert dijkstra(5, [(0,1,1),(1,2,1),(0,2,4),(2,3,1),(1,3,9),(3,4,1)], 0) == [0,1,2,3,4]
    print("All tests passed!")
