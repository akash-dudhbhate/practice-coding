# 13 — The Pitfall Gallery: Five Ways Tree Code Dies

> 5-minute read. Learn to recognize these on sight.

## 1. No `None` guard

```python
# WRONG — crashes on the first empty subtree
def depth(root):
    return 1 + max(depth(root.left), depth(root.right))
# AttributeError: 'NoneType' object has no attribute 'left'

# RIGHT — the empty-subtree answer comes FIRST
def depth(root):
    if root is None:
        return 0
    return 1 + max(depth(root.left), depth(root.right))
```

The base case is the first line you write, never an afterthought.

## 2. Dropping the recursive return (insert / delete)

```python
# WRONG — the built subtree never re-attaches
if val < root.val:
    insert_bst(root.left, val)

# RIGHT — catch what the recursion hands you
if val < root.val:
    root.left = insert_bst(root.left, val)
```

The contract: recursion returns a (possibly new) subtree; catching it
with `=` is the whole job.

## 3. Local-only BST validation

```python
# WRONG — passes invalid trees like 5/1/6/3/7
ok = node.left.val < node.val < node.right.val   # (also crashes on None)

# RIGHT — the range narrows as you descend (chapter 12)
return lo < node.val < hi and \
       is_bst(node.left, lo, node.val) and \
       is_bst(node.right, node.val, hi)
```

## 4. BFS without the level snapshot

```python
# WRONG — children leak into the current round; levels blur
while q:
    node = q.popleft()

# RIGHT — freeze the level size first
while q:
    for _ in range(len(q)):          # only nodes queued BEFORE this level
        node = q.popleft()
```

(Bonus sin: `q.pop()` instead of `popleft()` silently turns BFS into
DFS.)

## 5. Confusing "what I return" with "the answer" (diameter-type)

The diameter path's peak can sit inside ANY subtree — often not the
root. So each node *returns height* (what its parent needs) while
updating `nonlocal best` with `left_h + right_h` (the real candidate).
Writing `return max(...)` where you meant `best = max(...)` swaps the
two roles and silently returns height as the answer — no crash, just
wrong.

## Edge cases to always test

- `None` root → `0`, `[]`, or `True` — whatever the empty answer is
- single node
- a degenerate vine — does deep recursion still return correctly?
- a tree that looks fine LOCALLY but breaks a GLOBAL rule (ch. 12)

## Your turn

Someone's `inorder` crashes with `AttributeError` on the input `[]`
(empty list → `build_tree` gives `None`). Which pitfall is it, and
what's the one-line fix?

<details><summary>Answer</summary>
Pitfall #1 — no `None` guard. `build_tree([])` returns `None`, and the
function hits `root.left` on `None`. Fix: first line,
`if root is None: return []`.
</details>

---

**← Prev** [12 — LCA & validate-BST](12-lca-and-validate.md) ·
**Next →** [14 — The recipe](14-the-recipe.md)
