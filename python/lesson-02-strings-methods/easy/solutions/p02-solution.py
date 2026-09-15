"""
SOLUTION: Reverse String (Easy)
================================
Reverse a string without using slicing.
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
    print("All tests passed!")
