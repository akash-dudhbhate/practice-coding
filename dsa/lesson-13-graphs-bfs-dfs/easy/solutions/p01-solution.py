"""
SOLUTION: Build an Adjacency List — (Easy)
==============================
Seed all n vertices first so isolated ones still appear, then append
each undirected edge BOTH ways. O(n + E) time and space.
"""
def build_adjacency(n, edges):
    adj = {v: [] for v in range(n)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    return adj

if __name__ == "__main__":
    assert build_adjacency(4, [(0,1),(0,2),(1,3)]) == {0:[1,2], 1:[0,3], 2:[0], 3:[1]}
    assert build_adjacency(3, []) == {0:[], 1:[], 2:[]}
    assert build_adjacency(2, [(0,1)]) == {0:[1], 1:[0]}
    assert build_adjacency(5, [(1,2)]) == {0:[], 1:[2], 2:[1], 3:[], 4:[]}
    assert build_adjacency(1, []) == {0:[]}
    print("All tests passed!")
