# 11 — Merge Two Sorted Lists & the Big Picture

> 5-minute read. The dummy node returns — then everything ties together.

## The idea, plain words

Zip two sorted chains into one sorted chain by repeatedly comparing front
nodes and attaching the smaller one — like merging two sorted stacks of
cards: look at both tops, take the smaller, repeat.

## Run it

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

def merge_two(a, b):
    dummy = Node()
    tail = dummy
    while a and b:                # both lists still have nodes
        if a.val <= b.val:
            tail.next = a; a = a.next
        else:
            tail.next = b; b = b.next
        tail = tail.next          # advance EVERY round
    tail.next = a or b            # hook whichever remainder survives
    return dummy.next             # the real head

a = Node(1, Node(3, Node(5)))     # 1 -> 3 -> 5
b = Node(2, Node(4))              # 2 -> 4
print(to_list(merge_two(a, b)))   # [1, 2, 3, 4, 5]
```

Output:

```
[1, 2, 3, 4, 5]
```

## The merge, step by step

```
list1: 1 -> 3 -> 5          list2: 2 -> 4
dummy -> ?                  tail = dummy

compare 1 vs 2: take 1   dummy->1,   tail=1
compare 3 vs 2: take 2   ...->2,     tail=2
compare 3 vs 4: take 3   ...->3,     tail=3
compare 5 vs 4: take 4   ...->4,     tail=4
list2 exhausted: tail.next = a -> hook ALL of list1's remainder -> ...->5
```

Notice the whole chapter-07 toolkit in action: `dummy` erases the
"first attach is special" problem, `tail.next = a or b` hooks the
survivor in one line (a `Node` is always truthy; the exhausted side is
`None`), and `tail` moves every round so nothing gets overwritten.

## The big picture — three muscles this lesson builds

1. **Pointer rescue** — before overwriting `node.next`, save it. Almost
   every linked-list bug is a lost reference (reversal's `nxt`, this
   merge's `tail` discipline).
2. **Dummy nodes** — whenever you build a chain whose head isn't known
   yet, a fake head makes the first splice identical to all others.
3. **Speed-ratio pointers** — fast/slow answers "middle", "cycle",
   "nth-from-end" without ever knowing the length.

Whenever a problem says **"in O(1) space"** or **"in one pass"** on a
linked list, the answer is almost always one of these three.

## Common mistake

Forgetting `tail.next = a or b` — the merged list silently drops the
un-merged tail of the longer input. The loop only runs while BOTH lists
have nodes; somebody's remainder is always left over.

## Your turn

In the merge, why is `a or b` safe? Could it pick the wrong list?

<details><summary>Answer</summary>
After `while a and b`, at least one of `a`, `b` is `None`. If `a` is
`None` (falsy), `a or b` returns `b`. If `a` is a node (always truthy —
objects are truthy), it returns `a`. Either way you get the non-exhausted
survivor — or `None` if both are done, which is also correct.
</details>

## What you now know

What a node is, why there's no index, how to walk (`curr = curr.next`),
rewire (insert/delete), erase edge cases (dummy), find position by ratio
(fast/slow), detect loops (Floyd's), flip arrows (reverse), and zip chains
(merge). **That's the whole lesson.** The problems in
`easy/`→`medium/`→`hard/` now drill exactly this.

---

**← Prev** [10 — Reversing a list](10-reversing-a-list.md) ·
Done with concepts? → Open `task-explanation.md` and solve `easy/p01` next.
