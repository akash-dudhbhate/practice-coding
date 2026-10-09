# 10 — Inorder on a BST = Sorted. Always.

> 4-minute read. The free-est fact in the lesson.

## The idea, plain words

Back in chapter 03 our inorder printed `1 2 3 4 5 6 7` and it looked
suspiciously sorted. Here's why it HAD to be.

- Inorder says: **left subtree, then me, then right subtree.**
- The BST rule says: **everything left < me < everything right.**

So every node emits: *all smaller values — me — all larger values*.
Since that's true recursively inside each subtree too, the whole
printout is perfectly sorted. Not a coincidence — **the rule, read
aloud.**

```
        4
       / \
      2   6         inorder:  [ {1,2,3} ] 4 [ {5,6,7} ]
     / \ / \                  sorted inside the braces, recursively
    1  3 5  7               →  1 2 3 4 5 6 7
```

## In code — and the kth-smallest trick

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

print(inorder(root))        # [1, 2, 3, 4, 5, 6, 7]
print(inorder(root)[2])     # 3 — the 3rd smallest
```

"kth smallest in a BST" is a famous interview question — and it's just
**the kth thing inorder prints.** The fancy version walks inorder with
a counter and stops early instead of building the whole list; the
insight is identical: *inorder position = rank.*

## Why it exists

This is why BSTs matter beyond search: a BST is a **self-sorting
container**. Insert in any order; read out sorted — free, no `sort()`
call. `std::map` iteration is literally an inorder walk.

## Where it's used

Kth-smallest / kth-largest (inorder from the right side), range
queries ("all values between a and b" — inorder, pruning out-of-range
subtrees), sorted iteration, and even validating a BST — a true BST's
inorder is strictly increasing.

## Common mistake

Running inorder on a tree that ISN'T a BST and expecting sorted output.
Inorder on a random binary tree prints whatever the shape gives — the
sortedness comes from the BST rule, not the traversal.

## Your turn

Without running it: what does inorder print on ch. 06's INVALID tree
(5 on top, 1 left, 6 right with children 3 and 7)? What does that
output prove?

<details><summary>Answer</summary>
`1 5 3 6 7` — NOT sorted (5 lands before 3). And that's the point: a
non-increasing inorder is proof the tree isn't a valid BST. "Is
inorder strictly increasing?" is a legitimate validation strategy —
ch. 12's range method is the one interviewers usually push for.
</details>

---

**← Prev** [09 — BST delete](09-bst-delete.md) ·
**Next →** [11 — Balanced vs degenerate](11-balanced-vs-degenerate.md)
