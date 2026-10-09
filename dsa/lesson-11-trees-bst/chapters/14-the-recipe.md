# 14 — The Recipe: Recognize It in 10 Seconds

> 4-minute read. Ties all 13 chapters together.

## The five-step diagnosis

1. **"Visit / print every node"?** Pick the order by *when the root
   acts*: copy / serialize → **preorder** · BST sorted → **inorder** ·
   delete / roll-up (folder sizes, max_depth) → **postorder** ·
   levels / shortest depth → **BFS** with `for _ in range(len(q))`.

2. **"Compute one number about the whole tree"?** Recursion skeleton:
   `None → base answer; recurse left, right; combine`. If the answer
   can hide inside a subtree (diameter, max path) → return height,
   update a `nonlocal best`.

3. **"BST" in the problem?** Two superpowers: **guided descent**
   (`val < node` → go left — powers search, insert, LCA) and
   **inorder = sorted** (powers kth-smallest and validation).

4. **"Is this a valid BST?"** Never local parent-child checks. Carry
   `(lo, hi)` down: left child gets `(lo, node.val)`, right child gets
   `(node.val, hi)`.

5. **Say complexity out loud, always:** traversal = **O(n)** time
   (every node once). BST search / insert / delete / LCA = **O(h)** —
   O(log n) balanced, O(n) degenerate. Recursion space = **O(h)** call
   stack; BFS space = O(widest level).

## The cheat table

| you hear | reach for |
|----------|-----------|
| "sorted order from the tree" | inorder |
| "copy / serialize" | preorder (or level-order list) |
| "total / height / count" | postorder recursion skeleton |
| "nearest / shortest / levels" | BFS + snapshot loop |
| "find in a BST" | guided descent, O(h) |
| "kth smallest" | inorder + counter |
| "is it a valid BST" | `(lo, hi)` range |
| "common ancestor" | descend to the split |

## What you now know

Tree vocabulary; the node-as-three-slots model; the three DFS orders
and which question each answers; BFS with the snapshot line; the
recursion skeleton; the BST rule and why it's global; guided descent
for search / insert / LCA; delete's three cases; inorder-is-sorted;
why O(h) hides a balance asterisk; the range-validation trick.

**That's the whole lesson.** `easy/` drills the skeletons, `medium/`
mixes orders and BST ops, `hard/` combines them (diameter, serialize,
two-role returns). Go build.

---

**← Prev** [13 — Pitfall gallery](13-pitfall-gallery.md) ·
Done with concepts? → Open `task-explanation.md` and solve
`easy/p01` next.
