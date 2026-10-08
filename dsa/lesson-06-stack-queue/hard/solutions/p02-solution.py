"""
SOLUTION: Largest Rectangle in a Histogram (Hard)
==========================================
Monotonic INCREASING stack of indices. A shorter bar closes taller
ones: popped bar's rectangle width = (i-1) - (new_top+1) + 1. The
trailing 0 sentinel flushes the stack. O(n).
"""
def largest_rectangle_area(heights):
    stack = []                       # indices, heights increasing
    best = 0
    for i, h in enumerate(heights + [0]):   # sentinel flushes stack
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            best = max(best, height * (i - left))
        stack.append(i)
    return best

if __name__ == "__main__":
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
    assert largest_rectangle_area([2, 4]) == 4
    assert largest_rectangle_area([1, 1, 1, 1]) == 4
    assert largest_rectangle_area([6, 2, 5, 4, 5, 1, 6]) == 12
    assert largest_rectangle_area([5]) == 5
    assert largest_rectangle_area([]) == 0
    assert largest_rectangle_area([2, 0, 2]) == 2
    print("All tests passed!")
