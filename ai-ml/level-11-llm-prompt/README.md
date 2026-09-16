# Level 11 — LLM & Prompt Engineering

## What You'll Learn
- Three prompt styles: vague → detailed → structured
- Few-shot prompting (examples in the prompt)
- Temperature control
- Chain-of-thought reasoning
- Persona + format + context prompt structure
- Parsing structured (JSON) LLM output
- Prompt iteration, evaluation, system prompts

## Prerequisites
- No API keys needed — these exercises teach prompt design
  as text patterns you can test with any LLM.

## Problems

### Easy
1. `easy/p01-prompt-styles.py` — `make_prompts()` → 3 prompt variants
2. `easy/p02-few-shot.py` — `few_shot_prompt()` → example-based prompting
3. `easy/p03-temperature.py` — `explain_temperature()` → temp scale

### Medium
4. `medium/p01-chain-of-thought.py` — `chain_of_thought()` → step-by-step
5. `medium/p02-persona-format.py` — `structured_prompt()` → persona+format+context
6. `medium/p03-parse-output.py` — `parse_llm_output()` → extract JSON

### Hard
7. `hard/p01-prompt-iteration.py` — `iterate_prompts()` → v1→v3 scoring
8. `hard/p02-evaluate-prompt.py` — `evaluate_response()` → criteria checking
9. `hard/p03-system-prompts.py` — `get_personas()` → 4 system prompts

### Project
`project/` — Build a prompt library for a specific task.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
