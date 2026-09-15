# Lesson 20 — Debug Exercises

## Debug 01 (Easy: Vague Prompt
```python
prompt = "Write about Python"
# Output: random, unfocused
```
<details><summary>Answer</summary>
**Bug:** Too vague — model doesn't know what to focus on.
**Fix:** Be specific: "Write a 200-word tutorial about Python list comprehensions for beginners."
</details>

## Debug 02 (Medium: No Context
```python
prompt = "Summarize this"
# No text provided
```
<details><summary>Answer</summary>
**Bug:** No context — model doesn't know what to summarize.
**Fix:** "Summarize this article in 3 bullet points: [article text]".
</details>

## Debug 03 (Hard: Not Using Examples
```python
prompt = "Classify the sentiment"
# No examples of expected output
```
<details><summary>Answer</summary>
**Bug:** No examples — model may use different format than expected.
**Fix:** Few-shot: "Classify sentiment:
Text: 'I love it' → positive
Text: 'Terrible' → negative
Text: 'It's okay' → ?"
</details>
