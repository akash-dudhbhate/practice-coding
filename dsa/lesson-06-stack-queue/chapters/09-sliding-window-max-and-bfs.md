# 09 — Monotonic Deque (Sliding-Window Max) + FIFO (BFS)

> 6-minute read. Two advanced queue-family patterns, one chapter.

## The idea, plain words

**Sliding-window maximum:** a window of size k slides across an array;
report the max at each step.

```
nums = [1,3,-1,-3,5,3,6,7], k=3   →   [3, 3, 5, 5, 6, 7]
```

Naive: `max(window)` per step → O(n·k). The deque trick: keep **indices
of candidates, values decreasing front → back**. The front is always
the current max. When a bigger element arrives, everything smaller
behind it can *never* be max again — evict them from the back. "Useless
forever" — the monotonic-stack idea rotated.

**BFS (breadth-first search):** explores a graph layer by layer —
enqueue the start, then loop `popleft → visit → enqueue neighbors`.
FIFO guarantees you visit every node at distance d before any at
d+1 → shortest path in unweighted graphs. (Preview only — full
treatment in lesson 13.)

## Hand-trace the window, `[1,3,-1,-3,5,3,6,7]`, k=3

```
i=0 ( 1): dq=[0]
i=1 ( 3): 3>1 → pop 0; dq=[1]
i=2 (-1): -1<3 → dq=[1,2];  window full → max = nums[1] = 3
i=3 (-3): dq=[1,2,3];  max=3
i=4 ( 5): evict back: 5>-3,5>-1,5>3 → pop 3,2,1; dq=[4]; max=5
i=5 ( 3): dq=[4,5]; max=5
i=6 ( 6): evict 5,4 → dq=[6]; max=6
i=7 ( 7): evict 6 → dq=[7]; max=7
output: [3, 3, 5, 5, 6, 7]
```

## Try it

```python
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()                     # indices, values decreasing front→back
    out = []
    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:        # slid out the left edge
            dq.popleft()
        while dq and nums[dq[-1]] < x:      # useless forever — evict
            dq.pop()
        dq.append(i)
        if i >= k - 1:                      # window full → record front
            out.append(nums[dq[0]])
    return out
```

```python
print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))
```

```
[3, 3, 5, 5, 6, 7]
```

Each index enters and leaves the deque at most once → O(n). And BFS in
four lines (mental model for now):

```python
# dist = {start: 0};  q = deque([start])
# while q:
#     node = q.popleft()                    # FIFO: nearest first
#     for nxt in neighbors(node):
#         if nxt not in dist: dist[nxt] = dist[node] + 1; q.append(nxt)
```

## Why it exists

- Window max: re-computing `max()` per window throws away everything
  you already learned. The deque remembers *who can still win* — and
  the front is always it.
- BFS: a stack would dive deep first (that's DFS) and can't promise
  shortest hops. Only FIFO visits in strict distance order.

## Where it's used

- Stream processing, trading signals ("max of the last k ticks")
- Shortest-path puzzles, social-network degrees, level-order trees,
  web crawlers (BFS)

## Common mistake

- `max(nums[i:i+k])` inside the slide loop → O(n·k) — the same
  "re-scan inside a loop" trap from lesson 05.
- BFS written with `pop()` instead of `popleft()` — silently becomes
  DFS. The code RUNS; the answers are wrong.
- Storing values instead of indices in the deque — you can't tell when
  a value slid out of the window. Indices carry their own expiry date.

## Your turn

In `max_sliding_window`, why does the first `while` check
`dq[0] <= i - k` instead of `<`?

<details><summary>Answer</summary>
The current window is indices `i-k+1 … i`. An index at `i-k` is one
step outside — already gone. `<=` evicts it right on time; `<` would
keep a stale max one step too long and could report a "max" from
outside the window.
</details>

---

**← Prev** [08 — Monotonic stack](08-monotonic-stack-next-greater.md) ·
**Next →** [10 — Two stacks make a queue](10-two-stacks-make-a-queue.md)
