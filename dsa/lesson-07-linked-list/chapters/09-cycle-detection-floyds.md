# 09 — Cycle Detection: Floyd's Algorithm

> 5-minute read. The meeting, step by step.

## The idea, plain words

A **cycle** is when some node's arrow points *backward* into the list, so
a walker goes around in circles forever instead of hitting `None`.

Floyd's trick: run `slow` (1 hop) and `fast` (2 hops) together. If there's
a cycle, `fast` eventually **laps** `slow` inside the loop — they land on
the same node. If `fast` ever reaches `None`, there's no cycle.

## Real-life analogy

Two runners on a circular track. The faster one gains a full lap on the
slower one eventually — they WILL cross paths. On a straight track (no
cycle), the fast runner just finishes and the slow one never sees them
again.

## The cycle we'll trace

```
1 -> 2 -> 3 -> 4
          ^    |
          |    v
          6 <- 5          (node 6's arrow points BACK to node 3)
```

## Run it

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:        # 'is' — same NODE, not same value!
            return True
    return False                # fast ran off the end

# build 1->2->3->4->5->6, then point 6 back at 3  -> cycle!
n1 = Node(1); n2 = Node(2); n3 = Node(3)
n4 = Node(4); n5 = Node(5); n6 = Node(6)
n1.next = n2; n2.next = n3; n3.next = n4
n4.next = n5; n5.next = n6; n6.next = n3   # the back-arrow

straight = Node(1, Node(2, Node(3)))       # 1->2->3->None — no cycle

print(has_cycle(n1))        # True  — they meet inside the loop
print(has_cycle(straight))  # False — fast falls off the end
```

Output:

```
True
False
```

## The meeting, step by step

```
round 0:  slow=1  fast=1
round 1:  slow=2  fast=3
round 2:  slow=3  fast=5
round 3:  slow=4  fast=3    (fast lapped! 5->6->3)
round 4:  slow=5  fast=5    slow is fast -> CYCLE FOUND
```

Why must they meet? Inside the loop, `fast` gains exactly **1 node per
round** on `slow`. On a circle, a pursuer gaining 1 per step can't skip
past — it must land on the same node. So "met" ⇔ "cycle exists."

## Why it exists

The naive fix is a `set` of visited nodes (`if node in seen`), which works
but costs **O(n) memory**. Floyd's answers the same question in **O(1)
space** — two pointers, nothing stored. When an interviewer says "do it in
constant space," this is the expected answer.

## Where it's used

Cycle detection (LeetCode 141), finding *where* a cycle starts (142 —
second phase of the same trick), happy-number detection, and anywhere a
graph-like structure might loop back on itself.

## Common mistake

- `slow == fast` instead of `slow is fast`. You care about **same node
  object**, not same value — two different nodes can both hold `7`. `is`
  is the correct, honest check.
- `while fast.next` alone — if `fast` becomes `None`, `fast.next` crashes.
  Need both halves: `fast and fast.next`.

## Your turn

In the trace above, at round 3 fast "jumps" from 5 back to 3 (via 6).
Could fast ever jump *over* slow without landing on it — i.e., miss the
meeting forever?

<details><summary>Answer</summary>
No. Inside the loop both pointers stay in the cycle, and fast gains
exactly 1 node per round on slow. A relative speed of 1 means fast
visits every gap size — it closes the gap to 0 and lands ON slow, never
skips it. (A fast pointer moving 3+ steps per round COULD skip — that's
why the trick specifically uses speeds 1 and 2.)
</details>

---

**← Prev** [08 — Fast & slow: the middle](08-fast-and-slow-middle.md) ·
**Next →** [10 — Reversing a list](10-reversing-a-list.md)
