"""
SOLUTION: Word Ladder — (Hard)
==============================
Implicit graph: words differ by one letter = neighbors. Bucket every
word by its L wildcard patterns ("hot" -> *ot, h*t, ho*) so finding all
neighbors is O(L) dict lookups instead of O(N·L) pairwise diffs. Then
ordinary BFS; levels = ladder length. O(N·L²) to build buckets.
"""
from collections import defaultdict, deque

def ladder_length(begin, end, word_list):
    if end not in word_list:
        return 0
    patterns = defaultdict(list)
    for w in word_list + [begin]:
        for i in range(len(w)):
            patterns[w[:i] + "*" + w[i+1:]].append(w)
    seen = {begin}
    q = deque([(begin, 1)])
    while q:
        word, depth = q.popleft()
        if word == end:
            return depth
        for i in range(len(word)):
            for nxt in patterns[word[:i] + "*" + word[i+1:]]:
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, depth + 1))
    return 0

if __name__ == "__main__":
    assert ladder_length("hit", "cog",
                         ["hot","dot","dog","lot","log","cog"]) == 5
    assert ladder_length("hit", "cog",
                         ["hot","dot","dog","lot","log"]) == 0
    assert ladder_length("hit", "lot", ["hit","hot","lot"]) == 3
    assert ladder_length("hot", "dog", ["hot","dog"]) == 0
    assert ladder_length("talk", "tail", ["talk","tall","tail"]) == 3
    print("All tests passed!")
