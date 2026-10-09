# 04 — Why Lookup Is Almost Free (O(1) average, O(n) worst)

> 5-minute read. The honest version of "dicts are fast."

## The idea, plain words

Claim: `"apple" in d` costs **O(1) — on average**.

- **Average case:** hash → jump to slot → bucket has ~1 pair → found.
  One hop, every time, whether the dict holds 10 pairs or a million.
- **Worst case:** *every* key collides into ONE slot → that bucket is a
  list of all n pairs → lookup scans it → **O(n)**, same as a list.

```
healthy table:   _   _   _   A   _   _   B   _   C   _    each bucket ~1
sick table:      _   _   _  [A,B,C,D,E,F,...]  _   _      one giant bucket
```

Real-life version: **a coat check.** One ticket → one hook → instant.
If the attendant hung every coat on hook #7, finding yours means digging
through the whole pile — that's the worst case.

## Why "average" is basically "always"

Two things keep buckets tiny in practice:

1. A **good hash function** spreads keys evenly (Python's does — our
   `ord(key[0])` toy was deliberately lumpy).
2. The table **grows**: when buckets start filling, Python quietly
   rebuilds a bigger table and re-slots everything. Chains stay ~1 long.

So in real life you quote **O(1) average** for dict/set lookups — and
interviewers accept it. The O(n) worst case is a trivia answer, not an
everyday event.

## The trade you just made

Hashing isn't free — it's a **space-for-time swap**. The dict keeps a
whole extra table (plus spare room for growth) just so lookups skip the
scan.

```python
seen = set(nums)    # pays O(n) extra memory...
x in seen           # ...to make this O(1) instead of O(n)
```

That swap — *memory for speed* — is the single most common optimization
in all of DSA. You'll use it in almost every problem in this lesson.

## Where it's used

Anywhere "is X in my collection?" appears inside a loop: dedup checks,
caches, visited-tracking, pair-finding. The lesson's pattern is always
the same: convert the thing you search into a dict/set.

## Common mistakes

- Saying "dict lookup is O(1)" without the word *average* in an
  interview — precision signals you understand collisions.
- Believing the syntax is the magic: `x in d` is O(1) but
  `x in some_list` is still a full O(n) scan. Same `in`, wildly
  different cost.

## Your turn

A dict holds 1,000,000 pairs, but a terrible hash sent every key to
slot 3. What does `key in d` cost — and what would it cost with a
normal hash?

<details><summary>Answer</summary>
Terrible hash → one bucket of 1,000,000 → **O(n)** scan (up to a
million checks). Normal hash → spread across the table → ~1-pair
buckets → **O(1)**. Same dict, different luck — that's why we say
"average."
</details>

---

**← Prev** [03 — When keys collide](03-when-keys-collide.md) ·
**Next →** [05 — Sets: dicts without values](05-sets-dicts-without-values.md)
