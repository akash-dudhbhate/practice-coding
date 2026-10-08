"""
SOLUTION: Count Nodes (Easy)
============================
Same skeleton as max_depth, different combine: a node's subtree size
is 1 (itself) + left size + right size. Adds BOTH children instead
of taking the max.
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


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


if __name__ == "__main__":
    assert count_nodes(build_tree([3, 9, 20, None, None, 15, 7])) == 5
    assert count_nodes(None) == 0
    assert count_nodes(build_tree([1])) == 1
    assert count_nodes(build_tree([1, 2, 3, 4, 5, 6, 7])) == 7
    assert count_nodes(build_tree([1, None, 2, None, 3])) == 3
    print("All tests passed!")
