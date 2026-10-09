# Lesson 11 — Trees & BSTs

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson
lives in `chapters/` — **14 tiny files, ~5 minutes each**. Read one,
try the mini-practice at the bottom, take a breath, come back. That's
the design.

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [What is a tree?](chapters/01-what-is-a-tree.md) | every vocab word, on ONE picture |
| 02 | [A binary tree in code](chapters/02-tree-in-code.md) | `TreeNode`, `build_tree`, why not flat lists |
| 03 | [Three DFS orders](chapters/03-dfs-three-orders.md) | pre / in / post on the SAME tree — the classic confusion |
| 04 | [Level-order (BFS)](chapters/04-bfs-level-order.md) | the queue + the snapshot line |
| 05 | [The recursion skeleton](chapters/05-recursion-skeleton.md) | trust-the-children, the 90% pattern |
| 06 | [The BST rule](chapters/06-the-bst-rule.md) | left < node < right — *recursively* |
| 07 | [BST search](chapters/07-bst-search.md) | guided descent = lesson-09 halving |
| 08 | [BST insert](chapters/08-bst-insert.md) | walk down, plug in — and the load-bearing `=` |
| 09 | [BST delete](chapters/09-bst-delete.md) | the three cases + the successor swap |
| 10 | [Inorder = sorted](chapters/10-inorder-is-sorted.md) | why BSTs self-sort; kth-smallest |
| 11 | [Balanced vs degenerate](chapters/11-balanced-vs-degenerate.md) | when a BST is secretly a linked list |
| 12 | [LCA & validate-BST](chapters/12-lca-and-validate.md) | carrying info down the tree |
| 13 | [Pitfall gallery](chapters/13-pitfall-gallery.md) | the five ways tree code dies |
| 14 | [The recipe](chapters/14-the-recipe.md) | diagnose any tree problem in 10 seconds |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding
one beats skimming five.

## The one-paragraph answer (bookmark this)

> A tree is nodes with exactly one root and one path between any two
> nodes — hierarchy made structure. Traverse four ways: pre / in /
> post differ only in *when the root acts*; BFS goes floor by floor
> with a queue. Almost every tree function is one skeleton:
> `None → base answer; recurse children; combine`. A **BST** adds
> `left < node < right` recursively — buying O(h) search/insert via
> guided descent and free sorted output via inorder — where h is
> log n only if the tree stays balanced.

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py`
   after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
