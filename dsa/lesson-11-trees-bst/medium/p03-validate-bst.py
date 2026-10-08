"""
LESSON 11 — Trees & BSTs
MEDIUM P03 — Validate BST
============================================

CONCEPT:
  Checking "left child < node < right child" locally is NOT enough:
  a node deep in a right subtree must be larger than EVERY ancestor
  it passed on the left, not just its parent. Carry the allowed
  (lo, hi) range down: a node must sit strictly inside it; the left
  child inherits (lo, node.val), the right child (node.val, hi).

PROBLEM:
  Write a function `is_valid_bst(root) -> bool`. Strict ordering —
  no equal values allowed. Empty tree -> True.

TRY THIS INPUT:
  ```python
  print(is_valid_bst(build_tree([2, 1, 3])))
  print(is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6])))
  print(is_valid_bst(build_tree([5, 4, 6, None, None, 3, 7])))
  #        5
  #       / \
  #      4   6     <- 3 is in 5's RIGHT subtree but 3 < 5!
  #         / \
  #        3   7     local checks all pass; global range fails
  print(is_valid_bst(None))
  ```

EXPECTED OUTPUT:
  ```
  True
  False
  False
  True
  ```

CHECK: python3 check.py medium/p03
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
