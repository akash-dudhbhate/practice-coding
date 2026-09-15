# Lesson 20 — Easy P03: Chain-of-thought vs direct prompt for math
# Compares step-by-step reasoning with a direct answer prompt.

math_problem = "A store sells apples at $2 each and oranges at $3 each. If Sarah buys 4 apples and 3 oranges, and pays with a $20 bill, how much change does she receive?"

# Direct prompt (no reasoning)
direct_prompt = f"Solve: {math_problem}\nAnswer:"
mock_direct_answer = "$5"
print("=== Direct Prompt (no reasoning) ===")
print(f"Prompt: {direct_prompt}")
print(f"Response: {mock_direct_answer}")
print("Issue: The answer may be wrong because no reasoning is shown.\n")

# Chain-of-thought prompt (step-by-step)
cot_prompt = f"""Solve the following problem step by step.

Problem: {math_problem}

Step 1: Calculate the cost of apples.
Step 2: Calculate the cost of oranges.
Step 3: Calculate the total cost.
Step 4: Calculate the change.
Final Answer:"""

mock_cot_answer = """Step 1: 4 apples × $2 = $8
Step 2: 3 oranges × $3 = $9
Step 3: Total cost = $8 + $9 = $17
Step 4: Change = $20 - $17 = $3
Final Answer: $3"""

print("=== Chain-of-Thought Prompt ===")
print(f"Prompt: {cot_prompt}")
print(f"Response: {mock_cot_answer}")
print("Correct: The step-by-step reasoning leads to the right answer ($3).\n")

print("=== Comparison ===")
print("Direct prompt: Answered $5 (WRONG — likely guessed without computing).")
print("CoT prompt: Answered $3 (CORRECT — each step is verifiable).")
print()
print("Chain-of-thought prompting is more reliable for math problems because:")
print("1. Each step can be verified independently.")
print("2. Breaking the problem into steps reduces errors.")
print("3. The reasoning is transparent and debuggable.")
