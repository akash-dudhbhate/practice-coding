# 06 — Pop: swap the root with the last leaf, then bubble down

> 5-minute read. The mirror image of push.

## The idea, plain words

Popping removes the **root** — the minimum, which is the whole point of
the structure. But ripping out the root leaves a hole at the top and
breaks the shape. So:

1. **Save** the root value (that's your answer).
2. **Move the LAST element** into the root slot — the last slot is the
   only one you can remove while keeping the tree complete.
3. **Bubble down** (a.k.a. *sift-down*): while the moved item is bigger
   than a child, swap it with its **smaller** child.

## Hand-trace: pop `[1, 3, 5, 7, 4]`

```
step 0  remove root 1, move last (4) to the top:   array [4, 3, 5, 7]
             4
            / \
           3   5        4 > its children — violation
          /
         7

step 1  swap with the SMALLER child (3, not 5):    array [3, 4, 5, 7]
             3
            / \
           4   5
          /
         7

step 2  4's only child is 7, and 4 < 7 — stop.
        Pop returned 1, heap is [3, 4, 5, 7]. ✅
```

Why the **smaller** child? If you swapped `4` with `5` instead, `5`
would land on top of `3` — parent bigger than child, still broken.
Always swap with the child that can legally become the new parent.

## In real code

```python
import heapq

h = [1, 3, 5, 7, 4]
smallest = heapq.heappop(h)
print(smallest)      # 1
print(h)             # [3, 4, 5, 7]
```

The inside version — again just chapter-04 index math:

```python
def my_pop(h):
    top = h[0]
    h[0] = h.pop()                 # last element -> root
    i = 0
    while True:
        kids = [j for j in (2*i + 1, 2*i + 2) if j < len(h)]
        if not kids:
            break
        smallest_kid = min(kids, key=lambda j: h[j])
        if h[i] <= h[smallest_kid]:
            break                  # rule satisfied
        h[i], h[smallest_kid] = h[smallest_kid], h[i]
        i = smallest_kid
    return top

h = [1, 3, 5, 7, 4]
print(my_pop(h), h)                # 1 [3, 4, 5, 7]
```

## Why it exists

Same insight as push: removing the root can only break the rule along
ONE root-to-leaf path, so one downward walk repairs it. Moving the
*last* element up (rather than a child) keeps the tree complete for
free — the last slot is always removable.

## Where it's used

`heapq.heappop`, `heapq.heapreplace` (pop + push fused into one pass),
heapsort's extraction loop.

## Common mistake

Two classics: **swapping with the larger child** (leaves a violation —
always pick the smaller one in a min-heap), and **`heappop` on an empty
heap** which raises `IndexError` — guard with `if h:`. Also: if you only
want to *look* at the minimum, `h[0]` is O(1); `heappop` is O(log n)
**and deletes it**.

## Your turn

Pop `[1, 2, 4, 5, 3]`. What gets returned, and what's the array after?

<details><summary>Answer</summary>
Returns `1`. Move last (3) to root → `[3, 2, 4, 5]`. Children of 3 are
2 and 4 → smaller is 2 → swap → `[2, 3, 4, 5]`. Now 3's only child is
5, and `3 < 5` → stop. Final array: `[2, 3, 4, 5]`.
</details>

---

**← Prev** [05 — Push: bubble up](05-push-append-and-bubble-up.md) ·
**Next →** [07 — Why push and pop are O(log n)](07-why-push-and-pop-are-ologn.md)
