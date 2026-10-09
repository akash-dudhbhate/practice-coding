# 01 — What is an Algorithm?

> 5-minute read. One idea only.

## The idea, plain words

An **algorithm** is a recipe: a fixed set of steps that always produces an answer.

You already use algorithms in real life:

- **Finding a word in a dictionary** — open to the middle, see if your word is
  before or after, rip the book in half, repeat. That's an algorithm.
- **Washing dishes** — pick a plate, scrub, rinse, stack, repeat until none left.
  That's an algorithm too.

In code, an algorithm is just the recipe written as a function.

```python
def find_biggest(nums):      # recipe: "walk through, remember the biggest seen"
    biggest = nums[0]        # step 1: assume the first is biggest
    for x in nums:           # step 2: look at every number
        if x > biggest:      # step 3: found a bigger one? replace
            biggest = x
    return biggest           # step 4: hand back the winner
```

Feed it `[4, 9, 2, 7]` and it walks the list once and returns `9`. Same steps,
every time, always correct. That's an algorithm.

## Why this matters (for what's coming)

Here's the thing — **two different recipes can produce the same answer, but one
does way more work than the other.**

Finding a word in a dictionary:

- **Recipe A (slow):** start at page 1, read every word, one by one.
- **Recipe B (smart):** open the middle, split, repeat.

Both find the word. But recipe A touches every page (~500 pages), recipe B
touches ~9 pages. Same answer — wildly different amount of work.

Everything in this lesson is about learning to **measure that difference** —
before you run the code, just by looking at the recipe.

## Your turn (30 seconds)

`find_biggest([4, 9, 2, 7])` — how many times does the `if x > biggest`
comparison run?

<details><summary>Answer</summary>
4 times — once per element (including the first, which just loses to itself).
The recipe touches every element exactly once.
</details>

---

**Next →** [02 — What is "n"?](02-what-is-n.md)
