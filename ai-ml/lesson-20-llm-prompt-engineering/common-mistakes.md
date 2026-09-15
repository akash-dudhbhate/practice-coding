# Lesson 20 — Common Mistakes

## Mistake 01: Vague prompts
```python
# WRONG
"Write about Python"
# CORRECT
"Write a 200-word beginner tutorial on Python list comprehensions with 3 examples"
```

## Mistake 02: No output format
```python
# WRONG
"List the pros and cons"
# CORRECT
"List pros and cons as JSON: {"pros": [...], "cons": [...]}"
```

## Mistake 03: Not using examples
```python
# WRONG — zero-shot for complex format
"Extract entities"
# CORRECT — few-shot
"Extract: 'John works at Google' → {"name": "John", "company": "Google"}
'Jane works at Apple' → ?"
```

## Mistake 04: Wrong temperature
```python
# For factual answers: temperature=0
# For creative writing: temperature=0.7-1.0
```

## Mistake 05: Not iterating
```python
# Prompt engineering is iterative
# Try, evaluate, refine
# Keep a library of effective prompts
```
