# Lesson 03 — Intuition Checks

## Check 01: List Mutation
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```
What prints?
- (A) [1, 2, 3]
- (B) [1, 2, 3, 4]

<details><summary>Answer</summary>
**(B) [1, 2, 3, 4]** — `b = a` doesn't copy the list, it creates another reference to the SAME list. Modifying `b` modifies `a`. Use `b = a.copy()` or `b = a[:]` to copy.
</details>

## Check 02: Tuple Immutability
```python
t = (1, [2, 3])
t[1].append(4)
print(t)
```
What happens?

<details><summary>Answer</summary>
```
(1, [2, 3, 4])
```
Tuples are immutable — you can't change `t[1]` to a different list. But if a tuple contains a mutable object (like a list), you CAN modify that object. The tuple still points to the same list, but the list's contents changed.
</details>

## Check 03: List Comprehension
```python
nums = [1, 2, 3, 4, 5]
result = [n * 2 for n in nums if n > 2]
print(result)
```
What prints?

<details><summary>Answer</summary>
```
[6, 8, 10]
```
Filter first (n > 2: 3, 4, 5), then transform (×2: 6, 8, 10).
</details>

## Check 04: Append vs Extend
```python
a = [1, 2]
a.append([3, 4])
print(a)

b = [1, 2]
b.extend([3, 4])
print(b)
```
What prints (2 lines)?

<details><summary>Answer</summary>
```
[1, 2, [3, 4]]
[1, 2, 3, 4]
```
`append` adds the list as ONE element. `extend` unpacks and adds each element.
</details>

## Check 05: Sort vs Sorted
```python
nums = [3, 1, 4, 1, 5]
result = nums.sort()
print(result)
print(nums)
```
What prints (2 lines)?

<details><summary>Answer</summary>
```
None
[1, 1, 3, 4, 5]
```
`.sort()` sorts IN PLACE and returns `None`. The original list is modified. `sorted(nums)` returns a NEW sorted list and doesn't modify the original.
</details>
