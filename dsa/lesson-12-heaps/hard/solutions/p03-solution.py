"""
SOLUTION: Reorganize String (Hard)
==================================
Max-heap on (-freq, char). Each step places the most frequent char
DIFFERENT from the previous one — the just-used char waits one round
in `prev` before rejoining. If the heap is empty but prev remains,
separation is impossible -> "".
"""
import heapq
from collections import Counter


def reorganize_string(s):
    count = Counter(s)
    heap = [(-c, ch) for ch, c in count.items()]
    heapq.heapify(heap)
    out = []
    prev = None                       # (neg_count, char) held back one step
    while heap:
        neg_c, ch = heapq.heappop(heap)
        out.append(ch)
        if prev is not None:
            heapq.heappush(heap, prev)  # used char rejoins one step later
        prev = (neg_c + 1, ch) if neg_c + 1 < 0 else None
    if prev is not None:              # leftover couldn't be separated
        return ""
    return "".join(out)


if __name__ == "__main__":
    def ok(orig, res):
        if res == "":
            c = Counter(orig)
            # "" is only acceptable if truly impossible
            return c.most_common(1)[0][1] > (len(orig) + 1) // 2
        return (sorted(res) == sorted(orig)
                and all(res[i] != res[i + 1] for i in range(len(res) - 1)))

    assert ok("aab", reorganize_string("aab"))
    assert reorganize_string("aaab") == ""
    assert ok("aaabbc", reorganize_string("aaabbc"))
    assert reorganize_string("") == ""
    assert ok("vvvlo", reorganize_string("vvvlo"))
    assert ok("aabbcc", reorganize_string("aabbcc"))
    print("All tests passed!")
