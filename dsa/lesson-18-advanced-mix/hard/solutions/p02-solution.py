"""
SOLUTION: Max XOR of Two Numbers — Bitwise Trie (Hard)
======================================================
Insert each number's bit-path (MSB first) into a binary trie. For each
number, query greedily: take the opposite bit whenever a branch exists —
the highest bit you can flip outweighs all lower bits. O(32·n).
"""
def find_maximum_xor(nums):
    if len(nums) < 2:
        return 0
    L = max(nums).bit_length()               # only need bits up to the max
    if L == 0:
        return 0

    trie = {}
    for num in nums:
        node = trie
        for i in range(L - 1, -1, -1):
            node = node.setdefault((num >> i) & 1, {})

    best = 0
    for num in nums:
        node = trie
        cur = 0
        for i in range(L - 1, -1, -1):
            bit = (num >> i) & 1
            want = 1 - bit                   # prefer the opposite branch
            if want in node:
                cur |= 1 << i
                node = node[want]
            else:
                node = node[bit]
        best = max(best, cur)
    return best

if __name__ == "__main__":
    assert find_maximum_xor([3,10,5,25,2,8]) == 28      # 5 ^ 25
    assert find_maximum_xor([0]) == 0
    assert find_maximum_xor([5,5]) == 0
    assert find_maximum_xor([2,4]) == 6
    assert find_maximum_xor([8,10,2]) == 10             # 8 ^ 2
    assert find_maximum_xor([14,70,53,83,49,91,36,80,92,51,66,70]) == 127
    print("All tests passed!")
