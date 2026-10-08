"""
SOLUTION: Word Search (Hard)
==============================
From every matching start cell, DFS the 4 neighbors for the next char.
Mark visited by overwriting the cell with "#", RESTORE it after the
call returns — the purest choose/explore/unchoose. Out-of-bounds and
mismatch prune instantly.
"""
def exist(board: list, word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(r, c, k):
        if k == len(word):
            return True                        # spelled the whole word
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[k]:
            return False
        saved = board[r][c]                    # choose: mark visited
        board[r][c] = "#"
        found = (dfs(r + 1, c, k + 1) or dfs(r - 1, c, k + 1) or
                 dfs(r, c + 1, k + 1) or dfs(r, c - 1, k + 1))
        board[r][c] = saved                    # unchoose: restore
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

if __name__ == "__main__":
    b = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert exist(b, "ABCCED") is True
    assert exist(b, "SEE") is True
    assert exist(b, "ABCB") is False
    assert exist([["a"]], "a") is True
    assert exist([["a"]], "b") is False
    assert exist([["a", "a"]], "aa") is True
    assert exist([["a"]], "aa") is False
    print("All tests passed!")
