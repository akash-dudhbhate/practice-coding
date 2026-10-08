# Lesson 12 — Concepts Explained (Heaps)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What a Heap Is — complete tree + heap property

**What:** A heap is a **complete binary tree** (every level full except possibly the last, which fills left-to-right) obeying one ordering rule:

- **Min-heap:** every parent `<=` its children → the **minimum is always at the root**.
- **Max-heap:** every parent `>=` its children → the maximum is always at the root.

The rule is *vertical* only — siblings have no order between them. A heap is **not** a BST: `5`'s left child may be `7` while its right child is `6` — perfectly legal, since only parent-vs-children matters.

```
            1                  <- minimum sits at the root
           / \
          3   2                each parent <= its children
         / \ / \
        7  4 8  5
       /
      9                        <- last level fills LEFT to right
```

**Why it exists:** Lots of work is "repeatedly grab the smallest/biggest thing, then add more things." A sorted array makes grabbing O(1) but inserting O(n) (shifting); an unsorted array makes insert O(1) but grabbing O(n) (scanning). A heap splits the difference cleverly: **both are O(log n)** — you trade *full* order for *just enough* order to always find the extreme fast.

**Where it's used:** Priority queues everywhere (OS schedulers, event loops, `queue.PriorityQueue`), top-K queries, streaming medians, Dijkstra's shortest path and Prim's MST (lesson 14!), merge-k-sorted-streams, load balancing ("least busy server" = min-heap).

**What goes wrong without it:**
- **Calling it "sorted."** A heap array `[1,3,2,7,4,8,5,9]` isn't sorted — popping *produces* sorted order, the array itself doesn't hold it. People who expect `heap[1]` to be the 2nd smallest get `3` when the real answer is `2`.
- **Confusing it with a BST.** Heap: parent ≤ children (vertical, partial). BST: left < node < right (horizontal + vertical, total). Same tree shape, different rule, different jobs.

---

## The Array Trick — no pointers, just index math

**What:** A complete binary tree fits perfectly into a flat array — the completeness means no gaps. For node at index `i` (0-based):

```
        parent(i) = (i - 1) // 2
        left(i)   = 2i + 1
        right(i)  = 2i + 2
```

```
            [0]                  index: 0
           /   \
         [1]   [2]               index: 1, 2      parent(1) = parent(2) = 0
        /  \   /  \
      [3] [4] [5] [6]            index: 3,4,5,6   parent(4) = (4-1)//2 = 1
     /
   [7]                           index: 7        parent(7) = 3

array: [1, 3, 2, 7, 4, 8, 5, 9]
        i0  i1 i2 i3 i4 i5 i6 i7
```

**Why it exists:** Pointer-free = no node objects, no allocation churn, cache-friendly. It's *the* reason heaps are used in tight loops — a Python list IS the heap; `heapq` functions just maintain the invariant on your list.

**Where it's used:** `heapq` itself, binary heaps in every standard library, and any array-packed tree (segment trees use the same indexing).

**What goes wrong without it:**
- **Off-by-one in the formulas.** With 1-based indexing it's `parent = i//2, children = 2i/2i+1`; with 0-based (Python, everything here) it's `(i-1)//2` and `2i+1/2i+2`. Mixing the two conventions silently corrupts the heap.
- **Thinking the array must stay sorted.** It's "partially ordered": `heap[0]` is the min, but later positions have no global order guarantees.

---

## Sift-Up / Sift-Down — why insert and pop are O(log n)

**What:** Two repair operations that restore the heap property after a change:

- **Sift-up (on push):** append the new value at the end (next free slot in the complete tree), then swap it upward with its parent while it's smaller than the parent. Worst case: travels leaf → root = `height = log₂ n` swaps.
- **Sift-down (on pop):** pop removes the root (index 0); move the *last* element into the root slot, then swap it downward with its *smaller* child while a child is smaller. Again ≤ `log₂ n` swaps.

```
push 0 onto [1,3,2,7,4,8,5,9]:

        1                    1                    0
       / \                  / \                  / \
      3   2      →        3   2      →        1   2
     / \ / \             / \ / \             / \ / \
    7  4 8  5           7  0 8  5           3  4 8  5
   / \                 / \                 / \ /
  9   0   appended    9   4   sift-up     9  7

  0 appended, swaps with 4, then with 1 — 2 hops, done.
```

**Why it exists:** Each sift step walks one level of a height-`log₂ n` tree — that's the entire O(log n) guarantee, and it works *because* the tree is complete (bounded height by construction). This is also `heapify`'s story: `heapify` sift-downs every non-leaf bottom-up — a cute proof shows it's O(n) total, not O(n log n), which is why `heapify(list)` beats n pushes.

**Where it's used:** `heapq.heappush` = append + sift-up; `heapq.heappop` = swap-root-with-last + sift-down. You almost never write them in Python, but interviews ask you to *explain* or implement them.

**What goes wrong without it:**
- **Sifting down with the WRONG child** — must compare against the *smaller* child in a min-heap; swapping with the larger one leaves a violation.
- **Peeking with `pop`** when you just want the min: `heap[0]` is O(1); `heappop` is O(log n) AND removes it.
- **`heappop` on an empty heap** → `IndexError`. Guard with `if heap:`.

```python
import heapq

h = [5, 1, 3, 8, 4]
heapq.heapify(h)       # rearranges in place: [1, 4, 3, 8, 5]
heapq.heappush(h, 0)   # sift-up:   [0, 1, 3, 8, 5, 4]
heapq.heappop(h)       # -> 0, sift-down repairs: [1, 4, 3, 8, 5]
h[0]                   # peek min, O(1): 1
```

---

## `heapq` Is a MIN-Heap — the negation trick for max-heaps

**What:** Python ships only a min-heap. To get max-heap behavior, store **negated values**: push `-x`, pop and negate back. `-x` smallest at the root ⇔ `x` biggest.

```python
h = []
for x in [3, 1, 4]:
    heapq.heappush(h, -x)     # internal order: [-4, -1, -3]
-heapq.heappop(h)             # -> 4  (the real max)
```

For "smallest id / earliest time wins" priorities with payloads, push **tuples** `(priority, item)` — tuples compare lexicographically, so the heap orders by priority first, then by the second element as tiebreak.

```python
h = []
heapq.heappush(h, (2, "wake up"))
heapq.heappush(h, (1, "fix prod"))
heapq.heappush(h, (1, "answer pager"))
heapq.heappop(h)              # (1, 'answer pager') — ties break on 2nd element
```

**Why it exists:** One implementation serves both directions; negation works because ordering flips under negation, and tuples work because Python compares them element-by-element for free.

**Where it's used:** `last_stone_weight` (always smash two heaviest), task schedulers (highest frequency first), Dijkstra with `(distance, node)` tuples — the tuple trick IS how you attach payloads to priorities.

**What goes wrong without it:**
- **Forgetting to negate on the way back out** — you push `-x`, then treat `heappop(h)` as the max directly and get `-4`.
- **Tuples with uncomparable payloads** — `(2, node_a)` vs `(2, node_b)` tie-breaks by comparing `node_a < node_b`, which crashes on objects without `<`. Fix: insert a unique counter — `(priority, counter, item)`.
- **Negating when the tuple has a payload** — `(-dist, node)` works; negating a whole tuple doesn't.

---

## The Top-K Pattern — heap of size k

**What:** "Give me the k biggest" doesn't need the whole input sorted — it needs a **min-heap of size k** holding *the best k seen so far*:

```python
def kth_largest(nums, k):
    h = nums[:k]
    heapq.heapify(h)                    # min-heap of the first k
    for x in nums[k:]:
        if x > h[0]:                    # only bother if it beats the worst kept
            heapq.heapreplace(h, x)     # pop min + push in one step
    return h[0]                         # the k-th largest overall
```

**Why it exists:** sorting is O(n log n); this is **O(n log k)** — when k is small relative to n (top 10 of 10 million), that's the difference between sorting everything and barely noticing the data. For *streaming* input it's better still: you never store more than k items.

Flip it for "k smallest" → keep a max-heap (negated) of size k. The heap always holds "the k best so far," and its root is the *worst of the best* — the bar a newcomer must beat.

**Where it's used:** top-K frequent words, k closest points, kth largest in a stream, "merge k sorted" (heap holds one frontier element per list — a k-sized heap too).

**What goes wrong without it:**
- **Keeping the wrong heap direction** — for k *largest* you keep a *min*-heap (so the smallest of the kept k sits on top, easy to evict). Beginners build a max-heap "because we want largest," which keeps the whole input and answers nothing.
- **Pushing everything then popping** — `heappush` all n, pop k: O(n log n) space O(n). Works, but defeats the point; `heapreplace` or `pushpop` keeps size at k.

**Worked example — `kth_largest([3,2,1,5,6,4], 2)`:**

```
h = [2, 3]          heapified first k=2  (min on top)
x=1:  1 < h[0]=2    skip
x=5:  5 > 2         heapreplace -> h = [3, 5]
x=6:  6 > 3         heapreplace -> h = [5, 6]
x=4:  4 < 5         skip
answer: h[0] = 5    (the 2nd largest)
```

Expected output: **5**

---

## `heapq` Utilities — merge, nlargest, nsmallest, and the priority queue

**What:**

```python
heapq.nsmallest(k, iterable)   # k smallest — O(n log k), cleaner than hand-rolling
heapq.nlargest(k, iterable)
heapq.merge(a, b, c, ...)      # lazily merges SORTED iterables — never materializes all
heapq.heappushpop(h, x)        # push then pop — faster than two calls
heapq.heapreplace(h, x)        # pop then push — pops the min, always
```

`merge` yields elements in sorted order across any number of sorted sources — it's the engine of merge-k-sorted-lists.

**Why it exists:** these are battle-tested versions of exactly the patterns above — but `nlargest`/`nsmallest` can't express "size-k heap with custom predicate," so knowing the manual pattern still matters.

**Where it's used — the priority queue view:** a heap IS a priority queue: `(priority, item)` tuples. Dijkstra's algorithm (lesson 14) is literally `heappush(heap, (dist, node))` / `heappop` in a loop — the frontier always expands the closest known node. Event simulators, Huffman coding, A* — all the same shape.

**What goes wrong without it:**
- **`heapq.merge` input must already be sorted** — it doesn't sort; it *merges*. Feeding it unsorted lists produces garbage silently.
- **`heapreplace` vs `heappushpop`** — `heapreplace` pops FIRST (new item can't be the popped min), `heappushpop` pushes first (x can come right back out if it's the min). Top-K filtering wants `heapreplace` gated by `x > h[0]`.

---

## Two Heaps — the streaming-median pattern

**What:** To answer "median of everything seen so far" after every new element, keep the stream split in two:

```
lo = max-heap of the lower half   (Python: store negated)
hi = min-heap of the upper half

         lo                hi
        max↑              min↑
      [1, 2, 4]   |   [5, 8, 9]
                  ^
            the boundary — the median lives HERE
```

Invariants: `max(lo) <= min(hi)` (every lower-half element ≤ every upper-half element) and `len(lo) - len(hi)` ∈ {0, 1}. Then the median is `-lo[0]` when `lo` is bigger, else `(-lo[0] + hi[0]) / 2` — both O(1) reads off the roots.

**Why it exists:** Sorting the whole window per step is O(n log n) per insert → O(n² log n) for a stream. You never need the halves sorted — the median only depends on the two middle values, which are exactly the heap roots. O(log n) per insert, O(1) per median.

**How an insert works:** push into `lo`, immediately move `lo`'s max into `hi` (guarantees the ordering invariant), then if `hi` grew bigger than `lo`, move `hi`'s min back (guarantees the size invariant):

```python
heappush(lo, -x)
heappush(hi, -heappop(lo))      # lo hands its biggest to hi
if len(hi) > len(lo):           # hi got too big -> give lo its smallest
    heappush(lo, -heappop(hi))
```

**Worked example — stream `[5, 1, 4, 2, 3]`:**

```
x=5: lo=[-5] hi=[]        -> rebalance -> lo=[-5] hi=[]    median 5.0
x=1: lo=[-1] hi=[5]       (1 routed lo->hi, sizes ok)      median (1+5)/2=3.0
x=4: lo=[-4,-1] hi=[5]    (4 routed through lo, lo bigger) median 4.0
x=2: lo=[-2,-1] hi=[4,5]                                   median (2+4)/2=3.0
x=3: lo=[-3,-2,-1] hi=[4,5]                                median 3.0
```

**What goes wrong without it:** forgetting the rebalance-back step lets `hi` exceed `lo` by 2+, so the "median" reads a value that isn't the middle — see EXTRA-PRACTICE Debug 04.

---

## The Heap as Priority Queue — foreshadowing graphs

**What:** A heap is the engine inside a *priority queue*: items carry priorities, and the minimum-priority item is always on top. In Python that's tuples `(priority, tiebreak_counter, item)`.

**Where this pays off next lesson:** **Dijkstra's shortest path** (lesson 14) is a BFS where "next node to visit" means "closest frontier node," not "oldest":

```python
heap = [(0, start)]                       # (distance, node)
while heap:
    dist, node = heappop(heap)            # expand the closest frontier
    if dist > best_dist[node]:            # stale entry — skip it
        continue
    for nxt, w in graph[node]:
        heappush(heap, (dist + w, nxt))   # push relaxed distance
```

Two heap idioms to notice, because you'll see them again: the **lazy deletion** (push a better entry instead of removing the old one; skip stale pops) and **`(priority, item)` tuples** carrying payloads. Every "process in order of urgency" problem — event simulation, task scheduling, Huffman coding — is this loop.

**What goes wrong without it:** using a plain FIFO queue for Dijkstra visits nodes in hop-count order, not distance order — silently wrong shortest paths on weighted graphs. The heap is the difference between "nearest first" and "first-come first-served."

---

## The Recipe — recognize it in 10 seconds

1. **"kth largest/smallest/most frequent/closest"?** → heap of size k. Largest → min-heap of the k best; smallest → max-heap (negate).
2. **"Repeatedly take the min/max while inserting"?** → plain heap. Need max → negate; need payloads → tuples `(priority, counter, item)`.
3. **"Two-sided stream statistic" (median)?** → TWO heaps: max-heap for the lower half, min-heap for the upper half, keep sizes within 1.
4. **"Merge k sorted streams"?** → one heap entry per source, `(value, source_index, element_index)`.
5. Say the complexity out loud: push/pop **O(log n)**, peek **O(1)**, heapify **O(n)**, top-k selection **O(n log k)** vs sorting **O(n log n)**.

---

## The Pitfall Gallery — five ways heaps go wrong

**1. Expecting heap array = sorted array.**
```python
heapq.heapify(a)     # a[0] IS the min — a[1:] is NOT sorted
```
`heap[1]` is not the second-smallest. Pop it if you want it.

**2. Wrong heap direction for top-k.**
For k *largest*: keep a **min-heap of size k** (evict the smallest kept). A max-heap of the whole input is just... a sorted array with extra steps.

**3. Tuple tie-break crash.**
```python
heappush(h, (priority, item))        # ties compare item — needs __lt__
heappush(h, (priority, i, item))     # i = unique counter — never compares items
```

**4. Using `pop(0)`/list-sort inside the loop.**
Re-sorting (`h.sort()`) every iteration is O(n log n) per step — if you're doing that, you've built a slow heap by hand. Similarly `list.pop(0)` is O(n).

**5. `pop` when you meant `peek`.**
`heappop` removes. `h[0]` looks without touching. Also: `heappop([])` → `IndexError` — guard empty heaps.

**Edge cases to always test:** empty input, k = 1, k = len(nums), all-equal values (does the heap dedupe? No — it counts multiplicity, which is usually right), negative numbers (does your negation trick flip them correctly?), and "impossible" cases (reorganize-string when one char is > half the length → return "").
