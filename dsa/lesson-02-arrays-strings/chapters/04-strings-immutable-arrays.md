# 04 — Strings: arrays you can't write to

> 5-minute read. Everything from chapter 01, plus one rule.

## The idea, plain words

A **string is an array of characters**. Same contiguous boxes, same
index math, same O(1) jump — plus one new rule: **immutable**, meaning
"can't be changed after creation." You can *read* any character. You
can never *edit* one in place.

```python
s = "hello"
```

```
char:    [ h | e | l | l | o ]
index:     0   1   2   3   4
```

```python
print(s[0])      # -> 'h'  — O(1) jump, same as a list
print(s[4])      # -> 'o'
print(s[-1])     # -> 'o'  — -1 means "last box"
print(len(s))    # -> 5
# s[0] = 'H'     # TypeError! strings don't allow item assignment
```

Want `'H'` instead of `'h'`? You build a **new** string:

```python
s2 = "H" + s[1:]
print(s2)        # -> 'Hello'   (new string; s is still 'hello')
```

## Characters are secretly numbers

Under the hood each box stores a number — the character's code.
`ord` shows it, `chr` goes backward:

```python
print(ord('a'))   # -> 97
print(ord('A'))   # -> 65   (capital != lowercase!)
print(chr(98))    # -> 'b'
```

That's why `'a' < 'b'` works — it's comparing 97 < 98. Keep this in
your pocket; counting chapters use it.

## Your everyday toolbox (with honest costs)

```python
s = "hello world"
print(len(s))         # -> 11        O(1) — length is stored
print(s[0])           # -> 'h'       O(1) — the jump
print(s[0:5])         # -> 'hello'   O(k) — slice COPIES k chars
print(s[::-1])        # -> 'dlrow olleh'  O(n) — reversed copy
print(s.split())      # -> ['hello', 'world']  O(n) — scan once
print('e' in s)       # -> True      O(n) — it's a SEARCH, not a jump
```

| Op | Cost | Why |
|----|------|-----|
| `s[i]` | O(1) | address math |
| `len(s)` | O(1) | stored, not counted |
| `s[i:j]` | O(k) | copies the k chars |
| `s[::-1]` | O(n) | copies all n chars |
| `split`, `join` | O(n) | one pass each |
| `x in s`, `s.count(x)` | O(n) | scans the whole string |

Notice the pattern: **reads by index are free; anything that touches
every character costs O(n)** — and since strings are immutable, almost
everything "helpful" produces a fresh copy.

## Why it exists

Immutability sounds annoying but it's protective: strings get passed
around everywhere (filenames, keys, messages), and if one function
could silently edit a string, bugs would appear miles away from their
cause. Python chose safety — you opt into changes by building new
strings explicitly.

## Where it's used

Every text problem in this lesson — and basically every program with
user input, files, URLs, or names.

## Common mistake

Trying `s[0] = 'H'` to "fix" a character. It raises `TypeError:
'str' object does not support item assignment`. The fix is always the
same: build a new string (`'H' + s[1:]`, slicing, `join`, `replace`).

## Your turn

```python
s = "abcde"
```

What prints: `s[1:4]`, `s[-1]`, `ord(s[0])`?

<details><summary>Answer</summary>
`'bcd'` (slice = indices 1,2,3 — the end index is excluded), `'e'`,
`97`. The slice end being exclusive is the off-by-one trap of chapter
01 wearing a disguise.
</details>

---

**← Prev** [03 — Why is adding at the front expensive?](03-append-vs-insert.md) ·
**Next →** [05 — Running totals: pay once, remember forever](05-running-totals.md)
