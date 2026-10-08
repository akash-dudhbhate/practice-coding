"""
SOLUTION: Component Count via Union-Find — (Medium)
==============================
n singleton sets; each successful union merges two (count -= 1).
Redundant unions are no-ops. This is the streaming version of lesson
13's flood-count — union-find handles edges one at a time in ~O(1).
"""
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, v):
        while self.parent[v] != v:
            self.parent[v] = self.parent[self.parent[v]]
            v = self.parent[v]
        return v

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True

def components_after_unions(n, unions):
    uf = UnionFind(n)
    for a, b in unions:
        uf.union(a, b)
    return uf.count

if __name__ == "__main__":
    assert components_after_unions(6, [(0,1),(1,2),(3,4)]) == 3
    assert components_after_unions(5, []) == 5
    assert components_after_unions(4, [(0,1),(2,3),(1,2)]) == 1
    assert components_after_unions(3, [(0,1)]) == 2
    assert components_after_unions(1, []) == 1
    assert components_after_unions(4, [(0,1),(0,1)]) == 3   # redundant union
    print("All tests passed!")
