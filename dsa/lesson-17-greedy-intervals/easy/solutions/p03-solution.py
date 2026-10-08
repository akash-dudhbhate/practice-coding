"""
SOLUTION: Assign Cookies (Easy)
===============================
Sort both lists. Give the least-greedy remaining child the smallest
cookie that satisfies them — optimal because a larger cookie would be
"wasted" on a child who doesn't need it. Two pointers, O(n log n).
"""
def find_content_children(g, s):
    g = sorted(g)
    s = sorted(s)
    child = cookie = 0
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:       # this cookie satisfies this child
            child += 1                  # one more contented
        cookie += 1                     # cookie used (or too small → discard)
    return child

if __name__ == "__main__":
    assert find_content_children([1,2,3], [1,1]) == 1
    assert find_content_children([1,2], [1,2,3]) == 2
    assert find_content_children([10,9,8,7], [5,6,7,8]) == 2
    assert find_content_children([], [1,2]) == 0
    assert find_content_children([1,2,3], []) == 0
    assert find_content_children([1,2,3], [3]) == 1
    print("All tests passed!")
