# 08 — Fast & Slow Pointers: the Middle

> 4-minute read.

## The idea, plain words

Walk the list with **two pointers at different speeds**: `slow` hops 1
node per round, `fast` hops 2. When `fast` falls off the end, `slow` —
moving exactly half as fast — is standing on the **middle node**.

No counting, no length, no index. Just a speed ratio.

## Real-life analogy

Two hikers leave a trailhead together; one hikes twice as fast as the
other. When the fast hiker reaches the end of the trail, the slow one is
standing exactly at the halfway point — without anyone measuring distance.

## Run it

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle(head):
    slow = fast = head
    while fast and fast.next:   # fast needs TWO hops available
        slow = slow.next        # 1 hop
        fast = fast.next.next   # 2 hops
    return slow                 # fast fell off -> slow is mid

odd  = Node(1, Node(2, Node(3, Node(4, Node(5)))))   # 1->2->3->4->5
even = Node(1, Node(2, Node(3, Node(4))))            # 1->2->3->4
print(middle(odd).val)           # 3
print(middle(even).val)          # 3 — the SECOND middle (usually what you want)
```

Output:

```
3
3
```

## Hand-trace on `1 -> 2 -> 3 -> 4 -> 5 -> None`

```
start:   slow=1  fast=1
round 1: slow=2  fast=3     (fast can still go: fast.next = 4)
round 2: slow=3  fast=5     (fast.next = None -> loop ends)
return slow -> node 3  ✓ the middle
```

Fast covers ground twice as fast → when it has run the full list, slow has
run half of it. On even-length lists the loop ends one round earlier, so
slow lands on the second of the two middles (`3` in `1->2->3->4`).

## Why it exists

"Find the middle" is impossible without knowing the length — and the only
way to know the length is a full O(n) counting pass, then a second pass to
stop at n/2. Fast/slow does it in **one pass** and never counts anything.
That "answer a positional question by ratio, not counting" idea is what
makes it a classic.

## Where it's used

Middle-of-list, palindrome checks (split the list at mid), and the same
machinery powers cycle detection (next chapter) and nth-from-end.

## Common mistake

`while fast.next` instead of `while fast and fast.next`. When `fast`
becomes `None`, `fast.next` crashes with `AttributeError`. You must check
`fast` exists AND `fast.next` exists — because fast needs *two* safe hops.

## Your turn

On `1 -> 2 -> None`, trace the loop: where do slow and fast end, and what
does `middle` return?

<details><summary>Answer</summary>
Start: slow=1, fast=1. Round 1: slow=2, fast=None (1.next.next). Loop
condition `fast and fast.next` fails → return slow = node **2**. On a
2-node list the "middle" is the second node — the same second-middle
rule as even lists.
</details>

---

**← Prev** [07 — The dummy node trick](07-the-dummy-node.md) ·
**Next →** [09 — Cycle detection: Floyd's](09-cycle-detection-floyds.md)
