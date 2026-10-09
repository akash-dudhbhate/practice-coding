# 12 — Two Descent Tricks: LCA and Validate-BST

> 6-minute read. Carrying information DOWN the tree.

## The idea, plain words

Search showed descent answering "where is X." Two famous questions use
the same walk but carry extra info along the way.

## Trick 1 — LCA (lowest common ancestor)

The LCA of values a and b is the lowest node that is an ancestor of
BOTH — the fork where their upward paths first meet. On a BST, the
ordering finds it in one descent: walk down; both smaller → the fork
is left; both larger → right; the first node where they SPLIT (or one
equals the node) IS the LCA.

```python
def lca_bst(root, a, b):
    while root:
        if a < root.val and b < root.val:
            root = root.left            # both live below-left
        elif a > root.val and b > root.val:
            root = root.right           # both live below-right
        else:
            return root.val             # split point = the LCA
```

On our tree: `lca_bst(root, 1, 3)` → `2` (their paths fork at 2);
`lca_bst(root, 1, 7)` → `4` (only the root spans both sides).

## Trick 2 — is this actually a BST? (the famous bug)

From ch. 06 you know local checks lie. The fix: carry the allowed
**(min, max) range** down the recursion. The root may be anything
(−∞, +∞). Going LEFT lowers the ceiling to my value; going RIGHT
raises the floor.

```python
def is_bst(node, lo, hi):
    if node is None:
        return True
    if not (lo < node.val < hi):
        return False                             # outside allowed range
    return (is_bst(node.left, lo, node.val)      # left kids must be < me
        and is_bst(node.right, node.val, hi))    # right kids must be > me
```

On ch. 06's trap tree (`5` over `1` and `6`; `6` has children `3,7`):
node 6 gets range (5, +∞); its left child 3 gets (5, 6) — and 3 < 5 →
**False**. The range caught what parent-child checks couldn't.
`is_bst(our_tree, -inf, inf)` → `True`, as expected.

## Why it exists

Both tricks share one deep pattern: **each recursive step can ship
context downward** — "your legal range," "your ancestors so far."
Tree code looks local, but correctness is often about ancestors, and
the descent is your one chance to carry their influence.

## Where it's used

LCA: file systems (common parent folder), org charts ("lowest shared
manager"), version-control merge bases. Validate: anywhere BST
invariants are trusted — and the range idea generalizes to other
ordered structures.

## Common mistake — the local-check version

```python
# WRONG — passes the 5/1/6/3/7 trap tree (and crashes on None!)
ok = (node.left is None or node.left.val < node.val) and \
     (node.right is None or node.right.val > node.val)
```

Every node passes; the tree is still broken. A node's constraint comes
from EVERY ancestor — so the constraint must travel down with the
recursion.

## Your turn

On our tree: what does `lca_bst(root, 5, 7)` return — and what
`(lo, hi)` range does `is_bst` pass when it checks node 6?

<details><summary>Answer</summary>
`lca_bst(5, 7)` → `6` — the fork where 5 goes left and 7 goes right.
Node 6 is reached via `root.right`, so the floor was raised to 4:
`is_bst(6, 4, +∞)`. Its children then get (4, 6) for 5 and (6, +∞)
for 7 — both pass, correctly.
</details>

---

**← Prev** [11 — Balanced vs degenerate](11-balanced-vs-degenerate.md) ·
**Next →** [13 — Pitfall gallery](13-pitfall-gallery.md)
