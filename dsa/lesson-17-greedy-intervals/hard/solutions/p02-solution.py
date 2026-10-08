"""
SOLUTION: Gas Station (Hard)
============================
Two facts: (1) total gas < total cost → impossible (-1). (2) If tank
goes negative at i, NO station in the failed stretch works — restarting
there inherits the same deficit — so skip to i+1 and reset tank.
One pass decides feasibility AND the start. O(n) time, O(1) space.
"""
def can_complete_circuit(gas, cost):
    total = tank = start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:                 # stretch start..i can't contain the answer
            start = i + 1
            tank = 0
    return start if total >= 0 else -1

if __name__ == "__main__":
    assert can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]) == 3
    assert can_complete_circuit([2,3,4], [3,4,3]) == -1
    assert can_complete_circuit([5,1,2,3,4], [4,4,1,5,1]) == 4
    assert can_complete_circuit([3,1,1], [1,2,2]) == 0
    assert can_complete_circuit([2], [2]) == 0
    assert can_complete_circuit([1], [2]) == -1
    print("All tests passed!")
