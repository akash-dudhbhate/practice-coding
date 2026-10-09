# 08 — The Monotonic Stack: Next Greater Element

> 6-minute read. The "aha" pattern of this whole lesson.

## The idea, plain words

**Next greater element:** for each number, find the first bigger number
to its right (or -1 if none).

```
nums = [2, 1, 2, 4, 3]    →   [4, 2, 4, -1, -1]
```

Naive way: from each position, scan right → O(n²). The stack way: keep
a stack of elements **still waiting for their answer**, in decreasing
order ("monotonic" = never goes up inside the stack).

The magic moment: **when a new number pops an old one off the stack,
the new number IS the old one's answer.** It was the first bigger thing
to its right — that's *why* it popped it.

Real-life version: **people waiting for someone taller to walk by.**
When tall-enough walks past, the person at the front shouts "found
one!" and leaves — that passerby was their answer, permanently.

## Hand-trace `[2, 1, 2, 4, 3]` — stack holds INDICES

```
i=0 (2): stack empty → push 0              stack idx: [0]
i=1 (1): 1 < nums[0]=2 → push 1            stack: [0, 1]
i=2 (2): 2 > nums[1]=1 → pop 1, ans[1]=2
         2 > nums[0]=2? no (equal) → push 2
                                         stack: [0, 2]
i=3 (4): 4 > nums[2]=2 → pop 2, ans[2]=4
         4 > nums[0]=2 → pop 0, ans[0]=4
         stack empty → push 3              stack: [3]
i=4 (3): 3 < nums[3]=4 → push 4            stack: [3, 4]
end: indices 3, 4 never answered → stay -1

ans = [4, 2, 4, -1, -1]
```

Every index enters once and leaves at most once → **O(n)** total, not
O(n²).

## Try it

```python
def next_greater(nums):
    ans = [-1] * len(nums)
    stack = []                             # indices still waiting
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:   # x answers the top
            ans[stack.pop()] = x
        stack.append(i)
    return ans                             # leftovers stay -1
```

```python
print(next_greater([2, 1, 2, 4, 3]))   # the trace's answer
print(next_greater([5, 4, 3]))         # decreasing — nobody answers
```

```
[4, 2, 4, -1, -1]
[-1, -1, -1]
```

## Why it exists

The O(n²) scan asks "what's bigger than me, rightward?" fresh for EVERY
element. The stack notices an element that found its answer never needs
checking again — the newcomer answered it *permanently*. Holding only
the unanswered, in decreasing order, makes each pop a final answer.

## Where it's used — one pattern, many costumes

- **Daily temperatures** (`medium/p02`): "how many days until warmer?"
  Same code — push indices — but store a DISTANCE:
  `ans[i] = i - popped_index`, not the temperature.
  `[73,74,75,71,69,72,76,73]` → `[1,1,4,2,1,1,0,0]`.
- **Largest rectangle in histogram** (`hard/p02`): when a shorter bar
  pops a taller one, the popped bar's reign just ended — its max
  rectangle spans the range it ruled. Add a sentinel `0` at the end to
  force-flush the stack.
- Stock span, "remove k digits," trapping rain water.

## Common mistake — values vs indices

Storing **values** when you need **indices**. Daily temperatures asks
"how many days *later*?" — you must push `i` and compute `i - popped`;
a temperature can't tell you its position.

Two more: leftovers on the stack have NO answer — leaving them at -1 is
correct, not a bug. And `<` vs `<=` on the pop condition decides how
equal values behave — "next *strictly* greater" pops only strictly
smaller tops.

## Your turn

```python
print(next_greater([1, 3, 2]))
```

What prints? Trace the stack first.

<details><summary>Answer</summary>
`[3, -1, -1]` — 1 gets answered by 3 (pop, ans[0]=3), then 3 pushes;
2 < 3 so it just pushes. Indices 1 and 2 sit unanswered at the end →
-1, -1.
</details>

---

**← Prev** [07 — Balanced brackets](07-balanced-brackets.md) ·
**Next →** [09 — Sliding-window max & BFS](09-sliding-window-max-and-bfs.md)
