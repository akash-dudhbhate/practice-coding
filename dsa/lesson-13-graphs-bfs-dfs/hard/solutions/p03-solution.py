"""
SOLUTION: Clone a Graph — (Hard)
==============================
orig->clone dict is memo + visited set in one: create the clone BEFORE
recursing into neighbors, so cycles terminate and shared neighbors map
to ONE clone (not duplicates). Works with any node class exposing
.val / .neighbors — we only read them.
"""
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):
    if node is None:
        return None
    mapping = {}
    def dfs(orig):
        if orig in mapping:
            return mapping[orig]
        copy = Node(orig.val)
        mapping[orig] = copy                       # memoize FIRST
        copy.neighbors = [dfs(n) for n in orig.neighbors]
        return copy
    return dfs(node)

# --- test plumbing ---
def build_graph(adj):
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, nbrs in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in nbrs]
    return nodes[0] if nodes else None

def shape(node):
    """BFS -> sorted list of (val, sorted neighbor vals)."""
    seen, out, stack = set(), [], [node]
    while stack:
        v = stack.pop()
        if v in seen:
            continue
        seen.add(v)
        out.append((v.val, sorted(n.val for n in v.neighbors)))
        stack.extend(v.neighbors)
    return sorted(out)

if __name__ == "__main__":
    for adj in ([[2,4],[1,3],[2,4],[1,3]], [[]], [[2],[1]], [[2,3],[1,3],[1,2]]):
        orig = build_graph(adj)
        clone = clone_graph(orig)
        assert clone is not orig
        assert shape(clone) == shape(orig)
        # no object identity shared between orig and clone
        orig_nodes, seen, stack = set(), set(), [orig]
        while stack:
            v = stack.pop()
            if v in seen: continue
            seen.add(v); orig_nodes.add(id(v))
            stack.extend(v.neighbors)
        seen2, stack = set(), [clone]
        while stack:
            v = stack.pop()
            if v in seen2: continue
            seen2.add(v)
            assert id(v) not in orig_nodes
            stack.extend(v.neighbors)
    assert clone_graph(None) is None
    print("All tests passed!")
