"""
SOLUTION: Serialize / Deserialize (Hard)
========================================
Level-order with an explicit "N" marker for missing children —
structure is preserved because every slot is accounted for.
serialize uses BFS over node-or-None slots; deserialize replays the
same queue discipline to rebuild (exactly how build_tree works).
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


def tree_to_list(root):
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


def serialize(root):
    """Level-order encoding; 'N' records a missing child."""
    if root is None:
        return ""
    parts, q = [], deque([root])
    while q:
        node = q.popleft()
        if node is None:
            parts.append("N")
        else:
            parts.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
    while parts and parts[-1] == "N":   # trailing Ns carry no info
        parts.pop()
    return ",".join(parts)


def deserialize(data):
    if not data:
        return None
    vals = [None if tok == "N" else int(tok) for tok in data.split(",")]
    return build_tree(vals)             # same slot-by-slot rebuild


if __name__ == "__main__":
    t = build_tree([1, 2, 3, None, None, 4, 5])
    s = serialize(t)
    assert isinstance(s, str)
    assert tree_to_list(deserialize(s)) == [1, 2, 3, None, None, 4, 5]
    assert deserialize(serialize(None)) is None
    assert tree_to_list(deserialize(serialize(build_tree([42])))) == [42]
    vine = build_tree([1, None, 2, None, 3])
    assert tree_to_list(deserialize(serialize(vine))) == [1, None, 2, None, 3]
    big = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert tree_to_list(deserialize(serialize(big))) == [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    print("All tests passed!")
