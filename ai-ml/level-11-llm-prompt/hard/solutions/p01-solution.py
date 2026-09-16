"""Level 11 Llm Prompt — Hard P01 Solution"""

def solve():
    # Prompt optimization through iteration
    iterations = [
        {'version': 1, 'prompt': 'Summarize this.', 'score': 0.6},
        {'version': 2, 'prompt': 'Summarize in 3 bullet points.', 'score': 0.75},
        {'version': 3, 'prompt': 'Summarize in 3 bullet points with key metrics.', 'score': 0.85},
    ]
    for it in iterations:
        print(f"v{it['version']}: {it['prompt']} (score: {it['score']})")
    best = max(iterations, key=lambda x: x['score'])
    print(f"\nBest prompt: {best['prompt']}")
    return best

if __name__ == "__main__":
    solve()