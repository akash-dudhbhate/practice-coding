"""Level 11 Llm Prompt — Medium P02 Solution"""

def solve():
    template = '''
You are a {persona}. Your task is to {task}.

Context: {context}

Format your response as:
{format}

Input: {input}
'''
    example = template.format(
        persona='data scientist',
        task='explain a concept',
        context='machine learning basics',
        format='3 bullet points',
        input='What is overfitting?'
    )
    print(example)
    return template

if __name__ == "__main__":
    solve()