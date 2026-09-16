"""Level 11 Llm Prompt — Hard P02 Solution"""

def solve():
    def evaluate_llm_output(output, criteria):
        scores = {}
        for criterion in criteria:
            if criterion == 'length':
                scores['length'] = len(output) > 50
            elif criterion == 'format':
                scores['format'] = '{' in output or '[' in output
            elif criterion == 'accuracy':
                scores['accuracy'] = 'correct' in output.lower()
        return scores
    output = 'The answer is {"result": 42, "correct": true}'
    criteria = ['length', 'format', 'accuracy']
    scores = evaluate_llm_output(output, criteria)
    print(f"Evaluation: {scores}")
    return scores

if __name__ == "__main__":
    solve()