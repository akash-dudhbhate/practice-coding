# 01 — The problem: always grab the smallest (or biggest) fast

> 4-minute read. One idea only.

## The idea, plain words

Picture a hospital emergency room. Patients arrive constantly — a paper
cut, a broken arm, a heart attack. A normal line ("first come, first
served") would be a disaster: the heart-attack patient waits behind the
paper cut.

So the ER uses **triage**: when a doctor frees up, they don't ask "who
arrived first?" — they ask **"who is most urgent right now?"**

That's the whole problem this lesson solves:

- **add(item)** — new thing arrives
- **take_best()** — hand me the most extreme item (smallest, biggest,
  most urgent — whatever "best" means for the problem)

Repeat those two operations, thousands of times, on a collection that
keeps changing. A data structure built for exactly this is called a
**priority queue** — and a *heap* is the engine inside it.

Here's the dream, in fake code:

```python
# what we WANT to write (doesn't exist yet):
waiting = [3, 7, 1, 8]      # urgency scores in the ER
best = max(waiting)          # who goes first? -> 8
waiting.remove(best)         # they leave the waiting room
print(best, waiting)         # 8 [3, 7, 1]
```

Simple, right? `max` + `remove` works. The problem is **speed** — the
next chapter shows why this exact approach falls apart at scale.

## Why it exists

Tons of real systems are "repeatedly grab the extreme while new stuff
keeps arriving":

- OS scheduler — run the most important process next
- Web server — send work to the *least* busy worker
- "Top 10 scores" — keep only the best k of a stream

Every one of them needs `add` + `take_best` to be fast *at the same
time*. That's the unusual part — most structures make one fast and the
other slow.

## Where it's used

Priority queues everywhere: `queue.PriorityQueue`, task schedulers,
event loops, Dijkstra's shortest path (lesson 14 is built on this).

## Common mistake

Thinking "priority queue" is a fancy queue. A queue answers "who's
**oldest**?". A priority queue answers "who's **most extreme**?" —
completely different question, completely different answer.

## Your turn

ER waiting room: urgency scores `[2, 9, 5, 1]`. Who gets treated next?

<details><summary>Answer</summary>
The patient with urgency 9 — triage picks the *most extreme*, not the
first arrival. (The 2 could have been waiting for hours; 9 still wins.)
</details>

---

**Next →** [02 — Why the simple ideas are too slow](02-why-simple-ideas-are-too-slow.md)
