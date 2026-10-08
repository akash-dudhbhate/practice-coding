"""
SOLUTION: Combination Sum (Hard)
==============================
Recurse on (i, remaining): try candidates[j] only for j >= i, and pass
the SAME j forward (reuse allowed). Never revisiting lower j is what
kills permutation duplicates like [2,3] vs [3,2]. Prune on remaining<0.
"""
def combination_sum(candidates: list, target: int) -> list:
    out = []
    def dfs(i, remaining, path):
        if remaining == 0:
            out.append(path.copy())
            return
        for j in range(i, len(candidates)):   # never look back to j < i
            if candidates[j] > remaining:
                continue                      # overshoot -> skip
            path.append(candidates[j])        # choose
            dfs(j, remaining - candidates[j], path)  # same j = reuse ok
            path.pop()                        # unchoose
    dfs(0, target, [])
    return out

if __name__ == "__main__":
    assert sorted(map(sorted, combination_sum([2, 3, 6, 7], 7))) == [[2, 2, 3], [7]]
    assert combination_sum([2], 1) == []
    assert sorted(map(sorted, combination_sum([2, 3, 5], 8))) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert combination_sum([5], 5) == [[5]]
    print("All tests passed!")
