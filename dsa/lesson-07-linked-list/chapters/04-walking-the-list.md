# 04 — Walking the List: `curr = curr.next`

> 4-minute read. THE loop of this lesson — learn it cold.

## The idea, plain words

Traversal means visiting every node. There's exactly one way to move
forward: **follow the `.next` arrow.** The loop is always the same shape:

```python
curr = head          # a pointer named "curr" (current), starts at head
while curr is not None:
    # ... visit curr ...
    curr = curr.next # hop to the next node
```

## Run it and trace it

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# hand-build 1 -> 2 -> 3 -> None
head = Node(1, Node(2, Node(3)))

curr = head
while curr is not None:
    print(curr.val)
    curr = curr.next
```

Output:

```
1
2
3
```

Hand-trace — watch `curr` move down the chain:

```
list:   1 -> 2 -> 3 -> None

start:  curr=1        prints 1
hop 1:  curr=2        prints 2
hop 2:  curr=3        prints 3
hop 3:  curr=None     loop condition fails -> stop
```

Three hops, one pointer move each. When `curr` becomes `None`, we've
fallen off the end — that's the exit signal, not an error.

## Why it exists

There is no `for i in range(len(list))` here — no index, no `len()`. The
`while curr` walk IS the `for` loop of linked lists. Every problem starts
with this skeleton: find, sum, print, delete — all are "walk and do
something at each node."

## Where it's used

Literally every linked-list function ever written. Variations you'll meet:
`while curr.next` (stop BEFORE the end — for deletes), and two walkers at
different speeds (chapter 08).

## Common mistake

```python
# BAD PATTERN — given head = Node(1, Node(2, Node(3))):
while head is not None:   # works, BUT...
    head = head.next      # you moved the head itself!
```

It prints fine — but `head` now points at `None` and **your list is gone
from the caller's point of view.** Always copy `head` into `curr` and move
`curr`. The head is the door handle; don't carry it around.

## Your turn

```python
# given head = Node(1, Node(2, Node(3))) — the 1 -> 2 -> 3 chain:
curr = head          # start at node 1
while curr:
    curr = curr.next
print(curr)          # what prints?
```

<details><summary>Answer</summary>
`None`. The loop keeps hopping until `curr` falls off the end. `while curr`
is shorthand for `while curr is not None` — a `Node` is always truthy,
`None` is falsy.
</details>

---

**← Prev** [03 — Building a list](03-building-a-list.md) ·
**Next →** [05 — No index: why lookup is O(n)](05-no-index-lookup-on.md)
