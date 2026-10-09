# 07 — The Dummy Node Trick

> 4-minute read. A tiny object that deletes half your edge cases.

## The idea, plain words

A **dummy node** (a.k.a. *sentinel*) is a fake node parked *before* the
real head. It holds no meaningful data — its only job is to exist, so
that "the first real node" stops being a special case.

## Real-life analogy

A train's **locomotive**. The engine pulls the cars but carries no
passengers. The first passenger car is "the car after the engine" — same
as every other coupling. Without the engine, the first car needs special
handling ("wait, which car is first?").

## The problem it solves

Chapter 06's delete had a hidden wrinkle: to delete a node you need the
node *before* it. But the **head has no node before it** — so deleting the
head needs its own `if`:

```python
# WITHOUT dummy (sketch): head is a special case needing its own branch
if node_to_remove is head:
    head = head.next          # different code path!
else:
    prev.next = prev.next.next
```

With a dummy, the head is just "the node after dummy" — same code for
every position:

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def remove_value(head, target):
    dummy = Node(next=head)   # fake node parked before the real head
    prev = dummy
    while prev.next:                    # while there's a node after prev
        if prev.next.val == target:     # that node is the victim
            prev.next = prev.next.next  # hop over it
        else:
            prev = prev.next            # advance
    return dummy.next                   # real head may have changed!

head = Node(1, Node(2, Node(3)))
print(to_list(remove_value(head, 2)))   # [1, 3] — deleted a middle node

head = Node(1, Node(2, Node(3)))        # rebuild a fresh 1 -> 2 -> 3
print(to_list(remove_value(head, 1)))   # [2, 3] — head deleted, NO special case
```

Output:

```
[1, 3]
[2, 3]
```

Hand-trace `remove_value(head, 1)` — deleting the HEAD without special
casing:

```
start:  dummy -> 1 -> 2 -> 3 -> None
        prev      prev.next = node 1 (the victim)

prev.next = prev.next.next:
        dummy -> 2 -> 3 -> None        (1 is bypassed)
return dummy.next  ->  node 2 is the new head
```

You met dummy once already — in `build_list` (ch. 03) it gave `tail`
somewhere to hang the first node. Same trick, two uses.

## Why it exists

Two situations scream "use a dummy":

1. **The head itself might change** — delete/remove functions (above).
2. **You're building a chain whose head doesn't exist yet** — `build_list`,
   merging (ch. 11). `tail = dummy` makes the first attach identical to
   all later ones.

## Where it's used

Remove-nth-from-end, merge two sorted lists, partition, k-group reversal —
anywhere "the first node is awkward." Interviewers notice when you reach
for a dummy: it means you know where edge cases hide.

## Common mistake

Returning `head` instead of `dummy.next`. If the head was deleted, your
old `head` variable still points at the dead node. `dummy.next` always
tracks the *current* real head — that's the whole point of parking the
dummy there.

## Your turn

In `remove_value`, why does the loop check `prev.next` instead of `prev`?

<details><summary>Answer</summary>
Because deletes need to stand on the node BEFORE the victim. `prev.next`
is the candidate victim; `prev` is the rewiring tool. If we advanced
`prev` onto the victim, we'd have no handle to the node before it.
</details>

---

**← Prev** [06 — Insert & delete](06-insert-and-delete.md) ·
**Next →** [08 — Fast & slow pointers: the middle](08-fast-and-slow-middle.md)
