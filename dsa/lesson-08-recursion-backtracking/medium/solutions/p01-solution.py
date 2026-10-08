"""
SOLUTION: Subsets (Medium)
==============================
Include/skip decision tree: at index i, branch into "take nums[i]" and
"skip it". Every leaf records one subset. path.append/pop keeps ONE
path list hot; path.copy() snapshots each answer — append the copy.
"""
def subsets(nums: list) -> list:
    out = []
    def dfs(i, path):
        if i == len(nums):
            out.append(path.copy())   # snapshot — path is still live
            return
        path.append(nums[i])          # choose: include nums[i]
        dfs(i + 1, path)              # explore
        path.pop()                    # unchoose
        dfs(i + 1, path)              # explore sibling: skip nums[i]
    dfs(0, [])
    return out

if __name__ == "__main__":
    assert sorted(map(sorted, subsets([1, 2]))) == [[], [1], [1, 2], [2]]
    assert len(subsets([1, 2, 3])) == 8
    assert subsets([]) == [[]]
    assert sorted(map(sorted, subsets([1, 2, 3]))) == [
        [], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    print("All tests passed!")
