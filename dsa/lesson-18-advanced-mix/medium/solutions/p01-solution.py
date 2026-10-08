"""
SOLUTION: Implement Trie (Medium)
=================================
Node = dict of children + is_end flag. insert walks/creates per char;
search needs path + is_end; startsWith needs only the path.
O(len(word)) per operation.
"""
class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        node = self
        for c in word:
            node = node.children.setdefault(c, Trie())
        node.is_end = True

    def _walk(self, s):
        """Return the node at the end of the path, or None if it dies."""
        node = self
        for c in s:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def search(self, word):
        node = self._walk(word)
        return node is not None and node.is_end

    def startsWith(self, prefix):
        return self._walk(prefix) is not None

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True
    trie.insert("app")
    assert trie.search("app") == True
    assert trie.search("apples") == False
    assert trie.startsWith("apples") == False
    trie.insert("application")
    assert trie.startsWith("appli") == True
    assert trie.search("appli") == False
    print("All tests passed!")
