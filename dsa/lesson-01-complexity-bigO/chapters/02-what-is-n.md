# 02 — What is "n"?

> 5-minute read. One idea only.

## The idea, plain words

When people say "n", they mean **the size of the input** — how many items the
recipe has to deal with.

- `nums = [4, 9, 2, 7]` → **n = 4**
- `nums = [4, 9, 2, 7, 1, 5, 8]` → **n = 7**
- a list of a million users → **n = 1,000,000**

That's it. `n` is just "how many things are we working on."

Why do we care about `n`? Because a recipe that's fast on 4 items might be
slow on a million. We want to know: **as n grows, how does the work grow?**

## See it with real numbers

```python
def print_all(nums):
    for x in nums:
        print(x)
```

- `print_all` on a list of 4 → prints 4 lines. Work = 4 steps.
- On a list of 1000 → 1000 lines. Work = 1000 steps.
- On a list of a million → a million lines.

The work is **equal to n**. Write it down: `work = n`.

Now a trickier one — "does the list contain a pair that sums to 10?":

```python
def has_pair(nums):
    for a in nums:            # n times
        for b in nums:        # n times INSIDE each outer round
            if a + b == 10:
                return True
    return False
```

With `n = 4`: the inner loop runs 4 times for EACH of the 4 outer rounds →
4 × 4 = **16** checks.

With `n = 100`: 100 × 100 = **10,000** checks.

With `n = 1,000,000`: a **trillion** checks. Your laptop does ~10 billion
simple ops a second → this takes ~100 seconds. Ouch.

The work here is **n × n = n²**. Notice the difference:

| n | work = n | work = n² |
|---|----------|-----------|
| 4 | 4 | 16 |
| 100 | 100 | 10,000 |
| 1,000,000 | 1,000,000 | 1,000,000,000,000 |

Same input size, two recipes, completely different worlds.

## Your turn

`for a in nums: for b in nums: for c in nums:` — three loops nested. How many
steps when n = 10? When n = 1000?

<details><summary>Answer</summary>
10³ = 1,000 for n=10. And 1000³ = **one billion** for n=1000.
Work = n³ — it gets out of hand even faster than n².
</details>

---

**← Prev** [01 — What is an algorithm](01-what-is-an-algorithm.md) ·
**Next →** [03 — Counting steps by hand](03-counting-steps-by-hand.md)
