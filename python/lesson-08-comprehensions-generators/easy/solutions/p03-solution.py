"""SOLUTION: Lengths Dict Comprehension (Easy)"""
def lengths(words):
    return {w: len(w) for w in words}

if __name__ == "__main__":
    assert lengths(["hi", "hello"]) == {"hi": 2, "hello": 5}
    print("All tests passed!")
