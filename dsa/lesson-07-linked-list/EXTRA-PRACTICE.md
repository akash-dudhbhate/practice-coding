# lesson-07-linked-list — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: What does head[i] cost?
```
1 -> 2 -> 3 -> 4 -> 5 -> ... -> 1000000
```
You want the node holding `999999`. Roughly how many `.next` hops?

- (A) 1
- (B) ~500,000
- (C) ~999,999

<details><summary>Answer</summary>
**(C) ~999,999** — there is no index jump; reaching node i costs O(i) hops.
That's the entire array-vs-list trade-off: random access was surrendered for
O(1) mid-list rewiring.
</details>

---

## Check 02: Lost reference
```python
curr.next = prev
nxt = curr.next
```
Reversal written in this order — what happens to the list after `curr`?

<details><summary>Answer</summary>
**It's lost.** `curr.next = prev` overwrites the only pointer to the rest of
the list; the `nxt` on line 2 just reads `prev` back. Rescue FIRST:
`nxt = curr.next` must run before the overwrite.
</details>

---

## Check 03: Fast & slow midpoint
```
1 -> 2 -> 3 -> 4    (even length)
slow = fast = head; while fast and fast.next: slow 1 hop, fast 2 hops
```
Which node does `slow` end on?
- (A) 2 (first middle)
- (B) 3 (second middle)
- (C) None

<details><summary>Answer</summary>
**(B) 3** — the standard loop yields the second middle. If a problem wants
the first (e.g., splitting for reorder), you stop one step earlier:
`while fast.next and fast.next.next`.
</details>

---

## Check 04: Why does Floyd's meet?
```
slow hops 1/step, fast hops 2/step, both inside a loop of length C
```
If fast is ahead by some gap when both are in the loop, what does the gap
do each step — and why is meeting guaranteed?

<details><summary>Answer</summary>
Fast gains **exactly 1 node per step** on slow. Gaps shrink by 1 (mod C)
until it hits 0 — they MUST meet within C steps, like a faster runner
lapping a slower one on a track. And if there's no loop, `fast` reaches
`None` — which is the "no cycle" answer.
</details>

---

## Check 05: The `a or b` hook
```python
tail.next = a or b      # after the merge loop
```
`a` is exhausted (`None`), `b` still has `4→5`. What lands on `tail.next`,
and why is this legal instead of another loop?

<details><summary>Answer</summary>
**`b`'s entire remaining chain** — `None or b` is `b`. The remainder is
already sorted and already linked, so one pointer splice appends all of it.
`or` picks the truthy operand; `None` is falsy, a Node is truthy.
</details>

---

## Debug Exercises — find and fix the bug

> Fix the broken code. Find bugs mentally before running.

---

## Debug 01 (Easy): Build that runs backwards

```python
def build_list(values):
    head = None
    for v in values:
        node = Node(v)
        node.next = head
        head = node
    return head
```

**Hint:** `to_list(build_list([1,2,3]))` gives `[3,2,1]` — why?

<details><summary>Answer</summary>

**Bug:** Each new node PREPENDS — the loop builds the list in reverse.
**Fix:** append at the end with a tail pointer (and a dummy for the empty
case):
```python
dummy = Node(); tail = dummy
for v in values:
    tail.next = Node(v); tail = tail.next
return dummy.next
```
</details>

---

## Debug 02 (Medium): Cycle detector that never finds

```python
def has_cycle(head):
    slow = head
    fast = head.next          # <- the bug
    while fast and fast.next:
        if slow is fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False
```

**Hint:** Works on many cycles but misses `1 -> 1` (self-loop) and some
2-cycles — and the meeting math was designed around a shared start.

<details><summary>Answer</summary>

**Bug:** `fast` starts one node ahead — on a self-loop `slow is fast`
never triggers before `fast.next` is fast itself… actually worse: the
offset start makes some small cycles unmeetable under this loop's guard.
The clean invariant is both start at `head`, THEN move — so any cycle is
entered symmetrically.
**Fix:**
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow is fast:
        return True
return False
```
</details>

---

## Debug 03 (Hard): Remove-nth that breaks on the head

```python
def remove_nth(head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    while fast.next:            # <- the bug
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
```

**Hint:** `remove_nth(1→2, 2)` should remove the head — instead it removes
the tail. When `fast` is already `None`, the loop skips and `slow` still
sits on the node to remove, not BEFORE it.

<details><summary>Answer</summary>

**Bug:** Two off-by-ones. The loop condition should be `while fast:` (so
`slow` stops one node BEFORE the target), and removing the head means
`head` itself changes — return `head` is stale. A dummy fixes both:
```python
dummy = Node(0, head)
fast = slow = dummy
for _ in range(n):
    fast = fast.next
while fast.next:
    fast = fast.next
    slow = slow.next
slow.next = slow.next.next
return dummy.next
```
`slow` lands on the node before the target in every case — including
n == length, where that node is the dummy.
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: Overwriting `.next` before saving it
```python
# WRONG — rest of list garbage-collected
curr.next = prev
curr = curr.next

# CORRECT
nxt = curr.next
curr.next = prev
curr = nxt
```

## Mistake 02: `while fast.next:` without checking `fast`
```python
# WRONG — fast.next.next crashes when fast is None
while fast.next:
    fast = fast.next.next

# CORRECT
while fast and fast.next:
    fast = fast.next.next
```

## Mistake 03: Comparing values instead of nodes
```python
# WRONG — two nodes holding 7 at different positions are NOT the same node
if slow.val == fast.val: return True

# CORRECT — cycle detection is about identity
if slow is fast: return True
```

## Mistake 04: No dummy → the head-removal special case
```python
# WRONG — removing the head needs "return head.next", a separate path
# CORRECT — dummy.next is the head; splicing it out looks like any splice
dummy = Node(0, head)
...slow.next = slow.next.next...
return dummy.next
```

## Mistake 05: Merging into a fresh list when nodes should be reused
```python
# WRONG — allocates new nodes; breaks "O(1) extra space" and identity tests
tail.next = Node(a.val)

# CORRECT — relink the EXISTING nodes; you're doing surgery, not copying
tail.next = a
a = a.next
```

## Mistake 06: Forgetting to cut the first half in reorder
```python
# WRONG — first half still linked to second half -> cycles / wrong output
second = mid.next
# ...interleave without severing...

# CORRECT — sever before reversing the second half
second = mid.next
mid.next = None
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Traverse with index bookkeeping
### Before
```python
def to_list(head):
    out = []
    i = 0
    node = head
    while node is not None:
        out.insert(i, node.val)
        i += 1
        node = node.next
    return out
```
### Problems
1. `i` exists only to feed `insert` — `append` does it for free
2. Extra variable `node` when `head` itself can walk (read-only traversal)

### After
```python
def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out
```

---

## Refactor 02 (Medium): Merge without a dummy
### Before
```python
def merge_two(a, b):
    if not a: return b          # special case 1
    if not b: return a          # special case 2
    if a.val <= b.val:          # special case 3: pick first node by hand
        head = a; a = a.next
    else:
        head = b; b = b.next
    tail = head
    while a and b:
        ...
    return head
```
### Problems
1. Three special cases just to establish the first node
2. The "who's first" logic duplicates the loop's comparison

### After
```python
def merge_two(a, b):
    dummy = Node()
    tail = dummy
    while a and b:
        if a.val <= b.val:
            tail.next = a; a = a.next
        else:
            tail.next = b; b = b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next
```
The dummy absorbs every "first node" question — one code path total.

---

## Refactor 03 (Hard): Reorder via array of nodes
### Before
```python
def reorder_list(head):
    nodes = []
    while head:
        nodes.append(head); head = head.next
    i, j = 0, len(nodes) - 1
    while i < j:
        nodes[i].next = nodes[j]
        i += 1
        if i == j: break
        nodes[j].next = nodes[i]
        j -= 1
    nodes[i].next = None
```
### Problems
1. O(n) extra space — defeats the pointer-surgery point
2. The interleave bookkeeping is easy to off-by-one

### After
```python
def reorder_list(head):
    if not head or not head.next:
        return
    slow = fast = head
    while fast.next and fast.next.next:   # first-middle variant
        slow = slow.next
        fast = fast.next.next
    second = slow.next                    # cut the list in two
    slow.next = None
    prev = None                           # reverse second half
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    first, second = head, prev            # interleave
    while second:
        t1, t2 = first.next, second.next
        first.next = second
        second.next = t1
        first, second = t1, t2
```
O(1) space, and each stage is a pattern you already own: middle, reverse,
merge-interleave.

---

## Approach Comparison — different ways to solve it

## Problem: Detect a cycle

### Approach 1: Seen-set — O(n) time, O(n) space
```python
seen = set()
while head:
    if head in seen:
        return True
    seen.add(head)
    head = head.next
return False
```
**Pros:** Obvious, works. **Cons:** O(n) memory; fails the classic "O(1)
space?" follow-up.

### Approach 2: Floyd's fast/slow — O(n) time, O(1) space
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow is fast:
        return True
return False
```
**Pros:** Constant space — the interview answer. **Cons:** Slightly less
obvious; requires trusting the "lap" argument.

**Winner:** Approach 2 — it's the reason this data structure is asked at
all: can you extract positional information without memory or indexing?

---

## Problem: Remove nth from end

### Approach 1: Two passes — O(2n) time
```python
# pass 1: count length L; pass 2: walk to node L-n-1 and splice
```
**Pros:** Easy to reason about. **Cons:** Two passes; the follow-up
("one pass?") is the actual question.

### Approach 2: Fast with n-step head start — O(n), one pass
```python
dummy = Node(0, head)
fast = slow = dummy
for _ in range(n): fast = fast.next
while fast.next:
    fast = fast.next; slow = slow.next
slow.next = slow.next.next
return dummy.next
```
**Pros:** One pass, and the dummy makes "remove the head" free.
**Cons:** Slightly trickier invariants.

**Winner:** Approach 2 — "nth from end" is really "maintain a gap of n
between two pointers", the same speed-ratio idea as middle/cycle.
