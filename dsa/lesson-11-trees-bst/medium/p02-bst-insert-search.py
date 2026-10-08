"""
LESSON 11 — Trees & BSTs
MEDIUM P02 — BST Insert + Search
============================================

CONCEPT:
  BST rule: for every node, left subtree < node < right subtree.
  Both operations ride the same GUIDED DESCENT — at each node ask
  "is val smaller (go left) or bigger (go right)?" and descend ONE
  side. For insert, when you fall off the tree (hit None) that's
  the slot — but you must RETURN the new node so the parent can
  attach it: `root.left = insert_bst(root.left, val)`.

PROBLEM:
  Write `insert_bst(root, val)` — inserts val per BST rules,
  returns the (possibly new) subtree root. Assume no duplicate vals.
  Write `search_bst(root, val)` — returns True/False.
  Each should touch only O(height) nodes.

TRY THIS INPUT:
  ```python
  root = None
  for v in [5, 3, 7, 1, 4]:
      root = insert_bst(root, v)
  print(tree_to_list(root))
  print(search_bst(root, 4))
  print(search_bst(root, 6))
  print(tree_to_list(insert_bst(root, 6)))
  ```

EXPECTED OUTPUT:
  ```
  [5, 3, 7, 1, 4]
  True
  False
  [5, 3, 7, 1, 4, 6]
  ```

CHECK: python3 check.py medium/p02
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
