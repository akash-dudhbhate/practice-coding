# 03 — Counting Steps by Hand

> 5-minute read. This is THE skill — do it slowly.

## The idea, plain words

Forget formulas. "Complexity" is just **counting how many times the work
inside the loop runs**. You can literally count it on your fingers with a
tiny input.

Let's do it together, one step at a time — no math notation yet.

## Example 1: one loop

```python
nums = [10, 20, 30, 40]        # n = 4

for x in nums:
    print(x)
```

Watch it run:

```
round 1: prints 10
round 2: prints 20
round 3: prints 30
round 4: prints 40
```

Count the `print` calls: **4**. The input had 4 items, the work was 4 steps.
So: **work = n**.

## Example 2: nested loops — this is where n² comes from

```python
nums = [10, 20, 30]            # n = 3

for a in nums:
    for b in nums:
        print(a, b)
```

Slow it down — the INNER loop finishes completely for EVERY outer round:

```
outer round a=10:  inner runs 3 times → (10,10) (10,20) (10,30)
outer round a=20:  inner runs 3 times → (20,10) (20,20) (20,30)
outer round a=30:  inner runs 3 times → (30,10) (30,20) (30,30)
```

Count the prints: 3 + 3 + 3 = **9**. The input had 3 items, work = 9 = 3 × 3.

So with n items: outer runs n times, inner runs n times per outer →
**work = n × n = n²**. That's literally all "n squared" means — the inner
loop repeats its whole n-length run n times.

## Example 3: early exit — you CAN stop early

```python
nums = [10, 20, 30, 40]

for x in nums:
    if x == 20:
        print("found")
        break               # stop the loop right here
```

If the target is at position 2, the loop only does **2 rounds**, not 4.
Counting steps depends on WHERE the answer is — we'll handle "best vs worst
case" in a later chapter. For now: counting = tracing the loop.

## Your turn (actually count, don't guess)

```python
nums = [1, 2, 3, 4, 5]
for a in nums:
    for b in nums:
        print(a + b)
```

How many `print` calls? Say the number out loud, then check.

<details><summary>Answer</summary>
25. Outer runs 5 times; inner runs 5 times per outer → 5 × 5 = 25.
</details>

---

**← Prev** [02 — What is "n"?](02-what-is-n.md) ·
**Next →** [04 — Why not just count seconds](04-why-not-seconds.md)
