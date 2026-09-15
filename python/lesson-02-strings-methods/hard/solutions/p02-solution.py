"""
SOLUTION: Run-Length Encoding (Hard)
=====================================
Compress a string using run-length encoding. "aaabbc" -> "a3b2c1".
"""
def run_length_encode(s: str) -> str:
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{s[i-1]}{count}")
            count = 1
    result.append(f"{s[-1]}{count}")
    return "".join(result)

if __name__ == "__main__":
    assert run_length_encode("aaabbc") == "a3b2c1"
    assert run_length_encode("abc") == "a1b1c1"
    assert run_length_encode("aaaa") == "a4"
    assert run_length_encode("") == ""
    print("All tests passed!")
