"""
LESSON 11 — Trees & BSTs
HARD P01 — Lowest Common Ancestor in a BST
============================================

CONCEPT:
  LCA = deepest node that is an ancestor of both p and q. In a
  GENERIC tree you'd search both subtrees. But a BST's ordering
  makes it a guided walk: if both targets are smaller than root the
  LCA is left; both bigger -> right; otherwise root IS the split
  point (p on one side, q on the other — or root equals one of
  them, since a node is its own ancestor).

PROBLEM:
  Write `lca_bst(root, p, q)` — returns the TreeNode that is the
  lowest common ancestor of the nodes holding values p and q.
  Both values are guaranteed present. O(height), single path.

TRY THIS INPUT:
  ```python
  root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
  #            6
  #           / \
  #          2   8
  #         / \ / \
  #        0  4 7  9
  #          / \
  #         3   5
  print(lca_bst(root, 2, 8).val)
  print(lca_bst(root, 2, 4).val)
  print(lca_bst(root, 3, 5).val)
  print(lca_bst(root, 7, 9).val)
  ```

EXPECTED OUTPUT:
  ```
  6
  2
  4
  8
  ```

CHECK: python3 check.py hard/p01
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
