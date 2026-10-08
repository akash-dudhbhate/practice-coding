# Lesson 07 — Linked Lists

## What you'll learn
- Nodes + pointers vs contiguous arrays (no O(1) indexing — you walk)
- Building a `Node` class plus `build_list` / `to_list` test helpers
- Iterative reversal with the prev/curr/nxt rescue pattern
- Fast & slow pointers: middle finding and Floyd's cycle detection
- The dummy-node trick for merging and splicing

## Lesson

A linked list is a chain of nodes — each holds a value and a `.next`
pointer. No index: position questions ("middle", "nth from end") are
answered by pointer speed, not arithmetic.

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### The helpers you'll write first

```python
def build_list(values):          # [1,2,3] -> 1->2->3->None
    dummy = Node()
    tail = dummy
    for v in values:
        tail.next = Node(v)
        tail = tail.next
    return dummy.next

def to_list(head):               # 1->2->3->None -> [1,2,3]
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out
```

### Reversal — the three-pointer dance

```python
prev, curr = None, head
while curr:
    nxt = curr.next      # rescue before overwriting!
    curr.next = prev
    prev = curr
    curr = nxt
# prev = new head
```

### Fast & slow

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next          # 1 hop
    fast = fast.next.next     # 2 hops
# cycle? -> slow is fast eventually. no cycle? -> fast hits None.
# middle? -> slow is at the midpoint when fast falls off.
```

### Dummy-node merge

```python
dummy = Node(); tail = dummy
while a and b:
    if a.val <= b.val: tail.next, a = a, a.next
    else:              tail.next, b = b, b.next
    tail = tail.next
tail.next = a or b
return dummy.next
```

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.
Every file is self-contained — define `Node` and helpers in each file as
needed. The checker feeds you nodes it builds itself (anything with `.val`
and `.next` works) and walks your returned head the same way.

### Easy (start here)
1. `easy/p01-build-linked-list.py` — Write `build_list(values)` returning the head of a chain built in order: `[1,2,3]` → `1→2→3→None`; `[]` → `None`.
2. `easy/p02-traverse-to-list.py` — Write `to_list(head)` collecting node values into a Python list: `1→2→3→4` → `[1,2,3,4]`; `None` → `[]`.
3. `easy/p03-find-middle.py` — Write `find_middle(head)` returning the middle node's VALUE via fast/slow: `1→2→3→4→5` → `3`; even length returns the SECOND middle: `1→2→3→4` → `3`.

### Medium
4. `medium/p01-reverse-iterative.py` — Write `reverse_list(head)` reversing in place with prev/curr/nxt: `1→2→3→4→5` → `5→4→3→2→1`; `None` → `None`.
5. `medium/p02-detect-cycle.py` — Write `has_cycle(head)` (Floyd's, O(1) space): a list whose tail points back to an earlier node → `True`; a normal list → `False`.
6. `medium/p03-merge-two-sorted.py` — Write `merge_two(a, b)` merging two sorted lists with a dummy node: `1→2→4` + `1→3→4` → `1→1→2→3→4→4`; hook the leftover tail with `a or b`.

### Hard
7. `hard/p01-remove-nth-from-end.py` — Write `remove_nth(head, n)` removing the nth node FROM THE END in ONE pass: `[1,2,3,4,5], n=2` → `1→2→3→5`. Fast starts n steps ahead of slow; a dummy absorbs the "remove the head" edge case.
8. `hard/p02-reorder-list.py` — Write `reorder_list(head)` mutating the list to `L0→Ln→L1→Ln-1→…`: `1→2→3→4` → `1→4→2→3`; `1→2,3,4,5` → `1→5→2→4→3`. Three moves you already know: find middle (fast/slow), reverse second half, interleave.
9. `hard/p03-reverse-k-group.py` — Write `reverse_k_group(head, k)` reversing each block of k nodes; a short tail (< k) stays put: `[1,2,3,4,5], k=2` → `2→1→4→3→5`; `k=3` → `3→2→1→4→5`. Count k nodes before committing to a reversal.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker —
  including the `Node` class; the checker uses its own nodes, so yours only
  need `.val` and `.next` attributes.
- Remove the TODO line when done.
- Run `python3 check.py <level>/<pNN>` to test one problem, `python3 check.py all` for everything.
- `coding-check.md` is your manual checklist; `EXTRA-PRACTICE.md` has drills.
- Solutions live in `<level>/solutions/` — look only AFTER trying.
