"""SOLUTION: Safe Int (Easy)"""
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None

if __name__ == "__main__":
    assert safe_int("42") == 42
    assert safe_int("abc") is None
    assert safe_int("") is None
    print("All tests passed!")
