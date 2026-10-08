"""
LESSON 11 — Trees & BSTs
EASY P02 — Max Depth
============================================

CONCEPT:
  The recursion skeleton: what does the function RETURN for a
  subtree, and how does a parent combine the children's answers?
  Here each node reports its subtree's HEIGHT:
      height(node) = 1 + max(height(left), height(right))
  Empty subtree reports 0 — that's the base case.

PROBLEM:
  Write a function `max_depth(root) -> int` that returns the height
  of the tree: the number of nodes on the longest root-to-leaf
  path. Empty tree -> 0, single node -> 1.

TRY THIS INPUT:
  ```python
  print(max_depth(build_tree([3, 9, 20, None, None, 15, 7])))
  print(max_depth(None))
  print(max_depth(build_tree([1])))
  print(max_depth(build_tree([1, 2, None, 3, None, 4])))
  ```

EXPECTED OUTPUT:
  ```
  3
  0
  1
  4
  ```

CHECK: python3 check.py easy/p02
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
