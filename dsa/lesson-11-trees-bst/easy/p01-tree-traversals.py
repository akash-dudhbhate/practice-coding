"""
LESSON 11 — Trees & BSTs
EASY P01 — Tree Traversals
============================================

CONCEPT:
  DFS has three flavors; the code is IDENTICAL except for where
  `visit(root)` sits relative to the two recursive calls:
    preorder  = visit, left, right      (root FIRST  — copy order)
    inorder   = left, visit, right      (root MIDDLE — sorted on a BST)
    postorder = left, right, visit      (root LAST   — delete order)

PROBLEM:
  Write three functions `inorder(root)`, `preorder(root)`,
  `postorder(root)` — each returns a list of node values in that
  order. Empty tree -> [].

TRY THIS INPUT:
  ```python
  t = build_tree([1, 2, 3, 4, None, 5, 6])
  #        1
  #       / \
  #      2   3
  #     /   / \
  #    4   5   6
  print(inorder(t))
  print(preorder(t))
  print(postorder(t))
  print(inorder(None))
  ```

EXPECTED OUTPUT:
  ```
  [4, 2, 1, 5, 3, 6]
  [1, 2, 4, 3, 5, 6]
  [4, 2, 5, 6, 3, 1]
  []
  ```

CHECK: python3 check.py easy/p01
"""

# === GIVEN HELPERS — do not edit ===
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals):
    """Level-order list -> TreeNode. None marks a missing child."""
    if not vals:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


def tree_to_list(root):
    """TreeNode -> level-order list (inverse of build_tree)."""
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


# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
