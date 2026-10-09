# 06 — The BST Rule: Ordering as Shape

> 5-minute read. One rule — held EVERYWHERE.

## The idea, plain words

A **Binary Search Tree** is a binary tree plus one rule, held at EVERY
node:

> **everything in my LEFT subtree < me < everything in my RIGHT subtree**

Not "my left child" — my ENTIRE left subtree. Read it again; that
bolded stretch is where everyone slips.

Check our tree (it's secretly been a BST all along):

```
        4
       / \
      2   6        at 4: {1,2,3} all < 4 < {5,6,7}  ✓
     / \ / \       at 2: {1} < 2 < {3} ✓   at 6: {5} < 6 < {7} ✓
    1  3 5  7
```

Every node obeys the rule → valid BST.

## And a tree that LOOKS fine but isn't

```
        5
       / \
      1   6        locally fine: 1<5 ✓  5<6 ✓  3<6<7 ✓
         / \
        3   7      BUT 3 < 5 while sitting in 5's RIGHT subtree —
                   violates the rule AT 5 → NOT a BST
```

Every parent-child check passes; the violation only exists relative to
an **ancestor**. (This exact trap gets its own chapter — #12.)

## In code — the leftmost node holds the min

If everything left is smaller, the SMALLEST value in a BST is found by
walking left until you can't:

```python
def tree_min(node):
    while node.left:            # smaller always lives left
        node = node.left
    return node.val
```

On our tree: `tree_min(root)` → `1`, and `tree_min(root.right)` → `5`
— the minimum of the right subtree, a.k.a. the **successor**, which
you'll need for delete in chapter 09.

## Why the rule buys speed — a taste

At every node the rule answers "is what I want left, right, or me?"
One comparison throws away an entire subtree — no scanning. Chapter 07
turns this into `search`: lesson-09's halving, with the sorted array
folded into a tree shape.

## Where it's used

`TreeMap` / `TreeSet` (Java), `std::map` (C++), database indexes
(B-trees are fat BSTs), anything needing *sorted data that also
changes* — leaderboards, ordered dicts, interval schedulers.

## Common mistake

Checking only `node.left.val < node.val < node.right.val`. That
verifies one neighborhood — the rule is about the whole subtree. The
5/1/6/3/7 tree passes every local check and is still broken; ch. 12
shows the fix (carry a range down).

## Your turn

Is this a BST?

```
        4
       / \
      2   6
       \
        5
```

<details><summary>Answer</summary>
No. Node 2's right subtree containing 5 is fine *locally* (5 > 2) —
but 5 also sits in 4's LEFT subtree, where everything must be < 4.
5 > 4 → violation at the root. Every node is judged against ALL its
ancestors, not just its parent.
</details>

---

**← Prev** [05 — The recursion skeleton](05-recursion-skeleton.md) ·
**Next →** [07 — BST search](07-bst-search.md)
