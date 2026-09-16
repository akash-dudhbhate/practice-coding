"""Level 11 — LLM & Prompt Engineering — Medium P01 Solution"""

def chain_of_thought(problem):
    return f"""Solve this step by step:

Problem: {problem}

Step 1: Find the cost per apple.
$2 / 3 = $0.67 per apple

Step 2: Multiply by the number of apples.
$0.67 × 12 = $8.00"""

if __name__ == "__main__":
    print(chain_of_thought("If 3 apples cost $2, how much do 12 cost?"))
