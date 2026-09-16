"""Level 12 — RAG Systems — Hard P03 Solution"""

import re

def rewrite_query(query):
    replacements = {
        r'\bML\b': 'machine learning',
        r'\bDL\b': 'deep learning',
        r'\bAI\b': 'artificial intelligence',
        r'\bNLP\b': 'natural language processing',
        r'\bCV\b': 'computer vision',
        r'\bRL\b': 'reinforcement learning',
    }
    result = query
    for abbrev, full in replacements.items():
        result = re.sub(abbrev, full, result)
    return result

if __name__ == "__main__":
    print(rewrite_query("What is ML?"))
    print(rewrite_query("Tell me about NLP"))
