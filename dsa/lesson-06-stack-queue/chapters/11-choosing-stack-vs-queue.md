# 11 — Stack vs Queue: How to Choose

> 3-minute read. The cheat sheet — bookmark this chapter.

## The one-question test

**"Which element do I need NEXT — the newest or the oldest?"**

- Newest (most recent first) → **stack**
- Oldest (arrival order) → **queue / deque**

## The decision table

| Task | Structure | Why |
|------|-----------|-----|
| Match brackets, nested structure | stack | must match most-recent opener |
| Reverse a sequence | stack | LIFO reverses for free |
| Undo / back button / DFS | stack | last thing done is first to undo |
| Next greater / days-until-warmer | monotonic stack | the pop moment = answer found |
| Largest rectangle / span | monotonic stack | defines each bar's reign |
| Process in arrival order | deque (FIFO) | fair order, O(1) both ends |
| BFS / shortest unweighted path | deque (FIFO) | distance-d before distance-d+1 |
| Max over sliding window | monotonic deque | front is always current max |
| Queue built from stacks | two stacks | pour reverses LIFO → FIFO |

## The complexity mantra

Every structure in this lesson gives **O(1) per operation** (amortized
for the two-stack queue). So every problem here runs in **O(n)** — the
same "each element enters and leaves once" argument as sliding windows.
If your stack/queue solution comes out O(n²), a hidden re-scan snuck in
— find it.

## Try it — pattern-recognition drill

Cover the table and answer:

1. "Check this JSON is well-formed" → ?
2. "Deliver print jobs fairly" → ?
3. "How many days until a warmer temperature?" → ?

<details><summary>Answers</summary>
1. stack (bracket matching). 2. deque FIFO (arrival order).
3. monotonic stack (daily temperatures = next greater, distance
version).
</details>

## Your turn

You're told: "for each element, find the first smaller element to its
LEFT." Which structure, and what changes?

<details><summary>Answer</summary>
Still a monotonic stack — just keep it INCREASING and scan
left-to-right: pop while the top is ≥ x; whatever remains on top is the
nearest smaller to the left; then push x. Same pattern, mirror image.
</details>

---

**← Prev** [10 — Two stacks make a queue](10-two-stacks-make-a-queue.md) ·
**Next →** [12 — The pitfall gallery](12-pitfall-gallery.md)
