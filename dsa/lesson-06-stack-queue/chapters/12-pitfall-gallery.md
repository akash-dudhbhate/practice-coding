# 12 — The Pitfall Gallery: Six Ways Stacks & Queues Go Wrong

> 4-minute read. Read once now, once before your interview.

## 1. `list.pop(0)` as a queue (ch. 05)

Works, but costs O(n) per call — every remaining element slides left.
n dequeues → O(n²). `collections.deque` + `popleft()` is O(1). Use it
whenever you remove from the front more than a handful of times.

## 2. Pop/peek on empty (ch. 02)

```python
stack = []
# stack.pop()      # IndexError: pop from empty list
# stack[-1]        # IndexError: list index out of range
```

Guard with `if stack:` / `while stack:`. In bracket problems a closer
on an empty stack means "unmatched" → return False, don't crash.

## 3. Forgetting the stack must end EMPTY (ch. 07)

An `is_balanced` that returns True unconditionally after the loop
passes `"((("` — three openers, zero closers. `return not stack` is
the final check, not a formality.

## 4. Storing values where you need INDICES (ch. 08, 09)

Daily temperatures needs *distances*; sliding-window max needs
*expiry*. Both must store `i` and look up `nums[i]`. Values alone
can't answer "which position?"

## 5. `<` vs `<=` on the pop condition (ch. 08, 09)

- "Next **strictly** greater" → pop while `nums[top] < x` — equals
  stay (they're not answers).
- "Sliding-window max" → pop while `nums[back] <= x` — letting equals
  go keeps the deque clean (the older index expires first anyway).

Ask: "does an equal element answer the question?" — then pick.

## 6. Pouring two stacks on EVERY dequeue (ch. 10)

Unconditional `while self.inbox: outbox.append(inbox.pop())` → O(n)
every call AND broken FIFO (newest leapfrogs un-served old elements).
Pour **only when `outbox` is empty** — that's the whole amortized
trick.

## Edge cases to always test

- empty input — `""` brackets → True; dequeue on empty → guard
- single element
- all-equal values (`[3,3,3]` — did you pick `<` or `<=` on purpose?)
- strictly decreasing input (`[5,4,3]` — nothing ever gets answered)
- bracket worst cases: `"(((...)))"`, `")("`, `"(]"`
- interleaved enqueue/dequeue — catches pour-order bugs (ch. 10)

## You made it

LIFO vs FIFO, O(1) ops, the reversal superpower, bracket matching,
monotonic stack/deque, two-stack queue, and every trap — that's the
lesson. Now go earn it: open `task-explanation.md`, then `easy/p01`.

<details><summary>One last question — why does "each element enters and leaves once" mean O(n)?</summary>
n elements × a constant number of touches (one push + at most one pop
each) = at most 2n operations → O(n). No element is ever re-examined.
That's what makes monotonic structures linear instead of the naive
O(n²).
</details>

---

**← Prev** [11 — Stack vs queue](11-choosing-stack-vs-queue.md) ·
Done with concepts? → Open `task-explanation.md` and solve `easy/p01`.
