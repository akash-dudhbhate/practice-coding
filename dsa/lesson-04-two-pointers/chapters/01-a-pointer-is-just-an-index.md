# 01 — A "Pointer" Is Just an Index Variable

> 3-minute read. One idea only — and it's smaller than you think.

## The idea, plain words

In this lesson, a **pointer** is a variable that stores an *index* into a
list. That's it. Nothing exotic — the `i` in `for i in range(len(nums))`
is already a pointer.

Real-life version: **your finger on a page.** Your finger doesn't contain
the word — it marks *where* the word is. Move the finger right, you're
pointing at the next word. The finger is the pointer; the word is `nums[p]`.

```python
nums = [10, 20, 30]
p = 0                    # pointer = index 0
print(nums[p])           # the VALUE at that spot
p += 1                   # finger slides right one slot
print(nums[p])
```

Output:

```
10
20
```

Two ways to picture it — same thing:

```
nums = [10, 20, 30]
        ↑
        p = 0          # p points at index 0 (the 10)

p → [10, 20, 30]       # shorthand we'll use all lesson
```

## Hand trace — small data

```python
nums = [5, 15, 25]
p = 0
while p < len(nums):     # while the finger is still inside the list
    print(p, nums[p])
    p += 1
```

```
p → [5, 15, 25]      prints "0 5"
    p → [5, 15, 25]  prints "1 15"
        p → [5, 15, 25]  prints "2 25"
p = 3 → p < 3 is False → stop
```

## Why it exists

Every pattern in this lesson is just **two of these index variables, moved
by rules.** If "pointer" ever sounds scary, swap in the word *finger* —
the whole technique is two fingers on the same row of numbers.

## Where it's used

Everywhere you already write loops. The new part (next chapter) is using
**two** fingers at once.

## Common mistake

Mixing up the pointer and the value: `p` is the index (`1`), `nums[p]` is
the value at that spot (`15`). `p += 1` moves the finger; it does **not**
add 1 to the number.

## Your turn

```python
nums = [4, 8, 15, 16]
p = 2
p += 1
print(nums[p])
```

What prints?

<details><summary>Answer</summary>
`16`. `p` starts at 2, `p += 1` makes it 3, and `nums[3]` is `16`.
The pointer moved — the list didn't change.
</details>

---

**Next →** [02 — The two-pointer idea](02-the-two-pointer-idea.md)
