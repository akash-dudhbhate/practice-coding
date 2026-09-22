"""
LEVEL 11 PROJECT — Prompt Library + Self-Test
=============================================

Build a reusable prompt toolkit — the thing every LLM app needs.
Then prove your prompts work with an automated test harness.

BUILD `PromptLibrary` class with these methods:
  - summarize(text, n_bullets=3)
  - classify(text, categories)          → few-shot style prompt
  - extract_json(text, keys)            → structured-output prompt
  - explain(concept, audience="beginner")→ persona + level prompt
  - chain_of_thought(problem)           → step-by-step prompt

Then `self_test(lib)` that checks every generated prompt for:
  - mentions the required format (bullets/JSON/steps)
  - includes the input text
  - length under 500 chars (prompts shouldn't be bloated)

EXPECTED OUTPUT:
  ```
  summarize:   PASS (234 chars, mentions '3 bullet points')
  classify:    PASS (198 chars, mentions 'categories')
  extract_json:PASS (187 chars, mentions 'json' + all keys)
  explain:     PASS (165 chars, mentions 'beginner')
  cot:         PASS (142 chars, mentions 'step by step')
  All prompts passed!
  ```

WHY TEST PROMPTS: prompts are code. They break silently when
  edited. A test suite catches regressions — this is real
  "prompt engineering" in industry.
"""

# === WRITE YOUR CODE BELOW ===

class PromptLibrary:
    # TODO: 5 prompt-builder methods
    pass


def self_test(lib):
    # TODO: validate each prompt, print PASS/FAIL per method
    pass


if __name__ == "__main__":
    lib = PromptLibrary()
    self_test(lib)
