"""
SOLUTION: Top-K Frequent Words (Easy)
=====================================
Heap tuples compare lexicographically: (-freq, word) sorts high
frequency first and alphabetical second, all in one key.
nsmallest over that key does the whole top-K.
"""
import heapq
from collections import Counter


def top_k_frequent_words(words, k):
    count = Counter(words)
    # key: freq DESC (negated), word ASC — smallest tuple = best word
    return heapq.nsmallest(k, count.keys(), key=lambda w: (-count[w], w))


if __name__ == "__main__":
    assert top_k_frequent_words(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"]
    assert top_k_frequent_words(["i", "love", "leetcode", "i", "love", "coding"], 3) == ["i", "love", "coding"]
    assert top_k_frequent_words(["the", "day", "is", "sunny", "the", "the", "the",
                                 "sunny", "is", "is"], 4) == ["the", "is", "sunny", "day"]
    assert top_k_frequent_words(["a", "b", "a"], 1) == ["a"]
    print("All tests passed!")
