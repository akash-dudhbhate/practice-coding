"""
SOLUTION: Shortest Path in an Unweighted Graph — (Medium)
==============================
BFS with a dist dict: first time the target pops, its level is provably
minimal (FIFO visits distance d fully before d+1). `dist` doubles as
the visited set. -1 when the queue empties without reaching target.
"""
from collections import deque

def shortest_distance(adj, start, target):
    dist = {start: 0}
    q = deque([start])
    while q:
        v = q.popleft()
        if v == target:
            return dist[v]
        for nxt in adj[v]:
            if nxt not in dist:
                dist[nxt] = dist[v] + 1
                q.append(nxt)
    return -1

if __name__ == "__main__":
    sq = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2]}
    assert shortest_distance(sq, 0, 3) == 2
    assert shortest_distance(sq, 0, 0) == 0
    assert shortest_distance({0:[1],1:[0],2:[]}, 0, 2) == -1
    assert shortest_distance({0:[1],1:[0,2],2:[1,3],3:[2]}, 0, 3) == 3
    assert shortest_distance({0:[1,2,3],1:[0],2:[0],3:[0]}, 0, 3) == 1
    print("All tests passed!")
