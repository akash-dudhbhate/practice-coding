# 02 — Array vs Linked List: the Memory Picture

> 4-minute read.

## The idea, plain words

An **array** (Python `list`) is one long row of numbered boxes sitting
side by side in memory. A **linked list** is a scatter of boxes anywhere
in memory, each holding a note saying where the next box lives.

## Real-life analogy

- **Array = a bookshelf.** Books sit shoulder-to-shoulder in numbered
  slots. Want slot 3? Grab it instantly. Want to *insert* a book in the
  middle? You must slide every book after it one slot over.
- **Linked list = a scavenger hunt.** Each item can be hidden anywhere;
  each one tells you where to look next. Inserting a new clue = rewrite
  one card. Nobody has to shift.

## The picture — memorize this

```
ARRAY (contiguous memory)                 LINKED LIST (scattered nodes)

 index   0    1    2    3                 head
        [10][20][30][40]                   |
        ^ jump straight to [2]             v
        O(1) by index                   +---+    +---+    +---+
                                        |10 |--->|20 |--->|30 |---> None
                                        +---+    +---+    +---+
                                        reach node 2 by walking:
                                        head -> next -> next   O(i)
```

Same data, different layout:

- **Array:** the boxes are neighbors → Python can compute "slot 2's
  address" directly → `nums[2]` is instant.
- **Linked list:** the boxes are scattered → the ONLY way to find node 2
  is to start at `head` and follow arrows.

## What it buys and costs

| Operation | Array | Linked list |
|-----------|-------|-------------|
| Get item i | O(1) — jump straight there | O(n) — walk from head |
| Insert/delete at front | O(n) — shift everything | O(1) — rewire one arrow |
| Insert/delete in middle | O(n) — shift | O(1) *once you're at the node* |
| Extra memory | just the data | + one pointer per node |

The trade, in one sentence: **linked lists swap instant indexing for
instant rewiring.**

## Why it exists

Arrays are terrible when items arrive/leave unpredictably in the middle or
front — every insert is a furniture-moving day. A linked list makes
"insert here" cost one arrow change. That's why queues, caches, and undo
stacks love it.

## Where it's used

You'll choose between these two shapes all through DSA. Interviewers ask
"array or linked list?" precisely because the trade-off is the point.

## Common mistake

Writing `head[2]`. There is no index — that line throws a `TypeError`.
If you catch yourself wanting `list[i]`, remember: you're walking, not
indexing.

## Your turn

To reach the 1000th item: which is faster, array or linked list? To insert
a new item at the very FRONT: which is faster?

<details><summary>Answer</summary>
Reaching item 1000: **array** (O(1) index vs O(n) walk). Inserting at the
front: **linked list** (O(1) rewire vs O(n) shift of every element).
</details>

---

**← Prev** [01 — What is a node?](01-what-is-a-node.md) ·
**Next →** [03 — Building a list in Python](03-building-a-list.md)
