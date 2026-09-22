"""Level 11 — LLM & Prompt Engineering — Hard P03 Solution"""

def get_personas():
    return {
        "helpful": "You are a helpful assistant. Be concise and accurate.",
        "expert": "You are an expert data scientist. Provide detailed technical explanations.",
        "creative": "You are a creative writer. Be imaginative and engaging.",
        "critical": "You are a critical reviewer. Point out flaws and improvements.",
    }

if __name__ == "__main__":
    for k, v in get_personas().items():
        print(f"{k}: {v}")
