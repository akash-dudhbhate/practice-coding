# Lesson 11 — Concepts Explained (Trees & BSTs)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Tree Anatomy — root, leaf, height, depth

**What:** A tree is nodes connected by edges with two rules: **exactly one root**, and **exactly one path between any two nodes** (no cycles, no node with two parents). In a **binary tree** every node has at most two children, conventionally named `left` and `right`.

```
            3            <- root (depth 0)
           / \
          9   20         <- internal nodes (depth 1)
             /  \
            15   7       <- leaves (depth 2): no children
         9 is also a leaf.

  depth of node  = how far DOWN from the root   (root = 0)
  height of node = how far UP to its deepest leaf (leaf = 0)
  height of tree = height of root = 2 here
```

**Why it exists:** Arrays store things in a line; linked lists too. But lots of data is *hierarchical* — a file system, an org chart, an HTML document, a JSON object, a decision tree. A tree is the minimal structure that captures "one thing contains/owns several things, recursively."

**Where it's used:** File systems, DOM (every HTML page is a tree), JSON/XML parsers, database indexes (B-trees), compiler syntax trees (the expression `2 + 3 * 4` parses into a tree where `*` sits below `+`), autocomplete tries, game AIs (move trees).

**What goes wrong without it:**
- Representing a hierarchy as a flat list of `(id, parent_id)` pairs works, but "find all descendants of X" becomes repeated scans — O(n²) instead of one traversal.
- Code that treats trees like lists: "iterate to the end" doesn't exist — you must *recurse* or *queue*, and pick an order.

**The node class + list helpers you get in every problem file:**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Level-order list -> tree.  None marks a missing child.
# build_tree([3, 9, 20, None, None, 15, 7]) builds the diagram above.
def build_tree(vals): ...

# Tree -> level-order list (inverse of build_tree).
def tree_to_list(root): ...
```

`[3, 9, 20, None, None, 15, 7]` reads left-to-right, level-by-level, like the diagram flattened.

---

## DFS Traversals — inorder / preorder / postorder / level-order

**What:** To "traverse" a tree means to visit every node exactly once. There is no natural "next" like in a list — so we pick an order. **DFS** (depth-first) dives to a leaf before backtracking; it comes in three flavors differing only in **when you visit the node relative to its children**. **BFS / level-order** goes floor by floor using a queue.

```
            1
           / \
          2   3
         / \
        4   5

preorder  (visit, left, right):  1 2 4 5 3   root FIRST  — "copy the tree" order
inorder   (left, visit, right):  4 2 5 1 3   root MIDDLE — sorted on a BST!
postorder (left, right, visit):  4 5 2 3 1   root LAST   — "delete the tree" order
level-order (BFS, floor by floor): [[1], [2,3], [4,5]]
```

| Traversal | When node is visited | Mnemonic | Classic use |
|-----------|---------------------|----------|-------------|
| preorder  | before children | "me first" | serialize/copy a tree |
| inorder   | between children | "me in the middle" | BST → sorted order |
| postorder | after children | "me last" | delete tree, dir sizes |
| level-order | by depth | "floor by floor" | shortest depth, print levels |

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

```python
from collections import deque
def level_order(root):
    if root is None:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):        # snapshot the level size FIRST
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        out.append(level)
    return out
```

**Why it exists:** Different questions need different orders. "Print a BST sorted" needs the root between its subtrees (inorder). "Total size of a directory" needs children summed before the parent can report (postorder). "Copy this tree" needs the parent created before children can attach (preorder). "Distance from root" is literally the level number (BFS).

**Where it's used:** Serializing trees (preorder/level-order), evaluating expression trees (postorder), `rm -r` and `du` (postorder: children must be handled before the parent), `find`/`ls -R` (preorder-ish), chess engines (BFS for shortest mate, DFS for deep lines).

**What goes wrong without it:**
- **Confusing the three DFS orders** — they differ only in where `visit` sits. People memorize code but can't predict output; the fix is the mental picture: write `L, visit, R` slots and place `visit` left/middle/right.
- **`for _ in range(len(q))` forgotten in BFS** — without snapshotting the level size, children you just enqueued get processed in the same "level," and your levels merge into a plain flat BFS.
- **Using a stack-pop for BFS** (or vice versa): BFS needs `popleft()` from a deque. `pop()` from the end turns it into DFS and levels come out scrambled.
- **Modifying structure while traversing** — deleting nodes during preorder frees children before you visit them; that's exactly why deletion wants postorder.

**Worked example — all four orders on one tree:**

```
            1
           / \
          2   3
         /   / \
        4   5   6

preorder:  1 2 4 3 5 6        (root, then whole left, then whole right)
inorder:   4 2 1 5 3 6        (whole left, root, whole right)
postorder: 4 2 5 6 3 1        (whole left, whole right, root)
levels:    [1] [2,3] [4,5,6]
```

Expected output of `inorder(build_tree([1,2,3,4,None,5,6]))`: **[4, 2, 1, 5, 3, 6]**

---

## Recursion on Trees — the "combine children's answers" pattern

**What:** Almost every tree function has the same skeleton:

```python
def f(root):
    if root is None:
        return BASE_CASE              # what does an empty subtree answer?
    left_answer  = f(root.left)       # trust the recursion
    right_answer = f(root.right)      # trust the recursion
    return combine(root, left_answer, right_answer)
```

The discipline: **decide what the function returns for a subtree, then trust it.** Don't trace 5 levels deep — ask "if `f(root.left)` gave me the right answer for the left subtree, what do I do with it?"

```python
def max_depth(root):                    # returns: height of subtree
    if root is None:
        return 0                        # empty tree has height 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def count_nodes(root):                  # returns: number of nodes in subtree
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

**Why it exists:** A tree is a *recursive definition* — each child is itself a tree. Iterative tree code needs an explicit stack and bookkeeping; recursion lets the call stack hold the "path back to the root" for free. The function's return value is the message a subtree sends up to its parent.

**Where it's used:** `max_depth`, `count_nodes`, `sum`, `diameter` (each node reports its height up AND updates a global best), `is_balanced` (return height or -1 if unbalanced — a return value carrying two facts), LCA, serialize — basically this entire lesson.

**What goes wrong without it:**
- **Missing the base case** — forgetting `if root is None` → `AttributeError: 'NoneType' object has no attribute 'left'`. The empty-subtree answer is the *first* thing to write, not an afterthought.
- **Returning the wrong thing** — e.g., in `max_depth` returning the max *so far* instead of the subtree height; the parent then can't combine. Ask "what does my caller need from me?"
- **Global answer vs return value confusion** — for `diameter`, the path's "highest point" may be inside a subtree, not at the root. So each node *returns height* (what the parent needs) and *updates a nonlocal best* (the real answer). Mixing the two up is the classic hard-problem bug.
- **Modifying and recursing inconsistently** — e.g., `insert` that doesn't return the new subtree root to its parent: the new node gets orphaned.

**Worked example — `max_depth` on the anatomy tree:**

```
max_depth(3)
├─ max_depth(9)  = 1   (leaf: 1 + max(0,0))
└─ max_depth(20)
   ├─ max_depth(15) = 1
   └─ max_depth(7)  = 1
   = 1 + max(1,1) = 2
= 1 + max(1, 2) = 3
```

Expected output of `max_depth(build_tree([3,9,20,None,None,15,7]))`: **3**

---

## The BST — ordering as structure

**What:** A **Binary Search Tree** adds one rule to a binary tree: for every node, **everything in its left subtree is smaller, everything in its right subtree is larger.**

```
            5
           / \
          3   7          3 < 5 < 7
         / \   \
        1   4   9        1 < 3 < 4 < 5 < 7 < 9
```

**Search:** start at root; too big → go left; too small → go right; equal → found.
**Insert:** same walk; when you fall off the tree (hit `None`), attach the new node there.

```python
def search_bst(root, val):
    if root is None:
        return False
    if val == root.val:
        return True
    return search_bst(root.left if val < root.val else root.right, val)

def insert_bst(root, val):
    if root is None:
        return TreeNode(val)            # found the empty slot — attach here
    if val < root.val:
        root.left = insert_bst(root.left, val)    # hand the new subtree UP
    else:
        root.right = insert_bst(root.right, val)
    return root
```

**Why inorder-on-BST = sorted:** inorder visits `left → node → right`. On a BST, left is all-smaller, right is all-larger — so the output is *all smaller values, then the node, then all larger values*, recursively: exactly sorted order. `inorder` of the tree above → `1 3 4 5 7 9`. This is why "kth smallest in a BST" is just "the kth thing inorder prints."

**Why it exists:** Sorted arrays give O(log n) *search* but O(n) *insert* (shifting). Linked lists give O(1) insert but O(n) search. A balanced BST gives **O(log n) for both** — the ordering is stored in the *shape*, not in contiguous memory.

**Where it's used:** `TreeMap`/`TreeSet` in Java, `std::map` in C++, database indexes (B-trees are fat BSTs), anything needing "sorted data that also changes" — leaderboards, ordered dictionaries, interval scheduling.

**What goes wrong without it:**
- **Validate-BST by comparing only parent-vs-children** — the classic bug. `is_valid_bst` on this tree is FALSE even though every node passes a local check:

```
            5
           / \
          1   6
             / \
            3   7        <- 3 sits in 5's RIGHT subtree but 3 < 5!
```

  Local checks (`node.left.val < node.val`) all pass; the violation is global. You must carry a **(min, max) range** down the recursion: `is_valid(node, lo, hi)` → node must be strictly inside `(lo, hi)`; left child gets `(lo, node.val)`, right child gets `(node.val, hi)`.
- **Insert without returning the subtree** — `insert_bst(root.left, val)` as a bare statement attaches the new node to nothing when `root.left` was `None`. The `root.left = insert_bst(...)` assignment is load-bearing.
- **Assuming BST = balanced** — see below.

**Worked example — searching for 4:**

```
at 5:  4 < 5 → go left
at 3:  4 > 3 → go right
at 4:  found.    3 hops for 6 nodes — O(height), not O(n)
```

---

## Balance — why shape is everything

**What:** A BST's promises only hold if the tree is **bushy** — height ≈ `log₂ n`. Nothing in the BST *rules* forces that. Insert sorted data into a plain BST and you get a **degenerate tree**: a straight line, which is just a linked list with extra `None`s.

```
insert 1,2,3,4,5 in that order:

            1
             \
              2          height = 4, not log₂(5) ≈ 2.3
               \
                3        search for 5 = 5 hops = O(n)
                 \
                  4
                   \
                    5
```

| | balanced | degenerate |
|---|---|---|
| height | `log₂ n` | `n` |
| search/insert | O(log n) | O(n) — same as a list scan |
| shape | bushy | a vine |

**Why it exists:** This gap is why **self-balancing** BSTs were invented — AVL trees and red-black trees rotate nodes on every insert/delete to keep height ≈ `log n`. `std::map` is red-black; that's the machinery behind its O(log n) guarantee.

**Where it's used:** Interview questions probe this directly ("what's the worst case for BST insert?" → O(n) if unbalanced) and indirectly — `diameter`, `is_balanced`, and every "why is this slow" discussion about sorted inserts.

**What goes wrong without it:**
- **Feeding sorted input to a plain BST** and expecting O(log n) — you silently built a linked list.
- **"Balanced" ≠ "complete"** — complete = every level full except maybe the last, filled left-to-right (that's the *heap* property, next lesson). Balanced only means heights of subtrees stay within ~1. People conflate them constantly.

**The intuition check for this lesson:** for a BST with n nodes, is `search` O(log n) or O(n)? **Answer: O(height) — and height is only log n if something keeps it balanced.**

---

## The Recipe — recognize it in 10 seconds

1. **"Visit/print every node"?** Pick the order by *when the root acts*: copy/serialize → preorder; BST sorted → inorder; delete/aggregate-up → postorder; levels/shortest-depth → BFS with `for _ in range(len(q))`.
2. **"Compute a number about the whole tree"?** → recursion skeleton: base case for `None`, recurse both children, combine. If the answer can hide inside a subtree (diameter, max path), *return height/sum* and update a `nonlocal best`.
3. **"BST" mentioned?** → two superpowers: *guided descent* (`val < node.val` → go left) and *inorder = sorted*. Search/insert/LCA all ride the descent; kth-smallest and validate ride inorder/ranges.
4. **"Validate a BST"?** → never local parent-child checks; carry `(lo, hi)` bounds down.
5. Always say complexity out loud: traversal = **O(n) time**; BST search/insert = **O(h) time** where h is height — O(log n) balanced, O(n) degenerate; recursion space = **O(h)** call stack.

---

## The Pitfall Gallery — five ways tree code goes wrong

**1. No `None` guard.**
```python
# WRONG — crashes on empty subtree
def depth(root):
    return 1 + max(depth(root.left), depth(root.right))
# CORRECT
def depth(root):
    if root is None:
        return 0
    return 1 + max(depth(root.left), depth(root.right))
```

**2. Forgetting the return on the recursive insert/search.**
```python
# WRONG — returns None implicitly; child never links up
def insert(root, val):
    if val < root.val:
        insert(root.left, val)
# CORRECT
def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root
```

**3. Local-only BST validation.**
```python
# WRONG — passes [5,1,6,None,None,3,7] which is NOT a BST
ok = (node.left is None or node.left.val < node.val) and \
     (node.right is None or node.right.val > node.val)
# CORRECT — range narrows as you descend
def valid(node, lo, hi):
    if node is None:
        return True
    return lo < node.val < hi and \
           valid(node.left, lo, node.val) and \
           valid(node.right, node.val, hi)
```

**4. BFS without the level-size snapshot.**
```python
# WRONG — levels blur into flat BFS
while q:
    node = q.popleft()
    out[-1].append(node.val)     # which level are we in??
# CORRECT — freeze the level size before popping
while q:
    level = []
    for _ in range(len(q)):      # only the nodes that were here when we started
        node = q.popleft()
        ...
    out.append(level)
```

**5. Confusing returned value with the answer (diameter-type problems).**
The diameter path's top isn't necessarily the root — a subtree can hold the answer. So the recursion *returns height* (for the parent to combine) while a `nonlocal best` accumulates `left_h + right_h` at each node. Writing `return max(...)` where you meant `best = max(...)` swaps the two roles and silently returns height as the answer.

**Edge cases to always test:** `None` root (empty tree → `0`/`[]`/`True`), single node, degenerate left/right line (deep recursion — does it still return correctly?), and for BST problems a tree that *looks* fine locally but violates the global range.
