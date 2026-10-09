# 03 — What a heap actually is

> 5-minute read. The core definition.

## The idea, plain words

A **heap** is a tree with exactly two rules:

**Rule 1 — the shape:** it's a **complete binary tree**. Every node has
at most 2 children, every level is completely full except maybe the
last, and the last level fills in **left to right** — no gaps.

**Rule 2 — the order:** every parent is ≤ both its children
(**min-heap**), or ≥ both its children (**max-heap**). Follow the rule
down every branch and the extreme value is *forced* to sit at the root.

```
VALID min-heap:            BROKEN min-heap:

        1                        5
       / \                      / \
      3   5                    3   8        <- 5 > 3: a child is
     / \                      / \               SMALLER than its parent
    7   4                    9   6           -> rule violated

root = minimum ✅           root says "5" but 3 exists below 💀
```

The crucial subtlety: **the rule is vertical only.** Parents vs their
own children — that's it. Siblings and cousins have NO order between
them. In the valid heap above, `3` and `5` aren't ordered, and `7`
sitting left of `4` is perfectly legal.

So a heap is **not sorted** and **not a BST** (binary search tree,
where *everything* left of a node is smaller). A heap keeps *partial*
order — just enough that the minimum is always on top.

## Check one by hand — runnable

```python
def is_min_heap(a):
    """Every child must be >= its parent."""
    for i in range(1, len(a)):
        parent = (i - 1) // 2
        if a[parent] > a[i]:
            return False
    return True

print(is_min_heap([1, 3, 5, 7, 4]))     # True
print(is_min_heap([1, 5, 3, 7, 4]))     # False — 5 (idx1) > child 4 (idx4)
```

## Why it exists

Partial order is *cheaper* to maintain than full order. A sorted list
re-shuffles on every insert because it promises "element #3 is the 3rd
smallest." A heap only promises "element #0 is THE smallest" — one
promise is much easier to keep, which is exactly why insert and remove
can both be O(log n) (chapters 05–07).

## Where it's used

Inside every priority queue: `heapq`, `queue.PriorityQueue`, OS
schedulers, heapsort, Dijkstra.

## Common mistake

**Expecting the heap array to look sorted.** `[1, 3, 5, 7, 4]` is a
valid heap — but read it as a list and `4` sits *after* `7`. Only
`heap[0]` is guaranteed to be the min; `heap[1]` is NOT the 2nd
smallest. Popping repeatedly *produces* sorted order; the stored array
never holds it.

## Your turn

Is `[2, 5, 4, 8, 3, 6]` a valid min-heap?

<details><summary>Answer</summary>
No. Index 1 holds 5, and its children are at indices 3 and 4 → values 8
and 3. But `5 > 3` — a parent bigger than its child breaks the rule.
(Spot the trap: reading left-to-right "2,5,4,8,3,6" *looks* plausible —
you have to check parent-vs-children, not neighbors.)
</details>

---

**← Prev** [02 — Why simple ideas are too slow](02-why-simple-ideas-are-too-slow.md) ·
**Next →** [04 — The array trick](04-the-array-trick.md)
