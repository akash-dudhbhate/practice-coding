"""
SOLUTION: Swap Pairs (Medium)
==============================
Swap every pair of adjacent elements. Last stays if odd.
"""
def swap_pairs(items: list) -> list:
    result = items[:]
    for i in range(0, len(result) - 1, 2):
        result[i], result[i + 1] = result[i + 1], result[i]
    return result

if __name__ == "__main__":
    assert swap_pairs([1, 2, 3, 4, 5]) == [2, 1, 4, 3, 5]
    assert swap_pairs([1, 2]) == [2, 1]
    assert swap_pairs([1]) == [1]
    assert swap_pairs([]) == []
    print("All tests passed!")
