# 02 — A Binary Tree in Code

> 5-minute read. The picture becomes Python.

## The idea, plain words

"Binary" just means at most two children, named `left` and `right`.
A node is a tiny object with three slots — value, left, right:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

And here's our tree — the SAME tree from chapter 01 — built in one
expression:

```python
root = TreeNode(4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(6, TreeNode(5), TreeNode(7)))

print(root.left.right.val)   # 3 — root's left child's right child
print(root.right.left.val)   # 5
```

Read `TreeNode(2, TreeNode(1), TreeNode(3))` as "a 2 whose children are
leaf-1 and leaf-3." **The nesting IS the drawing** — tilt the code
sideways and you see the diagram.

## The helpers every problem file gives you

In `easy/` → `hard/` you never build nodes by hand. Each file ships:

```python
build_tree([4, 2, 6, 1, 3, 5, 7])   # list -> tree, level by level
tree_to_list(root)                   # tree -> the same list back
```

The list is the diagram flattened **floor by floor**: root first, then
the depth-1 row left-to-right, then the depth-2 row. `None` marks a
missing child: `[3, 9, 20, None, None, 15, 7]` means "9 has no
children; 20's children are 15 and 7."

## Why trees beat flat storage for hierarchy

You *could* store a hierarchy as flat `(id, parent_id)` pairs — SQL
tables do exactly that. But then "show me everything under X" means
scanning the whole table for X's kids, then re-scanning for each kid's
kids… O(n) per level. With real node links it's one walk: **each node
holds arrows straight to its children.** The tree spends memory on
links so hierarchy questions are answered by following arrows, not
searching.

## Common mistake

Thinking `[4, 2, 6, 1, 3, 5, 7]` "is" the tree. It's just a convenient
*serialization* — the tree written in one line. The real tree is
objects pointing at objects.

## Your turn

What list would you feed `build_tree` to make a root 4 with only a
left child 2 (no right child)?

<details><summary>Answer</summary>
`[4, 2, None]` — the depth-1 row is "left = 2, right = missing."
(`[4, 2]` works too — trailing Nones get omitted.)
</details>

---

**← Prev** [01 — What is a tree?](01-what-is-a-tree.md) ·
**Next →** [03 — Three DFS orders](03-dfs-three-orders.md)
