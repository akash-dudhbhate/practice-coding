# 04 — The array trick: a tree hiding inside a list

> 5-minute read. The most important mechanical chapter.

## The idea, plain words

Here's a sneaky fact: a *complete* binary tree fits into a flat array
with **zero wasted space** — because "complete" means no gaps. Just lay
the tree down level by level:

```
tree:          1             array: [1, 3, 5, 7, 4]
              / \                    i0 i1 i2 i3 i4
             3   5
            / \
           7   4
```

Read the tree left-to-right, top-to-bottom: `1, 3, 5, 7, 4` — that's
the array, in order. No node objects, no pointers. **A Python list IS
the heap.** The tree is just how we *visualize* the list.

To walk the "tree" inside the array, you only need three formulas —
for the node at index `i`:

```
parent(i)  = (i - 1) // 2
left(i)    = 2 * i + 1
right(i)   = 2 * i + 2
```

Hand-check on the picture: index 4 holds `4`; its parent is
`(4-1)//2 = 1` → index 1 holds `3`. Look at the tree — yes, `4` hangs
under `3`. And index 1's children are `2*1+1 = 3` and `2*1+2 = 4` →
values `7` and `4`. The picture agrees.

## Run the math

```python
a = [1, 3, 5, 7, 4]

i = 4                              # the 4
p = (i - 1) // 2
print("parent of", a[i], "is", a[p])        # parent of 4 is 3

i = 1                              # the 3
kids = [a[2*i + 1], a[2*i + 2]]
print("children of", a[i], "are", kids)     # children of 3 are [7, 4]
```

## Why it exists

Two reasons, and both are huge:

1. **No pointers.** Each node's "children" are just index math — no
   objects to create, no links to follow. Fast and memory-friendly.
2. **Completeness does the packing.** Because the tree has no holes,
   "next free slot" is always just `append` at the end — which is
   exactly what makes push (next chapter) so clean.

This is *the* reason `heapq` functions take a plain list — they
maintain the heap rule on your list using nothing but index math.

## Where it's used

`heapq` itself, binary heaps in every language's standard library, and
any array-packed tree (segment trees in advanced lessons use the exact
same indexing).

## Common mistake

**Mixing up 0-based and 1-based formulas.** Textbooks often use
1-based: `parent = i//2`, `children = 2i, 2i+1`. Python is 0-based:
`(i-1)//2` and `2i+1, 2i+2`. Mixing the two silently points at the
wrong nodes — everything "runs" but the heap is corrupt.

## Your turn

In `a = [1, 3, 5, 7, 4, 9, 8]`, what are the children of index 2,
and what values do they hold?

<details><summary>Answer</summary>
`left = 2*2+1 = 5`, `right = 2*2+2 = 6` → indices 5 and 6 → values
`9` and `8`. (And 5 ≤ both, so the heap rule holds at that node.)
</details>

---

**← Prev** [03 — What a heap is](03-what-a-heap-is.md) ·
**Next →** [05 — Push: append and bubble up](05-push-append-and-bubble-up.md)
