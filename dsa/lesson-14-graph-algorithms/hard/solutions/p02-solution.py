"""
SOLUTION: Network Delay Time — (Hard)
==============================
Dijkstra from source k; answer = max over shortest distances (the LAST
node to receive the signal sets the delay). Any inf => unreachable => -1.
Nodes are 1-indexed, so shift or size arrays n+1.
"""
import heapq

def network_delay_time(times, n, k):
    adj = {v: [] for v in range(1, n + 1)}
    for u, v, w in times:
        adj[u].append((v, w))
    INF = float("inf")
    dist = {v: INF for v in range(1, n + 1)}
    dist[k] = 0
    heap = [(0, k)]
    while heap:
        d, v = heapq.heappop(heap)
        if d > dist[v]:
            continue
        for nxt, w in adj[v]:
            nd = d + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(heap, (nd, nxt))
    worst = max(dist.values())
    return worst if worst < INF else -1

if __name__ == "__main__":
    assert network_delay_time([(2,1,1),(2,3,1),(3,4,1)], 4, 2) == 2
    assert network_delay_time([(1,2,1)], 2, 1) == 1
    assert network_delay_time([(1,2,1)], 2, 2) == -1
    assert network_delay_time([(1,2,1),(2,3,2),(1,3,4)], 3, 1) == 3
    assert network_delay_time([(1,2,5),(2,3,5),(1,3,100)], 3, 1) == 10
    print("All tests passed!")
