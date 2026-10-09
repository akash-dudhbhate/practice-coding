# 06 — Insert & Delete: Pointer Rewiring

> 5-minute read. Where linked lists earn their keep.

## The idea, plain words

To insert or delete a node, you don't move data — you **redraw arrows**.
Delete node X = make the node *before* X point to the node *after* X.
The victim isn't "removed" — it's just **skipped**, so nothing points at
it anymore.

## Real-life analogy

A conga line. To remove a person, the dancer in front of them grabs the
hand of the person *behind* them. Nobody moves their feet — one handhold
changes, and the middle person is out of the line.

## Delete — watch the arrows

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

head = Node(1, Node(2, Node(3)))   # 1 -> 2 -> 3 -> None
print("before:", to_list(head))

# delete the node AFTER head (the "2")
prev = head                        # node before the victim
victim = prev.next                 # node 2 — rescue it first
prev.next = victim.next            # 1's arrow jumps over 2, lands on 3
victim.next = None                 # optional: tidy the orphan

print("after: ", to_list(head))
```

Output:

```
before: [1, 2, 3]
after:  [1, 3]
```

Hand-trace the rewire:

```
before:   1 -> 2 -> 3 -> None
          prev  victim

prev.next = victim.next
          1 -------> 3 -> None
          prev      (2 is bypassed — nothing points at it)
```

**Cost: O(1)** — once you're standing at `prev`. Compare with an array:
deleting `nums[1]` shifts 3, 4, 5... one slot left — O(n) of moving data.

## Insert — same idea, two arrows

```python
# given prev = the node holding 1, in the list 1 -> 3 -> None:
new = Node(99)
new.next = prev.next    # 1. new node's arrow lands on what prev pointed to
prev.next = new         # 2. prev's arrow lands on new
# result: 1 -> 99 -> 3    ORDER MATTERS — see the mistake below
```

## Why it exists

This is the *benefit* side of the chapter-02 trade: O(1) rewrites instead
of O(n) shifting. Deleting the head is even simpler — `head = head.next`
— one line, no shifting.

## Where it's used

Remove-nth-from-end, partition lists, LRU cache evictions, reorder,
merge — nearly every problem is "find the right spot, then rewire."

## Common mistake

Doing step 2 before step 1 on insert:

```python
# WRONG ORDER — same setup (prev = node 1, new = Node(99)):
prev.next = new         # prev's arrow moved — but we never saved where it pointed!
new.next = prev.next    # now points at new itself -> tiny self-loop, rest LOST
```

Golden rule: **before overwriting any `.next`, make sure someone else is
holding whatever it pointed to.** Lost references are the #1 linked-list
bug — the bypassed nodes get garbage-collected and are unrecoverable.

## Your turn

On `1 -> 2 -> 3 -> None`, you run `head.next = head.next.next`. What does
the list look like now?

<details><summary>Answer</summary>
`1 -> 3 -> None`. `head.next` pointed at node 2; `head.next.next` is node
3 — so node 1's arrow jumps over 2 straight to 3. Node 2 is orphaned.
(And because node 1 IS `head`, this works — no `prev` needed when deleting
the second node.)
</details>

---

**← Prev** [05 — No index](05-no-index-lookup-on.md) ·
**Next →** [07 — The dummy node trick](07-the-dummy-node.md)
