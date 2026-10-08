"""
SOLUTION: Tree Traversals (Easy)
================================
The three DFS orders differ ONLY in where root.val is appended:
before children (pre), between (in), after (post).
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


def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


if __name__ == "__main__":
    t = build_tree([1, 2, 3, 4, None, 5, 6])
    assert inorder(t) == [4, 2, 1, 5, 3, 6]
    assert preorder(t) == [1, 2, 4, 3, 5, 6]
    assert postorder(t) == [4, 2, 5, 6, 3, 1]
    assert inorder(None) == [] and preorder(None) == [] and postorder(None) == []
    vine = build_tree([1, None, 2, None, 3])
    assert inorder(vine) == [1, 2, 3]
    assert postorder(vine) == [3, 2, 1]
    print("All tests passed!")
