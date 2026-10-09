# 11 — Balanced vs Degenerate: Shape Is Everything

> 5-minute read. The asterisk on every O(log n) claim.

## The idea, plain words

BST search is **O(h)** — height, not log n. Height is log₂ n ONLY when
the tree is bushy. And nothing in the BST rule enforces bushiness.

Watch what happens when you insert sorted data:

```python
root = None
for v in [1, 2, 3, 4, 5]:
    root = insert_bst(root, v)
```

```
    1
     \
      2        every new value > everything → always goes right
       \
        3      height = 5 nodes, not ~log₂5 ≈ 3
         \
          4    searching for 5 takes 5 hops → O(n)
           \
            5
```

A "BST" that's secretly a linked list with extra `None`s. It has a
name: a **degenerate** tree — technically valid, practically useless.

| | balanced | degenerate |
|---|---|---|
| shape | bushy | a vine |
| height | ≈ log₂ n | n |
| search / insert | O(log n) | O(n) — a plain scan |

## Why it exists — and how the world fixed it

This gap is why **self-balancing BSTs** were invented. **AVL trees**
and **red-black trees** are plain BSTs plus a "rebalance after every
insert/delete" step — they rotate subtrees around to keep height ≈
log n no matter the input order. `std::map` is a red-black tree; that
machinery is what buys its guarantee. You won't implement rotations
this lesson — but you must KNOW the plain BST makes no such promise.

## Where it's used

Interviewers probe it directly — "worst case for BST insert?" (O(n):
sorted input into a plain BST) — and indirectly: `is_balanced` and
`diameter` problems are literally bushiness measurements.

## Common mistake — "balanced" ≠ "complete"

- **Balanced** — sibling subtree heights differ by at most ~1.
  A *height* condition.
- **Complete** — every level full except maybe the last, filled
  left-to-right. A *packing* condition (the heap property, lesson-12).

People conflate them constantly. Different words, different
guarantees — our 7-node tree happens to be both, which is what makes
it such a tidy teaching example.

## Your turn

`[4, 2, 6, 1, 3, 5, 7]` inserted into an empty BST gives our nice
tree; `[1,2,3,4,5,6,7]` gives a vine. Same data, same rule — what
differed, and what's the takeaway?

<details><summary>Answer</summary>
The INSERT ORDER — it alone determines shape. Sorted input maximally
unbalances (every value lands on one edge); a "middle-first" order
fills both sides. Takeaway: a plain BST's speed depends on
luck-of-arrival — unless you add rebalancing (AVL / red-black) or
shuffle the input first.
</details>

---

**← Prev** [10 — Inorder = sorted](10-inorder-is-sorted.md) ·
**Next →** [12 — LCA & validate-BST](12-lca-and-validate.md)
