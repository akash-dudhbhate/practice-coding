# 03 — Building a List in Python

> 4-minute read.

## The idea, plain words

Python has no built-in linked list, so we build the chain ourselves: a
`Node` class, one node per value, and a **`head`** variable that holds
the very first node. Lose `head` and the whole list is gone — it's the
only door in.

## The two helpers every problem uses

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(values):
    """[1, 2, 3]  ->  1 -> 2 -> 3 -> None, returns the head."""
    dummy = Node()           # fake node BEFORE the real head
    tail = dummy             # tail always points at the LAST node
    for v in values:
        tail.next = Node(v)  # hang a new node off the end
        tail = tail.next     # advance tail to it
    return dummy.next        # the real head = node after the fake

def to_list(head):
    """1 -> 2 -> 3 -> None  ->  [1, 2, 3], for printing/testing."""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

head = build_list([1, 2, 3])
print(to_list(head))         # [1, 2, 3]
print(to_list(build_list([])))  # []
```

Output:

```
[1, 2, 3]
[]
```

## Hand-trace `build_list([1, 2, 3])`

```
start:   dummy            tail=dummy
v=1:     dummy -> 1       tail=1
v=2:     dummy -> 1 -> 2  tail=2
v=3:     dummy -> 1 -> 2 -> 3   tail=3
return dummy.next  ->  the node holding 1 (skip the fake)
```

`dummy` is a throwaway node that gives `tail` something to hang the first
real node on — so empty lists and non-empty lists share one code path.
Chapter 07 gives it a full page; for now just nod and move on.

## Why it exists

You can't `print` a linked list (it shows `<Node object at 0x...>`) and
you can't hand-wire nodes for every test. `build_list`/`to_list` turn
"does my function work?" into one line: `to_list(my_func(build_list([1,2,3])))`.
Every problem in `easy/`→`hard/` assumes these two helpers.

## Where it's used

All 8 problems this lesson — plus real code: serializers, test fixtures,
debug `__repr__` methods.

## Common mistake

**Losing the head.** If you write `head = head.next` while building and
then `return head`, you return the TAIL — a 1-node list. Keep one pointer
(`dummy`) anchored at the start; only `tail` may move.

## Your turn

`build_list([7])` — what does `to_list` return, and where does `tail`
end up?

<details><summary>Answer</summary>
`to_list` returns `[7]`. `tail` ends on the node holding `7` (the only
real node), while `dummy.next` points at it. `tail` and `dummy.next`
are the same node — normal for a 1-element list.
</details>

---

**← Prev** [02 — Array vs linked list](02-array-vs-linked-list.md) ·
**Next →** [04 — Walking the list](04-walking-the-list.md)
