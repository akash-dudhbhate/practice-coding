"""
SOLUTION: Union-Find Basics — (Easy)
==============================
parent[] trees pointing at roots. find() path-compresses (halving hops
at each step); union() attaches the lower-rank root under the higher.
The ra == rb early return is load-bearing: it detects redundant unions
and protects count.
"""
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self._count = n

    def find(self, v):
        while self.parent[v] != v:
            self.parent[v] = self.parent[self.parent[v]]  # path halving
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
        self._count -= 1
        return True

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def count(self):
        return self._count

if __name__ == "__main__":
    uf = UnionFind(5)
    assert uf.count() == 5
    assert uf.same(0, 1) is False
    assert uf.union(0, 1) is True
    assert uf.same(0, 1) is True
    assert uf.same(0, 2) is False
    assert uf.count() == 4
    assert uf.union(0, 1) is False          # already merged — no-op
    assert uf.count() == 4
    assert uf.union(2, 3) is True
    assert uf.union(1, 3) is True
    assert uf.same(0, 2) is True            # transitive
    assert uf.count() == 2
    assert uf.same(0, 4) is False
    print("All tests passed!")
