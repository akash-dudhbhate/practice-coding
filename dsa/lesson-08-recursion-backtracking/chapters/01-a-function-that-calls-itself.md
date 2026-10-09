# 01 — A Function That Calls Itself

> 5-minute read. One idea only — this is the weirdest sentence in beginner
> programming, so we go slowly.

## The idea, plain words

**Recursion** = a function that calls *itself* inside its own body.

That sounds impossible — like a recipe that says "step 3: follow this
recipe." But think of **a line of people passing a message.** You're at the
front and want to know how many people are in line. You ask the person
behind you: "how many are behind *you*?" They ask the next person, who asks
the next... until the last person answers "zero — nobody's behind me." Then
each person adds 1 and passes the answer back up the line.

Nobody knew the whole answer. Each person just did one tiny step: *ask the
next person, add 1 to their answer.* That's recursion.

## Watch it run

```python
def countdown(n):
    if n == 0:                # nobody behind me — stop
        print("blast off!")
        return
    print(n)
    countdown(n - 1)          # ask the next "smaller" version

countdown(3)
```

Run it and you'll see:

```
3
2
1
blast off!
```

`countdown(3)` prints `3`, then *pauses itself* and runs `countdown(2)`.
That one prints `2` and pauses for `countdown(1)`, which pauses for
`countdown(0)` — which finally prints "blast off!" and finishes. Each
paused call then wakes up and finishes too. Four calls total, each one
waiting on the next.

## Why it exists

Some problems are **self-similar** — a big version made of smaller versions
of itself:

- A folder contains files... and smaller folders.
- A list is "one element plus a smaller list."
- A family tree is "a person plus their parents' trees."

A loop handles "do this n times." But when the *structure itself* repeats
at smaller sizes, the cleanest description is "handle one piece, then let
the same function handle the rest." The function IS the loop.

## Where it's used

Trees (lesson 11!), file-system walks, parsing, divide-and-conquer sorting
(merge sort, lesson 10), and this lesson's second half: **backtracking**.
Roughly half of interview problems have a recursive skeleton hiding inside.

## Common mistake

Don't panic-trace. When you see `countdown(n - 1)`, beginners try to
mentally run the WHOLE chain inside their head at once and get dizzy.
You don't need to. Just ask: "does it stop eventually, and does each call
get smaller?" Chapter 03 makes that a two-rule checklist.

## Your turn

What does `countdown(5)` print — all five lines, in order?

<details><summary>Answer</summary>
5, 4, 3, 2, 1, then "blast off!" — six lines total. Each call prints one
number then hands off to a call one smaller, until `countdown(0)` prints
the last line.
</details>

---

**Next →** [02 — The call stack: where paused calls wait](02-the-call-stack.md)
