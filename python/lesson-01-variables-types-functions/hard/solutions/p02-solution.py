"""
SOLUTION: Reverse String (Hard)
=================================
Reverse a string WITHOUT using slicing or reversed().
"""
def reverse_string(s: str) -> str:
    result = ""
    for char in s:
        result = char + result
    return result

if __name__ == "__main__":
    assert reverse_string("hello") == "olleh"
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    print("All tests passed!")
