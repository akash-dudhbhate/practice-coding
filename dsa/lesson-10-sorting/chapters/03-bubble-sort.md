# 03 — Bubble Sort: the biggest one floats up

> 5-minute read.

## The idea, plain words

Walk down the list. Whenever two neighbors are out of order, swap them.
Repeat until a full walk makes zero swaps.

Why "bubble"? On each pass, the **biggest remaining element gets pushed to
the end** — like a bubble rising to the surface. After pass 1 the largest
is in its final spot; after pass 2, the second-largest too.

## Watch it happen — trace `[5, 2, 4, 1]`

```
Pass 1 (push the biggest to the end):
  [5,2,4,1]  5>2 → swap → [2,5,4,1]
  [2,5,4,1]  5>4 → swap → [2,4,5,1]
  [2,4,5,1]  5>1 → swap → [2,4,1,5]   ← 5 is final
Pass 2 (last spot done, stop one earlier):
  [2,4,1,5]  2<4 → ok
  [2,4,1,5]  4>1 → swap → [2,1,4,5]   ← 4 is final
Pass 3:
  [2,1,4,5]  2>1 → swap → [1,2,4,5]   ← done
```

## The code

```python
def bubble_sort(arr):
    arr = arr[:]                          # don't trash the caller's list
    for end in range(len(arr) - 1, 0, -1):     # last `end` spots are final
        swapped = False
        for i in range(end):
            if arr[i] > arr[i + 1]:       # neighbors out of order?
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:                   # clean pass → already sorted!
            break
    return arr

print(bubble_sort([5, 2, 4, 1]))          # [1, 2, 4, 5]
```

The `swapped` flag is the early exit: if a whole pass swaps nothing, every
pair was already in order — quit early. That makes the *best case* O(n).

## Why it exists

Honestly? Mostly to teach. It's the simplest sort to explain (neighbors,
swap, repeat) and the early-exit flag is a nice idea. But it's almost never
the right choice in practice — it's just as O(n²) as the others while doing
MORE swaps than any of them.

## Where it's used

Classrooms, and occasionally as a "is this already sorted?" check — one
pass with the flag answers that in O(n).

## Common mistake

Forgetting the `swapped` flag — without it you always pay the full O(n²)
even on a sorted input. (Also: re-running over the tail — after pass k the
last k elements are FINAL, so the inner loop should stop earlier each
time.)

## Your turn

On `[1, 2, 3, 5, 4]`, how many passes does bubble sort need WITH the
early-exit flag?

<details><summary>Answer</summary>
2. Pass 1 swaps the `5,4` pair (and bubbles nothing else); pass 2 makes
zero swaps → flag triggers → stop. Without the flag it would still run
all 4 passes.
</details>

---

**← Prev** [02 — Sorted + stability](02-sorted-and-stability.md) ·
**Next →** [04 — Selection sort](04-selection-sort.md)
