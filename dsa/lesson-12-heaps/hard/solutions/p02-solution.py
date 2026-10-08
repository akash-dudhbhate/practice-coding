"""
SOLUTION: Task Scheduler (Hard)
===============================
Max-heap on remaining counts (negated). Each slot runs the most
frequent available task; tasks with counts left go to a cooldown
list keyed by the slot they're allowed back. Empty heap + nonempty
cooldown = idle slots — exactly what makes the answer > len(tasks).
"""
import heapq
from collections import Counter


def least_interval(tasks, n):
    if not tasks:
        return 0
    count = Counter(tasks)
    heap = [-c for c in count.values()]    # max-heap on frequencies
    heapq.heapify(heap)
    cooldown = []                          # (slot_available, -count)
    t = 0
    while heap or cooldown:
        t += 1
        if heap:
            c = heapq.heappop(heap) + 1    # negated count + 1 = one less remaining
            if c != 0:
                cooldown.append((t + n, c))
        # else: idle slot — everything is still on cooldown
        if cooldown and cooldown[0][0] == t:
            _, c = cooldown.pop(0)
            heapq.heappush(heap, c)
    return t


if __name__ == "__main__":
    assert least_interval(['A', 'A', 'A', 'B', 'B', 'B'], 2) == 8
    assert least_interval(['A', 'A', 'A', 'B', 'B', 'B'], 0) == 6
    assert least_interval(['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'], 2) == 9
    assert least_interval(['A', 'A', 'A', 'A', 'A', 'A',
                           'B', 'C', 'D', 'E', 'F', 'G'], 2) == 16
    assert least_interval(['A'], 5) == 1
    assert least_interval([], 3) == 0
    assert least_interval(['A', 'B'], 10) == 2   # different tasks need no gap
    print("All tests passed!")
