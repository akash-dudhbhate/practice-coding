# 01 — What is a Node?

> 4-minute read. One idea only.

## The idea, plain words

A **node** is a tiny bundle of two things:

1. a **value** — the data it carries, and
2. an **arrow** — a pointer to the *next* node.

That's the whole thing. No index, no position number. Just "what I hold"
and "who comes after me."

## Real-life analogy

Think of a **treasure hunt**. Each clue card says two things: a fun fact,
and where the NEXT clue is hidden. You can't jump to clue #3 directly —
you have to follow clue #1, which leads to clue #2, which leads to clue #3.
If a clue gets lost, everything after it is unreachable. The hunt ends when
a clue says "there's nothing after me."

A linked list is a treasure hunt made of nodes.

## The smallest possible version

In Python a node is just an object with two attributes:

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val    # the data
        self.next = next  # arrow to the next node (None = end of the line)

n3 = Node(3)              # last node: arrow points at None
n2 = Node(2, n3)          # n2's arrow points at n3
n1 = Node(1, n2)          # n1's arrow points at n2

print(n1.val)             # 1
print(n1.next.val)        # 2  — followed the arrow once
print(n1.next.next.val)   # 3  — followed it twice
print(n1.next.next.next)  # None — the "nothing after me" card
```

Output:

```
1
2
3
None
```

## Picture it

```
head
  |
  v
+---+      +---+      +---+
| 1 | ---> | 2 | ---> | 3 | ---> None
+---+      +---+      +---+
```

Every box is a node. Every `--->` is a `.next` arrow stored *inside* the
node. `None` is the wall at the end of the treasure hunt.

## Why it exists

Arrays keep all items in one big row of numbered slots. Sometimes you don't
want a numbered row — you want a chain you can grow, shrink, and rewire one
link at a time. The node is the smallest piece of that chain.

## Where it's used

Every problem in this lesson. Also real systems: browser history, undo
stacks, LRU caches, graph adjacency lists — anywhere a chain of "things
pointing at things" is the natural shape.

## Common mistake

Thinking `n1.next` is *the node after n1* forever. `.next` is just a
variable — you can re-point it (`n1.next = n3`), which is exactly how
deletes and reversals work. Arrows are rewritable, and that power is the
whole point.

## Your turn

With `n1 -> n2 -> n3` as above, what does `print(n1.next.next)` give —
`3`, `n3`, or `None`?

<details><summary>Answer</summary>
It gives `n3` — the node OBJECT itself, not its value. `n1.next.next` is
node 3 (prints something like `<Node object ...>`). You'd need
`n1.next.next.val` to get `3`.
</details>

---

**Next →** [02 — Array vs linked list: the memory picture](02-array-vs-linked-list.md)
