"""
SOLUTION: Validate BST (Medium)
===============================
Range propagation: each node must sit strictly inside (lo, hi);
children narrow the range. This catches violations a local
parent-child check can never see (e.g. 3 inside 5's right subtree).
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


def is_valid_bst(root, lo=float("-inf"), hi=float("inf")):
    if root is None:
        return True
    if not (lo < root.val < hi):
        return False
    return (is_valid_bst(root.left, lo, root.val)
            and is_valid_bst(root.right, root.val, hi))


if __name__ == "__main__":
    assert is_valid_bst(build_tree([2, 1, 3])) is True
    assert is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6])) is False
    assert is_valid_bst(build_tree([5, 4, 6, None, None, 3, 7])) is False
    assert is_valid_bst(None) is True
    assert is_valid_bst(build_tree([1])) is True
    assert is_valid_bst(build_tree([2, 2, 2])) is False
    assert is_valid_bst(build_tree([10, 5, 15, None, None, 6, 20])) is False
    assert is_valid_bst(build_tree([6, 2, 8, 0, 4, 7, 9])) is True
    print("All tests passed!")
