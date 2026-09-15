# Lesson 20 — Refactoring Challenges

## Refactor 01 (Easy): Hardcoded Prompts
### Before
```python
prompt = "Summarize this: " + text
```
### After
```python
from langchain.prompts import PromptTemplate
prompt = PromptTemplate.from_template("Summarize this: {text}")
```

## Refactor 02 (Medium): No Token Counting
### Before
```python
response = llm(long_text)  # may exceed token limit
```
### After
```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokens = tokenizer.encode(text)
if len(tokens) > 4096: text = tokenizer.decode(tokens[:4096])
```

## Refactor 03 (Hard): Manual Chain
### Before
```python
summary = llm(f"Summarize: {text}")
translation = llm(f"Translate to French: {summary}")
analysis = llm(f"Analyze: {translation}")
```
### After
```python
from langchain.chains import SequentialChain
chain = SequentialChain(chains=[summarize_chain, translate_chain, analyze_chain])
result = chain.run(text)
```
