"""
SOLUTION: Course Schedule — (Medium)
==============================
(a,b) = "a needs b" = edge b -> a. "Can finish all" = "graph is a
DAG". Kahn's count: emit indegree-0 courses; if all n emitted, acyclic.
"""
from collections import deque

def can_finish(num_courses, prereqs):
    adj = {v: [] for v in range(num_courses)}
    indeg = [0] * num_courses
    for a, b in prereqs:            # b -> a  (b must come first)
        adj[b].append(a)
        indeg[a] += 1
    q = deque(v for v in range(num_courses) if indeg[v] == 0)
    emitted = 0
    while q:
        emitted += 1
        for nxt in adj[q.popleft()]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return emitted == num_courses

if __name__ == "__main__":
    assert can_finish(2, [(1,0)]) is True
    assert can_finish(2, [(1,0),(0,1)]) is False
    assert can_finish(4, [(1,0),(2,1),(3,2)]) is True
    assert can_finish(1, []) is True
    assert can_finish(3, [(0,1),(1,2),(2,0)]) is False
    assert can_finish(5, [(1,0),(2,0),(3,1),(4,3)]) is True
    print("All tests passed!")
