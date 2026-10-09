# 03 — Three Ways to Walk a Tree: pre / in / post

> 6-minute read. THE most-confused topic of the lesson — go slow.

## The idea, plain words

A list has one obvious walk: left to right. A tree doesn't — from any
node you could visit the node itself first, or dive left first. So
"traverse" (visit every node exactly once) needs an agreed order.

All three DFS orders do the same dive — **left subtree fully, then
right subtree** — and differ in ONE thing: **when you visit the node
itself.**

Picture three slots per node: `L  V  R` (left, visit, right). Each
order just parks `V` in a different slot:

| order | slots | nickname | classic use |
|-------|-------|----------|-------------|
| preorder | **V** L R | "me first" | copy / serialize a tree |
| inorder | L **V** R | "me in the middle" | BST → sorted (ch. 10!) |
| postorder | L R **V** | "me last" | delete tree, folder sizes |

## Same tree, traced three ways — follow with a finger

```
        4
       / \
      2   6
     / \ / \
    1  3 5  7

preorder  (V,L,R):  4 2 1 3 6 5 7
inorder   (L,V,R):  1 2 3 4 5 6 7    <- suspiciously sorted… ch. 10
postorder (L,R,V):  1 3 2 5 7 6 4
```

Finger-trace preorder: visit 4; dive left — visit 2, dive to 1, back
up, visit 3; back to 4, dive right — visit 6, then 5, then 7. Always
"visit, then fully-left, then fully-right."

## In code — one line moves

```python
def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

Spot it? **The only thing that moves is where `[root.val]` sits** —
before both halves, between them, or after them. Everything else is
identical.

```python
# root = the same 7-node tree from chapter 02
print(preorder(root))    # [4, 2, 1, 3, 6, 5, 7]
print(inorder(root))     # [1, 2, 3, 4, 5, 6, 7]
print(postorder(root))   # [1, 3, 2, 5, 7, 6, 4]
```

## Why it exists

Different questions need the root at different moments:

- **Copy this tree** — parent must exist before children can attach →
  preorder.
- **Folder's total size** — a folder can't report until its children
  report → postorder (that's how `du` and `rm -r` really work).
- **Print a BST sorted** — left is all-smaller, right is all-larger,
  so the node belongs in the middle → inorder.

## Common mistake

Memorizing outputs instead of the picture. In an interview you'll get
a NEW tree — if you memorized `1 2 3 4 5 6 7` you freeze. The
finger-trace with `L V R` slots is the real skill.

## Your turn

On our tree, which order visits the root 4 last — and what does it
print right before the 4?

<details><summary>Answer</summary>
Postorder — it's "me last" by definition. Right before the 4 it
prints 6 (the last item of the right subtree's postorder: 5, 7, 6).
</details>

---

**← Prev** [02 — A binary tree in code](02-tree-in-code.md) ·
**Next →** [04 — Level-order (BFS)](04-bfs-level-order.md)
