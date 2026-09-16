"""Level 11 — LLM & Prompt Engineering — Easy P02 Solution"""

def few_shot_prompt(examples, query):
    lines = ["Classify the sentiment:", ""]
    for text, label in examples:
        lines.append(f'Text: "{text}" → {label}')
    lines.append(f'Text: "{query}" →')
    return "\n".join(lines)

if __name__ == "__main__":
    ex = [("I love it", "Positive"), ("Terrible", "Negative"), ("Meh", "Neutral")]
    print(few_shot_prompt(ex, "This is amazing!"))
