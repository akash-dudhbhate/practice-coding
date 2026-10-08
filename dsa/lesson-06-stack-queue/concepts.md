# Lesson 06 — Concepts Explained (Stacks & Queues)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Stack (LIFO) vs Queue (FIFO)

**What:** Two restricted-access structures that differ in ONE rule — which end you remove from.

- **Stack — Last In, First Out (LIFO).** A pile of plates: you push onto the top and pop off the top. The last thing in is the first thing out.
- **Queue — First In, First Out (FIFO).** A line at a coffee shop: you enqueue at the back and dequeue from the front. First in, first served.

```python
# STACK with a plain Python list — O(1) push and pop at the END
stack = []
stack.append(1)     # push  → [1]
stack.append(2)     # push  → [1, 2]
stack.append(3)     # push  → [1, 2, 3]
stack.pop()         # pop   → returns 3, stack is [1, 2]  (LAST out FIRST)
stack[-1]           # peek  → 2 (top, without removing)

# QUEUE with collections.deque — O(1) at BOTH ends
from collections import deque
queue = deque()
queue.append(1)     # enqueue → deque([1])
queue.append(2)     # enqueue → deque([1, 2])
queue.append(3)     # enqueue → deque([1, 2, 3])
queue.popleft()     # dequeue → returns 1, queue is deque([2, 3])  (FIRST out FIRST)
queue[0]            # peek front → 2
```

**Why it exists:** Most structures let you touch any element. Stacks and queues deliberately *restrict* you — and the restriction is the feature. LIFO naturally models "most recent thing first" (undo history, nested calls, innermost bracket). FIFO models "fair order of arrival" (task scheduling, BFS layers, print jobs).

**Where it's used:**
- Stack: function call stack (Python itself uses one per thread), undo/redo, expression evaluation, bracket matching, DFS, browser back button.
- Queue: task queues (Celery, RQ), BFS level-order traversal, message brokers, buffering, "process in arrival order" anywhere.

**What goes wrong without it:**
- Using a list where order discipline matters and forgetting which end is which: `list.pop()` pops the END (stack behavior); `list.pop(0)` pops the FRONT (queue behavior — but O(n)! see below).
- Implementing a queue with a plain list: `q.pop(0)` shifts every remaining element one slot left → O(n) per dequeue → O(n²) total. `deque.popleft()` is O(1). At n = 10⁵ dequeues that's ~10⁹ vs ~10⁵ element moves.
- Popping from an empty stack → `IndexError: pop from empty list`. Always guard with `if stack:` or `while stack:`.
- Confusing the top: for a list, `stack[-1]` is the top. People peek `stack[0]` and grab the *oldest* element instead of the newest.

**Worked example (order discipline):**

```python
# push 10, 20, 30 — what comes out?
stack = []
for x in [10, 20, 30]: stack.append(x)
print(stack.pop(), stack.pop(), stack.pop())   # 30 20 10   (reversed!)

queue = deque()
for x in [10, 20, 30]: queue.append(x)
print(queue.popleft(), queue.popleft(), queue.popleft())  # 10 20 30 (same order)
```

A stack *reverses* a sequence; a queue *preserves* it. That single fact powers easy problems like "reverse a string with a stack."

---

## Balanced Brackets — the canonical stack pattern

**What:** Given a string of brackets `()[]{}`, check that every opener has a matching closer *in the right order*. `"([)]"` is invalid — the `)` tries to close `[` before `]` does.

**Why it exists:** Nesting is everywhere — code blocks, HTML tags, JSON, math expressions. "Is this properly nested?" is the minimal version of "is this parseable?", and a stack is exactly the tool because the thing you must match next is always the *most recently opened* one — LIFO.

**Where it's used:** Compilers/interpreters (Python raises `SyntaxError` for unbalanced parens), editor bracket matching, JSON/XML validation, the `eval` of arithmetic with parentheses.

**The algorithm:** push every opener; on every closer, pop and check it matches; at the end the stack must be empty.

**What goes wrong without it:**
- Counting opens/closes (`"(" count == ")"` count) fails ordering: `")("` has equal counts but is invalid.
- Matching against *any* earlier opener instead of the *most recent*: `"([)]"` passes a naive "exists" check.
- Forgetting `stack` must be **empty at the end** — `"((("` pushes three, pops zero, and empty-check catches it.
- Popping on empty: closer with no opener, `")"` → crash if unguarded.

**Worked example — `"{[()]}"`:**

```
'{' → push          stack: ['{']
'[' → push          stack: ['{', '[']
'(' → push          stack: ['{', '[', '(']
')' → closer: top is '(' ✓ pop    stack: ['{', '[']
']' → closer: top is '[' ✓ pop    stack: ['{']
'}' → closer: top is '{' ✓ pop    stack: []
end → stack empty → BALANCED
```

Counter-example `"([)]"`: `)` arrives when top is `[` → mismatch → invalid.

```python
def is_balanced(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in s:
        if c in '([{':            # opener → push
            stack.append(c)
        elif c in ')]}':          # closer → must match most recent opener
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack              # nothing left unmatched
```

Expected output: `is_balanced("{[()]}")` → **True**, `is_balanced("([)]")` → **False**, `is_balanced("(((")` → **False**.

O(n) time, O(n) worst-case space (all openers, e.g. `"((((("`).

---

## The Monotonic Stack — next greater element & friends

**What:** A stack you keep *sorted* (usually decreasing) by evicting elements that violate the order when a new one arrives. The eviction moment is the magic: **when a new element pops an old one, you've just found the old one's "next greater element."**

**Why it exists:** The naive "next greater element" scans rightward from each position → O(n²). Key observation: an element that gets a "next greater" answer never needs to be reconsidered — the new element answered it permanently. A stack holds the *unanswered* elements; each is pushed once and popped once → O(n).

**Where it's used:** Next greater element, daily temperatures ("how many days until warmer?"), stock span, largest rectangle in histogram, "remove k digits to make smallest number," trapping rain water.

**What goes wrong without it:**
- Brute-force double loop: `for i: for j > i: if nums[j] > nums[i]` — O(n²), times out at n = 10⁵.
- Keeping a non-monotonic stack and re-scanning it per element → back to quadratic.
- Storing values when you need **indices** — daily temperatures asks "how many *days* later," so you must push indices and compute `right - left` distances, not the temperature values.
- Forgetting the leftovers: whatever's still on the stack at the end has NO greater element → answer -1 (or 0 days).

**Worked example — `nums = [2, 1, 2, 4, 3]`, find next greater for each:**

```
i=0 (2): stack empty → push 0          stack idx: [0]
i=1 (1): 1 < nums[0]=2 → push 1        stack: [0, 1]
i=2 (2): 2 > nums[1]=1 → pop 1, ans[1]=2;  2 > nums[0]? no (equal) → push 2
         stack: [0, 2]
i=3 (4): 4 > nums[2]=2 → pop 2, ans[2]=4;  4 > nums[0]=2 → pop 0, ans[0]=4
         stack empty → push 3           stack: [3]
i=4 (3): 3 < 4 → push 4                stack: [3, 4]
end: leftover indices 3, 4 → ans = -1
Result: [4, 2, 4, -1, -1]
```

```python
def next_greater(nums):
    ans = [-1] * len(nums)
    stack = []                       # indices of elements still waiting
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:   # x answers the top
            ans[stack.pop()] = x
        stack.append(i)
    return ans                       # leftovers already -1
```

Expected output for `next_greater([2, 1, 2, 4, 3])`: **[4, 2, 4, -1, -1]**

**Daily temperatures variant:** same code, but `ans[i] = i - popped_index` (distance, not value): `[73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]`.

**Largest-rectangle variant (hard p02):** extend the idea — when a shorter bar pops a taller one, the popped bar's max rectangle spans from the *new* stack top's index + 1 to `i - 1`. Add a sentinel `0` at the end to force-flush the stack.

---

## Deque for Sliding-Window Maximum; Queue for BFS

**What:** Two advanced queue-family patterns:

- **Monotonic deque — sliding window maximum.** Keep a deque of indices whose values are in *decreasing* order. The front is always the current window's max. On each step: drop indices that slid out the left (front), drop all values smaller than the new element (back — they'll never be max while the new element lives), push the new index, record `nums[dq[0]]`.
- **FIFO queue — BFS.** Breadth-first search explores a graph layer by layer: enqueue the start, then loop `pop left → visit → enqueue neighbors`. The FIFO order guarantees you visit every node at distance d before any at distance d+1 → shortest path in unweighted graphs. (Full treatment in lesson 13 — this is the preview.)

**Why it exists:**
- Window max: naive is `max(nums[i:i+k])` per window → O(n·k). The deque keeps each element entering/exiting once → O(n). It's the monotonic-stack idea rotated: eviction order = "useless forever."
- BFS: a stack (DFS) dives deep first and can't guarantee shortest hops. Only FIFO visits in distance order.

**Where it's used:** Sliding-window max/min in stream processing and trading signals; BFS in shortest-path puzzles, social-network degrees, level-order tree printing, web crawlers.

**What goes wrong without it:**
- `max()` inside the slide loop → O(n·k) — same trap as re-summing in lesson 05.
- Deque bookkeeping errors: comparing `nums[dq[0]] < nums[i]` with `<` vs `<=` (duplicates), storing values instead of indices (can't tell when they leave the window), forgetting to pop the front when it slides out.
- BFS with a stack (`pop()` instead of `popleft()`) silently becomes DFS — code runs, answers are wrong.
- `deque` vs `list`: `list.pop(0)` = O(n) shift → BFS on 10⁵ nodes becomes O(n²). Always `from collections import deque` for front-removal.

**Worked example — sliding window max, `nums = [1,3,-1,-3,5,3,6,7]`, `k=3`:**

```
i=0 (1):  dq=[0]
i=1 (3):  3>1 → pop 0; dq=[1]
i=2 (-1): -1<3 → dq=[1,2];  window full → max = nums[1] = 3
i=3 (-3): dq=[1,2,3];  max=3
i=4 (5):  dq[0]=1 still in window; evict back: 5>-3 pop, 5>-1 pop, 5>3 pop
          dq=[4]; max=5
i=5 (3):  dq=[4,5]; max=5
i=6 (6):  evict back: 6>3 pop, 6>5 pop → dq=[6]; max=6
i=7 (7):  evict 6 → dq=[7]; max=7
Output: [3, 3, 5, 5, 6, 7]
```

```python
from collections import deque
def max_sliding_window(nums, k):
    dq = deque()                   # indices, values decreasing front→back
    out = []
    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:       # slid out the left
            dq.popleft()
        while dq and nums[dq[-1]] < x:     # useless forever
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
```

Expected output: **[3, 3, 5, 5, 6, 7]**

---

## Two Stacks Make a Queue (and other design tricks)

**What:** Simulate FIFO using two LIFO stacks: `inbox` for enqueues, `outbox` for dequeues. When `outbox` is empty, pour `inbox` into it — the pour reverses order, undoing the LIFO → the oldest element lands on top.

```
enqueue 1,2,3:  inbox=[1,2,3]  outbox=[]
dequeue:        pour → inbox=[]  outbox=[3,2,1]  → pop → 1  ✓ oldest first!
dequeue:        outbox top = 2 → pop → 2 ✓
```

**Why it exists:** Classic interview design problem testing *amortized analysis*: each element is pushed and popped from each stack at most once, so dequeue is O(1) *amortized* even though a single pour is O(n). It's the same averaging argument as `list.append`.

**Where it's used:** The pattern generalizes — min-stack (parallel stack tracking minimums), two-stack browser history (back/forward), queue-on-stacks in languages lacking deque.

**What goes wrong without it:**
- Pouring `inbox → outbox` on *every* dequeue → O(n) each, defeats the point. Pour **only when outbox is empty**.
- `peek`/`dequeue` forgetting to check emptiness → pop on empty crash.
- Claiming dequeue is O(1) worst-case — it's amortized; say it correctly in interviews.

```python
class TwoStackQueue:
    def __init__(self):
        self.inbox, self.outbox = [], []
    def enqueue(self, x):
        self.inbox.append(x)
    def dequeue(self):
        if not self.outbox:                    # pour only when needed
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop() if self.outbox else None
```

---

## Choosing the Right Structure — cheat sheet

| Task | Structure | Why |
|------|-----------|-----|
| Match brackets, nested structure | stack | must match most-recent opener |
| Reverse a sequence | stack | LIFO reverses for free |
| Next greater / days-until-warmer | monotonic stack | pop moment = answer found |
| Max over sliding window | monotonic deque | front is always current max |
| Process in arrival order, BFS | deque (FIFO) | fair order, O(1) both ends |
| Largest rectangle / span | monotonic stack | boundary of each bar's reign |
| Design a queue from stacks | two stacks | pour reverses LIFO → FIFO |

**Complexity mantra for this lesson:** every structure gives O(1) per operation (amortized for two-stack queue), so every problem here runs in **O(n) time** — same "each element enters and leaves once" argument as sliding windows.

---

## The Pitfall Gallery — six ways stacks and queues go wrong

**1. `list.pop(0)` as a queue.**
Works but O(n) per call — every remaining element shifts one slot. n dequeues → O(n²). Use `collections.deque` + `popleft()` (O(1)) whenever you remove from the front more than a handful of times.

**2. Pop/peek on empty.**
`stack.pop()` or `stack[-1]` on `[]` → `IndexError`. Guard with `if stack:` / `while stack:`. In bracket problems, a closer arriving on an empty stack means "unmatched closer" — return False, don't crash.

**3. Forgetting the stack must end empty.**
`is_balanced` that returns True unconditionally after the loop passes `"((("` — every opener matched nothing. `return not stack` is the final check.

**4. Storing values where you need indices.**
Daily temperatures needs *distances*, sliding-window max needs *expiry* — both require storing `i`, then looking up `nums[i]`. Values alone can't answer "which position?"

**5. `<` vs `<=` on the pop condition.**
- "Next **strictly** greater" → pop while `nums[top] < x` — equals stay (they're not answers).
- "Sliding-window max" → pop while `nums[back] <= x` — equals leave (a stale duplicate can't be the max once a newer equal exists… actually keeping it is fine for *value*, but the older index expires first; `<=` keeps the deque cleaner).
Think: "does an equal element answer the question?" then pick the comparison.

**6. Pouring two stacks on every dequeue.**
`while self.inbox: outbox.append(inbox.pop())` run unconditionally → O(n) every call AND broken FIFO (newest lands on top of un-served old elements). Pour **only when outbox is empty** — that's the whole amortized trick.

**Edge cases to always test:** empty input, single element, all-equal values, strictly decreasing input (nothing ever answers), brackets-only `"(((...)))"`, and repeated interleave of enqueue/dequeue to catch pour-order bugs.
