# 10 — Monotonic Stack: Next Greater

> 5-minute read. Your lesson-06 stack, upgraded.

## The idea, plain words

You met stacks in lesson 06. A **monotonic** stack is just a stack kept
*sorted* — and the rule is beautiful:

> Push elements onto the stack. When a new element **breaks the
> order**, pop everything it dominates — and the new element IS the
> answer to each popped one.

Think of a line of people waiting to see a taller person. The stack
holds everyone still waiting (their heights shrink toward the top).
When a tall person arrives, every shorter waiter pops — *"you're the
answer I was waiting for."* Each element is pushed once and popped
once → **O(n)** total.

## Hand-trace — next greater, `[2, 1, 2, 4, 3]`

The stack holds **indices** of unresolved elements (values decrease
toward the top):

```
i=0 (2): push 0                 stack=[0]
i=1 (1): 1 < 2, keeps order     push 1   stack=[0,1]
i=2 (2): nums[1]=1 < 2 → pop 1 → ans[1]=2
         nums[0]=2 < 2? no →    push 2   stack=[0,2]
i=3 (4): pop 2 → ans[2]=4; pop 0 → ans[0]=4; stack empty; push 3
i=4 (3): 3 < 4 →                push 4   stack=[3,4]
end: leftovers never got an answer → -1
answer = [4, 2, 4, -1, -1] ✓
```

## In code — 7 lines

```python
def next_greater(nums):
    ans = [-1] * len(nums)
    stack = []                          # indices, values decreasing
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            ans[stack.pop()] = x        # x is THEIR next-greater
        stack.append(i)
    return ans

print(next_greater([2, 1, 2, 4, 3]))    # [4, 2, 4, -1, -1]
```

## Why it exists

"For each element, find the next position where X" naively scans right
per element → O(n²). The stack exploits a deeper truth: a popped
element never needs re-checking — anything that would've been its
answer already arrived (that's *why* it was safe to pop).

## Where it's used

Daily temperatures ("days until warmer"), stock span, next/previous
greater-or-smaller, largest rectangle, trapping-rain variants — the
whole "next position where…" family.

## Common mistake

Pushing **values** when you need **indices**. "How many days until
warmer" and "how wide is the rectangle" are *distance* questions —
impossible without positions. Push `i`; read values via
`nums[stack[-1]]`. Also: `while`, not `if` — one element can dominate
MANY tops (`[5,4,3,2,1]` then a 6 pops all five).

## Your turn

In the trace at `i=3` (value 4), the stack `[0,2]` emptied completely.
Why did BOTH pop, not just the top?

<details><summary>Answer</summary>
Both `nums[2]=2` and `nums[0]=2` are smaller than 4 — 4 is the
next-greater for *every* unresolved element to its left, not just the
nearest one. The `while` loop keeps popping until the top is ≥ 4.
</details>

---

**← Prev** [09 — The bitwise trie: max XOR](09-bitwise-trie-max-xor.md) ·
**Next →** [11 — Largest rectangle + circular arrays](11-rectangle-and-circular.md)
