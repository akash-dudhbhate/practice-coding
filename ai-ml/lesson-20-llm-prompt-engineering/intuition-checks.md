# Lesson 20 — Intuition Checks

## Check 01: What is prompt engineering?
<details><summary>Answer</summary>
Crafting input text to guide LLM output. Better prompts = better results without changing the model. Includes: clear instructions, examples, context, output format specification.
</details>

## Check 02: Zero-shot vs few-shot
```python
# Zero-shot: "Translate to French: Hello"
# Few-shot: "Translate: Hello → Bonjour, Goodbye → Au revoir, Thanks → ?"
```
<details><summary>Answer</summary>
Zero-shot — no examples, relies on model's pretraining. Few-shot — provide examples of input→output. Few-shot is more reliable for specific formats.
</details>

## Check 03: Chain of thought
```python
prompt = "Think step by step. If I have 3 apples and eat 1, then buy 2 more, how many do I have?"
```
<details><summary>Answer</summary>
Asking model to reason step by step improves accuracy on complex tasks. Model shows its reasoning, catches errors. Good for math, logic.
</details>

## Check 04: Temperature
```python
# temperature=0: deterministic, focused
# temperature=1: creative, varied
```
<details><summary>Answer</summary>
Controls randomness. 0 — always same output (good for factual tasks). 1 — varied output (good for creative writing). 0.7 is a good default.
</details>

## Check 05: System prompt
```python
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "How do I sort a list?"}
]
```
<details><summary>Answer</summary>
System prompt sets behavior/persona. User prompt is the actual question. Model responds in the style set by system prompt.
</details>
