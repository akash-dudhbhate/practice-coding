"""Level 13 — Agentic AI — Hard P02 Solution"""

def evaluate_agent(agent_output, expected, steps_used, min_steps, covered_parts, total_parts):
    return {
        "correctness": 1.0 if agent_output == expected else 0.5,
        "efficiency": min(min_steps / steps_used, 1.0),
        "completeness": covered_parts / total_parts
    }

if __name__ == "__main__":
    r = evaluate_agent("42", "42", 3, 3, 2, 3)
    print(r)
