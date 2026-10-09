# 11 — Greedy or Not? The recognition checklist

> 6-minute read. Sanity-check a greedy BEFORE you code it.

## The idea, plain words

Greedy code is short, so wrong greedy is seductive. The real skill:
spend **2 minutes trying to break your rule** on tiny inputs before
writing anything. Five checks:

1. **State the rule in one sentence.** "Always take the earliest-ending
   interval." Can't say it plainly? You have a vibe, not a greedy.
2. **Hunt a counterexample on n = 2–4.** A dozen hand cases. You're
   looking for ONE input where the local pick diverges from the global
   optimum.
3. **Try the exchange argument** (chapter 9). Can any optimal first choice
   be swapped for yours without making things worse?
4. **Check structural assumptions.** Interval greedy needs sorted input;
   Jump-Game reach needs non-negative jumps. If input can violate it,
   handle or reject.
5. **If it breaks, don't force it** — pivot to DP (lesson 15/16),
   binary-search-the-answer (lesson 9), or exhaustive-with-pruning.

## Watch it kill a wrong rule in 30 seconds

```
Rule candidate: keep LONGEST intervals first (for min-removals).
Try [[1,10],[2,3],[4,5]]:  keep [1,10] → must drop both small = 2 removals.
                           optimal: keep [2,3],[4,5] → drop only [1,10] = 1.
Rule broken in ONE 3-interval input → reject, use sort-by-end.
```

That's the whole technique — 30 seconds of small inputs killed a wrong
algorithm before it was written.

## The recipe — recognize the family in 10 seconds

1. **Intervals involved?** → sort (by START for merge/insert/
   meeting-check, by END for keep-max-non-overlapping), sweep once, track
   `current`/`last_end`.
2. **"Minimum/maximum count of choices" on a line?** → reach-tracking
   greedy (jump, gas, refuel).
3. **"Satisfy as many as possible"** (kids/cookies, jobs/machines)? →
   sort both lists, pair smallest-need with smallest-sufficient-resource.
4. **Can't prove it?** → coin-change trap: say so, use DP instead.

**Complexity to say out loud:** `O(n log n)` for the sort, `O(n)` sweep,
`O(1)` extra space besides the output.

## The pitfall gallery — six ways greedy goes wrong

1. **Wrong sort key** — sort-by-start on activity selection (ch. 5).
2. **`<=` vs `<` at boundaries** — touching merges in busy-time, is
   compatible in scheduling (ch. 4).
3. **Greedy where DP belongs** — weird coin denominations (ch. 2).
4. **Mutating while iterating** — build a `merged` output list; don't pop
   the list you're sweeping.
5. **Forgetting feasibility** — gas station `total < 0` → `-1`;
   `can_jump([0])` → `True`.
6. **Optimizing the wrong objective** — max reach ≠ min jumps; Jump-II
   needs the `boundary` variable (ch. 10).

**Edge cases to always test:** empty list, single element, all-disjoint,
all-overlapping (`[[1,10],[2,3],[4,5]]` merges to one), touching
endpoints, negative coordinates, guaranteed-unreachable (`[3,2,1,0,4]`).

## Why it exists

In an interview, *stating the greedy rule + one sentence of justification
+ admitting you'd switch to DP if it breaks* beats silently coding a wrong
greedy. The checklist is what makes that statement honest.

## Your turn

"Sort cookies and kids, give each kid the smallest cookie that satisfies
them" — greedy or not?

<details><summary>Answer</summary>
**Greedy, and legal.** Pairing smallest-need with smallest-sufficient
never strands you: any cookie that satisfies a greedier kid also satisfies
this one, so the swap can't hurt (exchange argument ✓). It's recipe
family #3 — sort both lists, one pass.
</details>

---

**← Prev** [10 — Reach-Tracking Greedy](10-reach-tracking.md) ·
Done with concepts? → Open `task-explanation.md` and solve `easy/p01` next.
