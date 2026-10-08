"""
SOLUTION: Letter Case Permutation (Medium)
==============================
Branch per OPTION: letters fork into lower/upper; digits have one
option — recurse straight through. 2^(#letters) results.
"""
def letter_case_permutation(s: str) -> list:
    out = []
    def dfs(i, path):
        if i == len(s):
            out.append("".join(path))
            return
        c = s[i]
        if c.isalpha():
            path.append(c.lower()); dfs(i + 1, path); path.pop()
            path.append(c.upper()); dfs(i + 1, path); path.pop()
        else:
            path.append(c); dfs(i + 1, path); path.pop()
    dfs(0, [])
    return out

if __name__ == "__main__":
    assert set(letter_case_permutation("a1b2")) == {"a1b2", "a1B2", "A1b2", "A1B2"}
    assert set(letter_case_permutation("3z4")) == {"3z4", "3Z4"}
    assert letter_case_permutation("123") == ["123"]
    assert len(letter_case_permutation("abc")) == 8
    print("All tests passed!")
