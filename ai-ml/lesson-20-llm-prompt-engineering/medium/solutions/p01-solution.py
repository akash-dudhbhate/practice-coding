# Lesson 20 — Medium P01: Prompt template system
# Templates for 3 tasks: summarization, translation, code review.

from string import Template


# Template definitions
templates = {
    "summarization": Template(
        "Summarize the following text in $length sentences.\n"
        "Focus on: $focus\n\n"
        "Text: $text\n\n"
        "Summary:"
    ),
    "translation": Template(
        "Translate the following text from $source_lang to $target_lang.\n"
        "Tone: $tone\n\n"
        "Text: $text\n\n"
        "Translation:"
    ),
    "code_review": Template(
        "Review the following $language code for:\n"
        "- Bugs and errors\n"
        "- Performance issues\n"
        "- Best practices\n"
        "- Readability\n\n"
        "Code:\n$text\n\n"
        "Review:"
    ),
}


def fill_template(task, **kwargs):
    """Fill a template with the given parameters and return the final prompt."""
    if task not in templates:
        raise ValueError(f"Unknown task: {task}. Available: {list(templates.keys())}")
    return templates[task].safe_substitute(**kwargs)


# Test all 3 templates
print("=== 1. Summarization Template ===")
summary_prompt = fill_template(
    "summarization",
    length="2",
    focus="key findings and implications",
    text="A new study shows that regular exercise improves memory function in adults over 50...",
)
print(summary_prompt)

print("\n=== 2. Translation Template ===")
translation_prompt = fill_template(
    "translation",
    source_lang="English",
    target_lang="Spanish",
    tone="formal",
    text="Hello, how are you today?",
)
print(translation_prompt)

print("\n=== 3. Code Review Template ===")
code_review_prompt = fill_template(
    "code_review",
    language="Python",
    text="def add(a, b): return a + b",
)
print(code_review_prompt)

print("\n=== Template System Benefits ===")
print("- Consistent prompt structure across tasks")
print("- Easy to modify templates without changing calling code")
print("- Placeholders make it clear what inputs are needed")
print("- Reusable across different content inputs")
