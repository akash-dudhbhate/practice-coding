"""
SOLUTION: Count Connected Components — (Medium)
==============================
Loop every vertex; each unvisited one starts a new component — count
it, then flood it. The `seen` set is shared across floods, which is
exactly what makes each component counted exactly once.
"""
def count_components(n, edges):
    adj = {v: [] for v in range(n)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen, count = set(), 0
    for v in range(n):
        if v not in seen:
            count += 1
            seen.add(v)
            stack = [v]
            while stack:
                for nxt in adj[stack.pop()]:
                    if nxt not in seen:
                        seen.add(nxt)
                        stack.append(nxt)
    return count

if __name__ == "__main__":
    assert count_components(5, [(0,1),(1,2),(3,4)]) == 2
    assert count_components(4, []) == 4
    assert count_components(4, [(0,1),(2,3)]) == 2
    assert count_components(3, [(0,1),(1,2),(0,2)]) == 1
    assert count_components(1, []) == 1
    print("All tests passed!")
