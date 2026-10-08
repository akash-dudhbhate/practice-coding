"""
SOLUTION: Diameter of a Tree (Hard)
===================================
Two channels, kept straight:
  - h() RETURNS height: 1 + max(left, right) — what the parent needs
  - best (nonlocal) is UPDATED with left + right — the candidate
    longest path whose top is this node. Answer may live in a subtree.
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


def diameter(root):
    best = 0

    def h(node):
        nonlocal best
        if node is None:
            return 0
        left = h(node.left)
        right = h(node.right)
        best = max(best, left + right)   # path THROUGH this node (edges)
        return 1 + max(left, right)      # height for the parent

    h(root)
    return best


if __name__ == "__main__":
    assert diameter(build_tree([1, 2, 3, 4, 5])) == 3
    assert diameter(build_tree([1, 2])) == 1
    assert diameter(None) == 0
    assert diameter(build_tree([1])) == 0
    # longest path avoids the root entirely: 8-6-4-2-5-7-9
    tricky = build_tree([1, 2, 3, 4, 5, None, None, 6, None, None, 7,
                         8, None, None, 9])
    assert diameter(tricky) == 6
    assert diameter(build_tree([1, 2, 3, 4, 5, 6, 7])) == 4
    print("All tests passed!")
