# 01 — The Guessing Game

> 4-minute read. One idea only.

## The idea, plain words

**Binary search** is the smart way to play "guess the number":

- I pick a secret number between 1 and 100.
- You guess. I only say "higher" or "lower."
- Bad strategy: guess 1, 2, 3, 4… (up to 100 guesses).
- Smart strategy: always guess the **middle**. 50 → "higher" → 75 → "lower"…
  Each guess throws away HALF the remaining numbers.

100 numbers → at most 7 guesses. A million → ~20. That's the whole trick.

## Watch it happen — the game, in code

```python
secret = 73                     # I'm thinking of this
lo, hi = 1, 100                 # numbers still possible
guesses = 0

while True:
    guess = (lo + hi) // 2      # always guess the middle
    guesses += 1
    if guess == secret:
        break
    elif guess < secret:        # "higher" → kill the bottom half
        lo = guess + 1
    else:                        # "lower" → kill the top half
        hi = guess - 1

print(guess, "found in", guesses, "guesses")
```

```
73 found in 6 guesses
```

Hand trace — watch `lo` and `hi` squeeze together:

```
range [1..100]  guess 50 → higher  → [51..100]
range [51..100] guess 75 → lower   → [51..74]
range [51..74]  guess 62 → higher  → [63..74]
range [63..74]  guess 68 → higher  → [69..74]
range [69..74]  guess 71 → higher  → [72..74]
range [72..74]  guess 73 → FOUND
```

Six guesses instead of up to 73. Nothing fancy — just "guess the middle,
trust the hint."

## Why it exists

The same recipe works on **sorted lists** — a sorted list IS the "higher/lower"
game. The element at the middle tells you which half your target can possibly
live in, so you never look at the other half. That's the entire lesson:
turn the guessing game into a function over array indices.

## Where it's used

Dictionary lookups (open to the middle!), `git bisect` (which commit broke
it?), database indexes, and a huge family of interview problems.

## Common mistake

Guessing near the edge instead of the middle. A guess of 51 in `[1..100]`
only kills 50 numbers if you're wrong — the middle guess is guaranteed to
kill half, no matter the answer.

## Your turn

Secret number is somewhere in 1–1000. How many guesses does the middle
strategy need, worst case?

<details><summary>Answer</summary>
10. Each guess halves: 1000 → 500 → 250 → 125 → 62 → 31 → 15 → 7 → 3 → 1.
That's 10 halvings. (Lesson 01 chapter 09 called this `log n`.)
</details>

---

**Next →** [02 — Why sorted is required](02-why-sorted.md)
