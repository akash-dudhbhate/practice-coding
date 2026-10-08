"""
SOLUTION: Meeting Rooms — Can Attend All? (Easy)
================================================
Sort by start; a clash exists iff some meeting starts before the
previous one ends. Touching endpoints don't clash (s >= prev_end).
O(n log n).
"""
def can_attend_all(intervals):
    iv = sorted(intervals)
    for i in range(1, len(iv)):
        if iv[i][0] < iv[i-1][1]:      # starts before previous ends → clash
            return False
    return True

if __name__ == "__main__":
    assert can_attend_all([[0,30],[5,10],[15,20]]) == False
    assert can_attend_all([[7,10],[2,4]]) == True
    assert can_attend_all([[1,5],[5,8],[8,10]]) == True   # back-to-back is fine
    assert can_attend_all([]) == True
    assert can_attend_all([[1,2]]) == True
    assert can_attend_all([[1,10],[2,3],[4,5]]) == False
    print("All tests passed!")
