"""
SOLUTION: Rotting Oranges — (Hard)
==============================
Multi-source BFS: ALL rotten cells enter the queue at level 0. Process
level-by-level (queue length snapshot per round) so `minutes` counts
rounds, not cells. Count fresh upfront; each rots decrements it. Leftover
fresh after BFS => -1. O(R·C) time and space.
"""
from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    while q and fresh > 0:
        for _ in range(len(q)):          # one round = one minute
            cr, cc = q.popleft()
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2     # mark rotten at enqueue time
                    fresh -= 1
                    q.append((nr, nc))
        minutes += 1
    return minutes if fresh == 0 else -1

if __name__ == "__main__":
    assert oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert oranges_rotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
    assert oranges_rotting([[0,2]]) == 0
    assert oranges_rotting([[1]]) == -1
    assert oranges_rotting([[2]]) == 0
    assert oranges_rotting([[2,1,1],[1,1,1],[0,1,2]]) == 2
    print("All tests passed!")
