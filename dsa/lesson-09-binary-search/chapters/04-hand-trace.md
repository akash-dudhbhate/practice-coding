# 04 — Hand Trace, Start to Finish

> 5-minute read. Run the template on paper once and it never feels magic again.

## The idea, plain words

Let's run the template on `nums = [1, 3, 5, 7, 9, 11]`, target `7`, and
draw the search space shrinking each step. Watch `lo`, `mid`, `hi` move —
this picture IS the algorithm.

```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        print(f"lo={lo} hi={hi} mid={mid} nums[mid]={nums[mid]}")
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

print("answer:", binary_search([1, 3, 5, 7, 9, 11], 7))
print("answer:", binary_search([1, 3, 5, 7, 9, 11], 8))
```

```
lo=0 hi=5 mid=2 nums[mid]=5
lo=3 hi=5 mid=4 nums[mid]=9
lo=3 hi=3 mid=3 nums[mid]=7
answer: 3
lo=0 hi=5 mid=2 nums[mid]=5
lo=3 hi=5 mid=4 nums[mid]=9
lo=3 hi=3 mid=3 nums[mid]=7
lo=4 hi=3
answer: -1
```

## The shrinking space — draw it

Target `7`, step by step. `^` marks lo/mid/hi, `x` = dead elements:

```
Step 1:  [ 1   3   5   7   9   11 ]
         ^lo       ^mid          ^hi
         nums[2]=5 < 7 → kill left:  [x  x  x | 7  9  11]

Step 2:  [ x   x   x   7   9   11 ]
                      ^lo ^mid  ^hi
         nums[4]=9 > 7 → kill right: [x  x  x | 7 | x  x]

Step 3:  [ x   x   x   7   x   x ]
                      ^lo=mid=hi
         nums[3]=7 → FOUND at index 3
```

Six elements, three probes. A linear scan could have taken six. Notice
step 3: `lo == hi` — the `<=` in `while lo <= hi` is what let us check
that last survivor.

Target `8` (not present): same probes, then `lo=4 > hi=3` — range empty,
return `-1`. The loop ending IS the proof it's not there.

## Why it exists

Interviewers ask you to trace, not just recite. More importantly — when
your own binary search misbehaves, printing `lo hi mid` each loop is THE
debugging move. You've just done it by hand.

## Where it's used

Dry-running code like this is the standard interview skill and the
standard debugging skill — same muscle.

## Common mistake

Tracing *only* the found case. The `8` trace above is the important one —
watch `lo` walk past `hi` and understand that "empty range" is the
algorithm's way of saying "not present."

## Your turn

Same array, target `1`. How many probes?

<details><summary>Answer</summary>
2 probes. Step 1: mid=2, nums[2]=5 > 1 → hi=1. Step 2:
mid=(0+1)//2=0, nums[0]=1 → found at index 0. The rounding-down of
`(lo + hi) // 2` sends mid to 0, which is exactly where the 1 lives.
</details>

---

**← Prev** [03 — The template, line by line](03-the-template.md) ·
**Next →** [05 — Why O(log n)](05-why-log-n.md)
