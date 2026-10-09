# 04 — Level-Order (BFS): Floor by Floor

> 5-minute read. The queue strikes back (lesson-06).

## The idea, plain words

DFS dives to a leaf before backtracking — depth-first. **BFS**
(breadth-first) does the opposite: **everyone on floor 0, then floor 1,
then floor 2** — like reading a page line by line instead of following
one character's plot to the end.

```
        4               floor 0:  [4]
       / \
      2   6             floor 1:  [2, 6]
     / \ / \
    1  3 5  7           floor 2:  [1, 3, 5, 7]
```

Output: `[[4], [2, 6], [1, 3, 5, 7]]`

The trick — a **queue** (lesson-06's FIFO hero): enqueue the root.
Repeat: dequeue a node, record it, enqueue its kids. Because a queue
is first-in-first-out, today's children wait behind the rest of
today's level — **the queue literally holds "the next floor" for you.**

## In code — and the famous snapshot line

```python
from collections import deque

def level_order(root):
    if root is None:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):      # freeze: only today's residents
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)    # tomorrow's residents
            if node.right: q.append(node.right)
        out.append(level)
    return out
```

Hand-trace on our tree:

```
q=[4]       → level size 1: pop 4, push 2,6       → out=[[4]]
q=[2,6]     → level size 2: pop 2 (push 1,3),
              pop 6 (push 5,7)                    → out=[[4],[2,6]]
q=[1,3,5,7] → level size 4: pop all, leaf kids    → +[1,3,5,7]
```

`print(level_order(root))` → `[[4], [2, 6], [1, 3, 5, 7]]`

## Why it exists

BFS answers "how FAR from the root" — the level number IS the
distance. Shortest depth, nearest leaf, "print the tree as it looks,"
friend-of-a-friend distance: all BFS. DFS answers "what's deep
inside" — totals, heights, exhaustive search. Same tree, different
superpower.

## Where it's used

`build_tree` / `tree_to_list` in your problem files (level-order is
THE serialization), shortest-path warm-ups for lesson-13 graphs,
level-by-level rendering, social-network distance.

## Common mistake

Forgetting `for _ in range(len(q))`. Without the snapshot, children
you just enqueued leak into the CURRENT round — your levels blur into
one flat list and you can't tell floor 1 from floor 2. The snapshot
says "only nodes already queued when this floor started belong to it."
(Related sin: `q.pop()` instead of `popleft()` silently turns BFS into
DFS — a stack, not a queue.)

## Your turn

After `out = [[4], [2,6]]` is built, what's in the queue, and how many
times does the inner `for` run next?

<details><summary>Answer</summary>
Queue holds `[1, 3, 5, 7]` — the children pushed while floor 1 was
popped. `len(q)` is frozen at 4, so the inner loop runs 4 times and
produces the `[1, 3, 5, 7]` level.
</details>

---

**← Prev** [03 — Three DFS orders](03-dfs-three-orders.md) ·
**Next →** [05 — The recursion skeleton](05-recursion-skeleton.md)
