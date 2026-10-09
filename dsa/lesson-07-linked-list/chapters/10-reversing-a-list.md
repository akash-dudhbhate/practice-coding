# 10 — Reversing a List: THE Iconic Walkthrough

> 5-minute read. If you learn one linked-list routine by heart, make it this one.

## The idea, plain words

Reverse = flip every arrow so the chain runs backwards. Three pointers do
it in one pass:

- `prev` — the part already reversed
- `curr` — the node whose arrow we're flipping right now
- `nxt` — a *rescue* pointer holding the rest of the list

## Real-life analogy

Reversing a conga line one dancer at a time: each dancer turns around and
grabs the hand of the person who was *behind* the already-turned group —
but only after a friend notes who was next in line, so nobody gets lost.

## The code — four lines in the loop

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

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next      # 1. RESCUE the rest of the list
        curr.next = prev     # 2. flip the arrow backward
        prev = curr          # 3. advance prev
        curr = nxt           # 4. advance curr via the rescue
    return prev              # prev is the new head (the old tail)

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(to_list(head))              # [1, 2, 3, 4, 5]
print(to_list(reverse_list(head)))# [5, 4, 3, 2, 1]
```

Output:

```
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
```

## Hand-trace `1 -> 2 -> 3 -> None` — memorize this picture

```
start:   None   1 -> 2 -> 3 -> None
         prev  curr
         (nxt = 2, rescue before we touch any arrow)

step 1:  None <- 1    2 -> 3 -> None
         prev=1?  no — watch labels:
                prev    curr        (prev=1, curr=2, nxt=3)

step 2:  None <- 1 <- 2    3 -> None
                       prev  curr   (prev=2, curr=3, nxt=None)

step 3:  None <- 1 <- 2 <- 3    curr=None -> loop ends
                              prev = node 3 = NEW HEAD
```

Pointer labels per round:

```
round | prev | curr | nxt  | action on curr.next
------|------|------|------|--------------------
  1   | None |  1   |  2   | 1.next = None
  2   |  1   |  2   |  3   | 2.next = 1
  3   |  2   |  3   | None | 3.next = 2
  end |  3   | None |  —   | return prev (3)
```

O(n) time, O(1) space. The same loop handles empty lists (skips, returns
`None`) and single nodes (flips `x.next` to `None`, returns `x`).

## Why it exists

Reversal is the *atom* of linked-list surgery — k-group reversal,
palindrome checks, and reorder all call on it. It's also the purest test
of "can you rewire pointers without losing nodes," which is why it's THE
most-asked linked-list interview question.

## Where it's used

LeetCode 206 directly; reverse-in-k-groups, add-two-numbers (digits stored
head-first), palindrome-via-reverse-second-half all build on it.

## Common mistake

Two classics:

- **Skipping the rescue:** `curr.next = prev` *before* `nxt = curr.next`.
  The moment you flip, the rest of the list has no incoming pointer →
  garbage-collected → you return a 1-node list.
- **`curr = curr.next` for step 4.** After the flip, `curr.next` points
  BACKWARD into the reversed part → you walk back and loop forever. Must
  advance via `nxt`.

## Your turn

Why does the function return `prev` and not `curr` or `head`?

<details><summary>Answer</summary>
When the loop ends, `curr` is `None` (it walked off the end) and `head`
still points at the OLD first node — which is now the tail. `prev` is
sitting on the last node processed = the old tail = the new head.
</details>

---

**← Prev** [09 — Cycle detection](09-cycle-detection-floyds.md) ·
**Next →** [11 — Merge & the big picture](11-merge-and-big-picture.md)
