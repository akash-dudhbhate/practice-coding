"""
LESSON 11 — Trees & BSTs
HARD P03 — Diameter of a Tree
============================================

CONCEPT:
  The diameter is the longest path between ANY two nodes, in edges —
  and it may not pass through the root. Every node is a candidate
  "top of the path": path_through(node) = height(left) + height(right).
  The recursion must do TWO jobs: RETURN height (what the parent
  needs to combine) and update a nonlocal best with left_h + right_h
  (the real answer). Mixing those channels is THE bug of this problem.

PROBLEM:
  Write `diameter(root) -> int` — edges on the longest path.
  Empty tree -> 0, single node -> 0.

TRY THIS INPUT:
  ```python
  print(diameter(build_tree([1, 2, 3, 4, 5])))
  #        1         longest path: 4-2-1-3 or 5-2-1-3
  #       / \
  #      2   3
  #     / \
  #    4   5
  print(diameter(build_tree([1, 2])))
  print(diameter(None))
  print(diameter(build_tree(
      [1, 2, 3, 4, 5, None, None, 6, None, None, 7, 8, None, None, 9])))
  #            1
  #           / \
  #          2   3
  #         / \
  #        4   5
  #       /     \
  #      6       7
  #     /         \
  #    8           9
  # longest path 8-6-4-2-5-7-9 = 6 edges — never visits node 1!
  ```

EXPECTED OUTPUT:
  ```
  3
  1
  0
  6
  ```

CHECK: python3 check.py hard/p03
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
