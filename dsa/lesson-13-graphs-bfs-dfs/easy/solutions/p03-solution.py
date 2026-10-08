"""
SOLUTION: DFS Traversal Order — (Easy)
==============================
Recursive preorder: record the vertex on entry, then recurse into its
neighbors in stored order. The call stack does the backtracking for
free. `seen` is the termination condition on cyclic graphs.
"""
def dfs_order(adj, start):
    out, seen = [], set()
    def helper(v):
        seen.add(v)
        out.append(v)
        for nxt in adj[v]:
            if nxt not in seen:
                helper(nxt)
    helper(start)
    return out

if __name__ == "__main__":
    adj = {0:[1,2], 1:[0,3], 2:[0,4,5], 3:[1], 4:[2], 5:[2]}
    assert dfs_order(adj, 0) == [0, 1, 3, 2, 4, 5]
    assert dfs_order({0:[]}, 0) == [0]
    assert dfs_order({0:[1], 1:[0], 2:[]}, 0) == [0, 1]   # disconnected
    assert dfs_order({0:[1], 1:[0,2], 2:[1]}, 0) == [0, 1, 2]
    print("All tests passed!")
