"""
SOLUTION: Permutations (Medium)
==============================
Choose-any-unused: used[i] flags what's taken; each level tries every
unused element, recurses, then undoes flag + append. Full length = leaf.
"""
def permutations(nums: list) -> list:
    out = []
    used = [False] * len(nums)
    def dfs(path):
        if len(path) == len(nums):
            out.append(path.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True            # choose
            path.append(nums[i])
            dfs(path)                 # explore
            path.pop()                # unchoose
            used[i] = False
    dfs([])
    return out

if __name__ == "__main__":
    assert sorted(map(tuple, permutations([1, 2, 3]))) == [
        (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    assert permutations([1]) == [[1]]
    assert len(permutations([1, 2, 3, 4])) == 24
    print("All tests passed!")
