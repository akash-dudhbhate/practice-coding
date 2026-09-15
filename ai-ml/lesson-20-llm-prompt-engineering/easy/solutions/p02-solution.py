# Lesson 20 — Easy P02: Few-shot prompt for sentiment classification
# Includes 3 examples (positive, negative, neutral) and tests with 5 new sentences.

few_shot_prompt = """Classify the sentiment of each sentence as positive, negative, or neutral.

Examples:
Sentence: "I love this product, it works perfectly!"
Sentiment: positive

Sentence: "The package arrived broken and customer service was rude."
Sentiment: negative

Sentence: "The item was delivered on Tuesday as scheduled."
Sentiment: neutral

Now classify the following sentences:
"""

test_sentences = [
    "This is the best meal I've ever had!",
    "The weather is okay today, nothing special.",
    "I can't believe how terrible the service was.",
    "I'm so excited about my new job opportunity!",
    "The meeting is at 3 PM in conference room B.",
]

# Mock LLM responses (in real usage, send the full prompt to an LLM API)
mock_responses = ["positive", "neutral", "negative", "positive", "neutral"]

print("=== Few-Shot Sentiment Classification ===\n")
print("Few-shot prompt template:")
print(few_shot_prompt)
print("=" * 50)

for sentence, sentiment in zip(test_sentences, mock_responses):
    full_prompt = few_shot_prompt + f'Sentence: "{sentence}"\nSentiment:'
    print(f"\nPrompt: ...Sentence: \"{sentence}\"\nSentiment:")
    print(f"Expected output: {sentiment}")

print("\n=== Summary ===")
print("Few-shot prompting provides the model with examples of the desired")
print("input-output pattern, helping it understand the task format and")
print("produce consistent classifications.")
