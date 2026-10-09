# 04 — Why We Count Steps, Not Seconds

> 4-minute read.

## The idea, plain words

You might think: "why not just run it and measure seconds?"

Because **seconds lie**:

- The same code runs 3× slower on an old laptop than a new one.
- It runs slower while a video call is hogging the CPU.
- Python vs C++ — same recipe, different speed.

But the **number of steps is identical on every machine**. If a recipe does
n² steps, it does n² steps on a phone, a laptop, or a supercomputer. The
supercomputer just does them faster — it doesn't make the recipe better.

So instead of "how many seconds," we ask **"how many steps, as a function
of n?"** That answer never changes with hardware.

## A picture that makes it obvious

Same recipe (work = n²), two machines:

```
                 old laptop        fast server
n = 1,000        0.1 sec           0.01 sec       ← both feel instant
n = 100,000      ~17 min           ~1.7 min       ← both are BAD
```

The fast server hides the problem at small n and still chokes at big n.
**A bad recipe is a bad recipe** — hardware only delays the pain.

## The real interview answer

When someone asks "how fast is your code?", the expected answer is never
"2 seconds." It's: "**it does about n steps** — it grows linearly" or
"it does n² — it explodes on big input."

That phrasing is called Big-O notation, and the next chapter finally
explains what `O(n)`, `O(n²)`, etc. actually mean — now that you can
count steps yourself.

## Your turn

Your code takes 2 seconds on 1,000 items and your friend says "just use a
faster computer." What's wrong with that plan?

<details><summary>Answer</summary>
If the work is n², at n = 1,000,000 even a 100× faster machine needs
hours. You can't outrun a bad growth shape — you fix the recipe.
</details>

---

**← Prev** [03 — Counting steps by hand](03-counting-steps-by-hand.md) ·
**Next →** [05 — What Big-O actually means](05-what-big-o-means.md)
