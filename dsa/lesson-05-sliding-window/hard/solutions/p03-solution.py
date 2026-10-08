"""
SOLUTION: Fruit Into Baskets (Hard)
==========================================
Exactly "longest subarray with at most 2 distinct values" — the P02
skeleton with k = 2. O(n) time, O(1) space (dict never holds > 3 keys).
"""
def total_fruit(fruits):
    left, best, count = 0, 0, {}
    for right, f in enumerate(fruits):
        count[f] = count.get(f, 0) + 1          # pick fruit into a basket
        while len(count) > 2:                   # third type → drop from left
            g = fruits[left]
            count[g] -= 1
            if count[g] == 0:
                del count[g]                    # empty basket frees a slot
            left += 1
        best = max(best, right - left + 1)
    return best

if __name__ == "__main__":
    assert total_fruit([1, 2, 1]) == 3
    assert total_fruit([0, 1, 2, 2]) == 3
    assert total_fruit([1, 2, 3, 2, 2]) == 4
    assert total_fruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
    assert total_fruit([1, 1, 1, 1]) == 4
    assert total_fruit([]) == 0
    print("All tests passed!")
