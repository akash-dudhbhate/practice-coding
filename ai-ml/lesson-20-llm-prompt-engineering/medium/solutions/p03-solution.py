# Lesson 20 — Medium P03: Temperature experiment
# Tests a creative prompt at different temperatures using mock responses.

creative_prompt = "Write a haiku about coding."

# Repeated haiku (temperature 0.0 produces identical output)
HAIKU_DETERMINISTIC = "Code flows like water,\nBugs hide in the silent dark,\nFix them one by one."

# Mock responses at different temperatures (3 runs each)
# In real usage, call the LLM API with temperature parameter
mock_results = {
    0.0: [
        HAIKU_DETERMINISTIC,
        HAIKU_DETERMINISTIC,
        HAIKU_DETERMINISTIC,
    ],
    0.5: [
        HAIKU_DETERMINISTIC,
        "Keys click in the night,\nLogic builds a steady path,\nPrograms come alive.",
        "Code flows like water,\nErrors flash then fade away,\nLogic wins the day.",
    ],
    1.0: [
        "Coffee fuels the mind,\nSemicolons dance wildly,\nBugs become features.",
        "Pixels form patterns,\nFunctions call across the void,\nStack overflow cries.",
        "Late night debugging,\nThe screen glows with secrets found,\nDawn breaks, code works now.",
    ],
    1.5: [
        "Electric thoughts bloom,\nSemicolons rebel now,\nChaos breeds beauty.",
        "Quantum bugs whisper,\nFunctions dream of infinite,\nCode becomes poetry.",
        "Binary rain falls,\nLoops spiral into stardust,\nCompiler weeps joy.",
    ],
}

print("=== Temperature Experiment ===")
print(f"Prompt: '{creative_prompt}'\n")

for temp, responses in mock_results.items():
    print(f"--- Temperature {temp} ---")
    for i, resp in enumerate(responses, 1):
        print(f"  Run {i}: {resp}")
    unique = len(set(responses))
    print(f"  Unique outputs: {unique}/3\n")

print("=== Analysis ===")
print("Temperature 0.0: Identical output every time (deterministic).")
print("  Use when: Consistency is critical (data extraction, classification, code generation).")
print()
print("Temperature 0.5: Mostly similar with minor variations.")
print("  Use when: Some creativity needed but mostly consistent (summarization, translation).")
print()
print("Temperature 1.0: Varied outputs with different imagery and structure.")
print("  Use when: Creativity is desired (brainstorming, creative writing, ideation).")
print()
print("Temperature 1.5: Highly varied, sometimes unpredictable or unusual.")
print("  Use when: Maximum creativity or exploring unconventional ideas (poetry, art).")
print("  Caution: May produce nonsensical or off-topic outputs.")
