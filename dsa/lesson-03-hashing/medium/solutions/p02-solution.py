"""
SOLUTION: Group Anagrams (Medium)
=================================
Signature key: "".join(sorted(word)) — "eat", "tea", "ate" all map to
"aet". Group words by signature in one pass.
"""
def group_anagrams(words: list) -> list:
    groups = {}
    for w in words:
        key = "".join(sorted(w))
        groups.setdefault(key, []).append(w)
    return list(groups.values())

if __name__ == "__main__":
    res = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(map(sorted, res)) == sorted(
        [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    )
    assert sorted(map(sorted, group_anagrams([""]))) == sorted([[""]])
    assert sorted(map(sorted, group_anagrams(["a"]))) == sorted([["a"]])
    assert group_anagrams([]) == []
    print("All tests passed!")
