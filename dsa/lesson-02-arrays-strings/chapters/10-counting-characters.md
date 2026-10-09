# 10 — Counting characters in one pass

> 4-minute read. Half of all string problems start here.

## The idea, plain words

**Frequency counting**: walk the string once and keep a tally of how
many times each character appears — in a `dict`, a key–value lookup
table.

Real-life version: **counting votes**. Each ballot comes in, you add a
tally mark under that candidate's name. One pass through the ballots,
and every count is done. You don't re-sort the whole pile for each
candidate.

## Build the tally

```python
def char_freq(text):
    freq = {}                            # empty dict: char -> count
    for c in text:
        freq[c] = freq.get(c, 0) + 1     # seen before? +1. New? 0+1.
    return freq

print(char_freq("aab"))      # -> {'a': 2, 'b': 1}
print(char_freq("hello"))    # -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

`freq.get(c, 0)` = "give me `freq[c]`, or `0` if `c` isn't in there
yet." First sighting of a character counts as 0, then `+1` makes it 1.

## Trace `"aab"` by hand

```
c = 'a':  freq.get('a',0) -> 0, write 1     freq = {'a': 1}
c = 'a':  freq.get('a',0) -> 1, write 2     freq = {'a': 2}
c = 'b':  freq.get('b',0) -> 0, write 1     freq = {'a': 2, 'b': 1}
```

Three characters, three dict touches → **O(n)**. (Dict lookups are O(1)
— the hash table trick from later lessons; for now, trust it.)

## The trap version

```python
# Looks clean — secretly O(n^2)
{c: text.count(c) for c in set(text)}
```

`text.count(c)` **re-scans the entire string** for every unique
character. It's the `in`-is-a-search lesson from chapter 02, one level
down: a hidden O(n) inside a loop → O(n²). The tally loop above does
the same job in one honest pass.

Batteries-included version:

```python
from collections import Counter
print(Counter("aab"))   # -> Counter({'a': 2, 'b': 1})
```

`Counter` *is* the tally loop, pre-written. Learn the `dict.get`
version first — interviews love seeing you don't need the import.

## Why it exists

Frequency is the backbone of half the string problems: anagrams ("same
counts?"), most-common-char, "first unique character," and `hard/p03`'s
count-then-label. One O(n) tally replaces a pile of rescans.

## Where it's used

`easy/p03` (build exactly this), `hard/p03` (pass 1 of two), anagram
checks, histograms, "which character appears most."

## Common mistake

```python
freq[c] += 1        # KeyError if c was never seen!
```

Bare `freq[c]` explodes on a new key. Always `freq.get(c, 0) + 1`, or
`freq[c] = freq.get(c, 0) + 1`. (Or `defaultdict(int)` — same idea.)

## Your turn

Mentally tally `"abca"` — what dict do you end with?

<details><summary>Answer</summary>
`{'a': 2, 'b': 1, 'c': 1}`. The `a` gets bumped twice (indices 0 and
3); first sighting of each char goes through the `get(c, 0)` branch.
</details>

---

**← Prev** [09 — Scan twice: count first, build second](09-two-passes.md) ·
**Next →** [11 — Building strings: `join`, not `+=`](11-join-not-plus-equals.md)
