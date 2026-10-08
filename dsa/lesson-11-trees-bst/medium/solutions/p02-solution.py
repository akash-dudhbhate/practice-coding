"""
SOLUTION: BST Insert + Search (Medium)
======================================
Guided descent: compare once, go one side. For insert, the returned
subtree root is caught by the parent — that's how a new node attached
at a None slot actually links into the tree.
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


def tree_to_list(root):
    if root is None:
        return []
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def insert_bst(root, val):
    if root is None:
        return TreeNode(val)             # fell off the tree: the slot
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root


def search_bst(root, val):
    if root is None:
        return False
    if val == root.val:
        return True
    return search_bst(root.left if val < root.val else root.right, val)


if __name__ == "__main__":
    root = None
    for v in [5, 3, 7, 1, 4]:
        root = insert_bst(root, v)
    assert tree_to_list(root) == [5, 3, 7, 1, 4]
    assert search_bst(root, 4) is True
    assert search_bst(root, 6) is False
    assert search_bst(root, 5) is True
    assert tree_to_list(insert_bst(root, 6)) == [5, 3, 7, 1, 4, 6]
    assert search_bst(root, 6) is True
    print("All tests passed!")
