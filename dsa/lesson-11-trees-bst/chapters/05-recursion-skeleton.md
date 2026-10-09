# 05 — The Recursion Skeleton: Trust the Children

> 5-minute read. The pattern behind 90% of tree problems.

## The idea, plain words

Here's the cheat code: **a subtree is a whole tree.** Node 2's subtree
in our tree is itself a perfectly good 3-node tree. So a function that
works on "a tree" automatically works on every subtree — call it on
`root.left` and `root.right` and *trust* it.

Every tree recursion is the same skeleton:

```python
def f(root):
    if root is None:
        return BASE_ANSWER          # 1. what does an EMPTY tree answer?
    left  = f(root.left)            # 2. trust it on the left subtree
    right = f(root.right)           # 3. trust it on the right subtree
    return COMBINE                  # 4. merge: me + left + right
```

The discipline: decide **what the function returns**, then never think
deeper than one level. "If `f(root.left)` hands me the right answer
for the whole left subtree, what do I do with it?" That question is
the entire thought process. (Lesson-08 trained this muscle; trees are
where it pays off.)

## Two examples, same skeleton

```python
def max_depth(root):                # returns: height (in nodes) of subtree
    if root is None:
        return 0                    # empty tree has height 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
                                     # me + the taller side

def count_nodes(root):              # returns: nodes in subtree
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
                                     # me + both sides
```

Only the COMBINE step differs: `1 + max(...)` vs `1 + left + right`.

## Hand-trace — max_depth on our tree (answers bubble UP)

```
        4
       / \
      2   6
     / \ / \
    1  3 5  7

leaves 1,3,5,7 → each returns 1        (1 + max(0, 0))
2 → 1 + max(1, 1) = 2      6 → 1 + max(1, 1) = 2
4 → 1 + max(2, 2) = 3      <- the answer arrives at the top
```

`print(max_depth(root), count_nodes(root))` → `3 7`

Think of each call as a worker who knows only "my value, plus two
coworkers' reports." Nobody sees the whole tree — yet the right answer
reaches the top.

## Why it exists

A tree IS a recursive definition — each child is a tree. Iterative
code would need a hand-managed stack tracking "where was I, what's
left"; recursion lets the call stack hold that path for free. The
return value is the message a subtree sends up to its parent.

## Where it's used

`max_depth`, `count_nodes`, `sum`, `is_balanced`, `diameter`,
serialize, LCA — nearly every problem in `easy/` and `medium/` is this
skeleton with a different COMBINE.

## Common mistake — two roles, one return value

Some answers hide INSIDE a subtree. The **diameter** (longest path
between any two nodes) may not pass through the root at all. So each
node *returns height* (what its parent needs) while updating a
`nonlocal best` with `left_h + right_h` (the real answer's candidate).
Confusing "the value I return" with "the value I'm collecting" is the
classic hard-problem bug — chapter 13's gallery has it on the wall.

## Your turn

Write `sum_tree(root)` — total of all values — using the skeleton.
What's the base answer? What's the combine?

<details><summary>Answer</summary>

```python
def sum_tree(root):
    if root is None:
        return 0                    # BASE: empty subtree sums to 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)
                                     # COMBINE: me + both sides
```

On our tree: 1+2+3+4+5+6+7 = **28**.
</details>

---

**← Prev** [04 — Level-order (BFS)](04-bfs-level-order.md) ·
**Next →** [06 — The BST rule](06-the-bst-rule.md)
