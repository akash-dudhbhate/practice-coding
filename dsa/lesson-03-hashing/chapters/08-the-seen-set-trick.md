# 08 — The Seen Set: Turning O(n²) into O(n)

> 5-minute read. The payoff chapter — this is why hash maps rule interviews.

## The idea, plain words

So many problems boil down to: *"for each item, check whether I've seen
something like it before."*

The naive way keeps a **list** of the past and asks `x in seen`. But
`in` on a list is a **hidden scan** — it checks every element. Inside an
n-round loop that's O(n) work n times: **O(n²)**.

The fix is one word: make `seen` a **set**. Same code, but `in` becomes
O(1): **O(n) total.**

```python
names = ["amit", "sara", "amit", "john", "sara", "amit"]
seen = set()                        # was: seen = []
for n in names:
    if n in seen:                   # list: O(n) scan · set: O(1) jump
        print(f"{n}: duplicate")
    else:
        seen.add(n)
        print(f"{n}: new")
```

```
amit: new
sara: new
amit: duplicate
john: new
sara: duplicate
amit: duplicate
```

## Feel the difference

```
list-seen: 6 items -> up to 6+5+4+3+2+1 = 21 checks
set-seen:  6 items -> 6 hash jumps                  ~ 6 checks

at n = 1,000,000:  list ~ 500 billion checks   (hangs)
                   set  ~ 1 million jumps      (instant)
```

## Second worked example — collect the duplicates

```python
nums = [4, 3, 2, 4, 3, 5]
seen = set()
dupes = set()
for x in nums:
    if x in seen:
        dupes.add(x)
    seen.add(x)
print(sorted(dupes))
```

```
[3, 4]
```

Walk: 4 new → 3 new → 2 new → **4 seen → dupe** → **3 seen → dupe** →
5 new.

## Why it exists

This is **the** interview transformation. Any brute force shaped like
"for each x, search the rest" becomes "for each x, ask the seen set" —
the inner search vanishes. Chapters 10 and 11 are fancier versions of
this exact move.

## Where it's used

Duplicate detection, marking visited nodes in graph traversal,
"contains a repeat" checks — anywhere a nested loop asks
"does Y exist?".

## Common mistakes

- Keeping `seen` as a list anyway "because it works" — it works on 6
  items and dies on a million.
- Adding to `seen` *before* checking — always **ask first, then
  remember**. (A sneakier version of this bug returns in chapter 10.)

## Your turn

`nums = [1, 2, 3, 2]` — run the second example in your head. What's in
`dupes` and what's in `seen`?

<details><summary>Answer</summary>
1 new → 2 new → 3 new → 2 already seen → `dupes = {2}`,
`seen = {1, 2, 3}`.
</details>

---

**← Prev** [07 — Grouping lookalikes](07-grouping-lookalikes.md) ·
**Next →** [09 — Keys can't change](09-keys-cant-change.md)
