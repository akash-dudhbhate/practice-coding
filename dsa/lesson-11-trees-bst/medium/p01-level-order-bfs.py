"""
LESSON 11 — Trees & BSTs
MEDIUM P01 — Level-Order BFS
============================================

CONCEPT:
  BFS visits the tree floor by floor using a QUEUE (FIFO), not a
  stack. The key move: inside `while q`, snapshot `len(q)` BEFORE
  the inner loop — that count is exactly "how many nodes belong to
  this level." Children enqueued during the loop belong to the NEXT
  level and must not leak into the current one.

PROBLEM:
  Write a function `level_order(root) -> list[list[int]]` that
  returns the values level by level, left to right.
  Empty tree -> [].

TRY THIS INPUT:
  ```python
  print(level_order(build_tree([3, 9, 20, None, None, 15, 7])))
  print(level_order(None))
  print(level_order(build_tree([1, 2, None, 3, None, 4])))
  ```

EXPECTED OUTPUT:
  ```
  [[3], [9, 20], [15, 7]]
  []
  [[1], [2], [3], [4]]
  ```

CHECK: python3 check.py medium/p01
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
