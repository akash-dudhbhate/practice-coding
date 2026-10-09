# 02 — How a Key Becomes a Slot (the hash function)

> 5-minute read. This is the magic trick — watch exactly how it works.

## The idea, plain words

Here's the puzzle: how does `d["apple"]` find its value *instantly*,
without checking every pair you stored?

Inside every dict is a plain array of numbered **slots** (also called
**buckets**). To decide where `"sara"` lives, the dict runs two steps:

1. **Hash it** — a **hash function** turns the key into a number.
   Any key → some number. Same key → always the same number.
2. **Mod it** — `number % table_size` squeezes that number into a valid
   slot index.

```
        key          hash              % 10           slot
      "sara"  →  ord("s") = 115   →   115 % 10   →     5

slots:  [ 0 ] [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ]
         _     _     _     _     _   ("sara",5)  _     _     _     _
```

Store `d["sara"] = 5` → the pair goes into slot 5.
Later, `"sara" in d` → hash again → same slot 5 → grab it. **No
scanning.**

## A hash function you can compute by hand

Python's real `hash()` is complicated, but the *idea* is simple. Here's a
toy one — take the first letter's code (`ord`) and mod by 10:

```python
def slot(key):
    return ord(key[0]) % 10    # first letter's number, squeezed into 10 slots

print(slot("sara"))   # ord('s') = 115 -> 5
print(slot("pen"))    # ord('p') = 112 -> 2
print(slot("sara"))   # same key -> always 5
```

```
5
2
5
```

That's the whole trick: **the key itself tells you where it lives.**
You don't search for the key — you *compute* its address.

## Why it exists

An array can jump to slot #5 in one step — O(1), always. Hashing converts
"find the thing named 'sara'" into "jump to slot 5". That's how
key → value lookup becomes instant instead of a full scan.

## Where it's used

Inside every Python `dict` and `set`, every cache, every database index.
You never write the hash yourself — `hash()` does it — but knowing it's
there explains everything else in this lesson.

## Common mistake

Thinking a dict "searches" for your key. It doesn't loop — it
*recomputes* the slot and jumps. That's why dict size barely matters:
slot 5 is slot 5 whether the table holds 10 pairs or 10 million.

## Your turn

Using `slot(key) = ord(key[0]) % 10`: where do `"tea"` and `"ant"` go?
(`ord('t') = 116`, `ord('a') = 97`)

<details><summary>Answer</summary>
`"tea"` → 116 % 10 = **6**. `"ant"` → 97 % 10 = **7**.
Different first letters *usually* mean different slots — and "usually"
is doing work there. Next chapter.
</details>

---

**← Prev** [01 — What is a dict?](01-what-is-a-dict.md) ·
**Next →** [03 — When keys collide](03-when-keys-collide.md)
