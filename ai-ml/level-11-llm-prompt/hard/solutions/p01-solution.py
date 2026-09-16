"""Level 11 — LLM & Prompt Engineering — Hard P01 Solution"""

def iterate_prompts(task):
    prompts = [
        (f"Summarize this.", 0.6),
        (f"Summarize in 3 bullet points.", 0.75),
        (f"Summarize in 3 bullet points with key metrics.", 0.85),
    ]
    return prompts

if __name__ == "__main__":
    for p, s in iterate_prompts("summarize a sales report"):
        print(f"{s:.2f}: {p}")
