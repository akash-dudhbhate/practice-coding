"""
SOLUTION: Largest Rectangle in Histogram (Hard)
===============================================
Stack of indices with increasing heights. A shorter incoming bar pops
taller ones: the popped bar's right edge is i, its left edge is just
past the new stack top → width = i - left. A sentinel height-0 pass at
i = n flushes every pending rectangle. O(n).
"""
def largest_rectangle_area(heights):
    stack = []                              # indices, heights increasing
    best = 0
    n = len(heights)
    for i in range(n + 1):
        cur = heights[i] if i < n else 0    # sentinel 0 forces the flush
        while stack and heights[stack[-1]] > cur:
            h = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            best = max(best, h * (i - left))
        stack.append(i)
    return best

if __name__ == "__main__":
    assert largest_rectangle_area([2,1,5,6,2,3]) == 10
    assert largest_rectangle_area([2,4]) == 4
    assert largest_rectangle_area([1]) == 1
    assert largest_rectangle_area([4,2,0,3,2,5]) == 6
    assert largest_rectangle_area([]) == 0
    assert largest_rectangle_area([6,2,0,9,2,9]) == 9
    assert largest_rectangle_area([2,2,2,2]) == 8        # whole array, height 2
    print("All tests passed!")
