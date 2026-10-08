"""
SOLUTION: Range Sum Queries (Medium)
==============================
Build prefix sums once (O(n)), then each query is P[j+1] - P[i] -> O(1).
P[i] = sum of first i elements, so P has len(nums)+1 entries.
"""
def answer_queries(nums: list, queries: list) -> list:
    P = [0]
    for x in nums:
        P.append(P[-1] + x)          # P[i] = nums[0] + ... + nums[i-1]
    return [P[j + 1] - P[i] for i, j in queries]

if __name__ == "__main__":
    assert answer_queries([1, 2, 3, 4, 5], [(0, 2)]) == [6]
    assert answer_queries([1, 2, 3, 4, 5], [(0, 2), (1, 4), (2, 2)]) == [6, 14, 3]
    assert answer_queries([1, 2, 3, 4, 5], [(0, 4)]) == [15]
    print("All tests passed!")
