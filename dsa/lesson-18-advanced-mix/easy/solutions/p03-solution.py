"""
SOLUTION: Count Set Bits (Easy)
===============================
Brian Kernighan's trick: n &= (n-1) erases the lowest set bit each
iteration — one loop step per 1-bit. Mask to 32 bits so negatives are
treated as unsigned (Python ints have infinite sign bits).
"""
def hamming_weight(n):
    n &= 0xFFFFFFFF                  # unsigned 32-bit view (handles negatives)
    count = 0
    while n:
        n &= n - 1                   # erase lowest set bit
        count += 1
    return count

if __name__ == "__main__":
    assert hamming_weight(11) == 3
    assert hamming_weight(128) == 1
    assert hamming_weight(0) == 0
    assert hamming_weight(255) == 8
    assert hamming_weight(2147483647) == 31
    assert hamming_weight(-1) == 32          # all 32 bits set
    print("All tests passed!")
