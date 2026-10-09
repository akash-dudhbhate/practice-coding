# 03 — When Keys Collide (two keys, one slot)

> 4-minute read. The catch from last chapter, solved.

## The idea, plain words

Our toy hash used `ord(key[0]) % 10`. Trouble: `"sara"` and `"sam"` both
start with 's' → both hash to slot 5.

Two different keys landing in the same slot is a **collision**.

```
"sara" → slot 5      "sam" → slot 5        uh oh — one slot, two keys
```

Real-life version: **two people assigned the same parking spot.** It
happens. The question isn't "how to prevent it" — it's "what now?"

## The fix: each slot is a small list

The standard fix is **chaining**: every slot holds a tiny list (a
**bucket**) of all the pairs that landed there.

```
slot 5:  [("sara", 5)]                      ← only sara so far

d["sam"] = 8   →  collision!
slot 5:  [("sara", 5), ("sam", 8)]          ← both live in slot 5 now

"sam" in d  →  hash → slot 5  →  walk the tiny list  →  found (2nd entry)
```

Lookup is still fast: jump to the slot (1 step), then check the 1–2 pairs
in that bucket. Most buckets hold ~1 item, so it's still basically
instant.

```python
# You can't see buckets in Python — it handles them invisibly.
# But the mechanism is real:
d = {"sara": 5, "sam": 8}   # maybe same slot internally — who cares
print(d["sam"])             # correct, always
```

```
8
```

## Why it exists

With 10 slots and thousands of possible keys, collisions are
*guaranteed* — more keys than slots means some must share, like more
pigeons than pigeonholes. Chaining accepts that and makes each collision
cheap instead of fatal.

## Where it's used

Inside every hash table ever built. Python does it silently — you'll
never write a bucket yourself. It matters because it explains the honest
speed claim in the next chapter: O(1) *on average*, not O(1) *always*.

## Common mistake

Thinking a collision is a bug. It's normal traffic. A dict with
collisions still works perfectly — that slot just does 2 checks instead
of 1.

## Your turn

With `slot = ord(key[0]) % 10`: `"pen"` → 2, `"pine"` → 2, `"oak"` → 1.
After storing all three, what's in slot 2's bucket, and roughly how many
steps does `d["pine"]` take?

<details><summary>Answer</summary>
Slot 2 holds `[("pen", ...), ("pine", ...)]` — a bucket of 2.
`d["pine"]` → compute slot 2 (1 step) → scan the bucket (up to 2
checks). ~3 steps instead of 1 — still tiny.
</details>

---

**← Prev** [02 — How a key becomes a slot](02-how-a-key-becomes-a-slot.md) ·
**Next →** [04 — Why lookup is almost free](04-why-lookup-is-almost-free.md)
