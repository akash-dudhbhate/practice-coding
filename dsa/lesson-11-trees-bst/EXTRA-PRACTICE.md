# lesson-11-trees-bst — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: Name that order

For this tree, write preorder, inorder, postorder by hand:

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \
      4   7
```

<details><summary>Answer</summary>

- preorder: `8 3 1 6 4 7 10 14` (root before each subtree)
- inorder: `1 3 4 6 7 8 10 14` — **sorted!** because it's a BST
- postorder: `1 4 7 6 3 14 10 8` (root after each subtree)

The instant way to check yourself: on a BST, inorder MUST come out sorted. If yours didn't, you misplaced `visit`.
</details>

---

## Check 02: Which traversal?

Match each task to preorder / inorder / postorder / level-order:

1. Print a BST's values sorted.
2. Compute the total size of a directory (children must be counted before the parent reports).
3. Clone a tree (parent object must exist before children attach).
4. Print an org chart, managers first, one row per rank.
5. Delete every node of a tree (children must be freed before the parent).

<details><summary>Answer</summary>
1. inorder · 2. postorder · 3. preorder · 4. level-order (BFS) · 5. postorder.

Mnemonic: does the parent act *before*, *between*, or *after* its children? That IS the traversal name.
</details>

---

## Check 03: What does it return?

```python
def mystery(root):
    if root is None:
        return 0
    left = mystery(root.left)
    right = mystery(root.right)
    return max(left, right) + 1
```

For `build_tree([1,2,3,4,None,None,None,5])` — what does it return, and what's the name we gave this shape?

<details><summary>Answer</summary>
Returns **4** — the max depth (tree is `1 → 2 → 4 → 5`, a left-leaning vine plus the leaf `3`).

The shape: `max(left, right) + 1` is the **combine** step of the recursion skeleton — each node reports "my subtree's height" to its parent. Same skeleton as `count_nodes`, different combine.
</details>

---

## Check 04: Is this a BST?

```
        10
       /  \
      5    15
          /  \
         6    20
```

<details><summary>Answer</summary>
**No.** Every local check passes: `5 < 10`, `10 < 15`, `6 < 15`, `15 < 20`. But `6` sits in `10`'s **right subtree**, so it must be `> 10` — and `6 < 10`. The violation is *global*, not local. This is the tree that kills every "compare node to its children" validator — you need the `(lo, hi)` range, where `6` inherits the range `(10, 15)` and fails.
</details>

---

## Check 05: Complexity spot-check

You're told `search_bst` on a 1000-node BST took ~1000 comparisons in the worst case. Is that consistent with "BST search is O(log n)"?

<details><summary>Answer</summary>
Yes — and it exposes the imprecise slogan. The real bound is **O(height)**. It's O(log n) only when the tree is *balanced*; feed sorted input to a plain BST and the tree degenerates into a linked list of height n, so ~1000 comparisons. The guarantee comes from self-balancing trees (AVL, red-black), not from the BST property itself.
</details>

---

## Check 06: Inorder k-th smallest

Without storing the whole list, how would you get the 3rd smallest value from a BST? What do you return early?

<details><summary>Answer</summary>
Inorder walk, counting nodes. When the count hits `k`, that's your answer — and you can **stop**: everything unvisited is larger anyway. Implementation trick: carry the count in a nonlocal/list, or use an iterative inorder with an explicit stack and pop `k` times. This is why "inorder on BST = sorted" matters — kth smallest = kth inorder visit.
</details>

---

## Debug Exercises — find and fix the bug

> Fix the broken code. Find bugs mentally before running.

---

## Debug 01 (Easy): Max depth — wrong combine

```python
def max_depth(root):
    if root is None:
        return 0
    return max_depth(root.left) + max_depth(root.right)
```

**Hint:** Run it mentally on a single-node tree. What should the answer be?

<details><summary>Answer</summary>

**Bug:** the combine adds the two heights — for `b([1])` it returns `0` instead of `1`, and for balanced trees it roughly doubles the count instead of taking the deeper side.
**Fix:** `return 1 + max(max_depth(root.left), max_depth(root.right))` — the node itself contributes 1, and a node's height is the *deeper* of its two subtrees, not the sum.
</details>

---

## Debug 02 (Medium): BST insert — orphaned node

```python
def insert_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        insert_bst(root.left, val)      # BUG
    else:
        insert_bst(root.right, val)     # BUG
    return root
```

**Hint:** Insert `[5, 3, 1]` and print `tree_to_list`. Where did `1` go?

<details><summary>Answer</summary>

**Bug:** the recursive call's return value is thrown away. When `root.left` is `None`, `insert_bst(None, val)` builds a new node — but nothing assigns it to `root.left`, so the node is created and dropped. `tree_to_list` shows `[5, 3]`: the `1` vanished.
**Fix:** `root.left = insert_bst(root.left, val)` / `root.right = insert_bst(root.right, val)`. Every recursive insert *returns its (possibly new) subtree root* — the parent must catch it.
</details>

---

## Debug 03 (Medium): Validate BST — local-only check

```python
def is_valid_bst(root):
    if root is None:
        return True
    if root.left and root.left.val >= root.val:
        return False
    if root.right and root.right.val <= root.val:
        return False
    return is_valid_bst(root.left) and is_valid_bst(root.right)
```

**Hint:** Try `b([5,4,6,None,None,3,7])`.

<details><summary>Answer</summary>

**Bug:** every parent-child pair locally satisfies `left < node < right`, so this returns `True` — but node `3` is inside `5`'s right subtree where everything must exceed `5`. Wrong answer.
**Fix:** carry the allowed range down the recursion:
```python
def is_valid_bst(root, lo=float("-inf"), hi=float("inf")):
    if root is None:
        return True
    if not (lo < root.val < hi):
        return False
    return (is_valid_bst(root.left, lo, root.val) and
            is_valid_bst(root.right, root.val, hi))
```
Node `3` is checked against `(5, 6)` and correctly fails.
</details>

---

## Debug 04 (Hard): Diameter — returning the answer instead of height

```python
def diameter(root):
    best = 0
    def h(node):
        nonlocal best
        if node is None:
            return 0
        left = h(node.left)
        right = h(node.right)
        best = max(best, left + right)
        return max(left, right)          # BUG
    h(root)
    return best
```

**Hint:** What does the parent do with this return value? What's missing?

<details><summary>Answer</summary>

**Bug:** `h` returns `max(left, right)` — the child's height *without counting the edge up to the parent*. Every level reports one less, so heights (and `best`) come out small. The subtree-height contract is "edges/nodes including me."
**Fix:** `return 1 + max(left, right)`. The two roles stay distinct: `best = max(best, left + right)` is the *answer* (path through this node, in edges), while the *return value* is height for the parent's use. Confusing them is THE diameter bug.
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: No `None` base case
```python
# WRONG — AttributeError on empty subtree
def f(root):
    return f(root.left) + f(root.right)
# CORRECT — the empty-subtree answer comes FIRST
def f(root):
    if root is None:
        return 0
    ...
```

## Mistake 02: Searching both sides of a BST
```python
# WRONG — that's O(n), you've thrown away the BST property
def search(root, val):
    if root is None: return False
    return root.val == val or search(root.left, val) or search(root.right, val)
# CORRECT — guided descent, O(h)
def search(root, val):
    if root is None: return False
    if val == root.val: return True
    return search(root.left if val < root.val else root.right, val)
```

## Mistake 03: Confusing the three DFS orders
The recursive bodies are IDENTICAL except where `visit(root)` sits:
```python
preorder:  visit; go left; go right      # root acts FIRST
inorder:   go left; visit; go right      # root acts MIDDLE
postorder: go left; go right; visit      # root acts LAST
```
If you can't predict output on a 3-node tree, you memorized code instead of the slot picture.

## Mistake 04: BFS without the level snapshot
```python
# WRONG — children contaminate the level being measured
while q:
    node = q.popleft()
    level.append(node.val)
    q.extend([node.left, node.right])    # these are NEXT level!
# CORRECT — freeze how many nodes belong to this level
while q:
    for _ in range(len(q)):
        node = q.popleft()
        ...
```

## Mistake 05: Assuming BST input is balanced
```python
# Inserting [1,2,3,4,5] in order builds a vine: height n, search O(n)
# Fix in real systems: AVL/red-black rotations. Fix in interviews:
# SAY IT — "O(h); O(log n) only if balanced; worst case O(n)."
```

## Mistake 06: Forgetting `nonlocal` for the accumulator
```python
def diameter(root):
    best = 0
    def h(node):
        best = max(best, ...)      # WRONG — UnboundLocalError (assigns → local var)
        ...
    # CORRECT — declare nonlocal best inside h, or use a list/self attribute
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Traversal with flag soup
### Before
```python
def inorder(root):
    out = []
    def go(node, flag):
        if node is None:
            return
        if flag == 0:
            out.append(node.val)
        go(node.left, 1)
        if flag == 1:
            out.append(node.val)
        go(node.right, 2)
        if flag == 2:
            out.append(node.val)
    go(root, 1)
    return out
```
### Problems
1. One function trying to be all three traversals — unreadable, and each call adds the value at three different points.
2. The `if` checks run per node per flag — accidental quadratic-ish logic on top of recursion.

### After — three tiny functions, or one honest recursive body
```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

---

## Refactor 02 (Medium): Level-order with nested index bookkeeping
### Before
```python
def level_order(root):
    out, q = [], deque([root])
    depth = 0
    while q:
        node, d = q.popleft()          # pairs (node, depth) everywhere
        ...
```
### Problems
1. Carrying `(node, depth)` tuples works, but it's bookkeeping you don't need — BFS already *is* level-by-level.

### After
```python
def level_order(root):
    if root is None:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):        # the snapshot replaces depth tracking
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        out.append(level)
    return out
```

---

## Refactor 03 (Hard): Validate-BST collecting inorder then checking sorted
### Before
```python
def is_valid_bst(root):
    vals = []
    def inorder(node):
        if node is None: return
        inorder(node.left); vals.append(node.val); inorder(node.right)
    inorder(root)
    return all(vals[i] < vals[i+1] for i in range(len(vals)-1))
```
### Problems
1. O(n) extra space for `vals` — the sorted check only needs the *previous* value.
2. Builds a whole list to answer a boolean that could early-exit.

### After — stream it (or use the range version)
```python
def is_valid_bst(root):
    prev = [None]
    def inorder(node):
        if node is None:
            return True
        if not inorder(node.left):
            return False
        if prev[0] is not None and node.val <= prev[0]:
            return False
        prev[0] = node.val
        return inorder(node.right)
    return inorder(root)
```
O(h) space, early-exits on first violation. (The `(lo, hi)` range version is equally good — arguably clearer. Both beat materializing the list.)

---

## Approach Comparison — different ways to solve it

## Problem: Validate a BST

### Approach 1: Range propagation
```python
def f(root, lo=float("-inf"), hi=float("inf")):
    if root is None: return True
    if not (lo < root.val < hi): return False
    return (f(root.left, lo, root.val) and
            f(root.right, root.val, hi))
```
**Pros:** Directly encodes "everything left < me < everything right"; early-exits. **Cons:** extra params can feel abstract until you trace it once.

### Approach 2: Inorder must be strictly increasing
```python
# inorder to a list, check sorted — or the streaming version above
```
**Pros:** Turns the problem into a fact you already know (BST inorder = sorted). **Cons:** list version costs O(n) space; streaming version has fussier control flow.

**Winner:** Approach 1 in interviews — it's the version that demonstrates you know WHY the local check fails. Mention Approach 2 as the cross-check.

---

## Problem: Level-order traversal

### Approach 1: `deque` + `len(q)` snapshot (shown above)
**Pros:** No per-node metadata; the loop structure IS the level boundary. **Cons:** none worth mentioning — this is the canonical version.

### Approach 2: BFS carrying `(node, depth)` pairs
```python
q = deque([(root, 0)])
while q:
    node, d = q.popleft()
    # append node.val to out[d]
```
**Pros:** Works when levels aren't cleanly separable (e.g., multiple roots). **Cons:** tuple per node; `out` must grow dynamically; more moving parts for the same result.

**Winner:** Approach 1 — simpler state, same O(n) time.

---

## Problem: Diameter of a binary tree

### Approach 1: Height-returning recursion + `nonlocal best`
```python
def f(root):
    best = 0
    def h(node):
        nonlocal best
        if node is None: return 0
        l, r = h(node.left), h(node.right)
        best = max(best, l + r)
        return 1 + max(l, r)
    h(root)
    return best
```
**Time O(n), space O(h).** **Pros:** one pass; every node is both a "height reporter" and a "candidate top of the longest path." **Cons:** the two-channels (return vs nonlocal) must be kept straight.

### Approach 2: For each node, compute left+right subtree heights separately
```python
# for every node: lh = height(node.left); rh = height(node.right); best = max(best, lh+rh)
# where height() itself is a fresh recursion → O(n²)
```
**Pros:** easier to see why it's right. **Cons:** recomputes heights — O(n log n) on balanced trees, O(n²) on vines.

**Winner:** Approach 1 — same idea as the brute force but each height is computed once and reused ("the parent's answer built from the children's answers" — the lesson's core pattern).
