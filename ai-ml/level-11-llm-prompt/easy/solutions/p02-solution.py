"""Level 11 Llm Prompt — Easy P02 Solution"""

def solve():
    few_shot = '''
Classify the sentiment:

Text: "I love this product!" → Positive
Text: "Terrible experience." → Negative
Text: "It's okay, nothing special." → Neutral
Text: "Best purchase ever!" → Positive
Text: "Would not recommend." → Negative
Text: "Meh." → Neutral

Text: "This is amazing!" → ?
'''
    print(few_shot)
    print("Expected: Positive")
    return few_shot

if __name__ == "__main__":
    solve()