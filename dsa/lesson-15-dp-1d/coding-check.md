# Lesson 15 — Coding Check

Use this to verify your solutions before asking for review.

## Easy

### p01 — Fibonacci memoized
- [ ] `fib(0)` returns `0`, `fib(1)` returns `1`
- [ ] `fib(10)` returns `55`
- [ ] `fib(50)` returns `12586269025` and returns *instantly* — naive recursion would take hours
- [ ] You can explain your state: `fib(n)` = nth Fibonacci number; base cases `n <= 1`

### p02 — Climbing stairs
- [ ] `climb_stairs(1)` returns `1`, `climb_stairs(2)` returns `2`
- [ ] `climb_stairs(5)` returns `8`
- [ ] `climb_stairs(45)` returns `1836311903` (efficiency proof)
- [ ] Recognized it's Fibonacci shifted by one: `ways(i) = ways(i-1) + ways(i-2)`

### p03 — Tribonacci
- [ ] `tribonacci(0)` returns `0`, `tribonacci(1)` and `tribonacci(2)` return `1`
- [ ] `tribonacci(4)` returns `4` (1+1+2)
- [ ] `tribonacci(25)` returns `1389537`
- [ ] Handles `n < 3` without the loop running / index errors

## Medium

### p01 — House robber
- [ ] `rob([1,2,3,1])` returns `4` (rob houses 0 and 2)
- [ ] `rob([2,7,9,3,1])` returns `12` (rob houses 0, 2, 4)
- [ ] `rob([2,1,1,2])` returns `4` — the end houses beat the middles
- [ ] `rob([])` returns `0`, `rob([5])` returns `5`
- [ ] Recurrence is `dp[i] = max(dp[i-1], nums[i] + dp[i-2])` — rob or skip

### p02 — Min cost climbing stairs
- [ ] `min_cost([10,15,20])` returns `15` (start at index 1, jump over the top)
- [ ] `min_cost([1,100,1,1,1,100,1,1,100,1])` returns `6`
- [ ] `min_cost([0,0,1])` returns `0` (free stairs work)
- [ ] Answer is `min(dp[n-1], dp[n-2])` — the top is PAST the last stair, not on it

### p03 — Coin change (min coins)
- [ ] `coin_change([1,2,5], 11)` returns `3` (5+5+1)
- [ ] `coin_change([2], 3)` returns `-1` (impossible → -1, not crash)
- [ ] `coin_change([1], 0)` returns `0` (zero amount needs zero coins)
- [ ] `coin_change([186,419,83,408], 6249)` returns `20` (greedy would fail; DP doesn't)
- [ ] Unreachable cells initialized to `inf`/`amount+1`, never `0`

## Hard

### p01 — Word break
- [ ] `word_break("leetcode", ["leet","code"])` returns `True`
- [ ] `word_break("applepenapple", ["apple","pen"])` returns `True`
- [ ] `word_break("catsandog", ["cats","dog","sand","and","cat"])` returns `False`
- [ ] `word_break("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa"])` returns `False` — and doesn't hang (memoized)
- [ ] State is a position/index, not the substring itself

### p02 — Longest increasing subsequence
- [ ] `length_of_lis([10,9,2,5,3,7,101,18])` returns `4`
- [ ] `length_of_lis([0,1,0,3,2,3])` returns `4`
- [ ] `length_of_lis([7,7,7,7])` returns `1` (strictly increasing — equals don't count)
- [ ] `length_of_lis([])` returns `0`
- [ ] Answer is `max(dp)` — the LIS can end anywhere, not necessarily at the last element

### p03 — Partition equal subset sum
- [ ] `can_partition([1,5,11,5])` returns `True` (`[1,5,5]` = `[11]`)
- [ ] `can_partition([1,2,3,5])` returns `False` (total is odd → instant False)
- [ ] `can_partition([1,2,5])` returns `False` (even total but no subset hits 4)
- [ ] `can_partition([1,1])` returns `True`
- [ ] Recognized the reduction: subset-sum to `total // 2` — boolean "can reach" DP

## How to verify

```bash
python3 check.py all            # all nine of your files
python3 check.py medium/p03     # just one
python3 check.py solutions      # sanity-check the reference solutions
```
