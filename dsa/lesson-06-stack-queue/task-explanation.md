# Lesson 06 — Stacks & Queues

## What you'll learn
- Stack (LIFO) vs queue (FIFO); Python `list` as stack, `collections.deque` as queue
- Balanced brackets — the canonical stack pattern
- Monotonic stack: next greater element, daily temperatures, histogram
- Monotonic deque: sliding-window maximum; FIFO queue: BFS prep
- Two-stack queue and amortized O(1); when to pick which structure

## Lesson

A **stack** removes the most recent element (`append`/`pop` on a list — both O(1)).
A **queue** removes the oldest (`deque.append` + `deque.popleft` — both O(1)).

```python
stack = []
stack.append(x)   # push — O(1)
stack.pop()       # pop top — O(1)   (list.pop(0) is O(n) — never for hot loops!)

from collections import deque
q = deque()
q.append(x)       # enqueue — O(1)
q.popleft()       # dequeue — O(1)
```

### The three stack patterns in this lesson
```python
# 1. Matching: opener pushes, closer pops-and-checks
if c in '([{': stack.append(c)
elif not stack or stack.pop() != match[c]: return False

# 2. Monotonic stack: pop moment = "you found your answer"
while stack and nums[stack[-1]] < x:
    ans[stack.pop()] = x          # next-greater / days-until-warmer
stack.append(i)

# 3. Monotonic deque: front is always the window max
while dq and nums[dq[-1]] <= x: dq.pop()
dq.append(i);  out.append(nums[dq[0]])
```

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here) — raw stack/queue mechanics
1. `easy/p01-balanced-brackets.py` — `is_balanced(s)` → True if every `()[]{}` opener is closed in the right order.
   `"{[()]}"` → True · `"([)]"` → False · `"((("` → False (stack non-empty at end).
2. `easy/p02-reverse-string-stack.py` — `reverse_with_stack(s)` → reversed string, built by push-then-pop. No slicing/`reversed()` allowed.
   `"hello"` → `"olleh"`.
3. `easy/p03-queue-with-list.py` — class `SimpleQueue` with `enqueue`, `dequeue`, `peek`, `is_empty`; dequeue on empty → `None`.
   Feel the `pop(0)` O(n) cost — then think about how a head-index or `deque` fixes it.

### Medium — the monotonic stack & friends
4. `medium/p01-next-greater-element.py` — `next_greater(nums)` → for each element, the first strictly-greater element to its right, else -1.
   `[2,1,2,4,3]` → `[4,2,4,-1,-1]`. O(n) via stack of waiting indices.
5. `medium/p02-daily-temperatures.py` — `daily_temperatures(temps)` → days until a warmer day, else 0.
   `[73,74,75,71,69,72,76,73]` → `[1,1,4,2,1,1,0,0]`. Same stack, but record `i - popped` (a distance, not a value).
6. `medium/p03-eval-postfix-rpn.py` — `eval_rpn(tokens)` → evaluate Reverse Polish Notation.
   `["2","1","+","3","*"]` → `9`. Pop TWO operands on each operator; the second pop is the LEFT operand; division truncates toward zero.

### Hard — deque + design patterns
7. `hard/p01-sliding-window-maximum.py` — `max_sliding_window(nums, k)` → max of every size-k window.
   `[1,3,-1,-3,5,3,6,7], k=3` → `[3,3,5,5,6,7]`. Monotonic deque, O(n) — the lesson-05 window carried by a better state structure.
8. `hard/p02-largest-rectangle-histogram.py` — `largest_rectangle_area(heights)` → biggest rectangle in the histogram.
   `[2,1,5,6,2,3]` → `10`. Monotonic *increasing* stack; a shorter bar closes taller ones; width = span between boundaries.
9. `hard/p03-queue-using-two-stacks.py` — class `TwoStackQueue` with `enqueue`, `dequeue`, `peek`, `empty`.
   inbox + outbox stacks; pour **only when outbox is empty** → O(1) amortized. dequeue/peek on empty → `None`.

### How to work
- Read `concepts.md` first — the cheat-sheet table maps problems to structures.
- Open a problem file, read the header, write your code under the TODO marker.
- Run `python3 check.py easy/p01` for one problem, `python3 check.py all` for all nine.
- `coding-check.md` is your manual checklist; `EXTRA-PRACTICE.md` has debug drills + a bonus MinStack design problem.
- Peek at `solutions/` only after a real attempt — then close it and redo from memory.
