"""
SOLUTION: Classify Number (Easy)
==================================
Return "positive", "negative", or "zero".
"""
def classify_number(n: int) -> str:
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    return "zero"

if __name__ == "__main__":
    assert classify_number(5) == "positive"
    assert classify_number(-3) == "negative"
    assert classify_number(0) == "zero"
    print("All tests passed!")
