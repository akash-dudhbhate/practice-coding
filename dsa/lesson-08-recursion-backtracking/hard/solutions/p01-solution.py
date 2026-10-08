"""
SOLUTION: N-Queens (Hard)
==============================
One queen per row = recursion depth is the row. Conflict pruning via
three sets: cols, d1 (r - c constant on \ diagonals), d2 (r + c constant
on / diagonals). Choose: place + mark all three; unchoose: restore.
"""
def solve_n_queens(n: int) -> list:
    out = []
    cols, d1, d2 = set(), set(), set()
    queens = [-1] * n              # queens[r] = column of row r's queen

    def dfs(r):
        if r == n:
            out.append(["." * c + "Q" + "." * (n - c - 1) for c in queens])
            return
        for c in range(n):
            if c in cols or (r - c) in d1 or (r + c) in d2:
                continue                       # conflicts -> skip
            queens[r] = c                      # choose
            cols.add(c); d1.add(r - c); d2.add(r + c)
            dfs(r + 1)                         # explore next row
            cols.discard(c); d1.discard(r - c); d2.discard(r + c)  # unchoose

    dfs(0)
    return out

if __name__ == "__main__":
    boards4 = {tuple(b) for b in solve_n_queens(4)}
    assert boards4 == {
        (".Q..", "...Q", "Q...", "..Q."),
        ("..Q.", "Q...", "...Q", ".Q.."),
    }
    assert solve_n_queens(1) == [["Q"]]
    assert solve_n_queens(2) == []
    assert len(solve_n_queens(5)) == 10
    print("All tests passed!")
