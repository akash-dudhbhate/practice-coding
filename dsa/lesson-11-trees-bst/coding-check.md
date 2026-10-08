# Lesson 11 — Coding Check

Use this to verify your solutions before asking for review.
`b()` below = `build_tree(...)` — the helper already in every file.

## Easy

### p01 — Tree traversals
- [ ] On `b([1,2,3,4,None,5,6])`: inorder `[4,2,1,5,3,6]`, preorder `[1,2,4,3,5,6]`, postorder `[4,2,5,6,3,1]`
- [ ] `inorder(None) / preorder(None) / postorder(None)` all return `[]`
- [ ] Degenerate right-line `b([1,None,2,None,3])`: inorder `[1,2,3]`, postorder `[3,2,1]`
- [ ] The ONLY difference between the three functions is where `root.val` goes relative to the two recursive calls

### p02 — Max depth
- [ ] `max_depth(b([3,9,20,None,None,15,7]))` returns `3`
- [ ] `max_depth(None)` returns `0`
- [ ] `max_depth(b([1]))` returns `1`
- [ ] `max_depth(b([1,2,None,3,None,4]))` returns `4` (degenerate = linked list, height = n)
- [ ] Combine step is `1 + max(left, right)` — not `left + right`

### p03 — Count nodes
- [ ] `count_nodes(b([3,9,20,None,None,15,7]))` returns `5`
- [ ] `count_nodes(None)` returns `0`
- [ ] `count_nodes(b([1,2,3,4,5,6,7]))` returns `7`
- [ ] Combine step is `1 + left + right` — same skeleton as p02, different combine

## Medium

### p01 — Level-order BFS
- [ ] `level_order(b([3,9,20,None,None,15,7]))` returns `[[3],[9,20],[15,7]]`
- [ ] `level_order(None)` returns `[]`
- [ ] `level_order(b([1,2,None,3,None,4]))` returns `[[1],[2],[3],[4]]`
- [ ] You snapshot `len(q)` BEFORE the inner loop — children must not leak into the current level
- [ ] You use `deque.popleft()` — `list.pop(0)` works but is O(n) per pop

### p02 — BST insert + search
- [ ] Inserting `5,3,7,1,4` into `None` gives `tree_to_list → [5,3,7,1,4]`
- [ ] Then `insert_bst(root, 6)` gives `[5,3,7,1,4,6]` (6 lands LEFT of 7, since 6 < 7)
- [ ] `search_bst(root, 4)` is `True`, `search_bst(root, 6)` is `False` before the insert
- [ ] `insert_bst` returns the subtree root AND the parent assigns it: `root.left = insert_bst(root.left, val)` — a bare recursive call orphans the new node
- [ ] `search_bst` only descends ONE side per call — if you visit both sides it's O(n), not O(h)

### p03 — Validate BST
- [ ] `is_valid_bst(b([2,1,3]))` → `True`
- [ ] `is_valid_bst(b([5,1,4,None,None,3,6]))` → `False` (4 < 5 in right subtree)
- [ ] `is_valid_bst(b([5,4,6,None,None,3,7]))` → `False` — the trap: every node passes a local check, but 3 < 5 sits in 5's right subtree
- [ ] `is_valid_bst(None)` → `True`
- [ ] `is_valid_bst(b([2,2,2]))` → `False` (no duplicates allowed — strict `<`/`>`)
- [ ] You carry `(lo, hi)` bounds down — a parent-vs-children check alone CANNOT solve this

## Hard

### p01 — LCA in a BST
- [ ] On `b([6,2,8,0,4,7,9,None,None,3,5])`: `lca_bst(root,2,8).val` → `6`
- [ ] `lca_bst(root,2,4).val` → `2` — a node is its own ancestor
- [ ] `lca_bst(root,3,5).val` → `4`
- [ ] Logic: both `< root` → go left; both `> root` → go right; else root is the split point → return it. ONE side per step, O(h).
- [ ] Did NOT use the generic binary-tree search — the BST ordering makes it a guided walk

### p02 — Serialize / deserialize
- [ ] `serialize` returns a `str`; `deserialize(str)` returns a `TreeNode`
- [ ] Round-trip: `tree_to_list(deserialize(serialize(b([1,2,3,None,None,4,5]))))` → `[1,2,3,None,None,4,5]`
- [ ] `deserialize(serialize(None))` is `None` — the empty tree survives the trip
- [ ] Single node `b([42])` round-trips
- [ ] Format is your choice, but it must record WHERE missing children are — "1,2,3" alone can't rebuild a skewed tree

### p03 — Diameter of tree
- [ ] `diameter(b([1,2,3,4,5]))` returns `3` (path `4→2→1→3`)
- [ ] `diameter(b([1,2]))` returns `1`, `diameter(None)` returns `0`
- [ ] `diameter` on a tree whose longest path avoids the root is correct — e.g. `b([1,2,3,4,5,None,None,6,None,None,7,8,None,None,9])` → `6` (path `8-6-4-2-5-7-9`, never visits node 1)
- [ ] The function RETURNS height (for the parent) and updates `nonlocal best` with `left_h + right_h` (the real answer) — these are two different numbers; don't return `best` from the helper

## How to verify

```bash
python3 check.py all            # all nine of your files
python3 check.py medium/p02     # just one
python3 check.py solutions      # sanity-check the reference solutions
```
