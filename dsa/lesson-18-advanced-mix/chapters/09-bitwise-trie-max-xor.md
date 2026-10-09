# 09 — The Bitwise Trie: Max XOR

> 5-minute read. Two lesson-18 tools, fused.

## The idea, plain words

*"Find the maximum `a ^ b` over all pairs in `nums`."*

Brute force: try every pair — O(n²). The trick: a number's bits ARE a
"word" over the alphabet `{0, 1}`. So build a **trie of bits** — insert
each number as a 32-step path, most significant bit first.

Then, for each `x`, walk the trie **preferring the opposite bit** at
every level. Opposite bit = differing column = a 1 in the XOR — you
literally construct the biggest possible answer bit by bit.

```
nums = [3, 10, 5, 25, 2, 8]  →  answer 28 = 5 ^ 25

  5 = 00101     at every top bit, the trie offered the opposite
 25 = 11001     of what 5 had — XOR is all 1s where it matters
xor = 11100 = 28
```

## Why "greedy" is actually correct

Bit `i` contributes `2^i` to the XOR. Even if EVERY lower bit flipped
to 1, they'd sum to `2^i - 1` — strictly less than that one bit. So
grabbing a differing bit can never be beaten by lower bits. Same shape
as every greedy proof from lesson 17: **the local choice dominates.**

## In code — trie of bits (~20 lines)

```python
def find_max_xor(nums):
    trie = {}
    for x in nums:
        node = trie
        for i in range(31, -1, -1):      # 32 bits, MSB first
            bit = (x >> i) & 1
            node = node.setdefault(bit, {})

    best = 0
    for x in nums:
        node = trie
        xor = 0
        for i in range(31, -1, -1):
            bit = (x >> i) & 1
            want = 1 - bit               # prefer the opposite bit
            if want in node:
                xor |= 1 << i            # this column becomes a 1
                node = node[want]
            else:
                node = node[bit]
        best = max(best, xor)
    return best

print(find_max_xor([3, 10, 5, 25, 2, 8]))   # 28  (= 5 ^ 25)
```

Each query walks ≤32 trie levels → O(32·n), i.e. O(n) with a fixed
constant. From O(n²) to O(n) by seeing numbers as words.

## Why it exists

It's the flagship "combine two tools" problem — and the reason tries
aren't just for strings. Recognizing "XOR pair optimization → bitwise
trie" is exactly what `hard/p02` tests.

## Where it's used

Max-XOR-pair problems, nearest-number queries under XOR metrics,
network address matching — and as the proof that "build a trie over
bits" is a general pattern, not a one-off.

## Common mistake

Walking the trie **least-significant bit first** — greedy only works
MSB→LSB, because high bits dominate. Also, inserting bits in the
*opposite* order you query them — both loops must use `range(31, -1, -1)`.

## Your turn

Why does preferring `want = 1 - bit` when it exists never lose to any
lower-bit combination?

<details><summary>Answer</summary>
One bit at position `i` is worth `2^i`. ALL bits below `i` together are
worth at most `2^i - 1` (`0111…1`). So a 1 higher up outweighs every
possible 1 below — take the differing bit whenever the trie offers it.
</details>

---

**← Prev** [08 — Two loners + Python's bit quirks](08-two-singles-and-python-quirks.md) ·
**Next →** [10 — Monotonic stack: next greater](10-monotonic-stack-next-greater.md)
