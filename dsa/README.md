# DSA — Data Structures & Algorithms (Basic → Top)

Learn DSA the same way as the other tracks: **concept → why it exists → where it's
used → what goes wrong without it → worked example → 9 practice problems per
lesson (3 easy / 3 medium / 3 hard) with solutions and automated checks.**

Prerequisite: the `python/` track (lessons 01–10 minimum). All problems are in
Python — the language used in most DSA interviews.

## How to work a lesson

1. Read `concepts.md` top to bottom — every concept explains what it is, why it
   was invented, where it's used in real projects, and what breaks without it.
2. Open `task-explanation.md` — it describes all 9 problems with exact inputs
   and expected outputs.
3. Solve in order: `easy/` → `medium/` → `hard/`. Write your own code in the
   `pNN-*.py` files — the `solutions/` folders are for checking AFTER you try.
4. Verify: `python3 check.py` runs every problem; `python3 check.py easy/p01`
   runs just one.
5. `coding-check.md` is your manual checklist; `EXTRA-PRACTICE.md` has debug
   drills, common mistakes, and refactoring challenges.

## The Path

| # | Lesson | What you can do after it |
|---|--------|--------------------------|
| 01 | `lesson-01-complexity-bigO` | Analyze time/space of any loop; speak Big-O fluently |
| 02 | `lesson-02-arrays-strings` | In-place array tricks, prefix sums, string scanning |
| 03 | `lesson-03-hashing` | Solve "find pair/count" problems in O(n) with dict/set |
| 04 | `lesson-04-two-pointers` | Sorted-array pairs, reverse-in-place, dedup tricks |
| 05 | `lesson-05-sliding-window` | Longest/shortest substring & subarray problems |
| 06 | `lesson-06-stack-queue` | Balanced brackets, monotonic stack, deque patterns |
| 07 | `lesson-07-linked-list` | Pointer surgery: reverse, detect cycle, merge |
| 08 | `lesson-08-recursion-backtracking` | Write clean recursive code; subsets/permutations |
| 09 | `lesson-09-binary-search` | Search in O(log n) + "search the answer" pattern |
| 10 | `lesson-10-sorting` | Implement the big sorts; know when each wins |
| 11 | `lesson-11-trees-bst` | Tree traversals, BST operations, recursion on trees |
| 12 | `lesson-12-heaps` | Top-K problems, priority scheduling with heapq |
| 13 | `lesson-13-graphs-bfs-dfs` | Build graph from edges; BFS shortest path, DFS explores |
| 14 | `lesson-14-graph-algorithms` | Topological sort, Dijkstra, union-find |
| 15 | `lesson-15-dp-1d` | Memoization, tabulation — fib to house-robber style |
| 16 | `lesson-16-dp-2d-knapsack` | Grid DP, knapsack, LCS-style two-sequence DP |
| 17 | `lesson-17-greedy-intervals` | Interval merging/scheduling, greedy choice proofs |
| 18 | `lesson-18-advanced-mix` | Tries, bit manipulation, monotonic stack — the last 10% |

## Interview reality check

- ~80% of DSA interview questions are lessons 02–15. Master those first.
- Say your complexity out loud for every solution — interviewers grade it.
- If stuck >20 min on easy / >35 on medium / >50 on hard → read the solution,
  close it, re-implement from memory the next day.
