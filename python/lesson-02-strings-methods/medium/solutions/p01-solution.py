"""
SOLUTION: Get Initials (Medium)
================================
Given a full name, return initials. "John Doe" -> "JD".
"""
def get_initials(name: str) -> str:
    parts = name.strip().split()
    return "".join(word[0].upper() for word in parts if word)

if __name__ == "__main__":
    assert get_initials("John Doe") == "JD"
    assert get_initials("Akash  Dev") == "AD"
    assert get_initials("single") == "S"
    assert get_initials("") == ""
    print("All tests passed!")
