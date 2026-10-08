# Lesson 06 — Coding Check

Use this to verify your solutions before asking for review.

## Easy

### p01 — Balanced brackets
- [ ] `is_balanced("{[()]}")` returns `True`
- [ ] `is_balanced("([)]")` returns `False` — closers must match the MOST RECENT opener
- [ ] `is_balanced("()[]{}")` returns `True`
- [ ] `is_balanced("(((")` returns `False` — stack must be empty at the end
- [ ] `is_balanced(")")` returns `False` — pop on empty would crash; guard it
- [ ] `is_balanced("")` returns `True`
- [ ] `is_balanced("a(b[c]d)e")` returns `True` — non-brackets ignored

### p02 — Reverse string via stack
- [ ] `reverse_with_stack("hello")` returns `"olleh"`
- [ ] `reverse_with_stack("abc")` returns `"cba"`
- [ ] `reverse_with_stack("")` returns `""`
- [ ] `reverse_with_stack("racecar")` returns `"racecar"`
- [ ] Actually pushes then pops — no `[::-1]` / `reversed()`

### p03 — Queue with a list
- [ ] Fresh queue: `is_empty()` → `True`, `dequeue()` → `None`, `peek()` → `None`
- [ ] After `enqueue(1,2,3)`: `peek()` → `1`, `dequeue()` → `1`, `2` — FIFO order
- [ ] `enqueue(4)` mid-stream still dequeues in order `3, 4`
- [ ] `dequeue()` after emptying returns `None` (no crash)
- [ ] Can you name the `pop(0)` cost and the `deque`/`head-index` fix?

## Medium

### p01 — Next greater element
- [ ] `next_greater([2, 1, 2, 4, 3])` returns `[4, 2, 4, -1, -1]`
- [ ] `next_greater([1, 2, 3, 4])` returns `[2, 3, 4, -1]`
- [ ] `next_greater([4, 3, 2, 1])` returns `[-1, -1, -1, -1]` — all leftovers stay -1
- [ ] `next_greater([5, 5, 5])` returns `[-1, -1, -1]` — strictly greater, so equal doesn't pop
- [ ] Stack stores INDICES; pop condition is `nums[stack[-1]] < x`

### p02 — Daily temperatures
- [ ] `daily_temperatures([73,74,75,71,69,72,76,73])` returns `[1,1,4,2,1,1,0,0]`
- [ ] `daily_temperatures([30,40,50,60])` returns `[1,1,1,0]`
- [ ] `daily_temperatures([90,80,70])` returns `[0,0,0]`
- [ ] `daily_temperatures([50,50,51])` returns `[2,1,0]` — equal temps don't pop (strictly warmer)
- [ ] Answer is a distance `i - j`, not the temperature itself

### p03 — Evaluate postfix (RPN)
- [ ] `eval_rpn(["2","1","+","3","*"])` returns `9`
- [ ] `eval_rpn(["4","13","5","/","+"])` returns `6`
- [ ] `eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])` returns `22`
- [ ] `eval_rpn(["3","4","-"])` returns `-1` — `a - b`, second pop is the left operand
- [ ] `eval_rpn(["-7","2","/"])` returns `-3` — `int(a/b)` truncates toward 0 (`a//b` would give -4)
- [ ] `eval_rpn(["5"])` returns `5`

## Hard

### p01 — Sliding window maximum
- [ ] `max_sliding_window([1,3,-1,-3,5,3,6,7], 3)` returns `[3,3,5,5,6,7]`
- [ ] `max_sliding_window([1], 1)` returns `[1]`
- [ ] `max_sliding_window([9,11], 2)` returns `[11]`
- [ ] `max_sliding_window([4,3,2,1], 2)` returns `[4,3,2]` — decreasing input still works
- [ ] `max_sliding_window([7,7,7], 2)` returns `[7,7]` — duplicates handled (`<=` evict, or index-based pop)
- [ ] Deque stores INDICES (needed to know when an element leaves the window)
- [ ] No `max(window)` call inside the loop — that's O(n·k)

### p02 — Largest rectangle in histogram
- [ ] `largest_rectangle_area([2,1,5,6,2,3])` returns `10` — the 5+6 block, height 5 × width 2
- [ ] `largest_rectangle_area([2,4])` returns `4`
- [ ] `largest_rectangle_area([1,1,1,1])` returns `4` — full-width flat rectangle
- [ ] `largest_rectangle_area([6,2,5,4,5,1,6])` returns `12`
- [ ] `largest_rectangle_area([5])` returns `5`; `[]` returns `0`
- [ ] Stack is monotonic INCREASING; a sentinel `0` (or final drain loop) flushes it
- [ ] Width uses stack top after pop: `i - (stack[-1] + 1)`, or `i` when stack empties

### p03 — Queue using two stacks
- [ ] `enqueue(1,2,3); peek()` → `1`; `dequeue()` → `1`
- [ ] Interleave: after dequeue, `enqueue(4)` → dequeues come out `2, 3, 4`
- [ ] `empty()` → `True` only when BOTH stacks are empty
- [ ] `dequeue()`/`peek()` on empty → `None`, no crash
- [ ] Pour `inbox → outbox` happens ONLY when outbox is empty — that's what makes it amortized O(1)
- [ ] Can you explain *why* amortized, not worst-case, O(1)? (Each element moves stacks at most twice.)

## How to verify

```bash
python3 check.py all            # all nine of your files
python3 check.py hard/p02       # just one
python3 check.py solutions      # sanity-check the reference solutions
```
