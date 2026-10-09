# 05 — No Index: Why Lookup is O(n)

> 3-minute read.

## The idea, plain words

An array knows where every item lives: `nums[500]` is one math operation
— "start address + 500 × slot size" → done. A linked list knows where
**one** node lives: `head`. Everything else must be reached on foot.

So finding the k-th node, or a node holding a target value, always means
walking from the front — up to **n hops**.

## Run it

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get(head, k):
    """Return the node at position k (0-based), or None."""
    curr = head
    for _ in range(k):        # hop k times
        if curr is None:
            return None       # k was past the end
        curr = curr.next
    return curr

head = Node(1, Node(2, Node(3)))   # 1 -> 2 -> 3 -> None
print(get(head, 0).val)            # 1 — zero hops
print(get(head, 2).val)            # 3 — two hops
print(get(head, 5))                # None — walked off the end
```

Output:

```
1
3
None
```

Hand-trace `get(head, 2)` on `1 -> 2 -> 3`:

```
curr=1  hop 1 -> curr=2  hop 2 -> curr=3   k=2 done -> return node 3
```

Two hops for index 2. For index *i* it's *i* hops — so worst case
(the last node, or a missing target) is **n hops → O(n)**.

## Why it exists

This is the *price* side of the chapter-02 trade. Linked lists gave up
random access to buy cheap inserts. It also explains a habit you'll see
everywhere: problems rarely ask for "the node at index k" — they ask for
the middle, a cycle, the nth-from-end, because those can be found by
clever *walking* instead of counting.

## Where it's used

Every "find" on a linked list: search a value, reach the tail, locate the
nth-from-end. Also the reason interviewers love asking "why is this O(n)
when the array version is O(1)?"

## Common mistake

Two, actually:

- `head[k]` — `TypeError`, no index exists.
- Forgetting the `curr is None` guard inside `get` — walking past the end
  makes `curr.next` crash with `AttributeError: 'NoneType'`. Always check
  the pointer exists *before* dereferencing it.

## Your turn

On `1 -> 2 -> 3 -> None`, how many `.next` hops does `get(head, 3)` take —
and what does it return?

<details><summary>Answer</summary>
It returns `None`. Trace: curr=1, hop→2, hop→3, hop→None — the guard
catches `curr is None` inside the loop and returns `None`. Index 3 is
one past the last node (length 3 means valid indices are 0–2).
</details>

---

**← Prev** [04 — Walking the list](04-walking-the-list.md) ·
**Next →** [06 — Insert & delete: pointer rewiring](06-insert-and-delete.md)
