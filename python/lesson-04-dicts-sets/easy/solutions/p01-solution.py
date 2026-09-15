"""
SOLUTION: Word Count (Easy)
=============================
Return a dict mapping each word (lowercased) to its count.
"""
def word_count(text: str) -> dict:
    words = text.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

if __name__ == "__main__":
    assert word_count("the cat the dog") == {"the": 2, "cat": 1, "dog": 1}
    assert word_count("") == {}
    print("All tests passed!")
