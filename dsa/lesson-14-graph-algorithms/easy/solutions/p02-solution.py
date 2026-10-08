"""
SOLUTION: Topological Sort a Small DAG — (Easy)
==============================
DFS postorder: a vertex is appended when it FINISHES (after everything
it points to). Reversed postorder = topo order. The 3-color state
doubles as a cycle detector: revisiting a 'visiting' vertex => cycle.
"""
def topo_order(n, edges):
    adj = {v: [] for v in range(n)}
    for a, b in edges:
        adj[a].append(b)
    state = [0] * n          # 0 unseen, 1 visiting, 2 done
    order = []
    cyclic = False
    import sys
    sys.setrecursionlimit(10000)

    def dfs(v):
        nonlocal cyclic
        state[v] = 1
        for nxt in adj[v]:
            if state[nxt] == 1:
                cyclic = True
                return
            if state[nxt] == 0:
                dfs(nxt)
                if cyclic:
                    return
        state[v] = 2
        order.append(v)

    for v in range(n):
        if state[v] == 0:
            dfs(v)
            if cyclic:
                return []
    return order[::-1]

if __name__ == "__main__":
    def valid(order, n, edges):
        if order == [] and n > 0:
            return False
        pos = {v: i for i, v in enumerate(order)}
        return (sorted(order) == list(range(n))
                and all(pos[a] < pos[b] for a, b in edges))
    assert valid(topo_order(4, [(0,1),(1,2),(2,3)]), 4, [(0,1),(1,2),(2,3)])
    assert valid(topo_order(3, [(0,1),(0,2)]), 3, [(0,1),(0,2)])
    assert topo_order(3, [(0,1),(1,0)]) == []
    assert valid(topo_order(2, []), 2, [])
    assert valid(topo_order(4, [(0,1),(0,2),(1,3),(2,3)]), 4,
                 [(0,1),(0,2),(1,3),(2,3)])
    print("All tests passed!")
