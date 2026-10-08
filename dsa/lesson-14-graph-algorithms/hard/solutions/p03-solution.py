"""
SOLUTION: Redundant Connection — (Hard)
==============================
Tree + 1 extra edge = exactly one cycle. Feed edges to union-find in
input order; the first union that FAILS (roots already equal) is the
edge closing the cycle — return it. Vertices 1-indexed => size n+1.
"""
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, v):
        while self.parent[v] != v:
            self.parent[v] = self.parent[self.parent[v]]
            v = self.parent[v]
        return v

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False                 # already connected: this edge cycles
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

def find_redundant_connection(edges):
    uf = UnionFind(len(edges) + 1)       # vertices are 1..n
    for a, b in edges:
        if not uf.union(a, b):
            return [a, b]

if __name__ == "__main__":
    assert find_redundant_connection([(1,2),(1,3),(2,3)]) == [2, 3]
    assert find_redundant_connection([(1,2),(2,3),(3,4),(1,4),(1,5)]) == [1, 4]
    assert find_redundant_connection([(1,2),(2,3),(3,1)]) == [3, 1]
    assert find_redundant_connection([(1,2),(2,3),(2,4),(3,4)]) == [3, 4]
    print("All tests passed!")
