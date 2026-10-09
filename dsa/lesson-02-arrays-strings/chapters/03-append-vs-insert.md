# 03 — Why is adding at the front expensive?

> 4-minute read. The flip side of contiguous memory.

## The idea, plain words

Contiguity made indexing free — but it's a **rental agreement**: box
`i` must sit right next to box `i-1`, always. So there's no empty space
"between" boxes to slip a new element into. To insert at the front,
every existing element has to **move one seat down** first.

Real-life version: **a queue at a ticket counter**. Join at the back —
nobody moves. Cut in at the front — every single person shuffles back
one step. The longer the line, the ruder the cut.

## Watch an insert happen

```python
nums = [3, 1, 4]
nums.insert(0, 99)
print(nums)   # -> [99, 3, 1, 4]
```

Inside memory, that one innocent line did this:

```
start:      [ 3 | 1 | 4 | _ ]
shift 4 ->  [ 3 | 1 | _ | 4 ]
shift 1 ->  [ 3 | _ | 1 | 4 ]
shift 3 ->  [ _ | 3 | 1 | 4 ]
write 99 -> [ 99| 3 | 1 | 4 ]
```

**4 moves to insert 1 item** — and with n items it's n moves →
**O(n) per insert**.

Compare the ends:

```python
nums.append(7)      # O(1) — drop into a spare slot at the END
nums.insert(0, 7)   # O(n) — shift EVERYONE right
nums.pop(0)         # O(n) — remove first, shift EVERYONE left
nums.pop()          # O(1) — take from the end, nobody moves
```

(`append` is technically "O(1) amortized" — occasionally it grabs a
bigger memory block. That's lesson-01 chapter 14; same asterisk.)

## The loop trap — this one matters

```python
data = [1, 2, 3, 4]

# SLOW: each insert(0) shifts everything → O(n) per call, O(n^2) total
result = []
for x in data:
    result.insert(0, x)
print(result)        # -> [4, 3, 2, 1]  ...at n× the cost

# FAST: O(n) total, same answer
result = list(reversed(data))
print(result)        # -> [4, 3, 2, 1]
```

n inserts × O(n) each = O(n²). For n = 100,000 that's ~10 billion
shifts vs ~100,000 copies. This is the #1 accidental-quadratic bug with
lists.

## Why it exists

The contiguous block can't grow "into" memory that's already occupied
by something else — so making room means moving furniture. It's the
price of the O(1) indexing you got in chapter 02.

## Where it's used

- **Rule of thumb:** build lists with `append`, treat the front as
  expensive.
- Need cheap adds/removes at *both* ends? `collections.deque` exists
  exactly for that (`deque.popleft()` is O(1)).
- Spotting `insert(0, ...)` or `pop(0)` inside a loop = instant O(n²)
  alarm in code review and interviews.

## Common mistake

Using `insert(0, x)` or `pop(0)` in a loop "because it's just one
line." One line can still be O(n) — multiply by n iterations and your
program crawls.

## Your turn

`result = []`, then `for x in [1,2,3]: result.insert(0, x)`. What's
the final list, and roughly how many element shifts happened?

<details><summary>Answer</summary>
`[3, 2, 1]`. Shifts: insert 1 → 0 shifts; insert 2 → 1 shift;
insert 3 → 2 shifts. Total 3 shifts for 3 inserts — the shift count
grows with the list, which is exactly the O(n)-per-insert pattern.
</details>

---

**← Prev** [02 — Why is `nums[5000]` as fast as `nums[0]`?](02-why-indexing-is-o1.md) ·
**Next →** [04 — Strings: arrays you can't write to](04-strings-immutable-arrays.md)
