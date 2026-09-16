# Level 11 — Concepts Reference

## Easy

### Prompt Styles
- Vague → detailed → structured. More specific = more predictable.
- Structured: JSON with named keys → parseable output.

### Few-Shot
- Show examples in the prompt; model continues the pattern.
- No training — just prompt engineering.

### Temperature
- 0 = deterministic; 1 = creative; >1.2 = may lose coherence.

## Medium

### Chain-of-Thought
- "Solve this step by step" → dramatically better reasoning
- The model generates intermediate steps before answering

### Persona + Format + Context
- Persona: who the model is
- Format: how to structure output
- Context: what domain/knowledge to use

### Structured Output
- Ask for JSON → `json.loads()` → programmatic use
- Find `{` to `}` in the response to extract it

## Hard

### Prompt Iteration
- v1 vague → v2 add format → v3 add constraints
- Score by specificity features

### Evaluation
- Check length, format compliance, keyword presence
- Automate before shipping a prompt

### System Prompts
- Set persona + constraints once, affects all responses
- Different personas = different answer styles for same question
