"""
SOLUTION: Count Words (Medium)
===============================
Count the number of words in a sentence.
"""
def count_words(sentence: str) -> int:
    return len(sentence.strip().split())

if __name__ == "__main__":
    assert count_words("Hello world") == 2
    assert count_words("  one  two  three  ") == 3
    assert count_words("") == 0
    print("All tests passed!")
