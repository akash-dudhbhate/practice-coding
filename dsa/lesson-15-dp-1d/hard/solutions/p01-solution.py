"""
SOLUTION: Word Break (Hard)
============================
Two equivalent views, both memoize on index i:
  top-down : can_break(i) = can s[i:] be segmented?
  bottom-up: dp[i]       = can s[:i] be segmented?
The memoized top-down version is shown; iterating word-lengths keeps
each check bounded by max word length instead of dict size.
"""
from functools import lru_cache


def word_break(s: str, wordDict: list[str]) -> bool:
    words = set(wordDict)
    maxlen = max((len(w) for w in words), default=0)

    @lru_cache(maxsize=None)
    def can_break(i: int) -> bool:
        if i == len(s):
            return True                     # empty suffix: done
        for L in range(1, maxlen + 1):      # try each possible next word
            if s[i:i + L] in words and can_break(i + L):
                return True
        return False

    return can_break(0)


if __name__ == "__main__":
    assert word_break("leetcode", ["leet", "code"]) is True
    assert word_break("applepenapple", ["apple", "pen"]) is True
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    assert word_break("", ["a"]) is True
    assert word_break("cars", ["car", "ca", "rs"]) is True
    assert word_break("a" * 35 + "b", ["a", "aa", "aaa", "aaaa"]) is False
    assert word_break("aaaaaaa", ["aaaa", "aaa"]) is True
    print("All tests passed!")
