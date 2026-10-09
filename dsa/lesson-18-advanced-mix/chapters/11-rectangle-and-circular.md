# 11 — Largest Rectangle + Circular Arrays

> 5-minute read. Two moves that finish the monotonic-stack set.

## The idea, plain words — move 1: flip the order

Chapter 10 kept a *decreasing* stack. For **largest rectangle in a
histogram**, keep an *increasing* stack of bar indices instead. When a
shorter bar arrives, pop taller bars — each popped bar's rectangle
**ends here**, and its left edge is just past the new stack top:

```
height h popped at index i:
    right edge = i
    left edge  = stack's new top (or start of array)
    width      = i - stack[-1] - 1      (or i if stack empty)
    area       = h × width
```

## Hand-trace — `[2, 1, 5, 6, 2, 3]` (with a sentinel 0 at the end)

```
i=0(2): push0        i=1(1): 2>1 → pop0 h=2 w=1 → area 2; push1
i=2(5): push2        i=3(6): push3
i=4(2): 6>2 → pop3 h=6 w=1 → 6
        5>2 → pop2 h=5 w=2 → 10    ← THE answer
        1<2 → push4
i=5(3): push5
i=6 (sentinel 0): pop5 h=3 w=1 → 3; pop4 h=2 w=4 → 8;
                  pop1 h=1 w=6 → 6; stack empty
best = 10   (bars 5 and 6 together: 2 wide × 5 tall)
```

## In code — note the sentinel trick

```python
def largest_rectangle_area(heights):
    stack = []                          # indices, heights increasing
    best = 0
    for i, h in enumerate(heights + [0]):   # extra 0 FLUSHES the stack
        while stack and heights[stack[-1]] > h:
            H = heights[stack.pop()]
            W = i if not stack else i - stack[-1] - 1
            best = max(best, H * W)
        stack.append(i)
    return best

print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))   # 10
```

## Move 2 — circular arrays: loop twice, push once

For "next greater, but the array wraps around" (`medium/p03`): run `i`
over `range(2*n)`, read `nums[i % n]` — the second pass pops leftovers
with wraparound answers. But **push only during the first n** or you
corrupt the stack:

```python
def next_greater_circular(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []
    for i in range(2 * n):
        x = nums[i % n]
        while stack and nums[stack[-1]] < x:
            ans[stack.pop()] = x
        if i < n:                    # only real positions get pushed
            stack.append(i)
    return ans

print(next_greater_circular([1, 2, 1]))       # [2, -1, 2]
print(next_greater_circular([5, 4, 3, 2, 1])) # [-1, 5, 5, 5, 5]
```

## Why it exists

Two problems, same skeleton — one pop-condition and one width/answer
formula away from each other. Master the skeleton once, swap the
details per problem. That's the real lesson-18 takeaway.

## Where it's used

Largest rectangle / maximal rectangle (`hard/p03`), trapping-rain
variants, stock span — and circular next-greater (`medium/p03`) plus
"next element with wraparound" questions generally.

## Common mistake

**Forgetting to flush.** `heights = [2,4]` never pops inside the loop —
pending bars die with their right edge unknown. The sentinel `0`
guarantees every bar pops. And on circular: pushing during the second
pass duplicates indices → garbage answers.

## Your turn

Why does the sentinel `0` at the end guarantee a flush?

<details><summary>Answer</summary>
Every real height is positive, so `0` is smaller than all of them — the
`while heights[stack[-1]] > h` pops the *entire* remaining stack. Each
pop computes its area with `i = n` as the right edge. Nothing pending
survives.
</details>

---

**← Prev** [10 — Monotonic stack: next greater](10-monotonic-stack-next-greater.md) ·
**Next →** [12 — Union-find: when it beats DFS](12-union-find-when-it-wins.md)
