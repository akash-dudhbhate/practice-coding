"""
SOLUTION: Replace Spaces with Underscores (Medium)
===================================================
Strip leading/trailing whitespace, then replace internal spaces with underscores.
"""
def replace_spaces(text: str) -> str:
    return text.strip().replace(" ", "_")

if __name__ == "__main__":
    assert replace_spaces("  hello world  ") == "hello_world"
    assert replace_spaces("no spaces") == "no_spaces"
    assert replace_spaces("  single  ") == "single"
    print("All tests passed!")
