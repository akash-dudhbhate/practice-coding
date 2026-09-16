"""Level 11 Llm Prompt — Easy P01 Solution"""

def solve():
    prompts = {
        'simple': 'Summarize this text.',
        'detailed': 'Summarize this text in 3 bullet points.',
        'structured': 'Summarize this text as JSON with keys: main_point, key_details.'
    }
    for name, prompt in prompts.items():
        print(f"{name}: {prompt}")
    return prompts

if __name__ == "__main__":
    solve()