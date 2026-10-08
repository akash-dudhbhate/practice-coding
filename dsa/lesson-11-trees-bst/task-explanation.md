# Lesson 11 — Trees & BSTs

## What you'll learn
- Tree vocabulary: root / leaf / height / depth, and the `TreeNode` class
- The three DFS orders (pre / in / post) + BFS level-order, and when each is right
- The recursion skeleton: base case → recurse children → combine answers
- BST search/insert via guided descent; why inorder prints a BST sorted
- Balance intuition: O(h) means O(log n) only if the tree stays bushy

## Lesson

Trees in these problems are built from **level-order lists** — every file gives
you `build_tree([3, 9, 20, None, None, 15, 7])` and `tree_to_list(root)` helpers
plus the `TreeNode` class. `None` in the list marks a missing child.

The whole lesson is two ideas:
1. **Pick a visit order** (pre / in / post / level) — they differ only in *when
   the root acts*.
2. **Recursion skeleton** —
   `None → base answer; answer = combine(f(left), f(right))`.
   Trust that each recursive call returns the right answer for its subtree.

A **BST** adds the rule *left < node < right (recursively)*, which buys you
guided descent (search/insert/LCA) and sorted inorder output — at O(h) cost,
where h is height.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here) — the traversal & recursion skeletons
1. `easy/p01-tree-traversals.py` — `inorder(root)`, `preorder(root)`, `postorder(root)` → each returns a list of values in that order.
   Tree `[1, 2, 3, 4, None, 5, 6]` → inorder `[4,2,1,5,3,6]`, preorder `[1,2,4,3,5,6]`, postorder `[4,2,5,6,3,1]`. Empty tree → `[]`.
2. `easy/p02-max-depth.py` — `max_depth(root)` → height of the tree (edges on the longest root→leaf path; empty = 0).
   `[3,9,20,None,None,15,7] → 3`. Degenerate `[1,2,None,3,None,4] → 4`.
3. `easy/p03-count-nodes.py` — `count_nodes(root)` → total number of nodes.
   `[3,9,20,None,None,15,7] → 5`, `[] → 0`. Same skeleton as p02 — different combine (`1 + left + right` instead of `1 + max`).

### Medium — BFS and the BST
4. `medium/p01-level-order-bfs.py` — `level_order(root)` → list of levels, each a list of values left-to-right.
   `[3,9,20,None,None,15,7] → [[3],[9,20],[15,7]]`. Queue + `for _ in range(len(q))` snapshot per level.
5. `medium/p02-bst-insert-search.py` — `insert_bst(root, val)` → returns root with `val` placed by BST rules; `search_bst(root, val)` → `True/False`.
   Insert `5,3,7,1,4` into an empty tree → `tree_to_list` gives `[5,3,7,1,4]`. Search for 4 → `True`, for 6 → `False`.
6. `medium/p03-validate-bst.py` — `is_valid_bst(root)` → `True` iff the BST rule holds **everywhere** (not just parent vs children).
   `[2,1,3] → True`; `[5,1,4,None,None,3,6] → False`; `[5,4,6,None,None,3,7] → False` — the `3` is in 5's right subtree but `< 5`. Carry `(lo, hi)` bounds down.

### Hard — combine children's answers, and structural round-trips
7. `hard/p01-lca-in-bst.py` — `lca_bst(root, p, q)` → the **node** that is the lowest common ancestor of values `p` and `q` (both guaranteed present). BST shortcut: if both < node go left, both > node go right, otherwise node IS the split point.
   BST `[6,2,8,0,4,7,9,None,None,3,5]`, `p=2, q=8` → node `6`; `p=2, q=4` → node `2` (a node can be its own ancestor).
8. `hard/p02-serialize-deserialize.py` — `serialize(root)` → `str`; `deserialize(data)` → root. Any format works — checked by round-trip: `tree_to_list(deserialize(serialize(t)))` must equal `tree_to_list(t)`. Must handle `None` and single nodes.
9. `hard/p03-diameter-of-tree.py` — `diameter(root)` → longest path between any two nodes, measured in **edges** (may not pass through root).
   `[1,2,3,4,5] → 3` (path `4→2→1→3`). Each node *returns its height* and *updates a `nonlocal best` with `left_h + right_h`* — the answer vs return-value split from concepts.md.

### How to work
- Read `concepts.md` first — the recipe section maps each problem to an order or skeleton.
- Every stub file ships `TreeNode`, `build_tree`, `tree_to_list` — use `tree_to_list` to eyeball your tree.
- Run `python3 check.py easy/p01` for one problem, `python3 check.py all` for all nine.
- `coding-check.md` is your manual checklist; `EXTRA-PRACTICE.md` has debug drills after you finish.
- Peek at `solutions/` only after a real attempt — then close it and redo from memory.
