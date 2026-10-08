"""
LESSON 11 — Trees & BSTs
HARD P02 — Serialize / Deserialize
============================================

CONCEPT:
  Serialize = flatten a tree to a string; deserialize = rebuild it.
  The trap: a bare list of values can't encode STRUCTURE — "1,2,3"
  could be a balanced tree or a right-leaning vine. You must record
  WHERE children are missing. Classic scheme: level-order (or
  preorder) writing a marker like "N" for None, so positions are
  unambiguous.

PROBLEM:
  Write `serialize(root) -> str` and `deserialize(data) -> TreeNode`
  such that deserialize(serialize(t)) rebuilds an identical tree —
  checked by `tree_to_list(...) == tree_to_list(t)`. Must handle the
  empty tree and single nodes. Format is your choice.

TRY THIS INPUT:
  ```python
  t = build_tree([1, 2, 3, None, None, 4, 5])
  s = serialize(t)
  print(type(s) == str)
  print(tree_to_list(deserialize(s)))
  print(deserialize(serialize(None)))
  print(tree_to_list(deserialize(serialize(build_tree([42])))))
  ```

EXPECTED OUTPUT:
  ```
  True
  [1, 2, 3, None, None, 4, 5]
  None
  [42]
  ```

CHECK: python3 check.py hard/p02
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
