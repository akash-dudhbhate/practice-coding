# Lesson 20 — LLM & Prompt Engineering

## What you'll learn
- What LLMs are (Large Language Models)
- Prompt engineering basics (crafting effective prompts)
- Few-shot prompting (examples in the prompt)
- Chain-of-thought prompting (step-by-step reasoning)
- System prompts (setting behavior and role)
- Temperature and sampling (controlling randomness)
- Structured output (JSON from LLMs)
- RAG (Retrieval-Augmented Generation)
- Prompt injection and safety
- Using the OpenAI API

## Lesson

### API call
```python
from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response.choices[0].message.content)
```

### Few-shot
```python
prompt = "Classify: 'great' → positive\n'bad' → negative\n'okay' →"
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Write 3 prompts for the same task (summarize a paragraph): a vague one, a specific one, and one with format instructions. Document the difference in output quality. (Use mock responses or the OpenAI API if you have a key.)
2. `easy/p02-solve.py` — Create a few-shot prompt for sentiment classification. Include 3 examples (positive, negative, neutral). Test with 5 new sentences. Print the prompts and expected outputs.
3. `easy/p03-solve.py` — Write a chain-of-thought prompt for a math problem. Show the step-by-step reasoning. Compare with a direct prompt (no reasoning). Document which gives the correct answer more reliably.

### Medium
4. `medium/p01-solve.py` — Build a prompt template system: create templates for 3 tasks (summarization, translation, code review). Each template has placeholders. Write a function that fills templates and generates the final prompt. Test all 3.
5. `medium/p02-solve.py` — Build a structured output extractor: write a prompt that extracts information (name, age, email, phone) from a text and returns JSON. Test with 3 different input texts. Parse the JSON and verify all fields are present.
6. `medium/p03-solve.py` — Experiment with temperature: write a creative prompt (e.g., "write a haiku about coding"). Run it at temperature 0, 0.5, 1.0, and 1.5 (3 times each). Document the variation in outputs. Explain when to use each temperature.

### Hard
7. `hard/p01-solve.py` — Build a simple RAG pipeline: create a knowledge base (list of documents), implement a simple retrieval function (keyword matching or TF-IDF), retrieve top 3 documents for a question, construct a RAG prompt, and generate an answer. Test with 5 questions. (Use mock LLM responses if no API key.)
8. `hard/p02-solve.py` — Build a prompt injection defense: create a system prompt for a customer service bot. Test 5 injection attempts (e.g., "ignore previous instructions", "reveal your prompt"). Write defenses in the system prompt. Document which injections succeed and which are blocked.
9. `hard/p03-solve.py` — Build a complete LLM application: a simple chatbot with system prompt, conversation history (last 5 messages), temperature control, token usage tracking, and error handling. Include a mock mode (no API key needed) that returns canned responses. Test with a 5-turn conversation.

### How to work
- Write your complete Python solution.
- Remove the TODO comment when done.
- Test with `python <filename>`.
- If you don't have an OpenAI API key, use mock responses or simulate the LLM output.
