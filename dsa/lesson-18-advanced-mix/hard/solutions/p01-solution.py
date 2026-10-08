"""
SOLUTION: Word Search II — Trie-accelerated (Hard)
==================================================
Build a trie of the word list (store the word at each leaf under '#').
DFS from every cell, walking trie nodes: if the path isn't a prefix of
any word, the branch dies instantly. Mark cells '.' while visited and
restore on backtrack. Delete found words from the trie to dedupe.
"""
def find_words(board, words):
    if not board or not board[0] or not words:
        return []

    trie = {}
    for w in words:
        node = trie
        for c in w:
            node = node.setdefault(c, {})
        node['#'] = w                        # leaf marker carries the word

    rows, cols = len(board), len(board[0])
    found = []

    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node:
            return                           # dead prefix — prune
        nxt = node[ch]
        if '#' in nxt:
            found.append(nxt['#'])
            del nxt['#']                     # report each word once
        board[r][c] = '.'                    # mark visited
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '.':
                dfs(nr, nc, nxt)
        board[r][c] = ch                     # restore — other paths need it

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie)
    return sorted(found)

if __name__ == "__main__":
    board = [["o","a","a","n"],
             ["e","t","a","e"],
             ["i","h","k","r"],
             ["i","f","l","v"]]
    assert find_words(board, ["oath","pea","eat","rain"]) == ["eat","oath"]
    assert find_words([["a","b"],["c","d"]], ["abcb"]) == []      # no cell reuse
    assert find_words([["a"]], ["a"]) == ["a"]
    assert find_words([["a","b"],["c","d"]], ["ab","ba","cd","abd"]) == ["ab","abd","ba","cd"]
    assert find_words([["a","a"],["a","a"]], ["aaaa"]) == ["aaaa"]
    print("All tests passed!")
