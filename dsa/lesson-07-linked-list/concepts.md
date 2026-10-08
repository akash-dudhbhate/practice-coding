# Lesson 07 — Concepts Explained (Linked Lists)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What a Linked List Is (vs an Array)

**What:** A linked list is a chain of *nodes*. Each node holds a value and a
pointer to the next node — that's it. There is no index, no contiguous block,
no `list[i]`. You only ever hold the *head* (first node) and walk forward one
`.next` at a time.

**Why it exists:** Arrays are great at random access but terrible at mid-list
insert/delete (everything shifts). A linked list trades O(1) indexing for
O(1) pointer rewiring: once you're *at* a node, inserting or deleting after
it costs one pointer change, no shifting.

**Where it's used:** Anything that grows/shrinks unpredictably at the ends or
middle — LRU cache chains, browser history, undo stacks, adjacency lists in
graphs, free-lists inside memory allocators. In interviews it's the #1
vehicle for testing pointer discipline.

```
ARRAY (contiguous memory)                 LINKED LIST (scattered nodes)

 index   0    1    2    3                 head
        [10][20][30][40]                   |
        ^ jump straight to [2]             v
        O(1) by index                   +---+    +---+    +---+
                                        |10 |--->|20 |--->|30 |---> None
                                        +---+    +---+    +---+
                                        reach node 2 by walking:
                                        head -> next -> next   O(i)
```

**What goes wrong without it:**
- `head[i]` does not exist. Beginners write `head[2]` and get a TypeError —
  or worse, simulate it with a loop without realizing why it's needed.
- Comparing nodes by VALUE instead of identity. Two different nodes can both
  hold `7`. Cycles and merges care about *which node*, not *which value*.
- Forgetting that `head` is just a pointer: if you rewire `head.next` before
  saving a reference to the old next node, the rest of the list is lost
  forever. Lost references = the classic linked-list bug.

**Worked example — walking instead of indexing:**

```python
node = head          # start at the front
while node is not None:
    print(node.val)  # visit
    node = node.next # the ONLY way forward
# prints 10, 20, 30 — then node becomes None and the loop stops
```

**Expected output:** `10 20 30` — three hops, one pointer move each.

---

## Building a Node Class and List Helpers

**What:** Python has no built-in linked list, so we make one:

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val      # the data
        self.next = next    # pointer to the next node (or None = end)
```

Two helpers make everything testable: `build_list(values)` converts
`[1,2,3]` into a chain and returns the head; `to_list(head)` walks the chain
and returns `[1,2,3]` again. They're the list↔list bridge every problem uses.

**Why it exists:** You can't `print` a linked list usefully, and you can't
hand-write nodes for every test. Build/walk helpers turn "does my function
work?" into a one-line assertion.

**Where it's used:** Every single problem in this lesson. Also real code:
serializers, test fixtures, `repr` for debugging.

**What goes wrong without it:**
- Building the chain backwards (each new node prepended) → tests feed you
  `[1,2,3]` and your function sees `3→2→1`.
- Losing the head: if you move `head` forward while building and return it,
  you return the TAIL. Always keep one pointer anchored at the start.
- Comparing with `==` on nodes you haven't defined `__eq__` for — compares
  identity, not values. That's why `to_list` exists: compare values, not nodes.

**Worked example — the dummy-tail build pattern:**

```python
def build_list(values):
    dummy = Node()          # fake node before the real head
    tail = dummy            # tail always points at the LAST node
    for v in values:
        tail.next = Node(v) # hang a new node off the end
        tail = tail.next    # advance tail
    return dummy.next       # real head = node after the fake

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

to_list(build_list([1, 2, 3]))   # [1, 2, 3]
to_list(build_list([]))          # []
```

`dummy` deserves attention: it's a throwaway node whose only job is giving
`tail` something to hang the first real node on — so the empty case and the
non-empty case share one code path. We'll meet it again in merging.

---

## Pointer Surgery: Reversing a List Iteratively

**What:** Flip every `.next` arrow so the list runs backwards. Three pointers
do it in one pass: `prev` (what we've reversed so far), `curr` (the node
we're flipping), `nxt` (rescued pointer to the rest of the list).

**Why it exists:** Reversal is the atom of linked-list surgery — k-group
reversal, palindrome checks, and reorder all call on it. It's also THE
interview question for "can you move pointers without losing nodes."

**Where it's used:** Any "process the list backwards" problem — reverse in
k-groups, add two numbers stored digit-head-first, palindrome via
reverse-the-second-half.

**The walkthrough — reversing 1→2→3→None:**

```
start:   None   1 -> 2 -> 3 -> None
         prev  curr  nxt

step 1:  save nxt=2, flip curr.next to prev
         None <- 1    2 -> 3 -> None
                prev  curr
step 2:  None <- 1 <- 2    3 -> None
                       prev  curr
step 3:  None <- 1 <- 2 <- 3    curr=None -> done
                              prev=new head
```

```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next      # 1. RESCUE the rest of the list
        curr.next = prev     # 2. flip the arrow
        prev = curr          # 3. advance prev
        curr = nxt           # 4. advance curr via the rescue
    return prev              # prev is the new head (old tail)
```

**What goes wrong without it:**
- Skipping step 1: `curr.next = prev` *before* saving `curr.next` → the rest
  of the list is garbage-collected. You return a 1-node list.
- `curr = curr.next` for step 4 (after the flip) → walks BACK into the
  reversed part → infinite loop. Must advance via `nxt`.
- Returning `head` or `curr` instead of `prev` — `head` still points at the
  old first node (now the tail); `curr` is `None`.

**Expected output:** `reverse 1→2→3→4→5` gives `5→4→3→2→1`, O(n) time, O(1)
space — the same loop handles empty (skips, returns `None`) and single-node
lists.

---

## Fast & Slow Pointers on a Linked Structure

**What:** Two walkers moving at different speeds — `slow` hops 1 node,
`fast` hops 2. Speed difference turns positional questions into pointer
questions without ever counting length.

**Why it exists:** You can't ask "are we halfway?" when there's no index and
no known length. But if `fast` hits the end while moving twice as fast,
`slow` MUST be at the midpoint — pure ratio, no counting. Same trick exposes
cycles: on a loop, the fast runner eventually laps the slow one.

**Where it's used:** Middle-of-list, cycle detection (Floyd's algorithm),
happy-number detection, "find where a cycle begins", palindrome splitting.

### Find the middle

```python
slow = fast = head
while fast and fast.next:     # fast needs TWO hops available
    slow = slow.next          # 1 hop
    fast = fast.next.next     # 2 hops
return slow                   # when fast falls off, slow is mid
```

For `1→2→3→4→5` slow stops at `3`. For even `1→2→3→4` it stops at `3` (the
SECOND middle) — that choice is what most problems want.

### Cycle detection (Floyd's)

```
    1 -> 2 -> 3 -> 4
              ^    |
              |    v
              6 <- 5          (tail points back to 3 — a cycle)

slow and fast both enter the loop; fast gains 1 node per step
inside it, so they MUST meet. No meeting before fast hits None
= no cycle.
```

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:        # 'is' — same NODE, not same value!
            return True
    return False                # fast ran off the end
```

**What goes wrong without it:**
- `slow == fast` instead of `is` — compares values on some setups, and even
  with identity `==` it's the wrong habit: you want "same object".
- `while fast.next:` without `fast` — `fast.next.next` on a dead end crashes.
- Starting `fast = head.next` offsets everything; both start at `head`.
- Using a `set` of seen nodes works (O(n) space) but misses the point —
  fast/slow does it in O(1) space.

---

## Merging and the Dummy-Node Trick

**What:** Merge two SORTED lists by repeatedly taking the smaller front node,
zipping them into one sorted chain. The trick that makes it clean is a
*dummy node*: a fake head that gives you a `tail` to append to, so every
splice is identical — no special "first node" case.

**Why it exists:** Splicing "whichever comes first" always hits the same
awkwardness: the result head doesn't exist yet when you attach the first
node. `dummy = Node(); tail = dummy` removes the special case — attach
through `tail.next`, return `dummy.next` at the end.

**Where it's used:** Merge two sorted lists (merge sort's heart), merge k
lists, reorder-list's final interleave, polynomial addition — anywhere you
build a new chain from existing nodes.

**The merge loop:**

```
list1: 1 -> 3 -> 5          list2: 2 -> 4
dummy -> ?                  tail = dummy

compare 1 vs 2: take 1   dummy->1,   tail=1
compare 3 vs 2: take 2   ...->2,     tail=2
compare 3 vs 4: take 3   ...->3,     tail=3
compare 5 vs 4: take 4   ...->4,     tail=4
list2 exhausted: hook ALL of list1's remainder -> ...->5
```

```python
def merge_two(a, b):
    dummy = Node()
    tail = dummy
    while a and b:               # both lists still have nodes
        if a.val <= b.val:
            tail.next = a; a = a.next
        else:
            tail.next = b; b = b.next
        tail = tail.next
    tail.next = a or b           # hook whichever remainder is left
    return dummy.next            # real head
```

The last line before `return` is the elegant part: one list is exhausted, so
`a or b` picks the survivor — no second loop needed.

**What goes wrong without it:**
- No dummy → the code special-cases "is result empty yet?" inside every
  iteration, or builds the first node separately. More paths, more bugs.
- Forgetting `tail.next = a or b` → the merged list silently drops the
  un-merged tail of the longer input.
- Re-walking `tail.next = tail.next.next` style — you must move `tail`
  EVERY iteration or nodes get overwritten.
- Careful with `a or b` when chains could be cycles — `or` picks on
  truthiness, and a `Node` object is always truthy; `a or b` is fine here
  only because the other operand is `None` when exhausted.

---

## The Big Picture

Three muscles this lesson builds:

1. **Pointer rescue** — before overwriting `node.next`, save it. Almost
   every linked-list bug is a lost reference (reversal's `nxt`, k-group's
   saved segment head).
2. **Dummy nodes** — whenever you build a chain whose head isn't known yet,
   a fake head makes the first splice identical to all others. Merge, k-group,
   remove-nth all use it.
3. **Speed-ratio pointers** — fast/slow answers "midpoint", "cycle",
   "nth from end" without ever knowing the length.

Whenever a problem says "in O(1) space" or "in one pass" on a linked list,
the answer is almost always one of these three.
