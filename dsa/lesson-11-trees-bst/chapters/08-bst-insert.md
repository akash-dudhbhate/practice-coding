# 08 — BST Insert: Walk Down, Plug In

> 5-minute read. Search that loses — then builds a rung where it fell.

## The idea, plain words

Insert IS search that fails to find. Walk down exactly like
`search_bst`; when you fall off the tree (hit `None`), that empty slot
is *precisely* where the new value belongs — the rule forced your
whole path, so attaching there keeps the tree a BST.

**Insert 8 into our tree:**

```
        4                        4
       / \                      / \
      2   6     insert 8 →     2   6
     / \ / \                  / \ / \
    1  3 5  7                1  3 5  7
                                        \
                                         8
```

Path: 8>4 right, 8>6 right, 8>7 right → `None` → attach as 7's right
child. New values in a BST always land at the bottom — **every insert
births a leaf.**

## In code — and the line everyone drops

```python
def insert_bst(root, val):
    if root is None:
        return TreeNode(val)                    # the empty slot: build it
    if val < root.val:
        root.left = insert_bst(root.left, val)  # hand the new subtree UP
    else:
        root.right = insert_bst(root.right, val)
    return root                                 # parent re-links to me
```

Two load-bearing details:

- `return TreeNode(val)` — the new node is *returned* so the parent
  call can attach it.
- `root.left = insert_bst(...)` — the assignment **re-wires** the
  (possibly brand-new) subtree back onto the parent. Without it the
  new node is created and immediately orphaned.

Quick check — insert 8, then print inorder (ch. 10 explains why this
comes out sorted):

```python
root = insert_bst(root, 8)
print(inorder(root))      # [1, 2, 3, 4, 5, 6, 7, 8] — still sorted!
```

## Why it exists

This is the "mutating sorted data cheaply" promise: no shifting n
elements like a sorted array — just O(h) walking plus one pointer
assignment. Build a whole BST from scratch the same way:

```python
root = None
for v in [4, 2, 6, 1, 3, 5, 7]:
    root = insert_bst(root, v)      # caller always re-takes the root
```

## Where it's used

`std::map::insert`, database index maintenance, any "add to sorted
collection" operation.

## Common mistake

```python
# WRONG — the new node never attaches
if val < root.val:
    insert_bst(root.left, val)     # returned subtree dropped on the floor
```

The recursion RETURNS the subtree it built; catching it with `=` is
the whole job. Same contract at the top: `root = insert_bst(root, v)`.

## Your turn

After inserting 8 into our tree, insert 9. Where does it land — and
what does the tree's right edge look like now?

<details><summary>Answer</summary>
Path: 9>4 → right, 9>6 → right, 9>7 → right, 9>8 → right → lands as
8's right child. The right edge is now a vine: 4→6→7→8→9, four nodes
in a straight line. (Chapter 11: keep doing this and your "tree"
becomes a linked list.)
</details>

---

**← Prev** [07 — BST search](07-bst-search.md) ·
**Next →** [09 — BST delete](09-bst-delete.md)
