"""
LESSON 11 — Trees & BSTs
EASY P03 — Count Nodes
============================================

CONCEPT:
  Same recursion skeleton as max_depth, different combine step.
  Each node reports its subtree's SIZE:
      size(node) = 1 + size(left) + size(right)
  Instead of max() you add — the node counts itself plus BOTH
  subtrees. Skeleton first, combine second.

PROBLEM:
  Write a function `count_nodes(root) -> int` that returns the
  total number of nodes in the tree. Empty tree -> 0.

TRY THIS INPUT:
  ```python
  print(count_nodes(build_tree([3, 9, 20, None, None, 15, 7])))
  print(count_nodes(None))
  print(count_nodes(build_tree([1, 2, 3, 4, 5, 6, 7])))
  ```

EXPECTED OUTPUT:
  ```
  5
  0
  7
  ```

CHECK: python3 check.py easy/p03
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
