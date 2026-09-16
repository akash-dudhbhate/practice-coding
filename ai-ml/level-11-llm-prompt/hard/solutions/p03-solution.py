"""Level 11 Llm Prompt — Hard P03 Solution"""

def solve():
    system_prompts = {
        'helpful': 'You are a helpful assistant. Be concise and accurate.',
        'expert': 'You are an expert data scientist. Provide detailed technical explanations.',
        'creative': 'You are a creative writer. Be imaginative and engaging.',
        'critical': 'You are a critical reviewer. Point out flaws and improvements.'
    }
    for name, prompt in system_prompts.items():
        print(f"{name}: {prompt}")
    return system_prompts

if __name__ == "__main__":
    solve()