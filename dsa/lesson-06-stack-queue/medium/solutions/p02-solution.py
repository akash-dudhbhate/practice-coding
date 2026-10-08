"""
SOLUTION: Daily Temperatures (Medium)
==========================================
Monotonic stack again — but we store INDICES and record a DISTANCE:
when day i pops waiting day j, ans[j] = i - j. O(n).
"""
def daily_temperatures(temps):
    ans = [0] * len(temps)
    stack = []                          # indices of colder, waiting days
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            ans[j] = i - j              # days waited until warmer
        stack.append(i)
    return ans

if __name__ == "__main__":
    assert daily_temperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    assert daily_temperatures([30,40,50,60]) == [1,1,1,0]
    assert daily_temperatures([90,80,70]) == [0,0,0]
    assert daily_temperatures([30,60,90]) == [1,1,0]
    assert daily_temperatures([]) == []
    assert daily_temperatures([50,50,51]) == [2,1,0]
    print("All tests passed!")
