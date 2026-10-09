# 09 — BST Delete: The Three Cases

> 7-minute read. The longest chapter — deletion has three shapes.

## The idea, plain words

Deleting is easy until the target has children who need a new home.
Three cases, in order of annoyance:

- **Case 1 — the target is a LEAF.** Just unplug it. Nothing below.
- **Case 2 — ONE child.** Splice it out like a linked-list node: the
  parent points straight to the child.
- **Case 3 — TWO children.** Both subtrees need a boss. Trick: promote
  the target's **successor** — the smallest value in its right subtree
  (`tree_min(root.right)` from ch. 06). The successor is ≥ everything
  on the left and ≤ everything on the right, so the BST rule survives.
  Copy its *value* up, then delete the successor's old spot — which is
  always case 1 or 2, because a minimum has no left child.

## All three cases on our tree

```
        4                    4                    4                5
       / \                  / \                  / \              / \
      2   6   delete 1 →   2   6   delete 2 →   3   6  delete 4→ 3   6
     / \ / \                \ / \              / \              / \
    1  3 5  7               3 5  7            5   7            5→gone
                                                           leaf; 7 stays
      leaf                  one-child          two-children:
      unplug                splice 3 up        successor 5 copied up
```

## In code

```python
def delete_bst(root, val):
    if root is None:
        return None
    if val < root.val:
        root.left = delete_bst(root.left, val)
    elif val > root.val:
        root.right = delete_bst(root.right, val)
    else:                                       # found the target
        if root.left is None:
            return root.right                   # cases 1+2: right replaces me
        if root.right is None:
            return root.left                    # case 2: left replaces me
        succ = root.right                       # case 3
        while succ.left:
            succ = succ.left                    # smallest in right subtree
        root.val = succ.val                     # promote its value
        root.right = delete_bst(root.right, succ.val)  # delete old spot
    return root
```

Same contract as insert: `root.left = delete_bst(...)` re-links the
modified subtree back up. Delete is O(h) — one walk down, one fix-up.

Verify all three cases (on a fresh copy of our tree):

```python
root = delete_bst(root, 1)    # leaf
root = delete_bst(root, 2)    # now one child
root = delete_bst(root, 4)    # two children -> successor 5 takes over
print(inorder(root))          # [3, 5, 6, 7] — still sorted, still a BST
```

## Why it exists

Real sorted data isn't append-only — leaderboard entries expire, index
rows get deleted. Delete is the surgical price of the BST's O(h)
search: remove a node while preserving the ordering rule *everywhere*.

## Common mistake

Trying to physically detach and re-attach the successor node — messy
pointer surgery. The clean trick copies only its VALUE into the
target, then recursively deletes the successor's old spot (always an
easy case). Using the *predecessor* (max of left subtree) instead is
equally valid — pick one and be consistent.

## Your turn

Starting from the ORIGINAL tree (all 7 nodes), delete root 4. What
value ends up on top, and which node gets deleted second?

<details><summary>Answer</summary>
The successor is `tree_min(6's subtree)` = **5** — copied to the root.
Then `delete_bst(root.right, 5)` removes the old leaf-5 (case 1).
Final tree: 5 on top; left subtree {1,2,3}; right subtree 6→7.
</details>

---

**← Prev** [08 — BST insert](08-bst-insert.md) ·
**Next →** [10 — Inorder = sorted](10-inorder-is-sorted.md)
