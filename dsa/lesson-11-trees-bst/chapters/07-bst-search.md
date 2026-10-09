# 07 — BST Search: Guided Descent

> 5-minute read. Lesson-09's halving, wearing a tree costume.

## The idea, plain words

Binary search on `[1,2,3,4,5,6,7]`: check the middle (4), go left or
right, halve each step. A BST is that same game with the midpoints
**pre-arranged as a tree**:

```
        4            <- the "middle element"
       / \
      2   6          <- the middles of each half
     / \ / \
    1  3 5  7
```

**Search for 5 — the trace:**

- at 4: `5 > 4` → go RIGHT (the entire left subtree, eliminated)
- at 6: `5 < 6` → go LEFT
- at 5: found. **3 hops.**

**Search for 8:** 4 → right, 6 → right, 7 → right → `None` → not
there. (Remember this fall-off-the-bottom spot for chapter 08.)

Every comparison either finds the answer or discards a whole subtree —
you never scan. On a bushy tree each hop roughly halves what remains:
**O(height) = O(log n).**

## In code

```python
def search_bst(root, val):
    while root:                      # walk down till found or fall off
        if val == root.val:
            return True
        root = root.left if val < root.val else root.right
    return False                     # fell off the bottom: not here
```

(The recursive version is the same thinking:
`return search_bst(root.left if val < root.val else root.right, val)`.)

On our tree: `search_bst(root, 5)` → `True`, `search_bst(root, 8)` →
`False`. 3 hops for 7 nodes — and ~20 hops for a MILLION nodes, *if*
the tree stays bushy (chapter 11 is that asterisk).

## Why it exists

- Sorted array: O(log n) search but O(n) insert — shifting everything.
- Linked list: O(1) insert but O(n) search — scanning everything.
- Balanced BST: **O(log n) for both** — ordering stored in the
  pointers' *shape*, not contiguous memory. It's binary search you can
  mutate cheaply.

## Where it's used

Every "sorted but changing" container: `std::map`, database indexes,
leaderboards — plus LCA and kth-smallest ride this same descent.

## Common mistake

Saying search is O(log n) ALWAYS. It's **O(height)** — and height is
only log n while the tree is balanced. Feed sorted input into a plain
BST and you build a vine: O(n), identical to a list scan. Say "O(h)"
and earn respect.

## Your turn

On our tree, which nodes does `search_bst(root, 3)` touch — and what
did it skip entirely?

<details><summary>Answer</summary>
Touches 4 (go left), 2 (go right), 3 (found) — 3 nodes. It never
looked at {1, 5, 6, 7}: two whole subtrees eliminated by two
comparisons.
</details>

---

**← Prev** [06 — The BST rule](06-the-bst-rule.md) ·
**Next →** [08 — BST insert](08-bst-insert.md)
