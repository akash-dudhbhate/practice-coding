# 01 — What Is a Graph? (the map that isn't a list)

> 5-minute read. One idea only.

## The idea, plain words

A **graph** is just **things** plus **connections between them**. That's the
whole definition.

- The things are called **nodes** (or **vertices** — same thing).
- The connections are called **edges**.

Real-life version: **a friendship map.** Draw a dot for each person, draw a
line between dots if they're friends:

```
    A — B          A, B, C, D, E = people (nodes)
    |   |          the lines = "is friends with" (edges)
    C — D — E
```

Now answer questions just by looking: Can A reach E through friends? Yes —
`A → C → D → E`. Who is the most connected person? D (three lines touch it).
You just did graph analysis with your eyes.

## Why not just use a list or a tree?

You've seen arrays (a line of things) and trees (parent → children, like a
family tree or a folder structure). Those shapes have **rules**: a list is a
straight chain, a tree has one root and no loops.

Friendships break both rules. A is friends with B *and* C. B and C both know
D. There's a loop: `A — B — D — C — A`. No "top", no "order", no parent/child.
**Real relationships are networks, not chains** — so we need a shape with no
rules except "things connect to things." That shape is the graph.

```
LIST      TREE          GRAPH
a→b→c→d     a           A—B
           / \          |  |      ← loops allowed,
          b   c         C—D       ← no root, no order
```

## A graph in code (preview — details come in ch.03)

```python
# the drawing above, as data: each node -> list of friends
friends = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}
print(friends["D"])        # ['B', 'C', 'E']  — D has 3 friends
print("E" in friends["D"]) # True — D and E are connected
```

A dict where each node maps to its neighbors is already enough to answer
"who are D's friends?" instantly. Everything else in this lesson is built on
this one shape.

## Where it's used

Everywhere "things connect to things": social networks, Google Maps (cities +
roads), the internet itself (pages + links), package managers (libraries +
dependencies), git history (commits + parents).

## Your turn (30 seconds)

On the friendship map above — what is the **shortest** chain of friendships
from A to E? Count the hops.

<details><summary>Answer</summary>
3 hops: A — C — D — E (or A — B — D — E, same length). There's no shorter
route because nothing connects to E except D, and D is 2 hops from A.
</details>

---

**Next →** [02 — Graph words, made friendly](02-graph-words-made-friendly.md)
