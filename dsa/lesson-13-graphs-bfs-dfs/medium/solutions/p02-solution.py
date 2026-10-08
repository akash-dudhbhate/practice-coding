"""
SOLUTION: Number of Islands — (Medium)
==============================
Grid = implicit graph: 4-directional neighbors within bounds. Scan all
cells; each unvisited 1 is a new island — count it, then flood it with
DFS, flipping 1->0 at PUSH time (free visited set, no duplicates).
"""
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count += 1
                grid[r][c] = 0
                stack = [(r, c)]
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            stack.append((nr, nc))
    return count

if __name__ == "__main__":
    assert num_islands([[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]) == 3
    assert num_islands([[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]) == 1
    assert num_islands([[0,0],[0,0]]) == 0
    assert num_islands([[1]]) == 1
    assert num_islands([[1,0,1],[0,1,0],[1,0,1]]) == 5   # diagonals don't count
    print("All tests passed!")
