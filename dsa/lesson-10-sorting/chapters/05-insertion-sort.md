# 05 — Insertion Sort: sorting a hand of cards

> 5-minute read.

## The idea, plain words

Real-life version: **how you sort cards dealt to you one at a time.** Your
left hand holds sorted cards. Pick up the next card, slide it left past
bigger cards, drop it in the gap.

In code: grow a sorted *prefix*. Take `arr[i]`, shift bigger elements one
spot right, insert it in the hole that opens up.

## Watch it happen — trace `[5, 2, 4, 1]`

```
start: [5 | 2, 4, 1]     left of | is sorted (a single card always is)

i=1, key=2: 5>2 → shift 5 right   [5,5,4,1] → insert → [2,5,4,1]
i=2, key=4: 5>4 → shift 5 right   [2,5,5,1] → insert → [2,4,5,1]
i=3, key=1: 5,4,2 all >1 → shift all three → insert → [1,2,4,5]
```

## The code

```python
def insertion_sort(arr):
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:    # shift bigger elements right
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key                  # drop key into the gap
    return arr

print(insertion_sort([5, 2, 4, 1]))       # [1, 2, 4, 5]
```

## Why it exists — the superpower

The `while` loop **exits the moment it hits something ≤ key**. On a
nearly-sorted array almost every element inserts immediately → close to
O(n), not O(n²). And on tiny arrays there's no recursion or bookkeeping
overhead at all. That's why real-world hybrid sorts — including Python's
own Timsort — switch to insertion sort on small chunks.

## Where it's used

- Inside hybrid sorts for small subarrays (~10–60 elements).
- Nearly-sorted streams: new items trickling into mostly-ordered data.
- It's stable too — elements only move past strictly bigger ones.

## Common mistake

Picking it for **reversed** input: every element must shift past every
other → the worst case, max O(n²). Insertion sort is fast exactly when the
input is *almost* sorted, slow when it's backwards.

## Your turn

On `[1, 2, 3, 5, 4]` — how many shifts does insertion sort do total?

<details><summary>Answer</summary>
1. The `4` shifts past `5` once and lands at index 3; every other element
finds `arr[j] <= key` immediately and the while loop does zero iterations.
Nearly sorted → nearly free.
</details>

---

**← Prev** [04 — Selection sort](04-selection-sort.md) ·
**Next →** [06 — Why all three are O(n²)](06-why-all-n2.md)
