# 02 — The Call Stack: Where Paused Calls Wait

> 5-minute read. This is the mechanism that makes chapter 01 possible.

## The idea, plain words

Every time Python calls a function — ANY function, recursive or not — it
creates a **frame**: a little sticky note recording "which function is
running, what its variables are, and where to resume when it returns."

When a function calls another function, the caller *pauses mid-line* and
its frame goes on a pile. The new call gets a fresh frame on top. When that
call returns, its frame is thrown away and the one underneath wakes up
exactly where it left off.

That pile is the **call stack** — the same data structure from **lesson 06
(stack & queue)**: push on top, pop off top, last-in-first-out. You learned
stacks as a container; now you see Python runs one internally on EVERY call.

## Watch it run — ordinary calls first

```python
def greet():
    print("hello")
    inner()                # greet pauses HERE, mid-function
    print("bye")           # ...and resumes HERE after inner returns

def inner():
    print("inside inner")

greet()
```

Output:

```
hello
inside inner
bye
```

While `inner()` ran, the stack looked like this — `greet` frozen underneath:

```
call stack (grows downward as we draw it)

main()
 └─ greet()          ← paused at the inner() line, "hello" already printed
      └─ inner()     ← currently running
```

`inner` finishes → its frame is popped → `greet` resumes → prints "bye" →
`greet`'s frame pops → `main` resumes.

## Now the recursive version

Same machinery — but the paused frames are *copies of the same function*,
each with its own private `n`:

```
countdown(3) running:

main()
 └─ countdown(3)     ← n=3 frozen, waiting
      └─ countdown(2)   ← n=2 frozen, waiting
           └─ countdown(1)  ← n=1 frozen, waiting
                └─ countdown(0)   ← prints "blast off!", returns
```

The key fact: **each frame has its OWN variables.** The `n` inside
`countdown(3)` is a different `n` than inside `countdown(2)`. That's why a
function can call itself without its variables colliding — they're stacked
in separate frames, like plates in a cafeteria dispenser.

## Why it exists

The stack is what lets a caller "go do something else and come back."
Without it, `greet` couldn't remember it still owed you a "bye". And frames
cost real memory — every waiting call is a sticky note taking up space.
Hold that thought; chapter 05 shows what happens when the pile gets too tall.

## Common mistake

Thinking recursive calls share variables. They don't — `n` in each frame is
separate. If you WANT shared state across all calls, it has to live outside
the function (a `global`, or a list passed in — backtracking uses exactly
that trick, chapter 08).

## Your turn

```python
def a():
    print("A-start")
    b()
    print("A-end")

def b():
    print("B")

a()
```

List the three lines of output in order.

<details><summary>Answer</summary>
A-start, B, A-end. `a` prints, pauses on `b()`, `b` prints and returns,
then `a` resumes at its next line.
</details>

---

**← Prev** [01 — A function that calls itself](01-a-function-that-calls-itself.md) ·
**Next →** [03 — The two rules](03-the-two-rules.md)
