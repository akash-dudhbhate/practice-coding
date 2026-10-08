"""
SOLUTION: LCA in a BST (Hard)
=============================
Guided walk: both targets smaller -> LCA is left; both bigger ->
right; otherwise this node is the split point (one on each side, or
the node IS one of the targets — a node is its own ancestor).
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    q, i = deque([root]), 1
    while q and i < len(vals):
        node = q.popleft()
        if vals[i] is not None:
            node.left = TreeNode(vals[i]); q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i]); q.append(node.right)
        i += 1
    return root


def lca_bst(root, p, q):
    while root is not None:
        if p < root.val and q < root.val:
            root = root.left            # both targets on the left
        elif p > root.val and q > root.val:
            root = root.right           # both targets on the right
        else:
            return root                 # split point (or root IS p/q)
    return None


if __name__ == "__main__":
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert lca_bst(root, 2, 8).val == 6
    assert lca_bst(root, 2, 4).val == 2     # node is its own ancestor
    assert lca_bst(root, 3, 5).val == 4
    assert lca_bst(root, 7, 9).val == 8
    assert lca_bst(root, 0, 5).val == 2
    assert lca_bst(root, 6, 9).val == 6     # root is an ancestor
    print("All tests passed!")
