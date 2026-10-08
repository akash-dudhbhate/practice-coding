"""
LESSON 17 — Greedy & Intervals
MEDIUM P03 — Jump Game: Is the End Reachable?
============================================

CONCEPT:
  Reach-tracking greedy — no sorting needed. Carry one variable `reach`:
  the farthest index any path so far can land on. Standing at index i is
  only possible if i <= reach; then greedily extend
  reach = max(reach, i + nums[i]). You never care WHICH jumps — only the
  maximum reach they afford.

PROBLEM:
  Write a function `can_jump(nums: list[int]) -> bool`. You start at
  index 0; nums[i] is the MAXIMUM jump length allowed from index i
  (you may jump any distance up to it). Return True if you can reach the
  last index. A single-element array is trivially True.

TRY THIS INPUT:
  ```python
  print(can_jump([2,3,1,1,4]))
  print(can_jump([3,2,1,0,4]))
  print(can_jump([0]))
  print(can_jump([2,0,0]))
  print(can_jump([1,1,0,1]))
  ```

EXPECTED OUTPUT:
  ```
  True
  False
  True
  True
  False
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
