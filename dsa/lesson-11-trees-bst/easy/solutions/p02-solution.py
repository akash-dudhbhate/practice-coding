"""
SOLUTION: Max Depth (Easy)
==========================
Each node reports its subtree's height: 1 + max(children's heights).
Empty subtree reports 0 — the base case the recursion stands on.
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


def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
    assert max_depth(build_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert max_depth(None) == 0
    assert max_depth(build_tree([1])) == 1
    assert max_depth(build_tree([1, 2, None, 3, None, 4])) == 4
    assert max_depth(build_tree([1, 2, 3, 4, 5, 6, 7])) == 3
    print("All tests passed!")
