"""Level 11 — LLM & Prompt Engineering — Medium P02 Solution"""

def structured_prompt(persona, context, format, question):
    return f"""You are a {persona}. Your task is to explain a concept.

Context: {context}

Format your response as:
{format}

Input: {question}"""

if __name__ == "__main__":
    print(structured_prompt("data scientist", "machine learning basics",
                             "3 bullet points", "What is overfitting?"))
