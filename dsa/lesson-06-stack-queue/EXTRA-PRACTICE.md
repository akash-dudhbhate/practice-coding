# lesson-06-stack-queue — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons
→ bonus design problem (MinStack).

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: Which structure?

For each task, say STACK, QUEUE, MONOTONIC STACK, or MONOTONIC DEQUE:

1. Undo button in a text editor.
2. "How many days until a warmer temperature?"
3. Print jobs processed in arrival order.
4. Max of every sliding window of size k.
5. Check that HTML tags are properly nested.
6. BFS over a social graph.

<details><summary>Answer</summary>
1. STACK (most recent action first) · 2. MONOTONIC STACK (pop = found the warmer day) · 3. QUEUE (FIFO fairness) · 4. MONOTONIC DEQUE (evict useless-back, expired-front) · 5. STACK (most recent open tag must close first) · 6. QUEUE (FIFO visits in distance order).
</details>

---

## Check 02: Order discipline

```python
stack, queue = [], deque()
for x in [1, 2, 3]:
    stack.append(x)
    queue.append(x)
print(stack.pop(), queue.popleft(), stack.pop(), queue.popleft())
```

<details><summary>Answer</summary>
```
3 1 2 2
```
Stack pops LIFO: 3 then 2. Queue pops FIFO: 1 then 2. Interleaved: `3 1 2 2`.
</details>

---

## Check 03: The pour question

In a two-stack queue, `inbox = [1,2,3]` (3 on top), `outbox = []`. After `dequeue()`, what does outbox look like and what is returned? Then `enqueue(4)` followed by `dequeue()` — what's returned?

<details><summary>Answer</summary>
Pour inbox→outbox: outbox = `[3,2,1]` (1 on top). `dequeue()` pops → **1**.

`enqueue(4)` → inbox = `[4]` (outbox non-empty so NO pour). `dequeue()` pops outbox top → **2** — correct FIFO order, and the 4 safely waits in inbox. If you had poured eagerly, 4 would sit *under* 2,3 and order would break... wait, actually pouring is only wrong for ORDER if done while outbox has items — 4 would land at the bottom of outbox? No: pouring pushes inbox's top (4) onto outbox's top — 4 would be ON TOP and dequeue would return 4 before 2. Correct only because we pour when outbox is empty.
</details>

---

## Check 04: Amortized — say it correctly

"Two-stack-queue dequeue is O(1)" — is that precisely true?

<details><summary>Answer</summary>
**Amortized O(1), not worst-case O(1).** A single dequeue CAN be O(n) — the pour that moves n elements. But each element is pushed into inbox once, moved to outbox once, popped once → at most 3 operations per element lifetime → n dequeues cost O(n) total → O(1) *on average per operation*. In an interview, always say the word "amortized."
</details>

---

## Check 05: deque vs list

```python
import time
def drain_list(xs):      # queue with list
    while xs: xs.pop(0)
def drain_deque(dq):     # queue with deque
    while dq: dq.popleft()
# n = 100_000 — roughly how much slower is the list version?
```

<details><summary>Answer</summary>
~**1000×+ slower** — and it scales quadratically. `list.pop(0)` copies all remaining n-1 pointers left → total ≈ n²/2 moves ≈ 5×10⁹. `deque.popleft()` unlinks a block → O(1) each, ~10⁵ total. A deque is a doubly-linked list of blocks, so both ends are O(1); a list is a contiguous array where only the END is O(1).
</details>

---

## Debug Exercises — find and fix the bug

---

## Debug 01 (Easy): Balanced brackets — counting instead of matching

```python
def is_balanced(s):
    return s.count("(") == s.count(")")
```

**Hint:** Try `")("`.

<details><summary>Answer</summary>

**Bug:** counts ignore ORDER — `")("` and `"((("` with a close elsewhere pass or fail wrongly. `")("` → 1==1 → True, but it's invalid.
**Fix:** stack of openers; closers must match `stack.pop()`; stack must end empty. Counting can never capture nesting order.
</details>

---

## Debug 02 (Medium): RPN — operand order swapped

```python
def eval_rpn(tokens):
    stack = []
    for tok in tokens:
        if tok in "+-*/":
            a = stack.pop()
            b = stack.pop()
            if tok == "+": stack.append(a + b)
            elif tok == "-": stack.append(a - b)   # ← suspicious
            elif tok == "*": stack.append(a * b)
            else: stack.append(int(a / b))
        else:
            stack.append(int(tok))
    return stack[-1]
```

**Hint:** Which operand does `pop()` return first?

<details><summary>Answer</summary>

**Bug:** `a = stack.pop()` grabs the RIGHT operand (pushed last). `["3","4","-"]` should be 3−4 = −1, but computes 4−3 = +1. `+` and `*` happen to be commutative so the bug hides until `-` or `/`.
**Fix:** `b = stack.pop(); a = stack.pop()` — pop right first, then left; compute `a - b`, `a / b`.
</details>

---

## Debug 03 (Medium): Daily temperatures — storing values, not indices

```python
def daily_temperatures(temps):
    ans = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and stack[-1] < t:
            old = stack.pop()
            ans[i] = ???            # stuck — we know the temp, not the day
        stack.append(t)
    return ans
```

**Hint:** The answer is a distance in DAYS, not a temperature.

<details><summary>Answer</summary>

**Bug:** pushing temperatures loses positions — you can't compute "how many days later" from a value. You can only fill `ans[?]`... but which index?
**Fix:** push INDICES: `stack.append(i)`, compare `temps[stack[-1]] < t`, and record `ans[j] = i - j` for each popped `j`.
</details>

---

## Debug 04 (Hard): Two-stack queue — eager pouring

```python
class TwoStackQueue:
    def __init__(self):
        self.inbox, self.outbox = [], []
    def enqueue(self, x):
        self.inbox.append(x)
    def dequeue(self):
        while self.inbox:                       # pours EVERY call
            self.outbox.append(self.inbox.pop())
        return self.outbox.pop()
```

**Hint:** enqueue(1,2,3); dequeue()→1; enqueue(4); dequeue()→?

<details><summary>Answer</summary>

**Bug:** pouring while outbox is non-empty breaks order AND costs O(n) every call. Trace: after first dequeue, outbox=[3,2]; enqueue(4) → inbox=[4]; next dequeue pours 4 onto outbox → [3,2,4] → pops **4** instead of 2. FIFO broken.
**Fix:** pour only when `not self.outbox`. Also restores amortized O(1).
</details>

---

## Debug 05 (Hard): Sliding-window max — forgetting expiry

```python
def max_sliding_window(nums, k):
    dq = deque()
    out = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
```

**Hint:** What happens when the max index slides past the left edge?

<details><summary>Answer</summary>

**Bug:** stale indices never leave. `[4,3,2,1], k=2`: dq keeps [0] forever — index 0 exits the window at i=2 but stays front → reports 4 for window [2,1] (should be 2).
**Fix:** first loop step — `while dq and dq[0] <= i - k: dq.popleft()`. This is why you store indices, not values.
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: `list.pop(0)` for a queue
```python
# WRONG — O(n) per call, O(n²) overall
q = []
q.pop(0)

# CORRECT — O(1)
from collections import deque
q = deque()
q.popleft()
```

## Mistake 02: Peeking/popping an empty stack
```python
# WRONG — IndexError on empty
top = stack[-1]

# CORRECT — guard first
if stack:
    top = stack[-1]
```

## Mistake 03: Storing values when you need indices
```python
# WRONG — can't compute distances or expiry
stack.append(nums[i])

# CORRECT — store the index, look up the value
stack.append(i)
... nums[stack[-1]] ...
```

## Mistake 04: Forgetting "stack must end empty" (brackets)
```python
# WRONG — "(((" returns True
return True   # after the loop

# CORRECT
return not stack
```

## Mistake 05: `//` instead of `int(/)` for negative division (RPN)
```python
# WRONG — -7 // 2 == -4 (floors toward -∞)
# CORRECT — int(-7 / 2) == -3 (truncates toward 0)
stack.append(int(a / b))
```

## Mistake 06: Monotonic stack with `<` vs `<=` confusion
```python
# "next STRICTLY greater" pops on < ; duplicates stay → correct
while stack and nums[stack[-1]] < x:
# window-max evicts on <= so the older duplicate doesn't linger as a fake max
while dq and nums[dq[-1]] <= x:
```
Ask: do equal elements answer the question? Strictly-greater → keep equals (`<`). Window-max → evict equals too (`<=`) so stale duplicates can't pretend to be the max.

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Branchy bracket logic
### Before
```python
def is_balanced(s):
    stack = []
    for c in s:
        if c == "(" or c == "[" or c == "{":
            stack.append(c)
        elif c == ")":
            if not stack or stack.pop() != "(": return False
        elif c == "]":
            if not stack or stack.pop() != "[": return False
        elif c == "}":
            if not stack or stack.pop() != "{": return False
    return not stack
```
### Problems
1. Three near-identical branches — a mapping table kills the duplication.

### After
```python
def is_balanced(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack
```

---

## Refactor 02 (Medium): Duplicated drain-the-stack tail
### Before
```python
def largest_rectangle_area(heights):
    stack, best = [], 0
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            H = heights[stack.pop()]
            W = i - stack[-1] - 1 if stack else i
            best = max(best, H * W)
        stack.append(i)
    # then ANOTHER loop to drain the leftover stack... 10 more lines
```
### Problems
1. The drain loop duplicates the pop-body → two places to fix a bug.

### After
```python
def largest_rectangle_area(heights):
    stack, best = [], 0
    for i, h in enumerate(heights + [0]):   # sentinel flushes for free
        while stack and heights[stack[-1]] > h:
            H = heights[stack.pop()]
            W = i - stack[-1] - 1 if stack else i
            best = max(best, H * W)
        stack.append(i)
    return best
```

---

## Refactor 03 (Hard): Operator soup in RPN
### Before
```python
if tok == "+": stack.append(a + b)
elif tok == "-": stack.append(a - b)
elif tok == "*": stack.append(a * b)
elif tok == "/": stack.append(int(a / b))
```
### Problems
1. Works, but a dispatch table is tidier when operators multiply.

### After
```python
import operator
OPS = {"+" : operator.add, "-": operator.sub,
       "*" : operator.mul, "/": lambda a, b: int(a / b)}
...
stack.append(OPS[tok](a, b))
```

---

## Approach Comparison — different ways to solve it

## Problem: Next greater element

### Approach 1: brute force scan-right
```python
def f(nums):
    ans = []
    for i in range(len(nums)):
        ans.append(-1)
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                ans[i] = nums[j]; break
    return ans
```
**Pros:** Dead simple. **Cons:** O(n²) — n=10⁵ means 10¹⁰ worst-case ops.

### Approach 2: monotonic stack (forward)
```python
def f(nums):
    ans = [-1]*len(nums); stack = []
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            ans[stack.pop()] = x
        stack.append(i)
    return ans
```
**Pros:** O(n), each index pushed/popped once. **Cons:** the "pop = answered" insight isn't obvious at first.

### Approach 3: monotonic stack (backward scan)
```python
def f(nums):
    ans = [-1]*len(nums); stack = []
    for i in range(len(nums)-1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()                  # discard useless small right values
        if stack: ans[i] = stack[-1]
        stack.append(nums[i])
    return ans
```
**Pros:** O(n) too; sometimes feels more intuitive ("peek right via stack"). **Cons:** stores values, so it can't give you indices/distances.

**Winner:** Approach 2 — it generalizes to distances (daily temps) and boundaries (histogram).

---

## Problem: Sliding window maximum

### Approach 1: `max()` per window — O(n·k). Fails at scale.

### Approach 2: heap — push every element, evict lazily. O(n log k) — works but slower.

### Approach 3: monotonic deque — O(n).
```python
dq = deque()
for i, x in enumerate(nums):
    while dq and dq[0] <= i-k: dq.popleft()   # expiry
    while dq and nums[dq[-1]] <= x: dq.pop()  # domination
    dq.append(i)
```

**Winner:** Approach 3 — it's the same amortized logic ("each index enters/exits once") and it doubles as the sliding-window-MIN solution by flipping the comparison.

---

## Bonus Design Problem — MinStack

> Not in the 9-file grid — do it here on paper, then code it up yourself.

**Design a stack supporting `push(x)`, `pop()`, `top()`, `get_min()` — all O(1).**

The insight: a plain stack can't track a running minimum, so keep a **parallel stack** where `mins[-1]` is "the minimum of everything below it":

```python
class MinStack:
    def __init__(self):
        self.data = []   # values
        self.mins = []   # mins[i] = min(data[:i+1])
    def push(self, x):
        self.data.append(x)
        self.mins.append(min(x, self.mins[-1]) if self.mins else x)
    def pop(self):
        self.mins.pop(); return self.data.pop()
    def top(self):
        return self.data[-1]
    def get_min(self):
        return self.mins[-1]
```

Trace `push(5), push(3), push(7), get_min(), pop(), get_min()`:
`mins = [5,3,3]` → get_min→3 → pop removes 7/3's entry → get_min→3.

**Check yourself:** why does popping `mins` alongside `data` never lose information? Because `mins[i]` only ever describes `data[:i+1]` — once `data[i]` is gone, its min-record is irrelevant.

This is the same "two structures, one answers the question the other can't" trick as TwoStackQueue — and it's a favorite follow-up in interviews.
