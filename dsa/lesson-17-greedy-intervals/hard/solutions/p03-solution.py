"""
SOLUTION: Partition Labels (Hard)
=================================
Each letter spans [first_idx, last_idx] — an interval. A part can end
only when i reaches the max last-index of every letter seen inside it
(same boundary-extension idea as Jump Game II). Precompute last[c],
sweep once. O(n) time, O(alphabet) space.
"""
def partition_labels(s):
    last = {c: i for i, c in enumerate(s)}   # last occurrence of each char
    result = []
    start = end = 0
    for i, c in enumerate(s):
        end = max(end, last[c])              # stretch the part's right edge
        if i == end:                         # every letter inside is finished
            result.append(i - start + 1)
            start = i + 1
    return result

if __name__ == "__main__":
    assert partition_labels("ababcbacadefegdehijhklij") == [9,7,8]
    assert partition_labels("eccbbbbdec") == [10]
    assert partition_labels("a") == [1]
    assert partition_labels("abac") == [3,1]
    assert partition_labels("ababcbaca") == [9]
    assert partition_labels("abcd") == [1,1,1,1]
    print("All tests passed!")
