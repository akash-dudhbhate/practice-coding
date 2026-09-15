# Lesson 20 — Approach Comparison

## Problem: Get Structured Output

### Approach 1: Natural language
```python
"List the names as a comma-separated list"
```
**Cons:** Model may add extra text.

### Approach 2: JSON format
```python
"Return JSON: {"names": ["Alice", "Bob"]}"
```

### Approach 3: Function calling
```python
# Use OpenAI function calling API
functions = [{"name": "extract_names", "parameters": {...}}]
```

**Winner:** Approach 3 — guaranteed structured output. Approach 2 if no function calling.

---

## Problem: Complex Reasoning

### Approach 1: Direct answer
```python
"What's 15% of 240?"
```

### Approach 2: Chain of thought
```python
"Think step by step. What's 15% of 240?"
```

**Winner:** Approach 2 — more accurate for complex reasoning.
