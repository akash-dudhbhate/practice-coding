# 01 — What Is a Tree? (the vocabulary chapter)

> 5-minute read. One idea only: the words.

## The idea, plain words

A **tree** is a bunch of **nodes** (boxes holding a value) connected by
**edges** (lines), with two rules:

1. Exactly one node is the **root** — the top, where every walk starts.
2. Exactly one path connects any two nodes — no loops, no node with two
   parents.

Think of a **family tree**: one founding ancestor at the top, every
person has exactly one parent (in this simplified picture) and any
number of children, and nobody is their own grandpa — no cycles.

Same shape as: a file system (folders inside folders), an org chart,
HTML (`<body>` contains `<div>`s), JSON objects.

## The words, on one picture — memorize THIS tree

```
        4          <- root: the one node with no parent (depth 0)
       / \
      2   6        <- children of 4 · also parents of the row below
     / \ / \
    1  3 5  7      <- leaves: no children (depth 2)
```

- **node** — one circle. Seven of them here.
- **edge** — one line. Always `nodes − 1` = 6 here.
- **parent / child** — 4 is 2's parent; 2 is 4's child. Same link, two
  directions, like "mom" and "daughter" naming one relationship.
- **leaf** — 1, 3, 5, 7: the endpoints that stop the branches.
- **internal node** — 4, 2, 6: anything with children.
- **siblings** — 1 and 3 share parent 2.
- **subtree** — "2 plus everything under it" is itself a complete,
  perfectly good tree. That one fact powers the whole lesson.
- **depth** of a node — edges DOWN from the root. Root = 0; leaves = 2.
- **height** of a node — edges down to its deepest leaf. Leaf = 0;
  the root's height IS the tree's height = 2 here.
- **binary tree** — every node has at most TWO children, named `left`
  and `right`. Everything in this lesson is binary.

⚠ **Convention check:** some sources count *nodes* for height, others
count *edges* (leaf = 1 vs leaf = 0). Our problem files count **nodes**
for `max_depth` (empty tree = 0, single node = 1). Both give
"≈ log₂ n" for balanced trees — just ask which ruler is in use.

## The words in code (a taste — next chapter builds properly)

```python
class TreeNode:                    # a node is just 3 slots
    def __init__(self, val=0, left=None, right=None):
        self.val = val             # the value this box holds
        self.left = left           # left child: a node or None
        self.right = right         # right child

root = TreeNode(4)                 # a lonely root
root.left = TreeNode(2)            # give it a left child
print(root.val, root.left.val)     # 4 2 — parent reaches child
```

## Why it exists

Lists store things in a line — item, next, next. But most real data is
**hierarchical**: one thing owns several things, which each own several
things. A tree is the smallest shape that captures "contains,
recursively."

## Where it's used

File systems, the DOM (every webpage is a tree), JSON/XML parsers,
database indexes (B-trees), compilers (`2 + 3 * 4` parses into a tree
so `*` binds tighter), autocomplete tries, chess move-trees.

## Common mistake

Saying a node "is" its child. `root.left` isn't the *value* 2 —
`root.left.val` is the 2; `root.left` is a whole 3-node subtree. Tree
code constantly zooms into subtrees; keep that in mind.

## Your turn

In the tree above: what's the depth of node 5, and the height of
node 6 (counting edges)?

<details><summary>Answer</summary>
Depth of 5 = 2 (two edges down: 4→6, 6→5). Height of 6 = 1 (one edge
down to its deepest leaf, either 5 or 7).
</details>

---

**Next →** [02 — A binary tree in code](02-tree-in-code.md)
