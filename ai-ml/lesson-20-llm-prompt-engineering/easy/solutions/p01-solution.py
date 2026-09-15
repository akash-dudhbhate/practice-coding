# Lesson 20 — Easy P01: Three prompts for summarization (vague, specific, format)
# Uses mock responses to demonstrate the difference in output quality.

PROMPT_LABEL = "Prompt:"
RESPONSE_LABEL = "Response:"

paragraph = """
Machine learning is a subset of artificial intelligence that enables systems
to learn and improve from experience without being explicitly programmed.
It focuses on developing computer programs that can access data and use it
to learn for themselves. The process begins with observations or data, such
as examples, direct experience, or instruction. The primary aim is to allow
computers to learn automatically without human intervention or assistance
and adjust actions accordingly.
"""

# Prompt 1: Vague
prompt_vague = "Summarize this: " + paragraph
mock_response_vague = "ML is a type of AI that learns from data."
print("=== Vague Prompt ===")
print(PROMPT_LABEL, prompt_vague)
print(RESPONSE_LABEL, mock_response_vague)
print("Issue: Too brief, misses key details about the learning process.\n")

# Prompt 2: Specific
prompt_specific = (
    "Summarize the following paragraph in 2-3 sentences. "
    "Focus on what machine learning is, how it works, and its primary goal. "
    "Keep it clear and concise.\n\n" + paragraph
)
mock_response_specific = (
    "Machine learning is a subset of AI that allows systems to learn from data "
    "without explicit programming. It works by using observations, examples, or "
    "instructions to help computers learn automatically. The primary goal is to "
    "enable computers to learn and adjust actions without human intervention."
)
print("=== Specific Prompt ===")
print(PROMPT_LABEL, prompt_specific)
print(RESPONSE_LABEL, mock_response_specific)
print("Better: Covers what, how, and goal in 3 sentences.\n")

# Prompt 3: With format instructions
prompt_format = (
    "Summarize the following paragraph using this format:\n"
    "- Definition: [1 sentence]\n"
    "- How it works: [1 sentence]\n"
    "- Goal: [1 sentence]\n\n"
    + paragraph
)
mock_response_format = (
    "- Definition: Machine learning is a subset of AI that enables systems to learn from data.\n"
    "- How it works: It uses observations, examples, or instructions to learn automatically.\n"
    "- Goal: To allow computers to learn without human intervention and adjust actions accordingly."
)
print("=== Format-Specified Prompt ===")
print(PROMPT_LABEL, prompt_format)
print(RESPONSE_LABEL, mock_response_format)
print("Best: Structured output with clear labels for each part.\n")

print("=== Conclusion ===")
print("Vague prompts produce vague, incomplete responses.")
print("Specific prompts produce more targeted, complete responses.")
print("Format instructions produce structured, easy-to-parse responses.")
