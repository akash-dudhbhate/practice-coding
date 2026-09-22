"""Level 11 — LLM & Prompt Engineering — Easy P01 Solution"""

def make_prompts(text):
    return {
        "simple": f"Summarize this text.",
        "detailed": f"Summarize this text in 3 bullet points.",
        "structured": f"Summarize this text as JSON with keys: main_point, key_details."
    }

if __name__ == "__main__":
    p = make_prompts("ML models learn from data")
    for k, v in p.items():
        print(f"{k}: {v}")
