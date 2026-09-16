"""Level 13 Agentic Ai — Hard P02 Solution"""

def solve():
    def evaluate_agent(agent_output, criteria):
        scores = {}
        if 'correct' in criteria:
            scores['correctness'] = 0.9 if 'answer' in agent_output else 0.3
        if 'efficient' in criteria:
            scores['efficiency'] = 0.8 if len(agent_output) < 100 else 0.5
        if 'complete' in criteria:
            scores['completeness'] = 0.85 if len(agent_output) > 10 else 0.4
        return scores
    output = "The answer is 42"
    criteria = ['correct', 'efficient', 'complete']
    scores = evaluate_agent(output, criteria)
    print(f"Agent evaluation: {scores}")
    return scores

if __name__ == "__main__":
    solve()